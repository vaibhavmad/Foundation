# API Fundamentals Burst — Plan

**Purpose**: Short "API fundamentals" learning phase in Foundation before resuming AI_SEO_Writer Day 2. Learn APIs in a general sense (not only OpenAI) using **~15 scripts** covering all scenarios. First 3 guided (code in steps + you read docs); Tasks 4–15 unguided (task only — you struggle, find docs, fix errors, learn). Makes learning concrete.

**Status**: In progress. Topics finalised Feb 1, 2026. Script 1 complete (Jan 26). AI_SEO_Writer paused for this burst.
**Current**: Script 2 next (Guided — API key GET). Topic 4 — Data format (JSON) covered.

**After this**: Do Database (SQLite) fundamentals per `Foundation/database_practice/DATABASE_FUNDAMENTALS_PLAN.md`, then resume AI_SEO_Writer Day 2 (Database setup), then Day 3–4 (OpenAI) with the same mental model.

---

## Topics to learn / cover (FINAL — February 1, 2026)

1. **What is an API**
   - API = your code sends a request to another service and gets a structured response back.
   - We use HTTP (GET, POST) and JSON; no need to build our own API yet — we *consume* APIs.

2. **HTTP basics**
   - **Methods**: GET (read/fetch data; params in URL or query string) vs POST (send data; often in request body).
   - **URL**: Base URL, path (endpoint), query parameters (e.g. `?city=London`).
   - **Request body**: Used with POST; often JSON. GET typically has no body.
   - **Status codes**: 200 (OK), 400 (bad request), 401 (unauthorized), 403 (forbidden), 404 (not found), 429 (rate limit), 500 (server error). How to check in code: `response.status_code`.

3. **Authentication**
   - **No auth**: Some APIs are public (e.g. JSONPlaceholder, REST Countries).
   - **API key**: Secret credential; never hardcode — use `.env`, load with `python-dotenv` + `os.getenv()`. Pass key in header (e.g. `Authorization`) or query param per API docs. Check "no key" and exit with a clear error.

4. **Data format — JSON**
   - **What**: Key–value pairs and arrays; human-readable text format. APIs often send and receive JSON.
   - **In Python**: Parse with `response.json()` (from `requests`) or SDK’s response object. Access data: dict keys, list indices, nested objects.
   - **Sending**: Build a Python dict; pass as `json=...` (requests) or let SDK build the body.

5. **Making the request (Python)**
   - **Using `requests`**: `requests.get(url, params=..., headers=...)`, `requests.post(url, json=..., headers=...)`. Response: `.status_code`, `.json()`, `.text`.
   - **Using an SDK** (e.g. OpenAI): `client.some_method(...)`; SDK does HTTP for you. Response shape is in the SDK docs (e.g. `response.choices[0].message.content`).

6. **Errors and handling**
   - **What can go wrong**: Missing or invalid API key (401), rate limit (429), timeout, server error (500), empty or malformed response.
   - **How to handle**: Use try/except; check `response.status_code` before parsing; parse error body if API returns JSON errors; print clear message and exit or retry. Guard for empty content (e.g. `if not headline`).

7. **Developer process (same for any API)**
   - **Docs** → find base URL, auth, endpoints, parameters, response format, errors/rate limits.
   - **Auth** → none or load key from `.env`, pass per docs.
   - **Request** → build URL/body, send (requests or SDK).
   - **Response** → check status, then parse (e.g. `.json()` or SDK).
   - **Errors** → handle missing key, 4xx/5xx, timeout; don’t crash silently.

---

## Script approach: Guided (1–3) vs Unguided (4–15)

- **Scripts 1–3 — Guided**: AI writes code in steps and shares details. You do the **API documentation reading** to find useful info (base URL, auth, endpoints, params, response shape). You ask doubts as we go. Builds the pattern with support.
- **Tasks 4–15 — Unguided**: AI only gives the task: *"Write an API script to do X using Y API."* No step-by-step code. You: read the API docs, write the script, run into errors, fix them, and get it working. Struggle → fix → learn. Makes learning concrete and sticks.

---

## Scripts 1–3: Guided (code in steps; you read docs, ask doubts)

### Script 1: No-auth GET — JSONPlaceholder or REST Countries

