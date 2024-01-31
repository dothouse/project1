"""empty message

Revision ID: b6d11062372c
Revises: 36207b1c98dd
Create Date: 2024-01-22 20:28:24.866246

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b6d11062372c'
down_revision = '36207b1c98dd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('weather',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.String(length=200), nullable=False),
    sa.Column('point', sa.Integer(), nullable=False),
    sa.Column('point_name', sa.String(length=200), nullable=False),
    sa.Column('temperature', sa.Float(), nullable=False),
    sa.Column('humidity', sa.Float(), nullable=False),
    sa.Column('rain', sa.Float(), nullable=False),
    sa.Column('wind', sa.Float(), nullable=False),
    sa.Column('sun', sa.Float(), nullable=False),
    sa.Column('snow', sa.Float(), nullable=False),
    sa.Column('ground', sa.Float(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.Column('month', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('weather_point',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=False),
    sa.Column('addr', sa.String(length=200), nullable=False),
    sa.Column('lat', sa.Float(), nullable=False),
    sa.Column('lng', sa.Float(), nullable=False),
    sa.Column('point', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('weather_point')
    op.drop_table('weather')
    # ### end Alembic commands ###
