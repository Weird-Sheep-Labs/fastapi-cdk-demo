import os
from typing import Optional

from dyntastic import Dyntastic


class Song(Dyntastic):
    __table_name__ = os.environ["DYNAMODB_SONG_TABLE_NAME"]
    __table_host__ = os.getenv("DYNAMODB_HOST")
    __hash_key__ = "artist"
    __range_key__ = "title"

    artist: str
    title: str
    album: str
    key: Optional[str] = None
    bpm: Optional[int] = None
