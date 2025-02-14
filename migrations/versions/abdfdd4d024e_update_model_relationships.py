"""Update model relationships

Revision ID: abdfdd4d024e
Revises: 2cac19e8d129
Create Date: 2024-11-30 15:29:18.820627

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'abdfdd4d024e'
down_revision = '2cac19e8d129'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('activities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('lead_id', sa.Integer(), nullable=False),
    sa.Column('action', sa.String(length=100), nullable=False),
    sa.Column('details', sa.Text(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['lead_id'], ['leads.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('lead_id', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['lead_id'], ['leads.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('campaign_interactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('campaign_id', sa.Integer(), nullable=False),
    sa.Column('lead_id', sa.Integer(), nullable=False),
    sa.Column('email_sent', sa.DateTime(), nullable=True),
    sa.Column('email_opened', sa.DateTime(), nullable=True),
    sa.Column('link_clicked', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['campaign_id'], ['campaigns.id'], ),
    sa.ForeignKeyConstraint(['lead_id'], ['leads.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('email_tracking')
    with op.batch_alter_table('campaigns', schema=None) as batch_op:
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=True))
        batch_op.alter_column('status',
               existing_type=sa.VARCHAR(length=20),
               type_=sa.String(length=50),
               existing_nullable=True)
        batch_op.drop_column('scheduled_at')

    with op.batch_alter_table('email_templates', schema=None) as batch_op:
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=True))

    with op.batch_alter_table('leads', schema=None) as batch_op:
        batch_op.add_column(sa.Column('status', sa.String(length=50), nullable=True))
        batch_op.add_column(sa.Column('engagement_score', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('last_email_sent', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('last_email_opened', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('last_link_clicked', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('notes', sa.Text(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('leads', schema=None) as batch_op:
        batch_op.drop_column('notes')
        batch_op.drop_column('last_link_clicked')
        batch_op.drop_column('last_email_opened')
        batch_op.drop_column('last_email_sent')
        batch_op.drop_column('engagement_score')
        batch_op.drop_column('status')

    with op.batch_alter_table('email_templates', schema=None) as batch_op:
        batch_op.drop_column('updated_at')

    with op.batch_alter_table('campaigns', schema=None) as batch_op:
        batch_op.add_column(sa.Column('scheduled_at', sa.DATETIME(), nullable=True))
        batch_op.alter_column('status',
               existing_type=sa.String(length=50),
               type_=sa.VARCHAR(length=20),
               existing_nullable=True)
        batch_op.drop_column('updated_at')

    op.create_table('email_tracking',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('lead_id', sa.INTEGER(), nullable=False),
    sa.Column('email_id', sa.VARCHAR(length=36), nullable=False),
    sa.Column('subject', sa.VARCHAR(length=200), nullable=True),
    sa.Column('sent_at', sa.DATETIME(), nullable=True),
    sa.Column('opened_at', sa.DATETIME(), nullable=True),
    sa.Column('clicked_at', sa.DATETIME(), nullable=True),
    sa.Column('campaign_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['campaign_id'], ['campaigns.id'], ),
    sa.ForeignKeyConstraint(['lead_id'], ['leads.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email_id')
    )
    op.drop_table('campaign_interactions')
    op.drop_table('comments')
    op.drop_table('activities')
    # ### end Alembic commands ###
