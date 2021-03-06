"""initial migration

Revision ID: c7c16a885272
Revises: 
Create Date: 2018-03-12 20:31:16.447196

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c7c16a885272'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('grouptype',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('group', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_grouptype_group'), 'grouptype', ['group'], unique=False)
    op.create_table('meetingtype',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('meeting', sa.String(length=20), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_meetingtype_meeting'), 'meetingtype', ['meeting'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('stu_number', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_admin'), 'users', ['admin'], unique=False)
    op.create_index(op.f('ix_users_stu_number'), 'users', ['stu_number'], unique=True)
    op.create_table('asks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('leave_time', sa.DateTime(), nullable=True),
    sa.Column('group', sa.String(length=32), nullable=True),
    sa.Column('type_of_meeting', sa.String(length=32), nullable=True),
    sa.Column('actual_time', sa.String(length=64), nullable=True),
    sa.Column('reason_for_leave', sa.String(length=128), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_asks_group'), 'asks', ['group'], unique=False)
    op.create_index(op.f('ix_asks_reason_for_leave'), 'asks', ['reason_for_leave'], unique=False)
    op.create_index(op.f('ix_asks_type_of_meeting'), 'asks', ['type_of_meeting'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_asks_type_of_meeting'), table_name='asks')
    op.drop_index(op.f('ix_asks_reason_for_leave'), table_name='asks')
    op.drop_index(op.f('ix_asks_group'), table_name='asks')
    op.drop_table('asks')
    op.drop_index(op.f('ix_users_stu_number'), table_name='users')
    op.drop_index(op.f('ix_users_admin'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_meetingtype_meeting'), table_name='meetingtype')
    op.drop_table('meetingtype')
    op.drop_index(op.f('ix_grouptype_group'), table_name='grouptype')
    op.drop_table('grouptype')
    # ### end Alembic commands ###
