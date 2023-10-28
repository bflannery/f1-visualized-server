"""create race result table

Revision ID: ffd8f4f81a2c
Revises: af397c8ad988
Create Date: 2023-10-23 19:40:13.014906

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'ffd8f4f81a2c'
down_revision: Union[str, None] = 'af397c8ad988'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('race_result',
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
                    sa.Column('rank', sa.Integer(), nullable=True),
                    sa.Column('race_status_id', sa.Integer(), nullable=False),
                    sa.Column('time', sa.Text(), nullable=True),
                    sa.Column('time_ms', sa.Integer(), nullable=True),
                    sa.Column('fastest_lap', sa.Integer(), nullable=True),
                    sa.Column('fastest_lap_time', sa.Text(), nullable=True),
                    sa.Column('fastest_lap_time_ms', sa.Integer(), nullable=True),
                    sa.Column('fastest_lap_speed', sa.Text(), nullable=True),

                    sa.PrimaryKeyConstraint('id'),
                    sa.ForeignKeyConstraint(['race_id'], ['race.id'], ),
                    sa.ForeignKeyConstraint(['driver_id'], ['driver.id'], ),
                    sa.ForeignKeyConstraint(['constructor_id'], ['constructor.id'], ),
                    sa.ForeignKeyConstraint(['race_status_id'], ['race_status.id'], ),
                    )


def downgrade() -> None:
    op.drop_table('race_result')
