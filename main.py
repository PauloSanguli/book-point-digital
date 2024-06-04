from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware

from src.infra.http.views.admin import post_admin
from src.infra.http.views.admin import get_admin
from src.infra.http.views.admin import patch_admin
from src.infra.http.views.student import post_student
from src.infra.http.views.student import delete_student
from src.infra.http.views.student import get_student
from src.infra.http.views.teachers import get_teacher
from src.infra.http.views.teachers import post_teacher
from src.infra.http.views.teachers import delete_teacher

import uvicorn

from sqlalchemy.orm import Session
from sqlalchemy import select
from src.infra.models import engine, admin


app = FastAPI(title="API book school")

app.include_router(post_admin)
app.include_router(get_admin)
app.include_router(patch_admin)
app.include_router(delete_student)
app.include_router(post_student)
app.include_router(get_student)
app.include_router(get_teacher)
app.include_router(delete_teacher)
app.include_router(post_teacher)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

@app.get("/")
async def say_hello():
    return JSONResponse(
        content=jsonable_encoder({
            "msg": "api on air"
        })
    )
    

if __name__=="__main__":
    uvicorn.run(app=app, port=3715, host='0.0.0.0')
