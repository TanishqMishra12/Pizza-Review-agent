"""
RAG (Retrieval-Augmented Generation) system for pizza review queries.
"""
import os
from typing import List, Dict, Any
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.schema import Document
from dotenv import load_dotenv


class PizzaReviewRAG:
    """RAG system for querying pizza reviews using natural language."""
    
    def __init__(self, documents: List[Dict[str, str]], persist_directory: str = "./chroma_db"):
        """
        Initialize the RAG system with documents.
        
        Args:
            documents: List of document dictionaries with 'text' and 'metadata'
            persist_directory: Directory to persist the vector database
        """
        load_dotenv()
        
        # Validate API key
        if not os.getenv("OPENAI_API_KEY"):
            raise ValueError("OPENAI_API_KEY not found in environment variables")
        
        self.persist_directory = persist_directory
        self.documents = documents
        self.vectorstore = None
        self.qa_chain = None
        
        # Initialize embeddings
        embedding_model = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")
        self.embeddings = OpenAIEmbeddings(model=embedding_model)
        
        # Initialize LLM
        llm_model = os.getenv("LLM_MODEL", "gpt-3.5-turbo")
        self.llm = ChatOpenAI(model=llm_model, temperature=0)
        
    def setup_vectorstore(self):
        """Create and populate the vector database with review documents."""
        # Convert documents to LangChain Document format
        langchain_docs = [
            Document(page_content=doc['text'], metadata=doc['metadata'])
            for doc in self.documents
        ]
        
        # Create vector store with embeddings
        self.vectorstore = Chroma.from_documents(
            documents=langchain_docs,
            embedding=self.embeddings,
            persist_directory=self.persist_directory
        )
        
        print(f"✓ Vector database created with {len(langchain_docs)} documents")
        
    def setup_qa_chain(self):
        """Setup the question-answering chain with retrieval."""
        if self.vectorstore is None:
            raise ValueError("Vector store not initialized. Call setup_vectorstore() first.")
        
        # Create retriever
        retriever = self.vectorstore.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 5}  # Retrieve top 5 most relevant reviews
        )
        
        # Create QA chain
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=retriever,
            return_source_documents=True,
            verbose=False
        )
        
        print("✓ QA chain initialized")
        
    def query(self, question: str) -> Dict[str, Any]:
        """
        Query the RAG system with a natural language question.
        
        Args:
            question: Natural language question about pizza reviews
            
        Returns:
            Dictionary containing the answer and source documents
        """
        if self.qa_chain is None:
            raise ValueError("QA chain not initialized. Call setup_qa_chain() first.")
        
        # Execute query
        result = self.qa_chain({"query": question})
        
        # Format response
        response = {
            'question': question,
            'answer': result['result'],
            'source_reviews': []
        }
        
        # Extract source review information
        for doc in result['source_documents']:
            source_info = {
                'text': doc.page_content,
                'metadata': doc.metadata
            }
            response['source_reviews'].append(source_info)
        
        return response
    
    def initialize(self):
        """Initialize the complete RAG system (vectorstore and QA chain)."""
        print("Initializing Pizza Review RAG System...")
        self.setup_vectorstore()
        self.setup_qa_chain()
        print("✓ RAG system ready for queries!\n")
