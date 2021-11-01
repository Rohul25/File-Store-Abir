# (c) @AbirHasan2005

import os


class Config(object):
	API_ID = int(os.environ.get("API_ID"))
	API_HASH = os.environ.get("API_HASH")
	BOT_TOKEN = os.environ.get("BOT_TOKEN")
	BOT_USERNAME = os.environ.get("BOT_USERNAME")
	DB_CHANNEL = int(os.environ.get("DB_CHANNEL"))
	BOT_OWNER = int(os.environ.get("BOT_OWNER"))
	DATABASE_URL = os.environ.get("DATABASE_URL")
	UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL")
	LOG_CHANNEL = os.environ.get("LOG_CHANNEL", None)
	BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "1234567890").split())
	FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
	BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
	BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "-1001362659779 -1001255795497").split()))
	OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
	ABOUT_BOT_TEXT = f"""
This is Files Store Bot!
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

🤖 **My Name:** [Files Store Bot](https://t.me/{BOT_USERNAME})

📝 **Language:** [Python3](https://www.python.org)

📚 **Library:** [Pyrogram](https://docs.pyrogram.org)

📡 **Hosted on:** [Heroku](https://heroku.com)

🧑🏻‍💻 **Developer:** @ToRoBots

👥 **Support Group:** [TO RᴏBᴏᴛs](https://t.me/ToRoBots)

📢 **Updates Channel:** [TO RᴏBᴏᴛs](https://t.me/ToRoBots)
"""
	ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 **Developer:** @ToRoBots

<i>🔰 Welcome To </i><i><b>TO RᴏBᴏᴛs</b> 🔰

Here All The bots are useful & always we try to improve it. We try hard to make your life easier with Telegram. 

</i><i><b>NOTE :-</b> If Any Bot Is Not Working Message At [Soon].</i>
 """
	HOME_TEXT = """
**Hi, [{}](tg://user?id={})\n\nThis is File Store Bot**.
Send me any file I will save it in my Database. Also works for channel. Add me to channel as Admin with Edit Permission, I will add Save Uploaded File in Channel & add Sharable Button Link.

Created By [TO RᴏBᴏᴛs](https://t.me/ToRobots) With 💗.  
"""
