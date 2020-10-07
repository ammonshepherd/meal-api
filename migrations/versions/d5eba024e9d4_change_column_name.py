"""Change column name

Revision ID: d5eba024e9d4
Revises: 63578b4f2480
Create Date: 2020-10-07 15:21:39.920527

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5eba024e9d4'
down_revision = '63578b4f2480'
branch_labels = None
depends_on = None


def upgrade():
    op.alter_column('mealer', 'description', new_column_name='instructions')
    pass


def downgrade():
    op.alter_column('mealer', 'instruction', new_column_name='description')
    pass
