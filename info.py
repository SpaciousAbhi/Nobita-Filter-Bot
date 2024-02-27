import re
from os import environ
from Script import script
import asyncio

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Bot information
SESSION = environ.get('BQGlZx4Aof8s4VTu0nGtjYO9LVsim_OSDrv2xzZo9lQ8M75g2Q8Jw4wWQZYMrQlJxP1k2bYpw7zAexWNQcQUiF0KuLY7hySQqx8JpzbKotemFyI52wKvd1RYnhZ1JPpxYViMKP5SPrf2I-_UXscLeTHx4LbRfVoQt5aNXEzdknMBV9AG6YUlL1cipms0a6bsQDe_6yMd8ShIDMBFH-ie4PO-crhUGEbQT1suc4A5JGJ4DdVKvTb7VODeTSJJfyOYuJ_zVRPnSnO94MWTOYwIrOZuvoQ80ZXRPmQoVAnhryj9bfxvWIipEoJny3OgNBC8IPzkQXHatejemKcBlqH8u_RxeC6MJQAAAAAS1GglAA', 'Media_search')
API_ID = int(environ.get('27617054'))
API_HASH = environ.get('9dba979fbbb2152772a21f66f11116a4')
BOT_TOKEN = environ.get('7081840649:AAEqj7Eara5pmo9sy4BBXncvbzPXtjYOdoU')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', True))

PICS = (environ.get('PICS', 'https://telegra.ph/file/eb119179b4d2a13e71163.jpg https://telegra.ph/file/dc5a1a49c2786685ff97a.jpg https://telegra.ph/file/1a9519a68c4d45ac9455a.jpg https://telegra.ph/file/e5a3d6969f2082eecc3c1.jpg https://telegra.ph/file/57d6d774cf4baf2de5968.jpg')).split()
NOR_IMG = environ.get("NOR_IMG", "https://telegra.ph/file/61ef9818986cef9554017.jpg")
MELCOW_VID = environ.get("MELCOW_VID", "https://telegra.ph/file/61ef9818986cef9554017.jpg")
SPELL_IMG = environ.get("SPELL_IMG", "https://telegra.ph/file/61ef9818986cef9554017.jpg")

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '1654334233').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '-1002125043839').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '1654334233').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('-1002125043839')
auth_grp = environ.get('-1002118607833')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
AUTH_GROUPS = [int(ch) for ch in auth_grp.split()] if auth_grp else None
support_chat_id = environ.get('-1002118607833', '')
reqst_channel = environ.get('-1002118607833')
REQST_CHANNEL = int(reqst_channel) if reqst_channel and id_pattern.search(reqst_channel) else None
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None
NO_RESULTS_MSG = bool(environ.get("NO_RESULTS_MSG", True))

# MongoDB information
DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://madadi9597:1QriSE1XaKW9sBxz@cluster0.dqo97wg.mongodb.net/?retryWrites=true&w=majority")
DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Files')

# stickers
STICKERS = (environ.get('STICKERS', 'CAACAgUAAxkBAAEKk8BlNPrdTHUdjCkHswRS7FEGD57bQgADDQACryfoV7k_sTsjJTYAATAE CAACAgUAAxkBAAEKk75lNPrc-rw4n-xEqmgMA14lO_lzMQACLwcAApzI6VfWL2jjZeNSATAE')).split()

#Auto approve 
CHAT_ID = [int(app_chat_id) if id_pattern.search(app_chat_id) else app_chat_id for app_chat_id in environ.get('CHAT_ID', '').split()]
TEXT = environ.get("APPROVED_WELCOME_TEXT", "<b>{mention},\n\nʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴛᴏ ᴊᴏɪɴ {title} ɪs ᴀᴘᴘʀᴏᴠᴇᴅ.</b>")
APPROVED = environ.get("APPROVED_WELCOME", "on").lower()

# Others
VERIFY = bool(environ.get('VERIFY', False))
SHORTLINK_URL = environ.get('SHORTLINK_URL', 'publicearn.com')
SHORTLINK_API = environ.get('SHORTLINK_API', 'c464f482d973a7e88ba6cb7077a3afa5de229dd5')
IS_SHORTLINK = bool(environ.get('IS_SHORTLINK', True))
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in environ.get('DELETE_CHANNELS', '0').split()]
MAX_B_TN = environ.get("MAX_B_TN", "8")
MAX_BTN = is_enabled((environ.get('MAX_BTN', "True")), True)
PORT = environ.get("PORT", "8080")
GRP_LNK = environ.get('GRP_LNK', 'https://t.me/VenomStoneMoviesGroup')
CHNL_LNK = environ.get('CHNL_LNK', 'https://t.me/VenomStoneNetwork')
MSG_ALRT = environ.get('MSG_ALRT', 'ꜱʜᴀʀᴇ  ᴀɴᴅ  ꜱᴜᴘᴘᴏʀᴛ  ᴜꜱ')
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '1002113810572'))
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'VenomStoneMoviesGroup')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
IMDB = is_enabled((environ.get('IMDB', "False")), False)
AUTO_FFILTER = is_enabled((environ.get('AUTO_FFILTER', "True")), True)
AUTO_DELETE = is_enabled((environ.get('AUTO_DELETE', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", f"{script.CAPTION}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", CUSTOM_FILE_CAPTION)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL))
FILE_STORE_CHANNEL = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '-1002026830023 -1002078648489 -1002038220265 -1002045162941 -1002037786718 -1001567003485 -1001856689643')).split()]
MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

LANGUAGES = ["hindi", "hin", "tamil", "tam", "telugu", "tel", "english", "eng", "kannada", "kan", "malayalam", "mal"]
TUTORIAL = environ.get('TUTORIAL', 'https://youtu.be/0c-i2Lol6LU')
IS_TUTORIAL = bool(environ.get('IS_TUTORIAL', True))

LOG_STR = "Current Cusomized Configurations are:-\n"
LOG_STR += ("IMDB Results are enabled, Bot will be showing imdb details for you queries.\n" if IMDB else "IMBD Results are disabled.\n")
LOG_STR += ("P_TTI_SHOW_OFF found , Users will be redirected to send /start to Bot PM instead of sending file file directly\n" if P_TTI_SHOW_OFF else "P_TTI_SHOW_OFF is disabled files will be send in PM, instead of sending start.\n")
LOG_STR += ("SINGLE_BUTTON is Found, filename and files size will be shown in a single button instead of two separate buttons\n" if SINGLE_BUTTON else "SINGLE_BUTTON is disabled , filename and file_sixe will be shown as different buttons\n")
LOG_STR += (f"CUSTOM_FILE_CAPTION enabled with value {CUSTOM_FILE_CAPTION}, your files will be send along with this customized caption.\n" if CUSTOM_FILE_CAPTION else "No CUSTOM_FILE_CAPTION Found, Default captions of file will be used.\n")
LOG_STR += ("Long IMDB storyline enabled." if LONG_IMDB_DESCRIPTION else "LONG_IMDB_DESCRIPTION is disabled , Plot will be shorter.\n")
LOG_STR += ("Spell Check Mode Is Enabled, bot will be suggesting related movies if movie not found\n" if SPELL_CHECK_REPLY else "SPELL_CHECK_REPLY Mode disabled\n")
LOG_STR += (f"MAX_LIST_ELM Found, long list will be shortened to first {MAX_LIST_ELM} elements\n" if MAX_LIST_ELM else "Full List of casts and crew will be shown in imdb template, restrict them by adding a value to MAX_LIST_ELM\n")
LOG_STR += f"Your current IMDB template is {IMDB_TEMPLATE}"
