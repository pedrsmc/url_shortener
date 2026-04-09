from pydantic import BaseModel, HttpUrl
import datetime

class UrlCreate (BaseModel):
    target_url: HttpUrl

class Url (BaseModel):
    id = int
    original_url = str
    short_code = str
    clicks = int
    created_at = datetime

class Config:
    from_attributes = True