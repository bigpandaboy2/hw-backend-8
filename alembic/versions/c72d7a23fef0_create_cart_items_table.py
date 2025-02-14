"""Create cart_items table

Revision ID: c72d7a23fef0
Revises: 8c56b6b10e89
Create Date: 2025-02-14 15:23:51.326725

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c72d7a23fef0'
down_revision: Union[str, None] = '8c56b6b10e89'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'cart_items',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id'), nullable=False),
        sa.Column('flower_id', sa.Integer(), sa.ForeignKey('flowers.id'), nullable=False),
        sa.Column('quantity', sa.Integer(), nullable=False, server_default='1'),
    )


def downgrade():
    op.drop_table('cart_items')
