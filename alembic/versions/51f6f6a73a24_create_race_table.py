"""create race table

Revision ID: 51f6f6a73a24
Revises: 3642d8c88eb5
Create Date: 2023-10-18 06:01:52.867734

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '51f6f6a73a24'
down_revision: Union[str, None] = '3642d8c88eb5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('race',
                    sa.Column('id', sa.BigInteger(), nullable=False),
                    sa.Column('created_at', sa.DateTime(), server_default=sa.text("(now() at time zone 'utc')"),
                              nullable=True),
                    sa.Column('updated_at', sa.DateTime(), server_default=sa.text("(now() at time zone 'utc')"),
                              nullable=True),
                    sa.Column('season_id', sa.Integer(), nullable=False),
                    sa.Column('circuit_id', sa.Integer(), nullable=False),
                    sa.Column('round', sa.Integer(), nullable=False),
                    sa.Column('name', sa.Text(), nullable=False, unique=False),
                    sa.Column('date', sa.DateTime(), nullable=False, unique=False),
                    sa.Column('fp1_date', sa.DateTime(), nullable=True, unique=False),
                    sa.Column('fp2_date', sa.DateTime(), nullable=True, unique=False),
                    sa.Column('fp3_date', sa.DateTime(), nullable=True, unique=False),
                    sa.Column('qualifying_date', sa.DateTime(), nullable=True, unique=False),
                    sa.Column('sprint_date', sa.DateTime(), nullable=True, unique=False),
                    sa.Column('wiki_url', sa.Text(), nullable=True, unique=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.ForeignKeyConstraint(['season_id'], ['season.id'], ),
                    sa.ForeignKeyConstraint(['circuit_id'], ['circuit.id'], ),
                    )


def downgrade() -> None:
    op.drop_table('race')
