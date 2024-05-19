"""set column photo on admin

Revision ID: d8b443c97a08
Revises: c21ce4f58cad
Create Date: 2024-05-19 23:21:59.305951

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd8b443c97a08'
down_revision: Union[str, None] = 'c21ce4f58cad'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        "admin",
        sa.Column("photo", sa.TEXT)
    )


def downgrade() -> None:
    pass
