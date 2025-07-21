from fastapi import APIRouter
from schemas.schemas import InquiryRequest, LinkResponse, DocumentResponse, SearchResponse
from services.document_service.document_service_client import DocumentServiceClient

router = APIRouter()
document_service_client = DocumentServiceClient()

@router.post("/inquiry", response_model=LinkResponse)
def inquiry(request: InquiryRequest):
    return {"links": ["Chatbot will start soon"], "metadata": None}

@router.post("/link/", response_model=LinkResponse)
async def get_links(request: InquiryRequest):
    java_response, html_content = await document_service_client.fetch_document(
        request.project_name, request.document_name, request.created_by
    )
    links = [item["link"] for item in html_content]
    metadata = [
        {
            "project_name": item.get("project_name"),
            "document_name": item.get("document_name"),
            "link": item.get("link"),
            "created_by": item.get("created_by")
        }
        for item in html_content
    ]
    return {"links": links, "metadata": metadata}

@router.post("/document/", response_model=DocumentResponse)
async def get_document(request: InquiryRequest):
    java_response, html_content = await document_service_client.fetch_document(
        request.project_name, request.document_name, request.created_by
    )
    return {
        "java_response": java_response,
        "content": None,
        "document_id": None,
        "message": "Documents fetched and stored.",
        "metadata": html_content,
        "error": None
    }

@router.get("/chroma/search", response_model=SearchResponse)
async def search_documents(query: str, n_results: int = 5):
    
    results = document_service_client.search_documents(query, n_results)
    return {
        "query": query,
        "results": results,
        "total_results": len(results.get('ids', [])) if isinstance(results, dict) and results.get('ids') else 0
    }


