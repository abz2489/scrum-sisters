"""Create two training day fields in teams model

Revision ID: 8e40dd94cfeb
Revises: bd87efda174f
Create Date: 2023-10-05 19:23:39.551747

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8e40dd94cfeb'
down_revision = 'bd87efda174f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('teams', schema=None) as batch_op:
        batch_op.add_column(sa.Column('training_day1', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('training_day2', sa.Integer(), nullable=False))
        batch_op.drop_constraint('teams_days_id_fkey', type_='foreignkey')
        batch_op.create_foreign_key(None, 'days', ['training_day1'], ['id'])
        batch_op.create_foreign_key(None, 'days', ['training_day2'], ['id'])
        batch_op.drop_column('days_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('teams', schema=None) as batch_op:
        batch_op.add_column(sa.Column('days_id', sa.INTEGER(), autoincrement=False, nullable=False))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key('teams_days_id_fkey', 'days', ['days_id'], ['id'])
        batch_op.drop_column('training_day2')
        batch_op.drop_column('training_day1')

    # ### end Alembic commands ###
