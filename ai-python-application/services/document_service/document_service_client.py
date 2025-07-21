import httpx
from bs4 import BeautifulSoup
import sys
import os

from db.chroma_db import add_document_para, search_documents

class DocumentServiceClient:
    def __init__(self):
        pass

    def store_in_chromadb(self, project_name: str, document_name: str, content: str, link: str, created_by: str = None):
        try:
            document_ids = add_document_para(
               project_name=project_name,
               link=link,
               content=content,
               document_name=document_name,
               created_by=created_by
           )
            print(f"Document stored in ChromaDB with IDs: {document_ids}")
        except Exception as e:
            print(f"Warning: Failed to store document in ChromaDB: {e}")

    async def fetch_document(self, project_name: str, document_name: str, created_by: str = None) -> (str, list):
        java_backend_url = f"http://localhost:8080/documents/projectName/{document_name}"
        async with httpx.AsyncClient() as client:
            response = await client.get(java_backend_url)
            if response.status_code != 200:
                print(f"Failed to fetch documents from Java backend: {response.status_code}")
                return "", []
            try:
                documents = response.json()
            except Exception as e:
                print(f"Failed to parse JSON from Java backend: {e}")
                return "", []
            if not isinstance(documents, list) or not documents:
                print("No documents found in Java backend response.")
                return "", []
            contents = []
            for doc in documents:
                link = doc.get("filePath")
                doc_name = doc.get("documentName", document_name)
                proj_name = doc.get("projectName", project_name)
                creator = doc.get("createdBy", created_by)
                if not link:
                    continue
                content = await self.fetch_data(doc_name, link)
                self.store_in_chromadb(proj_name, doc_name, content, link, creator)
                contents.append({"link": link, "content": content, "project_name": proj_name, "document_name": doc_name, "created_by": creator})
            return response.text, contents

    async def fetch_data(self, document_name: str, link: str) -> str:
        async with httpx.AsyncClient() as client:
            response = await client.get(link)
            soup = BeautifulSoup(response.text, "html.parser")
            paragraphs = [p.get_text(strip=True) for p in soup.find_all("p") if p.get_text(strip=True)]
            if paragraphs:
                return "\n\n".join(paragraphs)
            return "Content not found"

    def search_documents(self, query: str, n_results: int = 5):
        try:
            return search_documents(query, n_results)
        except Exception as e:
            return {"error": f"ChromaDB not available: {e}"}


