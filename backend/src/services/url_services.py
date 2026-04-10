import random
import string
from sqlalchemy.orm import Session
from models.url_models import URL
from schemas.url_schema import UrlCreate

def generate_short_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=5))

def create_url(db: Session, url_data: UrlCreate):
    short_code = generate_short_code()
    
    db_url = URL(
        original_url=str(url_data.target_url),
        short_code=short_code
    )
    
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    
    return db_url