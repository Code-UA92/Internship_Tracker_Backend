"""create programmes table

Revision ID: 2dc6a645382f
Revises: 8ab8c149d948
Create Date: 2026-06-23 15:40:05.302794

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2dc6a645382f'
down_revision: Union[str, Sequence[str], None] = '8ab8c149d948'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'programmes',
        sa.Column('programme_id', sa.Integer, primary_key=True),
        sa.Column('company_id', sa.Integer, sa.ForeignKey('companies.company_id', name='fk_company'), nullable=False),
        sa.Column('type_id', sa.Integer, sa.ForeignKey('types.type_id', name='fk_type'), nullable=False),
        sa.Column('locations_id', sa.Integer, sa.ForeignKey('locations.location_id', name='fk_location'), nullable=False),
        sa.Column('title', sa.String(255)),
        sa.Column('description', sa.String),
        sa.Column('qualifications', sa.String),
        sa.Column('preferred_qualifications', sa.String),
        sa.Column('deadline', sa.Date)
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('programmes')
