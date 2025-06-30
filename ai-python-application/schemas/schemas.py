from pydantic import BaseModel

class InquiryRequest(BaseModel):
    userquery: str

class LinkResponse(BaseModel):
    link: str

    class Config:
        orm_mode = True 