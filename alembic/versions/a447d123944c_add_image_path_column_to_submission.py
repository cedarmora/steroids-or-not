"""Add image path column to Submission

Revision ID: a447d123944c
Revises: 4c695a1b29c7
Create Date: 2021-08-18 18:01:09.256659

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a447d123944c'
down_revision = '4c695a1b29c7'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('submission',
        sa.Column('image_path', sa.Text)
    )


def downgrade():
    op.drop_column('submission', 'image_path')
