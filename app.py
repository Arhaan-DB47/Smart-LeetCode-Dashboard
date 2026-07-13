"""
app.py — Flask application entry point for the LeetCode Pattern Dashboard.

This is the heart of your backend. It does three things:
1. Initializes the database when the app starts
2. Serves the single-page dashboard (index.html)
3. Will host all API routes (added in Phase 2)

WHY Flask?
- Minimal boilerplate — you see exactly what's happening
- Perfect for single-page apps with a REST API
- Easy to understand for portfolio reviewers
"""

from flask import Flask, render_template
from database import init_db

# ---------------------------------------------------------------------------
# App Factory
# ---------------------------------------------------------------------------

# Create the Flask app instance.
# __name__ tells Flask where to find templates/ and static/ folders.
app = Flask(__name__)


# ---------------------------------------------------------------------------
# Initialize database on startup
# ---------------------------------------------------------------------------

# This runs ONCE when the server starts. It creates tables if they
# don't exist, and skips if they do. Safe to run every time.
init_db()


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.route('/')
def index():
    """
    Serve the main dashboard page.
    
    Flask automatically looks in the 'templates/' folder for HTML files.
    So render_template('index.html') → templates/index.html
    """
    return render_template('index.html')


# ---------------------------------------------------------------------------
# Run the server
# ---------------------------------------------------------------------------

if __name__ == '__main__':
    # debug=True gives you:
    #   1. Auto-reload when you save a file (no manual restart needed)
    #   2. Detailed error pages in the browser
    # NEVER use debug=True in production — it's a security risk.
    app.run(debug=True, port=5000)
