"""Create flowers table

Revision ID: 8c56b6b10e89
Revises: d148fde19e97
Create Date: 2025-02-14 15:23:30.568959

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8c56b6b10e89'
down_revision: Union[str, None] = 'd148fde19e97'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'flowers',
        sa.Column('id', sa.Integer(), primary_key=True, index=True),
        sa.Column('name', sa.String(), nullable=False, unique=True),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('price', sa.Float(), nullable=False),
    )

def downgrade():
    op.drop_table('flowers')
