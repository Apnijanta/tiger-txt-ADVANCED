import os

API_ID = API_ID = 25912801

API_HASH = os.environ.get("API_HASH", "f14e8717578935103e2774559184a345")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6735419941:AAGI72d1Eni3t6puvcoN0vaAMf8KKcOpvlA")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 1306706536))

LOG = -1002070057679

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5987970971").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


