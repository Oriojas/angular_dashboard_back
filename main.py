import os
import uvicorn
import connect_provider
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


@app.post("/test_provider/")
async def test_provider():

    con_obj = connect_provider.test_Provider()

    info_block = con_obj.info()

    info_send = {"baseFeePerGas": info_block.get("baseFeePerGas"),
                 "difficulty": info_block.get("difficulty"),
                 "gasLimit": info_block.get("gasLimit"),
                 "gasUsed": info_block.get("gasUsed"),
                 "timestamp": info_block.get("timestamp")}

    json_compatible = jsonable_encoder(info_send)

    return JSONResponse(content=json_compatible)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8090)
