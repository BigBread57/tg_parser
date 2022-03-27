from fastapi import FastAPI
import uvicorn

from app.api.api import api_router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == '__main__':
    uvicorn.run('main:api', port=8000, host='0.0.0.0', reload=True)

app.include_router(api_router, prefix='/api/v1')
