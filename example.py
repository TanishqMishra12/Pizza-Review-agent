"""
Example script demonstrating how to use the Pizza Review Agent programmatically.
"""
from pizza_review_agent import PizzaReviewAgent


def run_examples():
    """Run example queries to demonstrate the agent's capabilities."""
    print("=" * 70)
    print("🍕 Pizza Review Agent - Example Queries 🍕")
    print("=" * 70)
    print("\nInitializing agent...\n")
    
    # Initialize the agent
    agent = PizzaReviewAgent()
    agent.load_reviews()
    agent.initialize_rag()
    
    # Example queries
    example_questions = [
        "What do customers say about Margherita pizza?",
        "Which pizza types have the highest ratings?",
        "What are the common complaints in negative reviews?",
        "How do customers feel about Hawaiian pizza?",
        "What makes a great pepperoni pizza according to reviews?"
    ]
    
    print("\n" + "=" * 70)
    print("Running Example Queries")
    print("=" * 70)
    
    for i, question in enumerate(example_questions, 1):
        print(f"\n{'=' * 70}")
        print(f"Example {i}: {question}")
        print("-" * 70)
        
        try:
            result = agent.query(question)
            print(f"\n💡 Answer:\n{result['answer']}")
            print(f"\n📚 Based on {len(result['source_reviews'])} relevant reviews")
            
        except Exception as e:
            print(f"❌ Error: {str(e)}")
    
    print("\n" + "=" * 70)
    print("Examples completed!")
    print("=" * 70)


if __name__ == "__main__":
    run_examples()
