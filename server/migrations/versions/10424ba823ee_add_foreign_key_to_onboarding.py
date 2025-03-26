"""add foreign key to onboarding

Revision ID: 10424ba823ee
Revises: 905d9f38b2e8
Create Date: 2025-03-26 18:00:00.000000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10424ba823ee'
down_revision = '905d9f38b2e8'
branch_labels = None
depends_on = None


def upgrade():
    # Use batch mode for SQLite migrations
    with op.batch_alter_table('onboardings', schema=None) as batch_op:
        batch_op.add_column(sa.Column('employee_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(
            'fk_onboardings_employee_id_employees',  # Constraint name
            'employees',                            # Referenced table
            ['employee_id'],                        # Columns in current table
            ['id']                                  # Referenced columns in the other table
        )


def downgrade():
    # Use batch mode for downgrades as well
    with op.batch_alter_table('onboardings', schema=None) as batch_op:
        batch_op.drop_constraint('fk_onboardings_employee_id_employees', type_='foreignkey')
        batch_op.drop_column('employee_id')
