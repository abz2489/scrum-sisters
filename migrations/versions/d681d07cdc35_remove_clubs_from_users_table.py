"""Remove clubs from users table

Revision ID: d681d07cdc35
Revises: 447c33682c41
Create Date: 2023-09-16 12:40:18.837690

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd681d07cdc35'
down_revision = '447c33682c41'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint('users_club_id_fkey', type_='foreignkey')
        batch_op.drop_column('club_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.add_column(sa.Column('club_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.create_foreign_key('users_club_id_fkey', 'clubs', ['club_id'], ['id'])

    # ### end Alembic commands ###
