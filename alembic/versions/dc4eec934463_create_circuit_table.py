"""create circuit table

Revision ID: dc4eec934463
Revises: 514670a1190d
Create Date: 2023-10-17 16:45:36.639960

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'dc4eec934463'
down_revision: Union[str, None] = '514670a1190d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('circuit',
                    sa.Column('id', sa.BigInteger(), nullable=False),
                    sa.Column('created_at', sa.DateTime(), server_default=sa.text("(now() at time zone 'utc')"),
                              nullable=True),
                    sa.Column('updated_at', sa.DateTime(), server_default=sa.text("(now() at time zone 'utc')"),
                              nullable=True),
                    sa.Column('reference', sa.Text(), nullable=False, unique=True),
                    sa.Column('name', sa.Text(), nullable=False, unique=True),
                    sa.Column('location', sa.Text(), nullable=False, unique=False),
                    sa.Column('country', sa.Text(), nullable=False, unique=False),
                    sa.Column('latitude', sa.Integer(), nullable=False, unique=False),
                    sa.Column('longitude', sa.Integer(), nullable=False, unique=False),
                    sa.Column('wiki_url', sa.Text(), nullable=True, unique=False),
                    sa.PrimaryKeyConstraint('id')
                    )

    op.create_index(op.f('ix_circuit_reference'), 'circuit', ['reference'], unique=True)
    op.create_index(op.f('ix_circuit_name'), 'circuit', ['name'], unique=True)


def downgrade() -> None:
    op.drop_index(op.f('ix_circuit_reference'), table_name='circuit')
    op.drop_index(op.f('ix_circuit_reference'), table_name='circuit')
    op.drop_table('circuit')
