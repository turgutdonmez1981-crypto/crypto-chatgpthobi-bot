ilk önce import os
from telegram import Bot

TOKEN = os.environ['TELEGRAM_TOKEN']
CHAT_ID = os.environ['TELEGRAM_CHAT_ID']

bot = Bot(token=TOKEN)
bot.send_message(chat_id=CHAT_ID, text="💬 Test mesajı: Chatgpthobi_bot çalışıyor ✅")
