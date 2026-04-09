import random
import string
import schemas, models

def generate_short_code():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=5))

# def create_url(db: Session, url_data: UrlCreate):

    