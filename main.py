from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'Hello world in FastAPI on uvicorn, mother fucka'}