- **API**: JSONPlaceholder (https://jsonplaceholder.typicode.com) or REST Countries (https://restcountries.com)
- **Auth**: None. No key, no signup.
- **Goal**: GET request, parse JSON, print part of response.
- **Your part**: Read API docs (base URL, endpoints, response format). Ask any doubts.
- **AI part**: Write code in steps with details.
- **Deliverable**: `script_01_no_auth_get.py` — fetches and prints a slice of the JSON.

### Script 2: API key GET with params — OpenWeatherMap or Open-Meteo

- **API**: OpenWeatherMap (free tier, key required) or Open-Meteo (no key).
- **Auth**: API key from `.env`, passed in query or header per API docs.
- **Goal**: GET with query params (e.g. city or lat/lon), parse JSON, print temp or similar.
- **Your part**: Read API docs (auth, params, response). Ask any doubts.
- **AI part**: Write code in steps with details.
- **Deliverable**: `script_02_key_get.py` — key from env, prints a field (e.g. temperature).

### Script 3: Existing OpenAI flow (key → request → response → errors)

- **Location**: AI_SEO_Writer `backend/tests/test_openai.py` (already exists).
- **Goal**: Same process — docs → auth → request → response → parse → errors.
- **Your part**: Read OpenAI API docs (optional refresh). Ask any doubts.
- **AI part**: Walk through code in steps; map each part to the process.
- **Action**: No new script; review/run `test_openai.py` and map to the developer flow.

---

## Tasks 4–15: Unguided (task only; you struggle, find docs, fix errors)

- **Format**: AI gives only: *"Write an API script to do X using Y API."* (X = goal, Y = API name or link.)
- **You**: Find the API docs, figure out base URL, auth, endpoints, params, response. Write the script. Run it. Hit errors. Read errors, check docs, fix. Repeat until it works.
- **AI**: No step-by-step code. Only the task. You can ask for hints or error help after you’ve tried.
- **Goal**: Concrete learning — docs → code → errors → fix → working script. Covers different scenarios (different methods, auth, JSON shapes, errors).

**Tasks 4–15 (unguided — task only; you read docs, write script, fix errors):**

| # | Task | Practices |
|---|------|-----------|
| **4** | Write an API script to fetch a list of 5 random dog image URLs using the [Dog CEO API](https://dog.ceo/dog-api/). | No-auth GET, JSON with list/`message`, extract string values. |
| **5** | Write an API script to fetch a random cat fact using the [Cat Facts API](https://catfact.ninja/) and save it to a text file. | No-auth GET, parse response, file I/O. |
| **6** | Write an API script to fetch today’s weather (temperature + wind speed) for a given latitude/longitude using the [Open-Meteo API](https://open-meteo.com/en/docs). | No-auth GET, query params (`latitude`, `longitude`), nested JSON. |
| **7** | Write an API script to fetch country details (capital, population, currencies) by country name or code using the [REST Countries API](https://restcountries.com/). | No-auth GET, path or query params, array response, nested fields. |
| **8** | Write an API script to retrieve one random user profile (name, email, location) using the [Random User Generator API](https://randomuser.me/documentation). | No-auth GET, nested JSON (`results` array), extract specific fields. |
| **9** | Write an API script to get the current exchange rate from USD to INR using a free currency API (e.g. [ExchangeRate-API](https://www.exchangerate-api.com/) free tier). | API key in header or query, `.env`, error handling (401/403). |
| **10** | Write an API script to create a new post (`title`, `body`, `userId`) using the [JSONPlaceholder API](https://jsonplaceholder.typicode.com/) `/posts` endpoint. | POST with JSON body, `Content-Type: application/json`, handle response. |
| **11** | Write an API script to update only the title of an existing post (e.g. post ID 1) using the [JSONPlaceholder API](https://jsonplaceholder.typicode.com/) `/posts/{id}` endpoint. | PATCH with partial JSON payload (vs full PUT). |
| **12** | Write an API script to fully replace an existing post (e.g. post ID 1) with new `title`, `body`, and `userId` using the [JSONPlaceholder API](https://jsonplaceholder.typicode.com/) `/posts/{id}` endpoint. | PUT with full JSON body; contrast with PATCH. |
| **13** | Write an API script to fetch the first 10–20 public repositories of a given GitHub username using the [GitHub REST API](https://docs.github.com/en/rest). | GET, path/query params, pagination (`per_page`), optional token (rate limits). |
| **14** | Write an API script to fetch public holidays for a given country and year using the [Nager.Date API](https://date.nager.at/Api). | GET, path parameters (`/api/v2/publicholidays/{year}/{countryCode}`), array of objects. |
| **15** | Write an API script using the **OpenAI Python SDK** to send a short prompt (e.g. “The weather today is”) and print the generated text completion. | SDK (not raw `requests`), API key from `.env`, nested response (`choices[0].message.content`). |

**Why this sequence:** No-auth GET (4–8) → API key GET (9) → POST (10) → PATCH (11) → PUT (12) → pagination / path params (13–14) → SDK (15). Covers GET/POST/PUT/PATCH, no-auth vs key, query vs path params, arrays and nested JSON, file I/O, and SDK usage. All APIs are free and well-documented.

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
