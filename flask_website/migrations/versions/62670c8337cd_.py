"""empty message

Revision ID: 62670c8337cd
Revises: 
Create Date: 2020-11-09 22:46:27.650332

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '62670c8337cd'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('task', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'task')
    # ### end Alembic commands ###
