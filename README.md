# FastAPI URL Shortener

A minimal, production-ready URL shortening service built with **FastAPI** and **SQLite**, featuring API documentation, click tracking, and easy deployment.

Long, unwieldy URLs can be a hassle to share, remember, or type. This service streamlines the process by converting lengthy links into short, human-friendly slugs and automatically redirecting users to the original address—while also tracking click counts for simple analytics.

---

## Features

* **Shorten URLs** via a clean RESTful endpoint
* **Redirect** shortened slugs to their original URLs
* **Click tracking**: store and retrieve visit counts per slug
* **OpenAPI / Swagger** UI auto-generated at `/docs`
* **Automatic database migrations** with SQLModel
* **Lightweight**: single-file SQLite database, no external services

---

## Tech Stack

* **Python** 3.9+
* **FastAPI**: high‑performance ASGI web framework
* **SQLModel**: ORM for SQLite built on SQLAlchemy & Pydantic
* **Uvicorn**: ASGI server for development
* **Pytest** & **HTTPX**: testing framework and HTTP client

---

## Directory Structure

```plaintext
URL-Shortener/
├── main.py               # FastAPI application and endpoints
├── models.py             # URL data model definitions
├── database.py           # Database setup and connection
├── requirements.txt      # Python dependencies
├── .gitignore            # Ignored files and folders
├── urls.db               # SQLite database (created at runtime)
├── tests/                # Automated tests
│   └── test_api.py       # Test suite for API endpoints
└── README.md             # Project documentation
```

---

## Prerequisites

* **Python** 3.9 or higher
* **pip** package manager
* (Optional) **virtualenv** or **venv** for isolation

---

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Aysenur-Erkin/URL-Shortener.git
   cd URL-Shortener
   ```
2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   # Windows PowerShell
   .\venv\Scripts\Activate.ps1
   # Windows CMD
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate
   ```
3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## Configuration

By default, the service uses a local SQLite database `urls.db` in the project root. To point to another database, edit the `DATABASE_URL` constant in **database.py**:

```python
# database.py
DATABASE_URL = "sqlite:///./urls.db"
# For PostgreSQL:
# DATABASE_URL = "postgresql://user:password@localhost/dbname"
```

---

## Usage

1. **Start the server**

   ```bash
   uvicorn main:app --reload
   ```
2. **Open the API docs**
   Navigate to `http://127.0.0.1:8000/docs` in your browser
3. **Shorten a URL**

   * **Linux/macOS or Windows with real curl**:

     ```bash
     curl.exe -X POST "http://127.0.0.1:8000/shorten?target_url=https://example.com"
     ```
   * **PowerShell**:

     ```powershell
     Invoke-RestMethod -Method POST "http://127.0.0.1:8000/shorten?target_url=https://example.com"
     ```

   **Response**:

   ```json
   { "short_url": "/Ab3xQ2" }
   ```
4. **Redirect by slug**
   Open `http://127.0.0.1:8000/Ab3xQ2` in your browser to be redirected
5. **Get statistics**

   ```bash
   curl http://127.0.0.1:8000/stats/Ab3xQ2
   # {"target_url":"https://example.com","clicks":1,"created_at":"2025-07-31T17:45:00"}
   ```

---

## API Reference

| Method | Path            | Query / Params        | Description                                         |
| ------ | --------------- | --------------------- | --------------------------------------------------- |
| POST   | `/shorten`      | `target_url` (string) | Generate a new slug and return `{ "short_url" }`    |
| GET    | `/{slug}`       | Path param `slug`     | Redirect to original URL                            |
| GET    | `/stats/{slug}` | Path param `slug`     | Return JSON with `{target_url, clicks, created_at}` |

---

## Testing

Automated tests use **pytest** and **HTTPX**.

1. **Run tests**

   ```bash
   pytest -q
   ```
2. **Coverage report** (optional)

   ```bash
   pip install pytest-cov
   pytest --cov=.
   ```




