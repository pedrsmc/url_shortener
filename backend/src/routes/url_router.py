from fastapi import APIRouter, Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
from database.url_database import get_db
from schemas.url_schema import UrlCreate

from services.url_services import (
    create_url,
    redirect_url
)

router = APIRouter()

@router.get("/")
def initial_page():
    return {"msg": "API funcionando! 🟢"}

@router.post("/shortener")
def generate_url(url_data: UrlCreate, db: Session = Depends(get_db)):
    new_url = create_url(db=db, url_data=url_data)
    
    return {
        "short_code": new_url.short_code,
        "short_url": f"http://localhost:8000/{new_url.short_code}",
        "original_url": new_url.original_url
    }

@router.get("/{short_code}")
def get_url(short_code: str, db: Session = Depends(get_db)):
    url = redirect_url(short_code, db)

    if url:
        return RedirectResponse(url)