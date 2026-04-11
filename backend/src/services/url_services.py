import random
import string
from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.url_models import URL
from schemas.url_schema import UrlCreate

def generate_short_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=5))

def create_url(db: Session, url_data: UrlCreate):
    short_code = generate_short_code()

    while db_url := db.query(URL).filter(URL.short_code == short_code).first():
        short_code = generate_short_code()
    
    db_url = URL(
        original_url=str(url_data.target_url),
        short_code=short_code
    )
    
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    
    return db_url

def redirect_url(short_code: str, db: Session):
    db_url = db.query(URL).filter(URL.short_code == short_code).first()

    if not db_url:
        raise HTTPException(status_code=404, detail="URL não encontrada")
    
    db_url.clicks += 1
    db.commit()

    return db_url.original_url