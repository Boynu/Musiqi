from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", "12210813"))
API_HASH = getenv("API_HASH", "e42eeae11a2f96bcfc5ec3b46a30adad")

BOT_TOKEN = getenv("BOT_TOKEN", "5855945910:AAGI0cfON_45Zpa6BsUC6HffhCOWg3iLYS8")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", "5751610471"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", "AgBpDmZAXe7_q17SF8Gtyg_CBBL81SgZRzPrh5cc4PtpGE9nkQXczN8_7_i1moki3P6AXoHetiY1wzlC470qBeRGaCWJSYl_Atomq8laFCQnCVOnSP2oUztAJKM1gbY3GqAkXoFDRxkzglMKFMp0fKHdDZnGbJaDsLJnoHlAaAbE9IDFvrMOpez0vOPpR9E6VxAi1BX2_IAg72vqYh7NvJcchLVolS1DeP0Gm6r0SeMUPk86TvrZ9LqVrDBOFOKNFM6Bva8qHFsw4ckbb5nxB5RAkmAL_vl-UjxT0O4aonCybp-qgzri0GLZw7nJB3gKR_sV5f4STfxRLt5P4HbNeIsCAAAAAVGTdKgA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DevilsHeavenMF")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/FallenAssociation")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5751610471").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
