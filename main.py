from utils.instagram_utils import login_instagram, get_follow_data
from utils.csv_utils import save_to_csv

def main():
    """
    Main execution flow:
    1. Log into Instagram.
    2. Retrieve followers and followees.
    3. Identify users who do not follow back.
    4. Print and export the result to a CSV file.
    """
    # Authenticate and get username
    L, username = login_instagram()

    # Retrieve follow data
    followers, following = get_follow_data(L, username)

    # Identify non-followers
    nonfollowers = following - followers

    # Print summary
    print(f"\n❌ {len(nonfollowers)} users do not follow you back:\n")
    for user in sorted(nonfollowers, key=lambda x: x.username.lower()):
        print(f"- {user.username}")

    # Export to CSV
    save_to_csv(nonfollowers)

if __name__ == "__main__":
    main()
