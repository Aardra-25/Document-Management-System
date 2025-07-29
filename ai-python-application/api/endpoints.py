from fastapi import APIRouter
from schemas.schemas import InquiryRequest, LinkResponse, DocumentResponse, SearchResponse
from services.document_service.document_service_client import DocumentServiceClient
from services.ai.llm.llm_service import ask_model

router = APIRouter()
document_service_client = DocumentServiceClient()


"""
Endpoint to fetch document links and metadata from the Java backend based on project, document, and creator.
"""
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


"""
Endpoint to search documents in ChromaDB using a query string and return the top N results.
"""
@router.get("/chroma/search", response_model=SearchResponse)
async def search_documents(query: str, n_results: int = 5):
    
    results = document_service_client.search_documents(query, n_results)
    return {
        "query": query,
        "results": results,
        "total_results": len(results.get('ids', [])) if isinstance(results, dict) and results.get('ids') else 0
    }


"""
Endpoint to ask a question with context retrieved from the most relevant documents in ChromaDB.
"""
@router.post("/ask")
async def ask_with_context(data: dict):
    user_query = data.get("query")
    if not user_query:
        return {"error": "No query provided."}
    chroma_results = document_service_client.search_documents(user_query, n_results=3)
    chunks = []
    if isinstance(chroma_results, dict) and chroma_results.get('documents'):
        chunks = chroma_results['documents'][0] if isinstance(chroma_results['documents'][0], list) else chroma_results['documents']
    context = '\n'.join(chunks)
    prompt = f"Context:\n{context}\n\nQuestion: {user_query}\nAnswer:"
    answer = ask_model(prompt)
    return {"answer": answer}


