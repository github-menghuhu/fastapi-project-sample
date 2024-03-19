"""add project table

Revision ID: ceccb2733163
Revises: 
Create Date: 2024-03-19 10:03:51.040226

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "ceccb2733163"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "project",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=20), nullable=False),
        sa.Column("desc", sa.String(length=200), nullable=True),
        sa.Column("tags", sa.JSON(), nullable=True),
        sa.Column("unique_id", sa.UUID(), nullable=False),
        sa.Column("is_delete", sa.Boolean(), nullable=False),
        sa.Column("created_time", sa.DateTime(), nullable=False),
        sa.Column("updated_time", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("unique_id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("project")
    # ### end Alembic commands ###