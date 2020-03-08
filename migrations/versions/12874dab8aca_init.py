"""init

Revision ID: 12874dab8aca
Revises: 
Create Date: 2020-03-09 01:03:08.136120

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '12874dab8aca'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('example',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('age', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name', 'age', name='uq_name_age')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('example')
    # ### end Alembic commands ###