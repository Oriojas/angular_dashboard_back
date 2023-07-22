import os
import uvicorn
import subprocess
from subprocess import PIPE
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware

URL = os.getenv("URL")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/test_provider/", status_code=201)
async def test_provider():

    result = subprocess.Popen(["python3", "test_connect_provider.py"], stdout=PIPE, stderr=PIPE)
    print(result.stderr.read())

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8090)
