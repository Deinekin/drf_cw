import requests

from config import settings


def send_telegram_message(chat_id, message):
    params = {
        "text": message,
        "chat_id": chat_id,
    }
    url = requests.get(
        f"https://api.telegram.org/bot{settings.TELEGRAM_TOKEN}/sendMessage", params=params
    )

    response = requests.get(url=url, params=params)

    if response.status_code == 200:
        return True
    return False

