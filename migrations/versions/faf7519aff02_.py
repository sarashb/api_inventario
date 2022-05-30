"""empty message

Revision ID: faf7519aff02
Revises: 66f18cfcf091
Create Date: 2022-05-24 12:23:27.284464

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'faf7519aff02'
down_revision = '66f18cfcf091'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('produto',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('descricao', sa.String(length=50), nullable=False),
    sa.Column('velocidade', sa.String(length=50), nullable=False),
    sa.Column('preco', sa.Float(), nullable=False),
    sa.Column('disponibilidade', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('produto')
    # ### end Alembic commands ###
