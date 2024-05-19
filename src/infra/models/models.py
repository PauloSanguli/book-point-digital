from sqlalchemy import MetaData, create_engine
from sqlalchemy import (
    Column, INTEGER,
    TEXT, VARCHAR, Table,
    ForeignKey
)


import os





engine = create_engine(str(os.getenv("DATABASE_URI")))
metadata = MetaData()


admin = Table(
    "admin",
    metadata,
    Column("id", INTEGER, autoincrement=True, primary_key=True),
    Column("email", VARCHAR(50), nullable=False,unique=True),
    Column("password", TEXT, nullable=False),
    Column("name", TEXT, nullable=False)
)

student = Table(
    "students",
    metadata,
    Column("id", INTEGER, autoincrement=True, primary_key=True),
    Column("name", TEXT, nullable=False),
    Column("classroom", INTEGER, nullable=False),
    Column("grade", VARCHAR(10), nullable=False),
    Column("turn", VARCHAR(20), nullable=False),
    Column("photo", TEXT),
    Column("course", TEXT)
)

teachers = Table(
    "teachers",
    metadata,
    Column("id", INTEGER, autoincrement=True, primary_key=True),
    Column("name", TEXT, nullable=False),
    Column("turn", VARCHAR(20), nullable=False),
    Column("photo", TEXT)
)

subjects = Table(
    "subjects",
    metadata,
    Column("id", INTEGER, autoincrement=True, primary_key=True),
    Column("subject", TEXT, nullable=False),
    Column("teacher_id", INTEGER, ForeignKey("teachers.id"))
)
