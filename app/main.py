from fastapi import FastAPI
from fastapi.responses import FileResponse

app = FastAPI()

@app.get('/')
async def root():
    return FileResponse('index.html')

@app.get('/calculate')
async def root():
    return FileResponse('index.html')
