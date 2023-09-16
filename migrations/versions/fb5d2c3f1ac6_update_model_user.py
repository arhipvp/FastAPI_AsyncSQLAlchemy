"""Update model User

Revision ID: fb5d2c3f1ac6
Revises: 1ab8dc817d78
Create Date: 2023-09-16 21:50:32.228493

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fb5d2c3f1ac6'
down_revision: Union[str, None] = '1ab8dc817d78'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('user', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('user', 'is_active',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column('user', 'is_superuser',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column('user', 'is_verified',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.drop_column('user', 'password')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.alter_column('user', 'is_verified',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column('user', 'is_superuser',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column('user', 'is_active',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column('user', 'hashed_password',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###
