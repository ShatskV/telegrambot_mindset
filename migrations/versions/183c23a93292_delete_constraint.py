"""delete constraint

Revision ID: 183c23a93292
Revises: bec446ef700d
Create Date: 2022-05-03 11:27:18.734601

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '183c23a93292'
down_revision = 'bec446ef700d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('tg_actions_tg_user_id_fkey', 'tg_actions', schema='bot', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('tg_actions_tg_user_id_fkey', 'tg_actions', 'tg_users', ['tg_user_id'], ['tg_user_id'], source_schema='bot', referent_schema='bot', ondelete='CASCADE')
    # ### end Alembic commands ###