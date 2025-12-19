#!/usr/bin/env python
"""
Demo script showing the Pizza Review Agent capabilities.
This script demonstrates the agent without requiring API calls (shows structure only).
For full functionality, use pizza_review_agent.py with an API key.
"""
from data_loader import PizzaReviewLoader


def show_dataset_overview():
    """Display an overview of the pizza review dataset."""
    print("=" * 70)
    print("🍕 Pizza Review Agent - Dataset Demo")
    print("=" * 70)
    
    # Load the data
    loader = PizzaReviewLoader('pizza_reviews.csv')
    loader.load_data()
    
    # Get statistics
    stats = loader.get_statistics()
    
    print("\n📊 Dataset Overview:")
    print("-" * 70)
    print(f"Total Reviews: {stats['total_reviews']}")
    print(f"Average Rating: {stats['average_rating']}/5.0 stars")
    print(f"\n🍕 Pizza Types Available:")
    for i, pizza_type in enumerate(stats['pizza_types'], 1):
        print(f"  {i}. {pizza_type}")
    
    print(f"\n📍 Locations Covered: {len(stats['locations'])} cities across the US")
    
    print(f"\n⭐ Rating Distribution:")
    for rating in sorted(stats['rating_distribution'].keys(), reverse=True):
        count = stats['rating_distribution'][rating]
        stars = "⭐" * int(rating)
        bar = "█" * count
        print(f"  {stars} ({rating}): {bar} ({count} reviews)")
    
    # Show sample reviews
    print("\n" + "=" * 70)
    print("📝 Sample Reviews:")
    print("-" * 70)
    
    documents = loader.get_documents()
    
    # Show a few diverse samples
    samples = [0, 4, 10, 15, 20]
    for idx in samples:
        if idx < len(documents):
            doc = documents[idx]
            meta = doc['metadata']
            print(f"\n{meta['customer_name']} - {meta['pizza_type']} - {meta['location']}")
            print(f"Rating: {'⭐' * int(meta['rating'])} ({meta['rating']}/5)")
            # Extract just the review text from the document
            review_start = doc['text'].find("Review: ") + 8
            review_text = doc['text'][review_start:]
            print(f"Review: {review_text[:100]}...")
    
    print("\n" + "=" * 70)
    print("🤖 Agent Capabilities:")
    print("-" * 70)
    print("""
The Pizza Review Agent can answer questions like:
  • "What do customers say about Margherita pizza?"
  • "Which pizza has the highest ratings?"
  • "Show me negative reviews"
  • "What are common complaints about Hawaiian pizza?"
  • "Which cities have the best pizza ratings?"
  • "Compare Margherita and Pepperoni reviews"
  • "What do customers say about the crust?"
  
To use the full agent with natural language queries:
  1. Set up your OpenAI API key in .env
  2. Run: python pizza_review_agent.py
  3. Start asking questions!
    """)
    print("=" * 70)


def show_example_workflow():
    """Show an example of how the RAG system works."""
    print("\n" + "=" * 70)
    print("🔍 How the RAG System Works:")
    print("-" * 70)
    print("""
1. Data Loading:
   ✓ Loads pizza reviews from CSV
   ✓ Converts each review into a structured document
   ✓ Creates 30 searchable documents
   
2. Vector Embedding:
   • Uses OpenAI's text-embedding-3-small model
   • Converts review text into numerical vectors
   • Stores vectors in ChromaDB for fast retrieval
   
3. Query Processing:
   User: "What do customers say about Margherita pizza?"
   
   a) Embed the query using the same embedding model
   b) Search ChromaDB for the 5 most similar reviews
   c) Retrieve relevant review documents
   
4. Answer Generation:
   • Sends query + retrieved reviews to GPT-3.5-turbo
   • LLM generates context-aware answer
   • Returns answer with source attribution
   
5. Response:
   💡 Answer: "Customers love Margherita pizza! Multiple reviewers
   mention the quality of ingredients, with fresh basil, San Marzano
   tomatoes, and fresh mozzarella being highlights..."
   
   📚 Based on 5 relevant reviews
    """)
    print("=" * 70)


if __name__ == "__main__":
    show_dataset_overview()
    show_example_workflow()
    
    print("\n✨ Ready to try it yourself?")
    print("   Set up your .env file and run: python pizza_review_agent.py")
