import os

from dotenv import find_dotenv, load_dotenv

# Bit of a hack to load environment variables in development
required_keys = ["DYNAMODB_HOST", "DYNAMODB_SONG_TABLE_NAME"]
if not all(os.getenv(key) for key in required_keys):
    load_dotenv(find_dotenv())
