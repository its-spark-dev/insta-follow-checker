import csv
import os

def save_to_csv(nonfollowers, filename="not_following_back.csv"):
    """
    Save a list of users who don't follow back to a CSV file inside the /out directory.

    Args:
        nonfollowers (set): A set of Instaloader Profile objects not following back.
        filename (str): Output CSV filename.
    """
    output_dir = "out"
    os.makedirs(output_dir, exist_ok=True)  # Create 'out' folder if it doesn't exist
    filepath = os.path.join(output_dir, filename)

    with open(filepath, "w", newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Username"])
        for user in sorted(nonfollowers, key=lambda x: x.username.lower()):
            writer.writerow([user.username])

    print(f"📄 Saved to {filepath}")
