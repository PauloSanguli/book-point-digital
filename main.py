from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from py_dotenv import read_dotenv


read_dotenv()

app = FastAPI()

@app.get("/book_school/")
async def say_hello():
    return JSONResponse(
        content=jsonable_encoder({
            "msg": "api on air"
        })
    )
