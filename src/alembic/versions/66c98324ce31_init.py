"""init

Revision ID: 66c98324ce31
Revises:
Create Date: 2026-06-17 10:38:29.772373

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects.postgresql import UUID

revision: str = '66c98324ce31'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Создание таблиц events и places."""
    op.create_table(
        'places',
        sa.Column('id', UUID(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('address', sa.String(), nullable=False),
        sa.Column('city', sa.String(), nullable=False),
        sa.Column('seats_pattern', sa.String(), nullable=False),
    )
    op.create_table(
        'events',
        sa.Column('id', UUID(), primary_key=True),
        sa.Column('name', sa.String(), nullable=False),
        sa.Column('place_id', UUID(), nullable=False),
        sa.Column('event_time', sa.DateTime(timezone=True), nullable=False),
        sa.Column('status', sa.String(), nullable=False),
        sa.Column('number_of_visitors', sa.Integer(), nullable=False),
        sa.Column('changed_at', sa.DateTime(timezone=True), nullable=False),
        sa.Column(
            'registration_deadline',
            sa.DateTime(timezone=True),
            nullable=False,
        ),
    )


def downgrade() -> None:
    """Удаление таблиц events и places."""
    op.drop_table('events')
    op.drop_table('places')
