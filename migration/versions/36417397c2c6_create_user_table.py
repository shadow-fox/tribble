"""create user table

Revision ID: 36417397c2c6
Revises: None
Create Date: 2013-12-26 16:18:46.573474

"""

# revision identifiers, used by Alembic.
revision = '36417397c2c6'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(80), unique=True),
        sa.Column('email', sa.String(120), unique=True),
        sa.Column('first_name', sa.String(50)),
        sa.Column('last_name', sa.String(50)),
        sa.Column('secondary_email', sa.String(120)),
        sa.Column('mobile', sa.Integer),
        sa.Column('secondary_mobile', sa.Integer),
        sa.Column('facebook_id', sa.Integer, unique=True),
        sa.Column('google_id', sa.Integer, unique=True),
        sa.Column('linkedin_id', sa.Integer, unique=True),
        sa.Column('gender', sa.String(6)),
        sa.Column('city', sa.String(100)),
        sa.Column('city_lat_long', sa.String(150)),
        sa.Column('salt', sa.String(64)),
        sa.Column('hash', sa.String(64)),
        sa.Column('ref_by', sa.String(32)),
        sa.Column('ref_link', sa.String(32)),
        sa.Column('status', sa.Integer),
        sa.Column('primary_role', sa.String(20)),
        sa.Column('seconday_role', sa.String(20)),
        sa.Column('last_login', sa.DateTime),
        sa.Column('created_at', sa.DateTime),
        sa.Column('modified_at', sa.DateTime)
    )


def downgrade():
    op.drop_table('user')
