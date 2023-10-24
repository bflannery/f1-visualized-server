"""create constructor standing table

Revision ID: 7170d57f1775
Revises: d8e9897356a8
Create Date: 2023-10-23 06:06:26.097327

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '7170d57f1775'
down_revision: Union[str, None] = 'd8e9897356a8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('constructor_standing',
                    sa.Column('id', sa.BigInteger(), nullable=False),
                    sa.Column('created_at', sa.DateTime(), server_default=sa.text("(now() at time zone 'utc')"),
                              nullable=True),
                    sa.Column('updated_at', sa.DateTime(), server_default=sa.text("(now() at time zone 'utc')"),
                              nullable=True),
                    sa.Column('race_id', sa.Integer(), nullable=False),
                    sa.Column('constructor_id', sa.Integer(), nullable=False),
                    sa.Column('points_total', sa.Integer(), nullable=False),
                    sa.Column('position', sa.Integer(), nullable=False),
                    sa.Column('wins', sa.Integer(), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.ForeignKeyConstraint(['race_id'], ['race.id'], ),
                    sa.ForeignKeyConstraint(['constructor_id'], ['constructor.id'], ),
                    )


def downgrade() -> None:
    op.drop_table('constructor_standing')
