from fastapi import FastAPI

from .routers import songs

app = FastAPI()
app.include_router(songs.router)


@app.get("/")
async def root():
    return {"message": "Hello"}
