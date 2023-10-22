from fastapi import FastAPI
from fastapi.routing import APIRouter
from mangum import Mangum
from routers import songs

app = FastAPI(title="FastAPI CDK Demo", summary="FastAPI CDK demo by Weird Sheep Labs")
router = APIRouter(prefix="/v1")
router.include_router(songs.router)
app.include_router(router)


@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI CDK demo by Weird Sheep Labs!"}


handler = Mangum(app)
