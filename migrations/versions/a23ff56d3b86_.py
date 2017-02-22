"""empty message

Revision ID: a23ff56d3b86
Revises: 1277d8a08214
Create Date: 2017-02-22 16:45:04.876768

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a23ff56d3b86'
down_revision = '1277d8a08214'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profile', sa.Column('password', sa.String(length=255), nullable=True))
    op.create_unique_constraint(None, 'user_profile', ['password'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_profile', type_='unique')
    op.drop_column('user_profile', 'password')
    # ### end Alembic commands ###
