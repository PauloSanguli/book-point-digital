"""create tables

Revision ID: a7b5a413c46c
Revises: 
Create Date: 2024-05-19 18:33:59.287913

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import (
    Column, INTEGER,
    TEXT, VARCHAR, ForeignKey
)


# revision identifiers, used by Alembic.
revision: str = 'a7b5a413c46c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    
    op.create_table(
        "admin",
        Column("id", INTEGER, autoincrement=True, primary_key=True),
        Column("email", VARCHAR(50), nullable=False,unique=True),
        Column("password", TEXT, nullable=False),
        Column("name", TEXT, nullable=False),
        Column("photo", TEXT),
    )

    op.create_table(
        "students",
        Column("id", INTEGER, autoincrement=True, primary_key=True),
        Column("name", TEXT, nullable=False),
        Column("classroom", INTEGER, nullable=False),
        Column("turn", VARCHAR(20), nullable=False),
        Column("photo", TEXT),
        Column("course", TEXT)
    )

    op.create_table(
        "teachers",
        Column("id", INTEGER, autoincrement=True, primary_key=True),
        Column("name", TEXT, nullable=False),
        Column("grade", VARCHAR(10), nullable=False),
        Column("turn", VARCHAR(20), nullable=False),
        Column("photo", TEXT)
    )

    op.create_table(
        "subjects",
        Column("id", INTEGER, autoincrement=True, primary_key=True),
        Column("subject", TEXT, nullable=False),
        Column("teacher_id", INTEGER, ForeignKey("teachers.id"))
    )



def downgrade() -> None:
    pass
