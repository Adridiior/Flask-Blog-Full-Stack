"""Add category to Post

Revision ID: 92d8b7c92d07
Revises: 3ba91eb40f76
Create Date: 2024-07-15 12:27:13.544793

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '92d8b7c92d07'
down_revision = '3ba91eb40f76'
branch_labels = None
depends_on = None

def upgrade():
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('category', sa.String(length=100), nullable=False, server_default='General'))
    # Non rimuovere il default, lasciare che sia 'General'
    # op.alter_column('post', 'category', server_default=None)

def downgrade():
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_column('category')
