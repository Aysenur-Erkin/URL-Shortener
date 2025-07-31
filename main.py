from fastapi import FastAPI, HTTPException, Depends
from fastapi.responses import RedirectResponse
from sqlmodel import select, Session
from random import choices
import string

from models import URL
from database import init_db, get_session


app = FastAPI(title="FastAPI URL Shortener")
init_db()

ALPHABET = string.ascii_letters + string.digits

def gen_slug(k: int = 6) -> str:
    return ''.join(choices(ALPHABET, k=k))

@app.post("/shorten", status_code=201)
def create_short_url(target_url: str, session: Session = Depends(get_session)):
    slug = gen_slug()
    while session.exec(select(URL).where(URL.slug == slug)).first():
        slug = gen_slug(7)
    url = URL(slug=slug, target_url=target_url)
    session.add(url)
    session.commit()
    session.refresh(url)
    return {"short_url": f"/{url.slug}"}

@app.get("/{slug}")
def redirect(slug: str, session: Session = Depends(get_session)):
    url = session.exec(select(URL).where(URL.slug == slug)).first()
    if not url:
        raise HTTPException(status_code=404, detail="Slug not found")
    url.clicks += 1
    session.add(url)
    session.commit()
    return RedirectResponse(url.target_url)

@app.get("/stats/{slug}")
def stats(slug: str, session: Session = Depends(get_session)):
    url = session.exec(select(URL).where(URL.slug == slug)).first()
    if not url:
        raise HTTPException(status_code=404, detail="Slug not found")
    return {
        "target_url": url.target_url,
        "clicks": url.clicks,
        "created_at": url.created_at
    }

