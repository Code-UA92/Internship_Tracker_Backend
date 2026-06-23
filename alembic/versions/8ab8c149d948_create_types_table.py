"""create types table

Revision ID: 8ab8c149d948
Revises: c463a25c02dd
Create Date: 2026-06-23 15:39:50.784741

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8ab8c149d948'
down_revision: Union[str, Sequence[str], None] = 'c463a25c02dd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'types',
        sa.Column('type_id', sa.Integer, primary_key = True),
        sa.Column('name', sa.String(50), unique = True, nullable = False)
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('types')
