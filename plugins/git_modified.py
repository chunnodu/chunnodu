import subprocess
from datetime import datetime
from pelican import signals

def get_git_modified_time(content):
    if not hasattr(content, 'source_path') or not content.source_path:
        return

    try:
        # Run git log to get the latest commit timestamp for the file
        output = subprocess.check_output(
            ["git", "log", "-1", "--format=%cd", "--date=iso-strict", content.source_path],
            encoding='utf-8',
            stderr=subprocess.DEVNULL
        ).strip()
        
        if output:
            # Parse the ISO string into a datetime object
            modified_date = datetime.fromisoformat(output)
            
            # Use locale formatting to match standard Pelican dates
            if hasattr(content, 'locale_date'):
                # Basic string format for locale date if we want to mimic Pelican's default
                content.locale_modified = modified_date.strftime('%B %d, %Y')
            
            content.modified = modified_date

    except (subprocess.CalledProcessError, ValueError):
        pass

def register():
    signals.content_object_init.connect(get_git_modified_time)
