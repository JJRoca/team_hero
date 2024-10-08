"""initial migration

Revision ID: fc5fec79a7a4
Revises: 
Create Date: 2024-09-17 17:38:09.481628

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = 'fc5fec79a7a4'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('hero', 'is_active',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=False,
               existing_server_default=sa.text("'1'"))
    op.create_index(op.f('ix_hero_age'), 'hero', ['age'], unique=False)
    op.create_index(op.f('ix_hero_name'), 'hero', ['name'], unique=False)
    op.create_index(op.f('ix_team_name'), 'team', ['name'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_team_name'), table_name='team')
    op.drop_index(op.f('ix_hero_name'), table_name='hero')
    op.drop_index(op.f('ix_hero_age'), table_name='hero')
    op.alter_column('hero', 'is_active',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True,
               existing_server_default=sa.text("'1'"))
    # ### end Alembic commands ###
