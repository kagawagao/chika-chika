import uvicorn
from fastapi import FastAPI

from app.log import logger

app = FastAPI(title="Chika Chika", version="0.1.0")


@app.get("/", include_in_schema=False)
async def root():
    logger.info("Hello World")
    return {"message": "Hello World"}


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
