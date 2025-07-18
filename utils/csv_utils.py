import csv
import os
from datetime import datetime

def save_to_csv(nonfollowers, filename_prefix="not_following_back"):
    """
    Save a list of users who don't follow back to a timestamped CSV file inside the /out directory.

    Args:
        nonfollowers (set): A set of Instaloader Profile objects not following back.
        filename_prefix (str): Prefix for the output filename.
    """
    output_dir = "out"
    os.makedirs(output_dir, exist_ok=True)  # Create 'out' folder if it doesn't exist

    # Create timestamped filename
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{filename_prefix}_{timestamp}.csv"
    filepath = os.path.join(output_dir, filename)

    # Write to CSV
    with open(filepath, "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Username"])
        for user in sorted(nonfollowers, key=lambda x: x.username.lower()):
            writer.writerow([user.username])

    print(f"📄 Saved to {filepath}")
