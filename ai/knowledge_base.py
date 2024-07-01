from phi.embedder.openai import OpenAIEmbedder
from phi.knowledge.combined import CombinedKnowledgeBase
from phi.knowledge.pdf import PDFUrlKnowledgeBase, PDFKnowledgeBase
from phi.knowledge.website import WebsiteKnowledgeBase
from phi.vectordb.pgvector import PgVector2

from ai.settings import ai_settings
from db.session import db_url

pdf_knowledge_base = CombinedKnowledgeBase(
    sources=[
        
        PDFUrlKnowledgeBase(urls = ["https://tscout.s3.ap-southeast-1.amazonaws.com/ai-chatbot/1b7213f6-6e69-4870-9875-4624d61f6b5d/c72d13f2-dd8c-4c51-b59c-b800af5f66c2"])
    ],
    vector_db=PgVector2(
        db_url=db_url,
        # Store the embeddings in ai.pdf_documents
        collection="pdf_documents",
        embedder=OpenAIEmbedder(model=ai_settings.embedding_model),
    ),
    # 2 references are added to the prompt
    num_documents=1,
)

website_knowledge_base = WebsiteKnowledgeBase(
    # Add URLs to the knowledge base
    # urls=["https://docs.phidata.com/introduction"],
    max_depth=1,
    # Number of links to follow from the seed URLs
    max_links=15,
    vector_db=PgVector2(
        db_url=db_url,
        # Store the embeddings in ai.website_documents
        collection="website_documents",
        embedder=OpenAIEmbedder(model=ai_settings.embedding_model),
    ),
    # 3 references are added to the prompt
    num_documents=3,
)
