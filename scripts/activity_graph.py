"""Render a GitHub contribution activity graph as an SVG.

Replacement for github-readme-activity-graph.vercel.app. Reads the public
contributions calendar (no token needed) and draws the last N days as a
line + area chart. Standard library only.

Usage: python scripts/activity_graph.py [username] [output.svg] [days]
"""
import re
import sys
import urllib.request
from datetime import date

USERNAME = sys.argv[1] if len(sys.argv) > 1 else "chunnodu"
OUTPUT = sys.argv[2] if len(sys.argv) > 2 else "activity-graph.svg"
DAYS = int(sys.argv[3]) if len(sys.argv) > 3 else 31

BG = "#ffffff"
TEXT = "#058c8c"
LINE = "#058c8c"
POINT = "#FFA18A"
AREA = "#8AFFFF"
GRID = "#e8e8e8"
BORDER = "#e4e2e2"

W, H = 1200, 420
PAD_L, PAD_R, PAD_T, PAD_B = 70, 30, 70, 60


def fetch_contributions(username):
    url = f"https://github.com/users/{username}/contributions"
    req = urllib.request.Request(url, headers={"User-Agent": "activity-graph"})
    html = urllib.request.urlopen(req, timeout=30).read().decode("utf-8")

    dates = {}
    for td in re.findall(r"<td[^>]*ContributionCalendar-day[^>]*>", html):
        d = re.search(r'data-date="([\d-]+)"', td)
        i = re.search(r'id="([^"]+)"', td)
        if d and i:
            dates[i.group(1)] = d.group(1)

    counts = {}
    for target, text in re.findall(r'<tool-tip[^>]*for="([^"]+)"[^>]*>([^<]*)</tool-tip>', html):
        if target not in dates:
            continue
        m = re.match(r"\s*(\d+) contribution", text)
        counts[dates[target]] = int(m.group(1)) if m else 0

    if not counts:
        raise SystemExit("No contribution data parsed; GitHub markup may have changed.")
    return sorted(counts.items())


def nice_max(v):
    if v <= 4:
        return 4
    step = 5 if v <= 25 else 10
    return ((v + step - 1) // step) * step


def render(days, username):
    values = [c for _, c in days]
    ymax = nice_max(max(values))
    plot_w = W - PAD_L - PAD_R
    plot_h = H - PAD_T - PAD_B
    n = len(days)

    def x(i):
        return PAD_L + plot_w * i / (n - 1)

    def y(v):
        return PAD_T + plot_h * (1 - v / ymax)

    pts = [(x(i), y(v)) for i, v in enumerate(values)]
    line = " ".join(f"{px:.1f},{py:.1f}" for px, py in pts)
    base = y(0)
    area = f"{pts[0][0]:.1f},{base:.1f} {line} {pts[-1][0]:.1f},{base:.1f}"

    out = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
        f'font-family="Segoe UI, Ubuntu, Helvetica, Arial, sans-serif">',
        f'<title>{username} contribution activity, last {n} days</title>',
        f'<rect x="0.5" y="0.5" width="{W - 1}" height="{H - 1}" rx="6" fill="{BG}" stroke="{BORDER}"/>',
        f'<text x="{W / 2}" y="40" text-anchor="middle" font-size="22" font-weight="600" fill="{TEXT}">'
        f"{username}'s Contribution Graph</text>",
    ]

    ticks = 4
    for t in range(ticks + 1):
        v = ymax * t / ticks
        ty = y(v)
        out.append(f'<line x1="{PAD_L}" y1="{ty:.1f}" x2="{W - PAD_R}" y2="{ty:.1f}" stroke="{GRID}"/>')
        out.append(f'<text x="{PAD_L - 12}" y="{ty + 4:.1f}" text-anchor="end" font-size="12" fill="{TEXT}">{v:g}</text>')

    for i, (d, _) in enumerate(days):
        out.append(f'<text x="{x(i):.1f}" y="{H - PAD_B + 20}" text-anchor="middle" font-size="12" fill="{TEXT}">'
                   f"{int(d[-2:])}</text>")

    out.append(f'<text x="22" y="{PAD_T + plot_h / 2}" text-anchor="middle" font-size="13" fill="{TEXT}" '
               f'transform="rotate(-90 22 {PAD_T + plot_h / 2})">Contributions</text>')
    out.append(f'<text x="{W / 2}" y="{H - 12}" text-anchor="middle" font-size="13" fill="{TEXT}">Days</text>')

    out.append(f'<polygon points="{area}" fill="{AREA}" fill-opacity="0.35"/>')
    out.append(f'<polyline points="{line}" fill="none" stroke="{LINE}" stroke-width="2.5" stroke-linejoin="round"/>')
    for (px, py), (d, v) in zip(pts, days):
        out.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="4" fill="{POINT}"><title>{d}: {v}</title></circle>')

    out.append("</svg>")
    return "\n".join(out)


def main():
    days = fetch_contributions(USERNAME)
    today = date.today().isoformat()
    days = [d for d in days if d[0] <= today][-DAYS:]
    with open(OUTPUT, "w") as f:
        f.write(render(days, USERNAME))
    print(f"Wrote {OUTPUT}: {days[0][0]} to {days[-1][0]}, {sum(c for _, c in days)} contributions")


if __name__ == "__main__":
    main()
