from fastapi import APIRouter
from schemas.schemas import InquiryRequest, LinkResponse
from services.document_service.document_service_client import DocumentServiceClient

router = APIRouter()
document_service_client = DocumentServiceClient()

@router.post("/inquiry", response_model=LinkResponse)
def inquiry(request: InquiryRequest):
    return {"link": "Chatbot will start soon"}

@router.post("/link/{project_name}", response_model=LinkResponse)
async def document1(request: InquiryRequest, project_name: str):
    java_response, html_content = await document_service_client.fetch_document(project_name)
    return {"link": html_content}

@router.post("/document/{project_name}", response_model=LinkResponse)
async def document(request: InquiryRequest, project_name: str):
    java_response, html_content = await document_service_client.fetch_document(project_name)
    return {"link": f"{java_response}: It will be saved"}

