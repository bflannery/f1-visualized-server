"""create sprint result table

Revision ID: 69d573250e70
Revises: ffd8f4f81a2c
Create Date: 2023-10-24 05:49:02.124357

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '69d573250e70'
down_revision: Union[str, None] = 'ffd8f4f81a2c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('sprint_result',
                    sa.Column('id', sa.BigInteger(), nullable=False),
                    sa.Column('created_at', sa.DateTime(), server_default=sa.text("(now() at time zone 'utc')"),
                              nullable=True),
                    sa.Column('updated_at', sa.DateTime(), server_default=sa.text("(now() at time zone 'utc')"),
                              nullable=True),
                    sa.Column('race_id', sa.Integer(), nullable=False),
                    sa.Column('driver_id', sa.Integer(), nullable=False),
                    sa.Column('constructor_id', sa.Integer(), nullable=False),
                    sa.Column('grid', sa.Integer(), nullable=False),
                    sa.Column('position', sa.Integer(), nullable=False),
                    sa.Column('points', sa.Integer(), nullable=False),
                    sa.Column('laps', sa.Integer(), nullable=False),
                    sa.Column('race_status_id', sa.Integer(), nullable=False),
                    sa.Column('time', sa.Text(), nullable=True),
                    sa.Column('time_ms', sa.Integer(), nullable=True),
                    sa.Column('fastest_lap', sa.Integer(), nullable=True),
                    sa.Column('fastest_lap_time', sa.Text(), nullable=True),
                    sa.Column('fastest_lap_ms', sa.Integer(), nullable=True),

                    sa.PrimaryKeyConstraint('id'),
                    sa.ForeignKeyConstraint(['race_id'], ['race.id'], ),
                    sa.ForeignKeyConstraint(['driver_id'], ['driver.id'], ),
                    sa.ForeignKeyConstraint(['constructor_id'], ['constructor.id'], ),
                    sa.ForeignKeyConstraint(['race_status_id'], ['race_status.id'], ),
                    )


def downgrade() -> None:
    op.drop_table('sprint_result')
