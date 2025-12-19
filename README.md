# 🍕 Pizza Review Agent

A specialized AI agent designed to perform **Natural Language Processing (NLP)** on customer feedback data. By leveraging a **Retrieval-Augmented Generation (RAG)** architecture, the system allows users to query a CSV dataset of pizza reviews using natural language, receiving context-aware answers in seconds. Unlike standard LLMs, this agent provides grounded responses based specifically on the provided review data.

## 🌟 Features

- **Natural Language Queries**: Ask questions about pizza reviews in plain English
- **RAG Architecture**: Combines document retrieval with LLM generation for accurate, grounded responses
- **Vector Database**: Uses ChromaDB for efficient similarity search across reviews
- **Context-Aware Answers**: Provides responses based on actual customer feedback
- **Source Attribution**: Shows which reviews were used to generate each answer
- **Interactive Mode**: Continuous query interface for exploring the dataset
- **Dataset Statistics**: Automatic analysis of review data

## 📋 Requirements

- Python 3.8 or higher
- OpenAI API key

## 🚀 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/TanishqMishra12/Pizza-Review-agent.git
   cd Pizza-Review-agent
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**:
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## 💻 Usage

### Interactive Mode

Run the agent in interactive mode to ask multiple questions:

```bash
python pizza_review_agent.py
```

This will start an interactive session where you can ask questions like:
- "What do customers say about Margherita pizza?"
- "Which pizza has the highest ratings?"
- "Show me negative reviews about Hawaiian pizza"
- "What are common complaints in the reviews?"
- "Which cities have the best pizza ratings?"

### Single Query Mode

Ask a single question from the command line:

```bash
python pizza_review_agent.py "What do customers think about pepperoni pizza?"
```

## 📊 Dataset

The project includes a sample dataset (`pizza_reviews.csv`) with 30 pizza reviews containing:
- Customer names
- Pizza types (Margherita, Pepperoni, Hawaiian, BBQ Chicken, etc.)
- Ratings (1-5 stars)
- Review text
- Location and date information

You can replace this with your own CSV file following the same format.

## 🏗️ Architecture

The system consists of three main components:

1. **Data Loader** (`data_loader.py`): Loads and preprocesses pizza reviews from CSV
2. **RAG System** (`rag_system.py`): Implements the retrieval-augmented generation pipeline
   - Embeds documents using OpenAI embeddings
   - Stores vectors in ChromaDB
   - Retrieves relevant reviews for each query
   - Generates answers using GPT model
3. **Agent** (`pizza_review_agent.py`): Main application with interactive interface

### RAG Workflow

```
User Query → Embed Query → Retrieve Similar Reviews → Generate Answer with LLM → Return Response
```

## 🔧 Configuration

You can customize the models used by editing the `.env` file:

```env
EMBEDDING_MODEL=text-embedding-3-small
LLM_MODEL=gpt-3.5-turbo
```

## 📝 Example Queries and Responses

**Q: "What do customers say about Margherita pizza?"**

A: Customers love Margherita pizza! Multiple reviewers mention the quality of ingredients, with fresh basil, San Marzano tomatoes, and fresh mozzarella being highlights. The simplicity of the pizza allows quality ingredients to shine through. Ratings are consistently high (4-5 stars).

**Q: "Which pizza type has the most negative feedback?"**

A: Hawaiian pizza receives the most polarized feedback, with some customers strongly disliking the pineapple topping, giving ratings as low as 1 star.

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Add more review data
- Improve the RAG pipeline
- Enhance the query interface
- Add new features

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

Built with:
- [LangChain](https://langchain.com/) - LLM application framework
- [ChromaDB](https://www.trychroma.com/) - Vector database
- [OpenAI](https://openai.com/) - Embeddings and language models 
