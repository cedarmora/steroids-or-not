"""create submission table

Revision ID: 4c695a1b29c7
Revises: 
Create Date: 2021-08-17 14:40:32.293420

"""
from alembic import op
import sqlalchemy as sa
import enum


# revision identifiers, used by Alembic.
revision = '4c695a1b29c7'
down_revision = None
branch_labels = None
depends_on = None

class Label(enum.Enum):
    natural = 1
    steroids = 2
    uncertain = 3
    irrelevant = 4

def upgrade():
    op.create_table(
        'submission',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('label', sa.Enum(Label)),
        sa.Column('data', sa.JSON),
    )


def downgrade():
    op.drop_table('submission')
