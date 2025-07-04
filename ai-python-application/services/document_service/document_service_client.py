from pydoc import doc
import httpx
from bs4 import BeautifulSoup

class DocumentServiceClient:
    async def fetch_document(self, project_name: str) -> str:
        java_backend_url = f"http://localhost:8080/document"
        async with httpx.AsyncClient() as client:
            response = await client.get(java_backend_url)
            link = "https://en.wikipedia.org/wiki/Maple_syrup"
            return response.text, await self.fetch_data(project_name, link)
            
    
    async def fetch_data(self, project_name: str, link: str) -> str:
        async with httpx.AsyncClient() as client:
            response = await client.get(link)
            soup = BeautifulSoup(response.text, "html.parser")
        
            content_div = soup.find("div", {"id": "mw-content-text"})
            if content_div:
                paragraphs = [p.get_text(strip=True) for p in content_div.find_all("p") if p.get_text(strip=True)]
                return "\n\n".join(paragraphs)
            return "Content not found"


