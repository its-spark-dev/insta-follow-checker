import csv
from pathlib import Path
from datetime import datetime

def save_to_csv(nonfollowers, filename_prefix="not_following_back"):
    """
    Save a list of users who don't follow back to a timestamped CSV file inside the /out directory.

    Args:
        nonfollowers (set): A set of Instaloader Profile objects not following back.
        filename_prefix (str): Prefix for the output filename.
    """
    output_dir = Path("out")
    output_dir.mkdir(parents=True, exist_ok=True)  # Cross-platform directory creation

    # Create timestamped filename
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{filename_prefix}_{timestamp}.csv"
    filepath = output_dir / filename

    # Write to CSV
    with filepath.open("w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Username"])
        for user in sorted(nonfollowers, key=lambda x: x.username.lower()):
            writer.writerow([user.username])

    print(f"📄 Saved to {filepath}")
