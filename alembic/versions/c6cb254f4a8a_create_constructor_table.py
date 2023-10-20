"""create constructor table

Revision ID: c6cb254f4a8a
Revises: 
Create Date: 2023-10-17 10:59:43.289654

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'c6cb254f4a8a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('constructor',
                    sa.Column('id', sa.BigInteger(), nullable=False),
                    sa.Column('created_at', sa.DateTime(), server_default=sa.text("(now() at time zone 'utc')"),
                              nullable=True),
                    sa.Column('updated_at', sa.DateTime(), server_default=sa.text("(now() at time zone 'utc')"),
                              nullable=True),
                    sa.Column('reference', sa.Text(), nullable=False, unique=True),
                    sa.Column('name', sa.Text(), nullable=False, unique=True),
                    sa.Column('nationality', sa.Text(), nullable=False, unique=False),
                    sa.Column('wiki_url', sa.Text(), nullable=True, unique=False),
                    sa.PrimaryKeyConstraint('id')
                    )

    op.create_index(op.f('ix_constructor_name'), 'constructor', ['name'], unique=True)
    op.create_index(op.f('ix_constructor_reference'), 'constructor', ['reference'], unique=True)


def downgrade() -> None:
    op.drop_index(op.f('ix_constructor_reference'), table_name='constructor')
    op.drop_index(op.f('ix_constructor_name'), table_name='constructor')
    op.drop_table('constructor')
