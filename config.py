from os import path, getenv

class config:
    API_ID = int(getenv("API_ID", ""))
    API_HASH = getenv("API_HASH", "")
    BOT_TOKEN = getenv("BOT_TOKEN", "")
    IP_API =getenv("ACCESS_TOKEN","")
    
con = config()
