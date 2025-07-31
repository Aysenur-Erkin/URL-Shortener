# FastAPI URL Shortener

A minimal, production-ready URL shortening service built with **FastAPI** and **SQLite**, featuring API documentation, click tracking, and easy deployment.

---

## Features

* **Shorten URLs** via a RESTful endpoint
* **Redirect** shortened slugs to their original URLs
* **Click tracking**: store and retrieve the number of visits per slug
* **OpenAPI / Swagger** UI auto-generated at `/docs`
* **Automatic database migrations** with SQLModel
* **Lightweight**: single-file SQLite database, no external dependencies

## Tech Stack

* **Python** 3.9+
* **FastAPI**: high-performance ASGI web framework
* **SQLModel**: ORM for SQLite based on SQLAlchemy and Pydantic
* **Uvicorn**: ASGI server for local development
* **Pytest**, **HTTPX**: testing framework and HTTP client

## Directory Structure

```
url-shortener-fastapi/
├── main.py               # FastAPI application and endpoints
├── models.py             # URL data model definitions
├── database.py           # Database connection and migration
├── requirements.txt      # Project dependencies
├── .gitignore            # Excluded files (venv, cache, DB file)
├── urls.db               # SQLite database file (created at runtime)
├── tests/                # Automated tests
│   └── test_api.py       # Test suite for API endpoints
└── README.md             # Project documentation (this file)
```

## Prerequisites

* **Python** 3.9 or higher installed on your system
* **pip** package manager
* (Optional) **virtualenv** or **venv** for isolation

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your_username/url-shortener-fastapi.git
   cd url-shortener-fastapi
   ```
2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS / Linux
   source venv/bin/activate
   ```
3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

By default, the service uses a local SQLite database `urls.db` in the project root. To change the database URL, modify the `DATABASE_URL` constant in **database.py**:

```python
# database.py
DATABASE_URL = "sqlite:///./urls.db"
# For PostgreSQL, you could use:
# DATABASE_URL = "postgresql://user:password@localhost/dbname"
```

## Usage

1. **Start the server**

   ```bash
   uvicorn main:app --reload
   ```
2. **Access the interactive API docs**

   * Open your browser at: `http://127.0.0.1:8000/docs`
3. **Shorten a URL**

   ```bash
   curl -X POST "http://127.0.0.1:8000/shorten?target_url=https://example.com"
   # Response:
   # {"short_url": "/Ab3xQ2"}
   ```
4. **Redirect by slug**

   * Navigate to `http://127.0.0.1:8000/Ab3xQ2`
   * You will be redirected to `https://example.com`
5. **Get statistics**

   ```bash
   curl http://127.0.0.1:8000/stats/Ab3xQ2
   # Response:
   # {"target_url": "https://example.com", "clicks": 1, "created_at": "2025-07-31T17:45:00.123456"}
   ```

## API Reference

| Method | Path            | Query / Params        | Response                                   |
| ------ | --------------- | --------------------- | ------------------------------------------ |
| POST   | `/shorten`      | `target_url` (string) | `{ "short_url": "/{slug}" }`               |
| GET    | `/{slug}`       | path slug             | HTTP redirect to original URL              |
| GET    | `/stats/{slug}` | path slug             | `{ "target_url", "clicks", "created_at" }` |

## Testing

Automated tests are written with **pytest** and **HTTPX**.

1. **Run tests**

   ```bash
   pytest -q
   ```
2. **Test coverage** (optional)

   ```bash
   pip install pytest-cov
   pytest --cov=.
   ```

**Code Style**:

* Follow PEP8 guidelines
* Use meaningful commit messages in imperative form (e.g., `fix: handle slug collision`)

## Roadmap

* [ ] Custom slug endpoint (`POST /custom`)
* [ ] Redis caching for high-performance redirects
* [ ] Basic front-end with HTML form and JavaScript
* [ ] Dockerfile for containerized deployment
* [ ] CI/CD pipeline with GitHub Actions

