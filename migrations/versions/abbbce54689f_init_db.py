"""init db

Revision ID: abbbce54689f
Revises: 
Create Date: 2024-09-13 16:52:15.562012

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'abbbce54689f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(length=100), nullable=True),
                    sa.Column('password_hash', sa.String(
                        length=100), nullable=True),
                    sa.Column('username', sa.String(
                        length=1000), nullable=True),
                    sa.Column('confirmed', sa.Boolean(), nullable=True),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'),
                    sa.UniqueConstraint('username')
                    )
    op.create_table('characters',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('url_name', sa.String(
                        length=100), nullable=True),
                    sa.Column('owner', sa.Integer(), nullable=True),
                    sa.Column('owner_username', sa.String(
                        length=100), nullable=True),
                    sa.Column('created_at', sa.DateTime(timezone=True),
                              server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
                    sa.Column('name', sa.String(length=64), nullable=False),
                    sa.Column('background', sa.String(
                        length=64), nullable=False),
                    sa.Column('custom_name', sa.String(
                        length=64), nullable=True),
                    sa.Column('custom_background', sa.String(
                        length=64), nullable=True),
                    sa.Column('strength', sa.Integer(), nullable=True),
                    sa.Column('strength_max', sa.Integer(), nullable=True),
                    sa.Column('dexterity', sa.Integer(), nullable=True),
                    sa.Column('dexterity_max', sa.Integer(), nullable=True),
                    sa.Column('willpower', sa.Integer(), nullable=True),
                    sa.Column('willpower_max', sa.Integer(), nullable=True),
                    sa.Column('hp', sa.Integer(), nullable=True),
                    sa.Column('hp_max', sa.Integer(), nullable=True),
                    sa.Column('deprived', sa.Boolean(), nullable=True),
                    sa.Column('items', sa.String(), nullable=True),
                    sa.Column('containers', sa.String(), nullable=True),
                    sa.Column('gold', sa.Integer(), nullable=True),
                    sa.Column('description', sa.String(
                        length=2000), nullable=True),
                    sa.Column('traits', sa.String(length=2000), nullable=True),
                    sa.Column('notes', sa.String(length=2000), nullable=True),
                    sa.Column('bonds', sa.String(length=2000), nullable=True),
                    sa.Column('scars', sa.String(length=2000), nullable=True),
                    sa.Column('omens', sa.String(length=2000), nullable=True),
                    sa.Column('custom_image', sa.Boolean(), nullable=True),
                    sa.Column('image_url', sa.String(
                        length=512), nullable=True),
                    sa.Column('armor', sa.String(length=16), nullable=True),
                    sa.Column('party_code', sa.String(
                        length=64), nullable=True),
                    sa.Column('party_id', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['owner'], ['users.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('parties',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('owner', sa.Integer(), nullable=True),
                    sa.Column('created_at', sa.DateTime(timezone=True),
                              server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True),
                    sa.Column('name', sa.String(length=64), nullable=False),
                    sa.Column('description', sa.String(
                        length=2000), nullable=True),
                    sa.Column('notes', sa.String(length=2000), nullable=True),
                    sa.Column('members', sa.String(
                        length=2000), nullable=True),
                    sa.Column('subowners', sa.String(
                        length=2000), nullable=True),
                    sa.Column('join_code', sa.String(
                        length=64), nullable=True),
                    sa.Column('party_url', sa.String(
                        length=200), nullable=True),
                    sa.Column('owner_username', sa.String(
                        length=100), nullable=True),
                    sa.Column('items', sa.String(), nullable=True),
                    sa.Column('containers', sa.String(), nullable=True),
                    sa.Column('events', sa.String(), nullable=True),
                    sa.Column('version', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['owner'], ['users.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('parties')
    op.drop_table('characters')
    op.drop_table('users')
    # ### end Alembic commands ###

