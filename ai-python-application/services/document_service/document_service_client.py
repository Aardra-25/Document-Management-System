import httpx
from bs4 import BeautifulSoup
import sys
import os

from db.chroma_db import add_document_para, search_documents

class DocumentServiceClient:
    def __init__(self):
        pass

    def store_in_chromadb(self, project_name: str, content: str, link: str):
        try:
            document_ids = add_document_para(
               project_name=project_name,
               link=link,
               content=content
           )
            print(f"Document stored in ChromaDB with IDs: {document_ids}")
        except Exception as e:
            print(f"Warning: Failed to store document in ChromaDB: {e}")

    async def fetch_document(self, project_name: str) -> str:
        java_backend_url = f"http://localhost:8080/document"
        async with httpx.AsyncClient() as client:
            response = await client.get(java_backend_url)
            link = "https://en.wikipedia.org/wiki/Maple_syrup"
            content = await self.fetch_data(project_name, link)
            self.store_in_chromadb(project_name, content, link)
            return response.text, content

    async def fetch_data(self, project_name: str, link: str) -> str:
        async with httpx.AsyncClient() as client:
            response = await client.get(link)
            soup = BeautifulSoup(response.text, "html.parser")
            content_div = soup.find("div", {"id": "mw-content-text"})
            if content_div:
                paragraphs = [p.get_text(strip=True) for p in content_div.find_all("p") if p.get_text(strip=True)]
                return "\n\n".join(paragraphs)
            return "Content not found"

    def search_documents(self, query: str, n_results: int = 5):
        
        try:
            return search_documents(query, n_results)
        except Exception as e:
            return {"error": f"ChromaDB not available: {e}"}


