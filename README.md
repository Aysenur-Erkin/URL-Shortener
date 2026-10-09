# URL-Shortener

A small URL shortener I wrote to learn FastAPI and SQLModel.

You send it a long URL, it gives back a 6-character slug. Opening `/<slug>` redirects to the original URL and counts the click. `/stats/<slug>` shows the click count.

Data is kept in a local SQLite file (`urls.db`), created in the folder you run the server from.

## Run

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Swagger UI: http://127.0.0.1:8000/docs

## Endpoints

| Method | Path | Does |
|---|---|---|
| POST | `/shorten?target_url=...` | creates a slug, returns `{"short_url": "/Ab3xQ2"}` |
| GET | `/{slug}` | redirects to the original URL, clicks + 1 |
| GET | `/stats/{slug}` | returns target URL, click count, creation time |

Unknown slugs return 404.

Example (PowerShell):

```powershell
Invoke-RestMethod -Method POST "http://127.0.0.1:8000/shorten?target_url=https://example.com"
Invoke-RestMethod "http://127.0.0.1:8000/stats/Ab3xQ2"
```

```json
{"target_url":"https://example.com","clicks":1,"created_at":"2025-07-31T17:45:00"}
```

## Test

```bash
python -m pytest
```

One test covers the full flow: shorten, check stats (0 clicks), visit, check stats again (1 click).

## Known limits

- `target_url` is not validated, any string is accepted.
- Slugs come from `random`, not `secrets`, so they are guessable.
- No migrations: tables are created with `create_all` on startup.
- No auth or rate limiting. This is a learning project, not something to put on the internet as is.
