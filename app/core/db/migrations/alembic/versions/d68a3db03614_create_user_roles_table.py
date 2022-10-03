"""create user roles table

Revision ID: d68a3db03614
Revises: 849d9aea7151
Create Date: 2022-09-29 09:44:32.832877

"""
from sqlalchemy.sql import func

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd68a3db03614'
down_revision = '849d9aea7151'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'user_roles',
        sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id'), nullable=False),
        sa.Column('role_id', sa.Integer, sa.ForeignKey('roles.id'), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=True), nullable=False, default=func.now(), server_default=func.now()),
        sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True, onupdate=func.now()),
    )

    op.create_primary_key(
        "pk_user_id_role_id",
        "user_roles",
        ["user_id", "role_id"],
    )


def downgrade() -> None:
    op.drop_table('user_roles')
