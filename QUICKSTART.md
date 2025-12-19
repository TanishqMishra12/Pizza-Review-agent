# Quick Start Guide

Get started with the Pizza Review Agent in 3 simple steps!

## Prerequisites
- Python 3.8+
- OpenAI API key ([Get one here](https://platform.openai.com/))

## Installation

```bash
# 1. Clone and navigate to the repository
git clone https://github.com/TanishqMishra12/Pizza-Review-agent.git
cd Pizza-Review-agent

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set up your API key
cp .env.example .env
# Edit .env and add your OpenAI API key
```

## Usage

### Try the Demo (No API Key Required)
```bash
python demo.py
```
See the dataset overview and how the RAG system works.

### Run Tests (No API Key Required)
```bash
python test_structure.py
```
Verify all components are working correctly.

### Interactive Mode (Requires API Key)
```bash
python pizza_review_agent.py
```
Ask questions in natural language about the pizza reviews.

### Single Query Mode (Requires API Key)
```bash
python pizza_review_agent.py "What do customers say about Margherita pizza?"
```

### Example Script (Requires API Key)
```bash
python example.py
```
Run predefined example queries.

## Example Questions

- "What do customers say about Margherita pizza?"
- "Which pizza has the highest ratings?"
- "Show me negative reviews about Hawaiian pizza"
- "What are common complaints in the reviews?"
- "Which cities have the best pizza ratings?"
- "Compare Margherita and Pepperoni reviews"

## Project Structure

```
Pizza-Review-agent/
├── pizza_review_agent.py    # Main agent application
├── rag_system.py            # RAG implementation
├── data_loader.py           # CSV data loader
├── pizza_reviews.csv        # Sample dataset (30 reviews)
├── demo.py                  # Demo without API key
├── example.py               # Example usage with API key
├── test_structure.py        # Test suite
├── requirements.txt         # Python dependencies
├── .env.example            # Environment variables template
├── README.md               # Full documentation
└── USAGE_GUIDE.md          # Detailed usage guide
```

## What's Happening Under the Hood?

1. **Data Loading**: Reads pizza reviews from CSV
2. **Embedding**: Converts reviews to vectors using OpenAI
3. **Storage**: Stores vectors in ChromaDB
4. **Query**: Your question is also converted to a vector
5. **Retrieval**: Finds 5 most similar reviews
6. **Generation**: GPT generates answer based on retrieved reviews
7. **Response**: You get a grounded answer with source attribution

## Cost Estimate

Typical usage costs are very low:
- First run: ~$0.001-0.01 (embeddings)
- Each query: ~$0.0001-0.001 (depends on answer length)

## Next Steps

- Check out [USAGE_GUIDE.md](USAGE_GUIDE.md) for detailed instructions
- Read [README.md](README.md) for architecture details
- Replace `pizza_reviews.csv` with your own review data

## Troubleshooting

**"OPENAI_API_KEY not found"**
→ Create `.env` file and add your API key

**"Module not found"**
→ Run `pip install -r requirements.txt`

**"CSV file not found"**
→ Ensure `pizza_reviews.csv` exists in the directory

## Support

For issues or questions, visit the [GitHub repository](https://github.com/TanishqMishra12/Pizza-Review-agent).
