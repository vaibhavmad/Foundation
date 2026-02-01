# API Fundamentals Burst — Plan

**Purpose**: Short "API fundamentals" learning phase in Foundation before resuming AI_SEO_Writer Day 2. Learn APIs in a general sense (not only OpenAI) using 2–3 small scripts and the same developer process.

**Status**: Not started. AI_SEO_Writer paused for this burst.

**After this**: Do Database (SQLite) fundamentals per `Foundation/database_practice/DATABASE_FUNDAMENTALS_PLAN.md`, then resume AI_SEO_Writer Day 2 (Database setup), then Day 3–4 (OpenAI) with the same mental model.

---

## Scripts (2–3 hours total)

### Script 1: No-auth GET — JSONPlaceholder or REST Countries

- **API**: JSONPlaceholder (https://jsonplaceholder.typicode.com) or REST Countries (https://restcountries.com)
- **Auth**: None. No key, no signup.
- **Goal**: GET request, parse JSON, print part of response.
- **Learn**: Base URL, endpoint path, query params (if any), `requests.get()`, `response.json()`, status code (200).
- **Deliverable**: One small script (e.g. `script_01_no_auth_get.py`) that fetches and prints a slice of the JSON.

### Script 2: API key GET with params — OpenWeatherMap or Open-Meteo

- **API**: OpenWeatherMap (free tier, key required) or Open-Meteo (no key).
- **Auth**: API key from `.env` (e.g. `OPENWEATHER_API_KEY`), passed in query or header per API docs.
- **Goal**: GET with query params (e.g. city or lat/lon), parse JSON, print temp or similar.
- **Learn**: Key in `.env`, `os.getenv()`, build URL or headers, same parse/error flow.
- **Deliverable**: One small script (e.g. `script_02_key_get.py`) that uses key from env and prints a field (e.g. temperature).

### Script 3: Existing OpenAI flow (key → request → response → errors)

- **Location**: AI_SEO_Writer `backend/tests/test_openai.py` (already exists).
- **Goal**: Treat it as the same process: docs → auth (key from `.env`) → request (client.chat.completions.create) → response (content, usage) → parse → errors (no key, empty response).
- **Learn**: Same mental model as Script 1 and 2; SDK wraps HTTP (POST, JSON body, JSON response).
- **Action**: No new script; review or run `test_openai.py` and map each step to the process below.

---

## Learning coverage (must be covered)

- **HTTP**: GET vs POST; URL vs body; status codes (200, 400, 401, 429, 500) — what they mean and how to check in code.
- **Auth**: No auth (Script 1) vs API key in header or query (Script 2, Script 3); keys in `.env`, never in code.
- **Data**: JSON in and out; parsing and using it in Python (`response.json()`, or SDK’s response object).
- **Errors**: What can go wrong (bad key, rate limit, timeout) and how to handle it in code (try/except, check status, exit or retry).
- **Process**: docs → auth → request → response → parse → errors. Same for any API.

---

## Process (developer flow)

1. **Docs**: Find base URL, authentication, endpoints, parameters, response format, error/rate-limit info.
2. **Auth**: None vs API key; if key, load from `.env` and pass in header or query.
3. **Request**: Build URL/body and send (e.g. `requests.get(url, headers=..., params=...)` or SDK).
4. **Response**: Check status (e.g. 200 vs 401 vs 429), then parse (e.g. `.json()` or SDK).
5. **Errors**: Handle missing key, 4xx/5xx, timeout; log or print and exit or retry as appropriate.

---

## Where this lives

- **Scripts**: `Foundation/api_practice/` (e.g. `script_01_no_auth_get.py`, `script_02_key_get.py`).
- **OpenAI**: `AI_SEO_Writer/backend/tests/test_openai.py` (Script 3 — review/run, no copy).
- **This plan**: `Foundation/api_practice/API_FUNDAMENTALS_PLAN.md`.

---

## After the burst

- Do **Database (SQLite) fundamentals** (see `Foundation/database_practice/DATABASE_FUNDAMENTALS_PLAN.md`). Then resume AI_SEO_Writer: Day 2 (Database setup with SQLAlchemy), then Day 3–4 (OpenAI) with the same mental model (docs → auth → request → response → parse → errors).
