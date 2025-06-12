from fastapi import FastAPI
from prisma import Prisma
import uvicorn
from contextlib import asynccontextmanager

prisma = Prisma()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await prisma.connect()
    yield
    await prisma.disconnect()

app = FastAPI(lifespan=lifespan)

@app.get("/")
async def root():
    return "Hello World from Chat API"

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
