# Pizza-Review-agent
This project involves the development of a specialized AI agent designed to perform  (NLP) on customer feedback data. By leveraging a  (RAG) architecture, the system allows users to query a CSV dataset of pizza reviews using natural language, receiving context-aware answers in seconds. this agent provides grounded responses 
Technical Stack:

Large Language Model: Llama 3.2 (via Ollama) for high-quality reasoning and response generation.

Embedding Model: BGE-Embed (via Ollama) to convert textual data into high-dimensional vectors.

Orchestration: LangChain, used to manage the data pipeline, document loading, and retrieval logic.

Storage: A Vector Database (ChromaDB) for efficient similarity searches.


Workflow:

Data Ingestion: The system loads a CSV file containing various pizza reviews.

Vectorization: The text is split into chunks and converted into embeddings using the BGE-Embed model. These are stored in a local vector database.

Retrieval & Generation: When a user asks a question (e.g., "What do people think about the crust?"), the system searches the vector database for the most relevant review snippets.

Contextual Answer: These snippets are fed into Llama 3.2, which synthesizes a concise, accurate response based strictly on the retrieved reviews.
