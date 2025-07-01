from pydoc import doc
import httpx

class DocumentServiceClient:
    async def fetch_document(self,project_name: str) -> str:
        java_backend_url = f"http://localhost:8080/document"
        async with httpx.AsyncClient() as client:
            response = await client.get(java_backend_url)
            
            return response.text
    


    