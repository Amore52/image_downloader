from envparse import env


delay = env('DELAY', default=14400, cast=int)
env.read_envfile('.env')
nasa_token = env('NASA_TOKEN')
filename_path = './images/'
tg_token = env('TG_TOKEN')
chat_id = env('CHAT_ID')