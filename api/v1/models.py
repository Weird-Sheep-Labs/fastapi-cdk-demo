import os
from typing import Optional

from dyntastic import Dyntastic


class Song(Dyntastic):
    __table_name__ = os.environ["DYNAMODB_SONG_TABLE_NAME"]
    __table_host__ = os.getenv("DYNAMODB_HOST")
    __hash_key__ = "Artist"
    __range_key__ = "Title"

    Artist: str
    Title: str
    Album: str
    Key: Optional[str] = None
    Bpm: Optional[int] = None
