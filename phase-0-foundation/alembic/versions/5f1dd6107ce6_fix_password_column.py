"""fix password column

Revision ID: 5f1dd6107ce6
Revises: 911c4f9ea2ca
Create Date: 2026-05-16 21:58:21.023641

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '5f1dd6107ce6'
down_revision: Union[str, Sequence[str], None] = '911c4f9ea2ca'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    op.alter_column('member', 'hash_password', new_column_name='password')


def downgrade() -> None:
    op.alter_column('member', 'password', new_column_name='hash_password')
