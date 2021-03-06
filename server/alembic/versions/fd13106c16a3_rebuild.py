"""rebuild

Revision ID: fd13106c16a3
Revises: 
Create Date: 2016-02-14 02:03:17.528580

"""

# revision identifiers, used by Alembic.
revision = 'fd13106c16a3'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    # op.drop_table('us_rules')
    # op.drop_table('us_gaz')
    # op.drop_table('us_lex')
    # op.drop_table('spatial_ref_sys')
    # op.drop_index('idx_user_addr_pos', table_name='user_addr')
    ### end Alembic commands ###
    pass


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_index('idx_user_addr_pos', 'user_addr', ['pos'], unique=False)
    op.create_table('spatial_ref_sys',
    sa.Column('srid', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('auth_name', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    sa.Column('auth_srid', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('srtext', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    sa.Column('proj4text', sa.VARCHAR(length=2048), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('srid', name=u'spatial_ref_sys_pkey')
    )
    op.create_table('us_lex',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('seq', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('word', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('stdword', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('token', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('is_custom', sa.BOOLEAN(), server_default=sa.text(u'true'), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name=u'pk_us_lex')
    )
    op.create_table('us_gaz',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('seq', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('word', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('stdword', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('token', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('is_custom', sa.BOOLEAN(), server_default=sa.text(u'true'), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name=u'pk_us_gaz')
    )
    op.create_table('us_rules',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('rule', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('is_custom', sa.BOOLEAN(), server_default=sa.text(u'true'), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name=u'pk_us_rules')
    )
    ### end Alembic commands ###
