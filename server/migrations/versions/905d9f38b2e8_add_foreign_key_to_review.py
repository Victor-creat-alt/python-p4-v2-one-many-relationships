"""add foreign key to Review

Revision ID: 905d9f38b2e8
Revises: e938cc97016d
Create Date: 2025-03-26 17:47:18.185366

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '905d9f38b2e8'
down_revision = 'e938cc97016d'
branch_labels = None
depends_on = None


def upgrade():
    # Use batch mode for SQLite migrations
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.add_column(sa.Column('employee_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(
            'fk_reviews_employee_id_employees',  # Constraint name
            'employees',                        # Referenced table
            ['employee_id'],                    # Columns in the current table
            ['id']                              # Referenced columns in the other table
        )


def downgrade():
    # Use batch mode for downgrades as well
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.drop_constraint('fk_reviews_employee_id_employees', type_='foreignkey')
        batch_op.drop_column('employee_id')
