from fastapi.routing import APIRouter

from ..models import Song

router = APIRouter()


@router.get("/songs/", tags=["songs"])
async def get_songs():
    return list(Song.scan())


@router.post("/songs/", tags=["songs"])
async def create_song(song: Song):
    song.save()
    return song
