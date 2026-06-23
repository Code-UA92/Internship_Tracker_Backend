"""create companies table

Revision ID: cdd080d89a05
Revises: 
Create Date: 2026-06-23 15:30:09.342857

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cdd080d89a05'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'companies',
        sa.Column('company_id', sa.Integer, primary_key = True),
        sa.Column('name', sa.String(50), unique = True, nullable = False),
        sa.Column('job_board_site', sa.String(255), nullable = False)
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('companies')
