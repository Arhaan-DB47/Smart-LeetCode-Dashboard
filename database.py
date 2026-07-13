"""
database.py — SQLite database layer for the LeetCode Pattern Dashboard.

This module handles:
1. Database initialization (creating tables on first run)
2. Connection management (safe open/close with context manager pattern)
3. CRUD helper functions (will be expanded in Phase 2)

WHY raw SQL instead of an ORM like SQLAlchemy?
- You'll understand every query that touches your data
- SQLite + raw SQL is zero-config and dependency-free
- For a single-table app, an ORM adds complexity without benefit
"""

import sqlite3
import os

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

# Database file lives in the project root. It's auto-created on first run.
DATABASE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'leetcode.db')


# ---------------------------------------------------------------------------
# Connection Helper
# ---------------------------------------------------------------------------

def get_db_connection():
    """
    Create and return a database connection.
    
    Key settings:
    - row_factory = sqlite3.Row → lets you access columns by NAME (row['name'])
      instead of by index (row[0]). Much more readable.
    """
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row  # This is the magic line — enables dict-like access
    conn.execute("PRAGMA foreign_keys = ON")  # Enforce foreign key constraints
    return conn


# ---------------------------------------------------------------------------
# Schema Initialization
# ---------------------------------------------------------------------------

def init_db():
    """
    Create all tables if they don't exist.
    
    Called once when the Flask app starts. The 'IF NOT EXISTS' clause means
    this is safe to call multiple times — it won't wipe existing data.
    """
    conn = get_db_connection()
    cursor = conn.cursor()

    # --- Problems table: stores every LeetCode problem you log ---
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS problems (
            id                INTEGER PRIMARY KEY AUTOINCREMENT,
            number            INTEGER NOT NULL,
            name              TEXT NOT NULL,
            difficulty        TEXT DEFAULT 'Medium',
            confidence_level  INTEGER NOT NULL DEFAULT 4,
            code_snippet      TEXT NOT NULL,
            notes             TEXT,
            pattern           TEXT,
            diagnosis         TEXT,
            times_reviewed    INTEGER DEFAULT 0,
            next_review       TEXT,
            created_at        TEXT DEFAULT (datetime('now')),
            updated_at        TEXT DEFAULT (datetime('now'))
        )
    ''')

    # --- Settings table: key-value store for user preferences ---
    # Using a key-value pattern means we can add new settings without
    # changing the schema. Much more flexible than adding columns.
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS settings (
            key   TEXT PRIMARY KEY,
            value TEXT NOT NULL
        )
    ''')

    # Insert default settings (OR IGNORE = skip if already exists)
    cursor.execute('''
        INSERT OR IGNORE INTO settings (key, value)
        VALUES ('daily_review_limit', '5')
    ''')

    conn.commit()
    conn.close()
    print(f"[OK] Database initialized at: {DATABASE_PATH}")


# ---------------------------------------------------------------------------
# Quick test — run this file directly to verify the DB works
# ---------------------------------------------------------------------------

if __name__ == '__main__':
    init_db()
    
    # Verify tables were created
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # List all tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = [row['name'] for row in cursor.fetchall()]
    print(f"[Tables] Created: {tables}")
    
    # Check default settings
    cursor.execute("SELECT * FROM settings")
    settings = {row['key']: row['value'] for row in cursor.fetchall()}
    print(f"[Settings] Defaults: {settings}")
    
    conn.close()
