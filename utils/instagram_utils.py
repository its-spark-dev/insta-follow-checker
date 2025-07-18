import instaloader
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def login_instagram():
    """
    Log into Instagram using credentials stored in environment variables.

    Returns:
        tuple: Instaloader instance and the username used to log in.
    """
    username = os.getenv("INSTA_USERNAME")
    password = os.getenv("INSTA_PASSWORD")

    if not username or not password:
        raise ValueError("Missing INSTA_USERNAME or INSTA_PASSWORD in environment variables.")

    L = instaloader.Instaloader()

    try:
        L.login(username, password)
        print("✅ Login successful.")
    except Exception as e:
        print("❌ Login failed:", e)
        exit(1)

    return L, username

def get_follow_data(L: instaloader.Instaloader, username: str):
    """
    Fetch followers and followees (people you follow) of the given Instagram profile.

    Args:
        L (Instaloader): Authenticated Instaloader instance.
        username (str): Instagram username.

    Returns:
        tuple: A set of followers and a set of followees.
    """
    profile = instaloader.Profile.from_username(L.context, username)
    print("📥 Fetching followers and followees...")
    followers = set(profile.get_followers())
    following = set(profile.get_followees())
    return followers, following
