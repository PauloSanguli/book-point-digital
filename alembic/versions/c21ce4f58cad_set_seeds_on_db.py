"""set seeds on db

Revision ID: c21ce4f58cad
Revises: a7b5a413c46c
Create Date: 2024-05-19 19:06:26.269190

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from src.infra.models import admin

# revision identifiers, used by Alembic.
revision: str = 'c21ce4f58cad'
down_revision: Union[str, None] = 'a7b5a413c46c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.bulk_insert(
        admin,
        [
            {
                "name": "Edilson Capo",
                "email": "edilsoncapo@example.com",
                "password": "$2b$12$wcAfB2CMZRWo1KUE7FQ06ejAq.449F/ptdR8bYD1bVyVqoF4MoPei"
            },
            {
                "name": "António Campos",
                "email": "antoniocampos@example.com",
                "password": "$2b$12$4cdUfLaBTG3/XIuH6AFaGuhfF3v.GS2zz9Wxsto2qcUMyaipVJQGq"
            }
        ]
    )


def downgrade() -> None:
    pass
