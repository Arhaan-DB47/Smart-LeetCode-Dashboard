# 🧠 Smart LeetCode Pattern Dashboard

A full-stack web application that tracks your LeetCode problem-solving journey, uses **AI to diagnose your weak patterns**, and schedules **spaced repetition reviews** based on your confidence level.

> **Built as a portfolio project** — clean architecture, no frameworks, every line intentional.

---

## 🚀 Project Status

| Phase | Description | Status |
|:-----:|-------------|:------:|
| **1** | Project Setup & Database | ✅ Complete |
| **2** | Backend API (CRUD Routes) | 🔲 Pending |
| **3** | Frontend Dashboard UI | 🔲 Pending |
| **4** | AI Integration (Groq LLM) | 🔲 Pending |
| **5** | Spaced Repetition Engine | 🔲 Pending |
| **6** | Polish & Portfolio-Ready | 🔲 Pending |

---

## 🎯 What This App Does

1. **Log problems you struggled with** — paste your code, write notes on what confused you
2. **AI-powered analysis** — an LLM identifies the core algorithmic pattern (Sliding Window, DP, etc.) and diagnoses your logical flaw
3. **Smart review scheduling** — a confidence-based spaced repetition system tells you *when* to revisit each problem
4. **Dashboard insights** — see your weak patterns, upcoming reviews, and progress at a glance

### Confidence-Based Review System

When you log a problem, you rate your understanding:

| Level | Meaning | Review Schedule |
|:-----:|---------|-----------------|
| 🟢 1 | Solved independently | 7 → 14 → 30 → 60 → 90 days |
| 🟡 2 | Needed hint/approach | 3 → 7 → 14 → 30 → 60 days |
| 🟠 3 | Needed partial code | 1 → 3 → 7 → 14 → 30 days |
| 🔴 4 | Didn't understand | 1 → 1 → 3 → 7 → 14 days |

The lower your confidence, the sooner you review. As you improve, the app backs off automatically.

---

## 🛠️ Tech Stack

| Layer | Technology | Why |
|-------|-----------|-----|
| Frontend | HTML, CSS, JavaScript (Vanilla) | Full control, no build step, portfolio-friendly |
| Backend | Python + Flask | Lightweight, easy to understand, great for APIs |
| Database | SQLite (built-in `sqlite3`) | Zero config, file-based, no setup needed |
| AI | Groq API (free tier) | Free, fast inference, Llama/Mixtral models |

---

## 📁 Project Structure

```
leetcode-dashboard/
├── app.py                     # Flask application entry point
├── database.py                # DB schema, init, connection helpers
├── generate_meta.py           # Script to generate problem lookup data
├── requirements.txt           # Python dependencies
├── .env                       # Groq API key (gitignored)
├── .gitignore
├── static/
│   ├── css/
│   │   └── style.css          # Styles (dark mode, glassmorphism)
│   ├── js/
│   │   └── app.js             # Frontend logic
│   └── data/
│       └── problems_meta.json # 693 LeetCode problems for auto-fill
└── templates/
    └── index.html             # Single-page dashboard
```

---

## ⚡ Quick Start

### Prerequisites
- Python 3.10+

### Setup

```bash
# Clone the repo
git clone https://github.com/Arhaan-DB47/Smart-LeetCode-Dashboard.git
cd Smart-LeetCode-Dashboard

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

Open **http://127.0.0.1:5000** in your browser.

The SQLite database (`leetcode.db`) is auto-created on first run.

---

## 📊 Database Schema

### `problems` table
| Column | Type | Description |
|--------|------|-------------|
| `id` | INTEGER | Auto-incrementing primary key |
| `number` | INTEGER | LeetCode problem number |
| `name` | TEXT | Problem title |
| `difficulty` | TEXT | Easy / Medium / Hard |
| `confidence_level` | INTEGER | 1-4 (drives review scheduling) |
| `code_snippet` | TEXT | Your failed/struggling code |
| `notes` | TEXT | Personal notes |
| `pattern` | TEXT | AI-identified algorithmic pattern |
| `diagnosis` | TEXT | AI diagnosis of logical flaw |
| `times_reviewed` | INTEGER | Review count |
| `next_review` | TEXT | Next review date (ISO format) |

### `settings` table
| Column | Type | Description |
|--------|------|-------------|
| `key` | TEXT | Setting name |
| `value` | TEXT | Setting value |

Default: `daily_review_limit = 5`

---

## 🗺️ Roadmap

- [x] **Phase 1** — Flask foundation, SQLite schema, 693-problem auto-fill lookup
- [ ] **Phase 2** — REST API with full CRUD (GET, POST, PUT endpoints)
- [ ] **Phase 3** — Modern dark-mode dashboard UI with glassmorphism
- [ ] **Phase 4** — Groq LLM integration for pattern analysis
- [ ] **Phase 5** — Confidence-weighted spaced repetition engine
- [ ] **Phase 6** — Charts, loading states, README polish, portfolio-ready

---

## 👤 Author

**Arhaan** — [GitHub](https://github.com/Arhaan-DB47)
