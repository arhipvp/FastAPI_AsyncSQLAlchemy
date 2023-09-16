"""empty message

Revision ID: 0103aa5e0b95
Revises: c37a83d6653d
Create Date: 2023-09-16 21:21:29.528249

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0103aa5e0b95'
down_revision: Union[str, None] = 'c37a83d6653d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
