"""create locations table

Revision ID: c463a25c02dd
Revises: cdd080d89a05
Create Date: 2026-06-23 15:39:33.268666

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c463a25c02dd'
down_revision: Union[str, Sequence[str], None] = 'cdd080d89a05'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'locations',
        sa.Column('location_id', sa.Integer, primary_key = True),
        sa.Column('name', sa.String(50), unique=True, nullable = False)
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('locations')
