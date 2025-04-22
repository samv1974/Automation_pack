import instaloader

def download_instagram_dp(username):
    try:
        loader = instaloader.Instaloader()
        print(f"🔍 Downloading profile picture of: {username}")
        loader.download_profile(username, profile_pic_only=True)
        print(f"✅ Downloaded successfully!")
    except Exception as e:
        print(f"❌ Error: {e}")

# Example usage:
# download_instagram_dp('nasa')
