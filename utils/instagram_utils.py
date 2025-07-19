import os
import time
from pathlib import Path

from dotenv import load_dotenv
from instaloader import Instaloader, Profile  # Profile도 import 추가
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

    L = Instaloader()  # instaloader. 제거

    default_path = str(Path.home() / ".config" / "instaloader")
    session_dir = os.getenv("SESSION_DIR", default_path)
    session_path = Path(session_dir).expanduser() / f"session-{username}"

    try:
        L.load_session_from_file(username, filename=str(session_path))
        print("✅ Logged in using session file.")
    except FileNotFoundError:
        print("❌ Session file not found. Please run 'instaloader --login {username}'")
        exit(1)

    return L, username

def get_follow_data(L: Instaloader, username: str):
    """
    Fetch the followers and followees for a given Instagram username.

    Args:
        L (instaloader.Instaloader): Authenticated instaloader instance.
        username (str): Target Instagram username.

    Returns:
        Tuple[Set[Profile], Set[Profile]]: A set of follower profiles and a set of followee profiles.

    Raises:
        ConnectionException: If Instagram blocks access due to rate limits or bot detection.
    """
    profile = Profile.from_username(L.context, username)  # instaloader. 제거

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
