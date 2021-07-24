"""First

Revision ID: 79a25814db94
Revises: 
Create Date: 2021-07-25 03:03:31.101238

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79a25814db94'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('posts',
    sa.Column('ig', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('text', sa.String(length=300), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('ig')
    )
    op.create_index(op.f('ix_posts_ig'), 'posts', ['ig'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_posts_ig'), table_name='posts')
    op.drop_table('posts')
    # ### end Alembic commands ###
