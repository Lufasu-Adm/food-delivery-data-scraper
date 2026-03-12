import os
import requests
import logging
from dotenv import load_dotenv

# Load variabel 
load_dotenv()

class TelegramNotifier:
    def __init__(self):
        self.bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
        self.chat_id = os.getenv("TELEGRAM_CHAT_ID")
        
        if not self.bot_token or not self.chat_id:
            logging.warning("Telegram credentials not found in .env. Notifications are disabled.")

    def send_message(self, text: str) -> None:
        """Mengirim pesan teks ke Telegram menggunakan Telegram Bot API."""
        if not self.bot_token or not self.chat_id:
            return

        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        payload = {
            "chat_id": self.chat_id,
            "text": text,
            "parse_mode": "HTML" 
        }

        try:
            response = requests.post(url, json=payload, timeout=10)
            if response.status_code == 200:
                logging.info("Telegram notification sent successfully.")
            else:
                logging.error(f"Failed to send Telegram message. Status: {response.status_code}")
        except Exception as e:
            logging.error(f"Telegram API request failed: {e}")