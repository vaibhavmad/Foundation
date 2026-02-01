# Database (SQLite) Fundamentals — Plan

**Purpose**: Learn SQLite basics in Foundation so Day 2 of AI_SEO_Writer (Database setup) can proceed. SQLite is fundamental to the AI_SEO_Writer plan (projects, keywords, articles, competitor content).

**Status**: Not started. Done alongside or after API fundamentals burst; before resuming AI_SEO_Writer Day 2.

**After this**: Resume AI_SEO_Writer Day 2 (SQLAlchemy setup, models, create_project / get_project / list_projects) using these fundamentals.

---

## Learning coverage (must be covered)

- **Why database vs files**: When to use a DB (structured data, query, relations) vs plain files.
- **SQLite**: Serverless, one file (e.g. `mydb.db`), no separate server; Python stdlib `sqlite3`.
- **Connection and cursor**: `sqlite3.connect(path)`, `conn.cursor()`, `cursor.execute(...)`, `conn.commit()`, `conn.close()`.
- **SQL basics**: `CREATE TABLE` (columns, types), `INSERT INTO`, `SELECT ... FROM`, optional `WHERE`. Enough to create a simple table, insert a row, and query it.
- **Foreign keys** (concept): One table referencing another (e.g. project_id in articles); why and when.
- **ORM (concept)**: What an ORM does (map Python objects to tables); SQLAlchemy will be used in Day 2 — here we do raw SQL first so the idea of "table, row, query" is clear.

---

## Suggested practice (Foundation)

1. **Script 1 — Create DB and table**: Use `sqlite3` to create a database file, create one simple table (e.g. `projects` with `id`, `name`, `created_at`), run `CREATE TABLE` via `cursor.execute()`.
2. **Script 2 — Insert and select**: Insert one or two rows with `INSERT INTO`, then `SELECT` and print results. Use `conn.commit()` after inserts.
3. **Script 3 — Optional**: Second table with a foreign key to the first (e.g. `items` with `project_id`); one `INSERT` and one `SELECT` that joins or filters by `project_id`.

**Deliverables**: Small scripts in `Foundation/database_practice/` (e.g. `script_01_create_table.py`, `script_02_insert_select.py`) so you're comfortable with connection, cursor, execute, commit, close.

---

## Where this lives

- **Scripts**: `Foundation/database_practice/` (e.g. `script_01_create_table.py`, `script_02_insert_select.py`).
- **This plan**: `Foundation/database_practice/DATABASE_FUNDAMENTALS_PLAN.md`.
- **Day 2 (AI_SEO_Writer)**: Will use SQLAlchemy on top of SQLite; schema and functions (create_project, get_project, list_projects) live in the project.

---

## Order relative to API burst

- You can do **API fundamentals burst first**, then **Database fundamentals**, then resume Day 2.
- Or **Database fundamentals first**, then API burst, then Day 2.
- Both are part of the current Foundation phase before resuming AI_SEO_Writer Day 2.
