"""empty message

Revision ID: f6e9da161a87
Revises: d5eba024e9d4
Create Date: 2020-10-20 15:50:53.037369

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f6e9da161a87'
down_revision = 'd5eba024e9d4'
branch_labels = None
depends_on = None


def upgrade():
    op.rename_table('mealer', 'meals')


def downgrade():
    op.rename_table('meals', 'mealer')
