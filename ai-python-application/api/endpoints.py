from fastapi import APIRouter
from schemas.schemas import InquiryRequest, LinkResponse

router = APIRouter()

@router.post("/inquiry", response_model=LinkResponse)
def inquiry(request: InquiryRequest):
    # For now, just return a static message
    return {"link": "Chatbot will start soon"}
