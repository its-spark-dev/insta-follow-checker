import os
import time

from dotenv import load_dotenv
import instaloader
from instaloader.exceptions import ConnectionException

# Load environment variables from .env file
load_dotenv()

def login_instagram():
    """
    Load session file from custom path (for 2FA accounts).
    """
    username = os.getenv("INSTA_USERNAME")
    if not username:
        raise ValueError("Missing INSTA_USERNAME in .env file")

    L = instaloader.Instaloader()

    session_path = f"/Users/kimcharming/.config/instaloader/session-{username}"

    try:
        L.load_session_from_file(username, filename=session_path)
        print("✅ Logged in using session file.")
    except FileNotFoundError:
        print("❌ Session file not found. Please run 'instaloader --login {username}'")
        exit(1)

    return L, username

def get_follow_data(L: instaloader.Instaloader, username: str):
    """
    Fetch followers and followees (people you follow) of the given Instagram profile,
    adding a delay between requests to avoid triggering Instagram's rate limit.

    Args:
        L (Instaloader): Authenticated Instaloader instance.
        username (str): Instagram username.

    Returns:
        tuple: A set of followers and a set of followees.
    """
    profile = instaloader.Profile.from_username(L.context, username)

    try:
        print("📥 Fetching followers...")
        followers = set()
        for follower in profile.get_followers():
            followers.add(follower.username)
            time.sleep(3)  # 💤 Delay to prevent rate-limiting

        print("📥 Fetching followees...")
        followees = set()
        for followee in profile.get_followees():
            followees.add(followee.username)
            time.sleep(3)  # 💤 Delay to prevent rate-limiting

        return followers, followees

    except ConnectionException as e:
        print(f"🚫 Instagram temporarily blocked access. Reason: {e}")
        print("⏳ Please wait 30–60 minutes before trying again.")
        exit(1)
