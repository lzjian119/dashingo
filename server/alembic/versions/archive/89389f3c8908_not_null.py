"""not null

Revision ID: 89389f3c8908
Revises: 2cfb0881345e
Create Date: 2016-02-13 16:55:14.173007

"""

# revision identifiers, used by Alembic.
revision = '89389f3c8908'
down_revision = '2cfb0881345e'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user_addr', 'uid',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('user_info', 'uid',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('user_star', 'rid',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('user_star', 'uid',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('user_statistic', 'uid',
               existing_type=sa.INTEGER(),
               nullable=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user_statistic', 'uid',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('user_star', 'uid',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('user_star', 'rid',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('user_info', 'uid',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('user_addr', 'uid',
               existing_type=sa.INTEGER(),
               nullable=True)
    ### end Alembic commands ###