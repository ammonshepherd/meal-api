"""empty message

Revision ID: 51be654be6f8
Revises: f6e9da161a87
Create Date: 2020-10-20 16:35:21.626737

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51be654be6f8'
down_revision = 'f6e9da161a87'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('plans',
    sa.Column('date', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('meals_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['meals_id'], ['meals.id'], name='meals_id', ondelete='CASCADE')
    )


def downgrade():
    op.drop_table('plans')
