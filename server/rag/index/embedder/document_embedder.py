import os
from typing import List, Dict, Optional
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.schema.document import Document
from server.constant.constants import OPENAI_EMBEDDING_MODEL_NAME, CHROMA_DB_DIR, CHROMA_COLLECTION_NAME
from server.logger.logger_config import my_logger as logger


class DocumentEmbedder:
    BATCH_SIZE = 30

    def __init__(self) -> None:
        self.llm_name = os.getenv('LLM_NAME')
        if self.llm_name == 'OpenAI':
            embeddings = OpenAIEmbeddings(
                openai_api_key=os.getenv('OPENAI_API_KEY'),
                model=OPENAI_EMBEDDING_MODEL_NAME)
        else:
            raise ValueError(f"Unsupported LLM_NAME '{self.llm_name}'. Must be in ['OpenAI'].")

        collection_name = CHROMA_COLLECTION_NAME
        persist_directory = CHROMA_DB_DIR
        logger.info(f"[DOC_EMBEDDER] init, collection_name: '{collection_name}', persist_directory: '{persist_directory}', llm_name: '{self.llm_name}'")
        collection_metadata = {"hnsw:space": "cosine"}
        self.chroma_vector = Chroma(
                collection_name=collection_name,
                embedding_function=embeddings,
                persist_directory=persist_directory,
                collection_metadata=collection_metadata)

    async def aadd_local_file_embedding(self,
        doc_id: int,
        url: str,
        chunk_text_vec: List[str],
        doc_source: int
    ) -> List[str]:
        file_documents_to_add = []
        for part_index, part_content in enumerate(chunk_text_vec):
            metadata: Dict[str, str] = {"source": url, "id": f"{doc_source}-{doc_id}-part{part_index}"}
            doc = Document(page_content=part_content, metadata=metadata)
            file_documents_to_add.append(doc)

        if file_documents_to_add:
            embedding_id_vec = await self.chroma_vector.aadd_documents(file_documents_to_add)
            logger.info(f"[DOC_EMBEDDER] doc_id={doc_id}, url={url}, doc_source={doc_source}, added {len(file_documents_to_add)} chunk parts to Chroma, embedding_id_vec={embedding_id_vec}")
            return embedding_id_vec
        else:
            return []

    async def adelete_document_embedding(self, embedding_id_vec: List[str]) -> Optional[bool]:
        for start in range(0, len(embedding_id_vec), self.BATCH_SIZE):
            batch = embedding_id_vec[start:start + self.BATCH_SIZE]
            await self.chroma_vector.adelete(batch)
        logger.info(f"[DOC_EMBEDDER] Deleted {len(embedding_id_vec)} embeddings from Chroma.")

    def delete_document_embedding(self, embedding_id_vec: List[str]) -> None:
        for start in range(0, len(embedding_id_vec), self.BATCH_SIZE):
            batch = embedding_id_vec[start:start + self.BATCH_SIZE]
            self.chroma_vector.delete(batch)
        logger.info(f"[DOC_EMBEDDER] Deleted {len(embedding_id_vec)} embeddings from Chroma.")


document_embedder = DocumentEmbedder()
