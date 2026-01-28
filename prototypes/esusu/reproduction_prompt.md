# Prompt for Reproducing Esusu Fintech Prototype

**Context:**
You are an expert UI/UX designer and frontend developer. Your task is to create a high-fidelity, interactive mobile app prototype for a fintech application similar to "Cash App". The prototype should focus on two specific features: **Rotational Savings (Esusu)** and **Social Investment (Copy Trading)**.

**Design System & Aesthetic:**
*   **Theme:** Ultra-modern Dark Mode.
*   **Colors:**
    *   Background: Deep Black (`#000000`) and Dark Grey (`#1A1A1A`) for cards.
    *   Accent: Vibrant Neon Green (`#00D632`) for primary actions and positive data.
    *   Text: White (`#FFFFFF`) for headings, Light Grey (`#888888`) for secondary text.
*   **Typography:** Clean, sans-serif font (e.g., Inter or SF Pro). Bold headings, readable body text.
*   **UI Elements:**
    *   Rounded corners (16px-20px for cards, 50% for buttons).
    *   Glassmorphism effects on overlays.
    *   Mobile-first layout (375px width constraint).
    *   Bottom Navigation Bar with icons for Home, Card, Invest, Esusu, Activity.

**Feature 1: Rotational Savings (Esusu/Ajo)**
*   **Concept:** A group of friends contributes a fixed amount monthly; one person takes the whole pot each month on a rotating schedule.
*   **Key UI Components:**
    *   **Header:** Group Name (e.g., "Vacation Fund").
    *   **Status Indicator:** A large circular progress widget showing the current cycle status (e.g., "Your turn in 2 weeks", "Cycle 3/5").
    *   **Action:** Large "Pay Contribution" button.
    *   **Timeline:** A vertical step-progress timeline showing the rotation schedule.
        *   *Past items:* Dimmed/Completed status (e.g., "Paid to Sarah - Jan").
        *   *Current item:* Highlighted/Active status (e.g., "Collecting for You - March").
        *   *Future items:* Pending status.
    *   **Members:** A horizontal stack of user avatars.

**Feature 2: Social Investment (Copy Trading)**
*   **Concept:** Users can automatically copy the trading portfolios of famous investors (e.g., Nancy Pelosi).
*   **Key UI Components:**
    *   **Trader Profile:** Large avatar, Name, and an "All Time Return" badge (e.g., "+45.2%").
    *   **Performance Chart:** A stylized bar or line chart showing growth over time (Green gradient fill).
    *   **Copy Controls:**
        *   Slider to select investment amount (e.g., $100 - $10,000).
        *   "Confirm Copy Trade" button.
        *   Explanation text: "Allocates proportionally to current holdings."
    *   **Holdings List:** A list of top assets in their portfolio (e.g., NVDA, MSFT) showing allocation % and recent performance.

**Deliverables:**
Generate the code (HTML/CSS) or design specs to render these screens with pixel-perfect precision, adhering strictly to the "Cash App" aesthetic described above.
