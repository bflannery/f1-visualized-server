"""create season table

Revision ID: 3642d8c88eb5
Revises: dc4eec934463
Create Date: 2023-10-17 16:59:12.647164

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '3642d8c88eb5'
down_revision: Union[str, None] = 'dc4eec934463'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('season',
                    sa.Column('id', sa.BigInteger(), nullable=False),
                    sa.Column('created_at', sa.DateTime(), server_default=sa.text("(now() at time zone 'utc')"),
                              nullable=True),
                    sa.Column('updated_at', sa.DateTime(), server_default=sa.text("(now() at time zone 'utc')"),
                              nullable=True),
                    sa.Column('year', sa.Text(), nullable=False, unique=True),
                    sa.Column('wiki_url', sa.Text(), nullable=True, unique=False),
                    sa.PrimaryKeyConstraint('id')
                    )

    op.create_index(op.f('ix_season_year'), 'season', ['year'], unique=True)


def downgrade() -> None:
    op.drop_index(op.f('ix_season_year'), table_name='season')
    op.drop_table('season')
