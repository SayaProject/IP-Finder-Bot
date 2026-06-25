from os import path, getenv

class config:
    API_ID = int(getenv("API_ID", "30422005"))
    API_HASH = getenv("API_HASH", "5170ded206641d73215baf40175a6924")
    BOT_TOKEN = getenv("BOT_TOKEN", "8928905291:AAGcU3-7FH0r1PmmYyGpbMpko3qMqSh3NAM")
    IP_API =getenv("ACCESS_TOKEN","513fceccaba807")
    
con = config()
