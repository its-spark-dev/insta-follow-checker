import os
import time
from pathlib import Path

from dotenv import load_dotenv
from instaloader import Instaloader, Profile
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

    L = Instaloader()

    default_path = Path.home() / ".config" / "instaloader"
    session_dir = Path(os.getenv("SESSION_DIR", default_path)).expanduser()
    session_path = session_dir / f"session-{username}"

    try:
        L.load_session_from_file(username, filename=str(session_path))
        print("✅ Logged in using session file.")
    except FileNotFoundError:
        print(f"❌ Session file not found at {session_path}.")
        print(f"👉 Run: instaloader --login {username}")
        exit(1)

    return L, username

def get_follow_data(L: Instaloader, username: str):
    """
    Fetch the followers and followees for a given Instagram username.

    Args:
        L (Instaloader): Authenticated instaloader instance.
        username (str): Target Instagram username.

    Returns:
        Tuple[Set[str], Set[str]]: A set of follower usernames and followee usernames.
    """
    profile = Profile.from_username(L.context, username)

    try:
        print("📥 Fetching followers...")
        followers = {f.username for f in profile.get_followers()}
        time.sleep(3)

        print("📥 Fetching followees...")
        followees = {f.username for f in profile.get_followees()}
        time.sleep(3)

        return followers, followees

    except ConnectionException as e:
        print(f"🚫 Instagram temporarily blocked access. Reason: {e}")
        print("⏳ Please wait 30–60 minutes before trying again.")
        exit(1)
