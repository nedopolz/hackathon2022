"""empty message

Revision ID: e3fcd030e724
Revises: 231830020bc1
Create Date: 2022-12-17 01:14:01.036952

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3fcd030e724'
down_revision = '231830020bc1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('telegram_id', sa.String(), nullable=True))
    op.drop_column('users', 'tg_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('tg_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('users', 'telegram_id')
    # ### end Alembic commands ###
