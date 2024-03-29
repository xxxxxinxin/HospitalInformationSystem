"""empty message

Revision ID: faba045124d2
Revises: a122b96c985f
Create Date: 2019-12-11 14:35:10.031176

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'faba045124d2'
down_revision = 'a122b96c985f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('prescription',
    sa.Column('prescriptionID', sa.CHAR(length=5), nullable=False),
    sa.Column('patien_ID', sa.CHAR(length=4), nullable=True),
    sa.Column('doctor_ID', sa.CHAR(length=4), nullable=True),
    sa.Column('prescriptionDate', sa.DATE(), nullable=True),
    sa.Column('paymentStatues', sa.CHAR(length=1), nullable=True),
    sa.ForeignKeyConstraint(['doctor_ID'], ['patient.patientID'], ),
    sa.ForeignKeyConstraint(['patien_ID'], ['medicalstaff.StaffID'], ),
    sa.PrimaryKeyConstraint('prescriptionID')
    )
    op.create_table('reservation',
    sa.Column('reservationID', sa.CHAR(length=4), nullable=False),
    sa.Column('doctor_ID', sa.CHAR(length=4), nullable=True),
    sa.Column('patien_ID', sa.CHAR(length=4), nullable=True),
    sa.Column('reservationDate', sa.DATE(), nullable=True),
    sa.Column('description', sa.VARCHAR(length=100), nullable=True),
    sa.ForeignKeyConstraint(['doctor_ID'], ['medicalstaff.StaffID'], ),
    sa.ForeignKeyConstraint(['patien_ID'], ['patient.patientID'], ),
    sa.PrimaryKeyConstraint('reservationID')
    )
    op.create_table('ward',
    sa.Column('wardNo', sa.CHAR(length=4), nullable=False),
    sa.Column('capacity', sa.Integer(), nullable=True),
    sa.Column('department_ID', sa.CHAR(length=3), nullable=True),
    sa.ForeignKeyConstraint(['department_ID'], ['department.departmentID'], ),
    sa.PrimaryKeyConstraint('wardNo')
    )
    op.create_index(op.f('ix_ward_wardNo'), 'ward', ['wardNo'], unique=False)
    op.create_table('warehouse',
    sa.Column('warehouseID', sa.CHAR(length=2), nullable=False),
    sa.Column('warehouseadmin_ID', sa.CHAR(length=4), nullable=True),
    sa.ForeignKeyConstraint(['warehouseadmin_ID'], ['medicalstaff.StaffID'], ),
    sa.PrimaryKeyConstraint('warehouseID')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('warehouse')
    op.drop_index(op.f('ix_ward_wardNo'), table_name='ward')
    op.drop_table('ward')
    op.drop_table('reservation')
    op.drop_table('prescription')
    # ### end Alembic commands ###
