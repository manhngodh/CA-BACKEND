"""update Job Data

Revision ID: 66560e7eb5f2
Revises: 73bd43242e9b
Create Date: 2023-08-26 10:54:44.850455

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '66560e7eb5f2'
down_revision = '73bd43242e9b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('job_data', sa.Column('description', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('job_data', 'description')
    # ### end Alembic commands ###