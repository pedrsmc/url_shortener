from fastapi import APIRouter
from services.url_services import (
    generate_short_code
)

router = APIRouter()

@router.get("/")
def initial_page():
    return {"msg": "API funcionando! 🟢"}

@router.get("/generate")
def generate():
    code = generate_short_code()
    return {"code": code}
