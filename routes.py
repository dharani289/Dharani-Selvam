from fastapi import APIRouter
from ai_core.gemini_generator import generate_document

router = APIRouter()

@router.post("/generate")
def generate(data: dict):
    result = generate_document(
        data.get("document_type"), data.get("parties"), data.get("terms"), data.get("dates"))
    return {"document": result}