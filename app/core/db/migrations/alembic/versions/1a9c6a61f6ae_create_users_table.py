"""create users table

Revision ID: 1a9c6a61f6ae
Revises: 
Create Date: 2022-09-29 09:23:35.748594

"""
from sqlalchemy.sql import func, expression

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '1a9c6a61f6ae'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(255), nullable=False),
        sa.Column('email', sa.String(255), nullable=False),
        sa.Column('phone', sa.String(255), nullable=False),
        sa.Column('password', sa.String(255), nullable=False),
        sa.Column('is_active', sa.Boolean, server_default=expression.true(), default=False, nullable=False),
        sa.Column('email_verified_at', sa.DateTime(timezone=True), nullable=True),
        sa.Column('last_logged_on', sa.DateTime(timezone=True), nullable=True),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, default=func.now(), server_default=func.now()),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True, onupdate=func.now()),
    )


def downgrade() -> None:
    op.drop_table('users')
