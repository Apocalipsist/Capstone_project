"""fixed tables

Revision ID: 00acdd992a7e
Revises: ac19acb7cad3
Create Date: 2022-11-23 12:03:32.108766

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '00acdd992a7e'
down_revision = 'ac19acb7cad3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('saved_workout',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('body', sa.String(length=50), nullable=False),
    sa.Column('weight', sa.Integer(), nullable=False),
    sa.Column('goal', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('saved_workout', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_saved_workout_timestamp'), ['timestamp'], unique=False)

    with op.batch_alter_table('notes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('title', sa.String(length=50), nullable=False))
        batch_op.add_column(sa.Column('body', sa.String(length=50), nullable=False))
        batch_op.add_column(sa.Column('weight', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('goal', sa.Integer(), nullable=False))
        batch_op.add_column(sa.Column('timestamp', sa.DateTime(), nullable=True))
        batch_op.create_index(batch_op.f('ix_notes_timestamp'), ['timestamp'], unique=False)
        batch_op.drop_column('note')
        batch_op.drop_column('workout')
        batch_op.drop_column('date_created')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('notes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date_created', sa.DATETIME(), nullable=False))
        batch_op.add_column(sa.Column('workout', sa.VARCHAR(length=50), nullable=False))
        batch_op.add_column(sa.Column('note', sa.VARCHAR(length=255), nullable=False))
        batch_op.drop_index(batch_op.f('ix_notes_timestamp'))
        batch_op.drop_column('timestamp')
        batch_op.drop_column('goal')
        batch_op.drop_column('weight')
        batch_op.drop_column('body')
        batch_op.drop_column('title')

    with op.batch_alter_table('saved_workout', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_saved_workout_timestamp'))

    op.drop_table('saved_workout')
    # ### end Alembic commands ###
