"""create books and book_audits tables

Revision ID: 0001_create_books
Revises: 
Create Date: 2025-09-09
"""
from alembic import op
import sqlalchemy as sa

revision = "0001_create_books"
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        "books",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("title", sa.String(length=200), nullable=False, unique=True),
        sa.Column("author", sa.String(length=100), nullable=False),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("status", sa.String(length=20), nullable=False, server_default="available"),
        sa.Column("created_at", sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP')),
    )

    op.create_table(
        "book_audits",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("book_id", sa.Integer, sa.ForeignKey("books.id", ondelete="CASCADE")),
        sa.Column("action", sa.String(length=50)),
        sa.Column("created_at", sa.DateTime(), server_default=sa.text('CURRENT_TIMESTAMP')),
    )

def downgrade():
    op.drop_table("book_audits")
    op.drop_table("books")
