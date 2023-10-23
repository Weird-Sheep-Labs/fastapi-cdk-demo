from fastapi.routing import APIRouter
from models import Song

router = APIRouter()


@router.get("/")
async def root():
    return {"message": "Welcome to the FastAPI CDK demo by Weird Sheep Labs!"}


@router.get("/songs/", tags=["songs"])
async def list_songs():
    return list(Song.scan())


@router.post("/songs/", tags=["songs"])
async def create_song(song: Song):
    song.save()
    return song


@router.get("/songs/delete/", tags=["songs"])
async def delete_songs():
    for song in Song.scan():
        song.delete()
