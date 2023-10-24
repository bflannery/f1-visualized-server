"""create contructor result table

Revision ID: cb945e606099
Revises: 51f6f6a73a24
Create Date: 2023-10-23 05:21:54.293572

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'cb945e606099'
down_revision: Union[str, None] = '51f6f6a73a24'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('constructor_result',
                    sa.Column('id', sa.BigInteger(), nullable=False),
                    sa.Column('created_at', sa.DateTime(), server_default=sa.text("(now() at time zone 'utc')"),
                              nullable=True),
                    sa.Column('updated_at', sa.DateTime(), server_default=sa.text("(now() at time zone 'utc')"),
                              nullable=True),
                    sa.Column('race_id', sa.Integer(), nullable=False),
                    sa.Column('constructor_id', sa.Integer(), nullable=False),
                    sa.Column('points', sa.Integer(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.ForeignKeyConstraint(['constructor_id'], ['constructor.id'], ),
                    sa.ForeignKeyConstraint(['race_id'], ['race.id'], ),
                    )


def downgrade() -> None:
    op.drop_table('constructor_result')
