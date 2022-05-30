"""empty message

Revision ID: 0f075c3494f3
Revises: b203895db024
Create Date: 2022-05-30 09:28:48.449566

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f075c3494f3'
down_revision = 'b203895db024'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('cliente', sa.Column('endereco_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'cliente', 'endereco', ['endereco_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'cliente', type_='foreignkey')
    op.drop_column('cliente', 'endereco_id')
    # ### end Alembic commands ###