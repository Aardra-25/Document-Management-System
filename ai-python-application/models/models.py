from sqlalchemy import Column, Integer, Text
from db.database import Base

class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(Text, nullable=False)
    link = Column(Text, nullable=False) 