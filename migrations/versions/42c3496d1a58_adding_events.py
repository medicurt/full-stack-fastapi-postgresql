"""adding events

Revision ID: 42c3496d1a58
Revises: 83ecc96e678f
Create Date: 2022-07-24 10:14:55.132535

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42c3496d1a58'
down_revision = '83ecc96e678f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('event',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('street_address', sa.String(), nullable=False),
    sa.Column('city', sa.String(), nullable=False),
    sa.Column('state_or_province', sa.String(), nullable=False),
    sa.Column('country', sa.String(), nullable=False),
    sa.Column('date_to_occur', sa.DateTime(), nullable=False),
    sa.Column('recurring', sa.Boolean(), nullable=True),
    sa.Column('admission_fee', sa.Float(), nullable=False),
    sa.Column('is_open', sa.Boolean(), nullable=False),
    sa.Column('max_participants', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('created_by', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['created_by'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_event_id'), 'event', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_event_id'), table_name='event')
    op.drop_table('event')
    # ### end Alembic commands ###
