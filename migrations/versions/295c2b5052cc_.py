"""empty message

Revision ID: 295c2b5052cc
Revises: 3ca95f0f598f
Create Date: 2022-05-20 22:17:18.951700

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '295c2b5052cc'
down_revision = '3ca95f0f598f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('password', sa.String(length=250), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'password')
    # ### end Alembic commands ###
