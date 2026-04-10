from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.url_database import get_db
from services.url_services import create_url
from schemas.url_schema import UrlCreate

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