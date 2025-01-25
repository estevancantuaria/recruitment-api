"""create users tables

Revision ID: 261b34c1664d
Revises: 
Create Date: 2025-01-24 10:54:22.602184

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '261b34c1664d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.BIGINT(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('cpf', sa.String(length=11), nullable=False),
    sa.Column('birth_date', sa.Date(), nullable=False),
    sa.Column('cellphone', sa.String(length=20), nullable=False),
    sa.Column('user_type', sa.Enum('YOUNGSTER', 'RECRUITER', name='usertype'), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cellphone'),
    sa.UniqueConstraint('cpf'),
    sa.UniqueConstraint('email')
    )
    op.create_table('recruiters',
    sa.Column('id', sa.BIGINT(), nullable=False),
    sa.Column('company', sa.String(length=100), nullable=False),
    sa.Column('position', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('youngsters',
    sa.Column('id', sa.BIGINT(), nullable=False),
    sa.Column('rg', sa.String(length=20), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('rg')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('youngsters')
    op.drop_table('recruiters')
    op.drop_table('users')
    # ### end Alembic commands ###