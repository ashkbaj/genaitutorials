"""empty message

Revision ID: 510423f391a7
Revises: 70d67df985fe
Create Date: 2024-05-13 12:09:19.366904

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '510423f391a7'
down_revision = '70d67df985fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('password', sa.String(length=16), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('password')

    # ### end Alembic commands ###
