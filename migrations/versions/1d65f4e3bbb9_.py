"""empty message

Revision ID: 1d65f4e3bbb9
Revises: d1c693f8649b
Create Date: 2019-12-11 14:44:44.740652

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1d65f4e3bbb9'
down_revision = 'd1c693f8649b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('department_ibfk_1', 'department', type_='foreignkey')
    op.drop_constraint('department_ibfk_2', 'department', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('department_ibfk_2', 'department', 'medicalstaff', ['doctor_ID'], ['StaffID'])
    op.create_foreign_key('department_ibfk_1', 'department', 'medicalstaff', ['nurse_ID'], ['StaffID'])
    # ### end Alembic commands ###
