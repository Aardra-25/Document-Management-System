from pydantic import BaseModel
from typing import Dict, Any, List, Optional

class InquiryRequest(BaseModel):
    userquery: str

class LinkResponse(BaseModel):
    link: str

    class Config:
        orm_mode = True

class DocumentResponse(BaseModel):
    java_response: Optional[str] = None
    content: Optional[str] = None
    document_id: Optional[str] = None
    message: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None
    error: Optional[str] = None

    class Config:
        orm_mode = True

class SearchResponse(BaseModel):
    query: str
    results: Dict[str, Any]
    total_results: int

    class Config:
        orm_mode = True 