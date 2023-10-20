"""create driver table

Revision ID: 514670a1190d
Revises: c6cb254f4a8a
Create Date: 2023-10-17 16:30:26.443940

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '514670a1190d'
down_revision: Union[str, None] = 'c6cb254f4a8a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('driver',
                    sa.Column('id', sa.BigInteger(), nullable=False),
                    sa.Column('created_at', sa.DateTime(), server_default=sa.text("(now() at time zone 'utc')"),
                              nullable=True),
                    sa.Column('updated_at', sa.DateTime(), server_default=sa.text("(now() at time zone 'utc')"),
                              nullable=True),
                    sa.Column('reference', sa.Text(), nullable=False, unique=True),
                    sa.Column('forename', sa.Text(), nullable=False, unique=False),
                    sa.Column('surename', sa.Text(), nullable=False, unique=False),
                    sa.Column('dob', sa.Text(), nullable=False, unique=False),
                    sa.Column('nationality', sa.Text(), nullable=False, unique=False),
                    sa.Column('code', sa.Text(), nullable=True, unique=False),
                    sa.Column('number', sa.Integer(), nullable=True, unique=False),
                    sa.Column('wiki_url', sa.Text(), nullable=True, unique=False),
                    sa.PrimaryKeyConstraint('id')
                    )

    op.create_index(op.f('ix_driver_reference'), 'driver', ['reference'], unique=True)


def downgrade() -> None:
    op.drop_index(op.f('ix_driver_reference'), table_name='driver')
    op.drop_table('driver')
