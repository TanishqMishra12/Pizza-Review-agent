# Pizza Review Agent - Usage Guide

This guide provides detailed instructions on how to use the Pizza Review Agent to query customer feedback using natural language.

## Table of Contents
- [Quick Start](#quick-start)
- [Setup](#setup)
- [Using the Agent](#using-the-agent)
- [Example Queries](#example-queries)
- [Understanding the Output](#understanding-the-output)
- [Customizing the Dataset](#customizing-the-dataset)
- [Troubleshooting](#troubleshooting)

## Quick Start

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up your OpenAI API key in `.env`:
   ```bash
   cp .env.example .env
   # Edit .env and add your API key
   ```

3. Run the agent:
   ```bash
   python pizza_review_agent.py
   ```

## Setup

### Prerequisites
- Python 3.8 or higher
- OpenAI API key (get one at https://platform.openai.com/)

### Installation Steps

1. **Clone the repository**:
   ```bash
   git clone https://github.com/TanishqMishra12/Pizza-Review-agent.git
   cd Pizza-Review-agent
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**:
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` file and add your OpenAI API key:
   ```
   OPENAI_API_KEY=sk-your-api-key-here
   ```

## Using the Agent

### Interactive Mode

The interactive mode allows you to ask multiple questions in a conversational manner:

```bash
python pizza_review_agent.py
```

You'll see a prompt where you can type your questions:
```
❓ Your question: What do customers say about Margherita pizza?
```

Type `quit`, `exit`, or `q` to stop the interactive session.

### Single Query Mode

To ask a single question from the command line:

```bash
python pizza_review_agent.py "What are the highest rated pizzas?"
```

### Programmatic Usage

You can also use the agent in your own Python scripts:

```python
from pizza_review_agent import PizzaReviewAgent

# Initialize the agent
agent = PizzaReviewAgent()
agent.load_reviews()
agent.initialize_rag()

# Ask a question
result = agent.query("What do customers say about Margherita pizza?")
print(result['answer'])
```

## Example Queries

Here are some example questions you can ask:

### General Questions
- "What do customers say about the pizza?"
- "What is the overall sentiment about the reviews?"
- "What are the most common pizza types mentioned?"

### Pizza-Specific Questions
- "What do customers say about Margherita pizza?"
- "How do people rate Hawaiian pizza?"
- "Which pizza type has the highest ratings?"
- "What are the negative reviews about Meat Lovers pizza?"

### Ingredient and Quality Questions
- "What do customers say about the crust?"
- "What complaints do customers have about toppings?"
- "What do reviews say about the cheese quality?"
- "Are there comments about the sauce?"

### Location-Based Questions
- "Which cities have the best pizza ratings?"
- "What do New York customers think?"
- "Are there location-specific preferences?"

### Rating and Sentiment Questions
- "Show me 5-star reviews"
- "What are the common complaints in negative reviews?"
- "Which pizzas get consistently high ratings?"
- "What makes customers give 1-star ratings?"

### Comparative Questions
- "Compare Margherita and Pepperoni reviews"
- "What's the difference between vegetarian options?"
- "Which meat pizza is more popular?"

## Understanding the Output

When you ask a question, the agent provides:

1. **Answer**: A natural language response based on the retrieved reviews
2. **Source Count**: Number of reviews used to generate the answer

Example output:
```
💡 Answer:
Customers love Margherita pizza! Multiple reviewers mention the quality 
of ingredients, with fresh basil, San Marzano tomatoes, and fresh 
mozzarella being highlights. The simplicity of the pizza allows quality 
ingredients to shine through. Ratings are consistently high (4-5 stars).

📚 Based on 5 relevant reviews
```

## Customizing the Dataset

### Using Your Own CSV File

You can use your own pizza review dataset by:

1. Creating a CSV file with the following columns:
   - `review_id`: Unique identifier for each review
   - `customer_name`: Name of the customer
   - `pizza_type`: Type of pizza ordered
   - `rating`: Rating (1-5 stars)
   - `review_text`: The actual review text
   - `date`: Date of the review
   - `location`: Location where the pizza was ordered

2. Save it as `pizza_reviews.csv` or specify the path:
   ```python
   agent = PizzaReviewAgent(csv_path="path/to/your/reviews.csv")
   ```

### Adding More Reviews

Simply add more rows to the CSV file. The agent will automatically process all reviews when initialized.

## Troubleshooting

### Common Issues

**1. Missing OpenAI API Key**
```
Error: OPENAI_API_KEY not found in environment variables
```
**Solution**: Make sure you've created a `.env` file with your API key.

**2. Import Errors**
```
ModuleNotFoundError: No module named 'langchain'
```
**Solution**: Install dependencies with `pip install -r requirements.txt`

**3. CSV File Not Found**
```
Error: Could not find pizza_reviews.csv
```
**Solution**: Make sure the CSV file exists in the same directory or provide the correct path.

**4. Rate Limit Errors**
```
Error: Rate limit exceeded
```
**Solution**: Wait a moment and try again, or upgrade your OpenAI API plan.

### Getting Help

If you encounter issues:
1. Check that all dependencies are installed
2. Verify your OpenAI API key is valid
3. Ensure the CSV file format matches the expected structure
4. Check the GitHub repository for updates or known issues

## Advanced Configuration

### Changing the Embedding Model

Edit `.env` to use a different embedding model:
```
EMBEDDING_MODEL=text-embedding-3-large
```

### Changing the LLM Model

Edit `.env` to use a different GPT model:
```
LLM_MODEL=gpt-4
```

Note: Different models have different costs and capabilities. Check OpenAI's pricing page for details.

### Adjusting Retrieval Parameters

In `rag_system.py`, you can modify the retrieval settings:
```python
retriever = self.vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 5}  # Retrieve top 5 most relevant reviews
)
```

Increase `k` to retrieve more reviews for each query (better context but slower).

## Best Practices

1. **Be Specific**: More specific questions get better answers
   - Good: "What do customers say about the crust texture in Margherita pizzas?"
   - Less Good: "Tell me about pizza"

2. **Use Natural Language**: The agent understands conversational queries
   - "Show me reviews where people complained about delivery"
   - "Which pizza should I order if I like spicy food?"

3. **Iterate**: If you don't get the answer you want, try rephrasing
   - Different phrasings may retrieve different relevant reviews

4. **Context Matters**: The agent can only answer based on the reviews in the dataset
   - Questions about things not mentioned in reviews won't have good answers

## API Costs

The agent uses OpenAI's API, which has associated costs:
- Embeddings: Used once when initializing the vector database
- LLM calls: Used for each query

Typical costs are very low (cents per session), but can add up with heavy usage. Monitor your OpenAI dashboard for actual costs.
