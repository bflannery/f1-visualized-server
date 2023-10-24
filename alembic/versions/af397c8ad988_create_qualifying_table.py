"""create qualifying table

Revision ID: af397c8ad988
Revises: b23804507afa
Create Date: 2023-10-23 19:10:01.595373

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'af397c8ad988'
down_revision: Union[str, None] = 'b23804507afa'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('qualifying',
                    sa.Column('id', sa.BigInteger(), nullable=False),
                    sa.Column('created_at', sa.DateTime(), server_default=sa.text("(now() at time zone 'utc')"),
                              nullable=True),
                    sa.Column('updated_at', sa.DateTime(), server_default=sa.text("(now() at time zone 'utc')"),
                              nullable=True),
                    sa.Column('race_id', sa.Integer(), nullable=False),
                    sa.Column('driver_id', sa.Integer(), nullable=False),
                    sa.Column('constructor_id', sa.Integer(), nullable=False),
                    sa.Column('position', sa.Integer(), nullable=False),
                    sa.Column('q1', sa.Text(), nullable=True),
                    sa.Column('q2', sa.Text(), nullable=True),
                    sa.Column('q3', sa.Text(), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.ForeignKeyConstraint(['race_id'], ['race.id'], ),
                    sa.ForeignKeyConstraint(['driver_id'], ['driver.id'], ),
                    sa.ForeignKeyConstraint(['constructor_id'], ['constructor.id'], ),
                    )


def downgrade() -> None:
    op.drop_table('qualifying')
