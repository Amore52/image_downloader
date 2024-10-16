import os

from dotenv import load_dotenv



load_dotenv()

delay = os.getenv('DELAY', 14400)
nasa_token = os.getenv('NASA_TOKEN')
filename_path = './images/'
tg_bot_token = os.getenv('TG_BOT_TOKEN')
tg_chat_id = os.getenv('TG_CHAT_ID')