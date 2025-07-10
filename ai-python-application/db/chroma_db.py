import chromadb
from chromadb.utils import embedding_functions
from core.config_chromadb import config

client = chromadb.PersistentClient(path=config.DATA_PATH)

embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name=config.EMBED_MODEL
)

collection = client.get_or_create_collection(
    name="documents",
    embedding_function=embedding_func
)

def get_embedding(text: str):
    return embedding_func([text])[0]

def split_by_paragraphs(content):
    return [para.strip() for para in content.split("\n\n") if para.strip()]

def add_document_para(project_name, link, content):
    chunks = split_by_paragraphs(content)
    
    total = len(chunks)
    ids = [
        f"{project_name}_{link.split('/')[-1]}_{i+1}_of_{total}"
        for i in range(total)
    ]
    embeddings = [get_embedding(chunk) for chunk in chunks]
    metadatas = [
        {"project_name": project_name, "link": link, "section_number": i+1, "total_sections": total}
        for i in range(total)
    ]
    collection.add(
        documents=chunks,
        ids=ids,
        embeddings=embeddings,
        metadatas=metadatas
    )
    return ids

def search_documents(query, n_results=5):
    return collection.query(query_texts=[query], n_results=n_results)
