"""create pit stop table

Revision ID: b23804507afa
Revises: 581299c823ce
Create Date: 2023-10-23 16:21:54.090870

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'b23804507afa'
down_revision: Union[str, None] = '581299c823ce'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('pit_stop',
                    sa.Column('id', sa.BigInteger(), nullable=False),
                    sa.Column('created_at', sa.DateTime(), server_default=sa.text("(now() at time zone 'utc')"),
                              nullable=True),
                    sa.Column('updated_at', sa.DateTime(), server_default=sa.text("(now() at time zone 'utc')"),
                              nullable=True),
                    sa.Column('race_id', sa.Integer(), nullable=False),
                    sa.Column('driver_id', sa.Integer(), nullable=False),
                    sa.Column('lap', sa.Integer(), nullable=False),
                    sa.Column('stop', sa.Integer(), nullable=False),
                    sa.Column('time_of_day', sa.Text(), nullable=False),
                    sa.Column('duration', sa.Text(), nullable=False),
                    sa.Column('duration_ms', sa.Text(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.ForeignKeyConstraint(['race_id'], ['race.id'], ),
                    sa.ForeignKeyConstraint(['driver_id'], ['driver.id'], ),
                    )


def downgrade() -> None:
    op.drop_table('pit_stop')
