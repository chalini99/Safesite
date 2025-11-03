import requests

# ✅ Your bot token as ONE STRING
BOT_TOKEN = "8473447853:AAHD0RM6I_3fKqhbRBxgyfpRI-fxjoivuRk"

# ⚠️ Replace this with your actual chat ID (from @userinfobot)
CHAT_ID = "YOUR_CHAT_ID_HERE"  # Example: "123456789"

def send_alert(message: str):
    """Send alert message to your Telegram bot chat."""
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()
        print("✅ Alert sent:", response.json())
        return response.json()
    except Exception as e:
        print("❌ Telegram alert failed:", e)
        return None
