"""create roles table

Revision ID: 849d9aea7151
Revises: 1a9c6a61f6ae
Create Date: 2022-09-29 09:23:44.539885

"""
from sqlalchemy.sql import func

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '849d9aea7151'
down_revision = '1a9c6a61f6ae'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'roles',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('role', sa.String(255), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, default=func.now(), server_default=func.now()),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True, onupdate=func.now()),
    )


def downgrade() -> None:
    op.drop_table('users')
