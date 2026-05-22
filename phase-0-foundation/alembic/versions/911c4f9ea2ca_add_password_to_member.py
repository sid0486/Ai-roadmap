"""add password to member

Revision ID: 911c4f9ea2ca
Revises: 413077a248af
Create Date: 2026-05-14 21:54:48.189529

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '911c4f9ea2ca'
down_revision: Union[str, Sequence[str], None] = '413077a248af'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.add_column('member', sa.Column('password', sa.String(), nullable=True))


def downgrade() -> None:
    op.drop_column('member', 'password')
