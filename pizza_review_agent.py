"""
Main Pizza Review Agent application.

This agent uses RAG (Retrieval-Augmented Generation) to answer questions
about pizza reviews from a CSV dataset using natural language.
"""
import os
import sys
from data_loader import PizzaReviewLoader
from rag_system import PizzaReviewRAG


class PizzaReviewAgent:
    """AI agent for querying pizza reviews using natural language."""
    
    def __init__(self, csv_path: str = "pizza_reviews.csv"):
        """
        Initialize the Pizza Review Agent.
        
        Args:
            csv_path: Path to the CSV file containing pizza reviews
        """
        self.csv_path = csv_path
        self.loader = None
        self.rag_system = None
        
    def load_reviews(self):
        """Load pizza reviews from CSV file."""
        print(f"Loading reviews from {self.csv_path}...")
        self.loader = PizzaReviewLoader(self.csv_path)
        self.loader.load_data()
        
        # Display statistics
        stats = self.loader.get_statistics()
        print(f"\n📊 Dataset Statistics:")
        print(f"  Total Reviews: {stats['total_reviews']}")
        print(f"  Average Rating: {stats['average_rating']}/5.0")
        print(f"  Pizza Types: {', '.join(stats['pizza_types'])}")
        print(f"  Locations: {len(stats['locations'])} cities")
        print()
        
    def initialize_rag(self):
        """Initialize the RAG system with loaded reviews."""
        if self.loader is None:
            self.load_reviews()
        
        documents = self.loader.get_documents()
        self.rag_system = PizzaReviewRAG(documents)
        self.rag_system.initialize()
        
    def query(self, question: str) -> dict:
        """
        Ask a question about pizza reviews.
        
        Args:
            question: Natural language question
            
        Returns:
            Dictionary containing answer and source reviews
        """
        if self.rag_system is None:
            raise ValueError("RAG system not initialized. Call initialize_rag() first.")
        
        return self.rag_system.query(question)
    
    def interactive_mode(self):
        """Run the agent in interactive mode for continuous querying."""
        print("=" * 70)
        print("🍕 Pizza Review Agent - Interactive Mode 🍕")
        print("=" * 70)
        print("\nAsk questions about pizza reviews in natural language!")
        print("Type 'quit' or 'exit' to stop.\n")
        print("Example questions:")
        print("  - What do customers say about Margherita pizza?")
        print("  - Which pizza has the highest ratings?")
        print("  - Show me negative reviews about Hawaiian pizza")
        print("  - What are common complaints in the reviews?")
        print("  - Which cities have the best pizza ratings?")
        print()
        
        while True:
            try:
                question = input("❓ Your question: ").strip()
                
                if not question:
                    continue
                    
                if question.lower() in ['quit', 'exit', 'q']:
                    print("\n👋 Thank you for using Pizza Review Agent!")
                    break
                
                print("\n🔍 Searching reviews...")
                result = self.query(question)
                
                print("\n" + "=" * 70)
                print("💡 Answer:")
                print("-" * 70)
                print(result['answer'])
                print("\n" + "=" * 70)
                print(f"📚 Based on {len(result['source_reviews'])} relevant reviews")
                print("=" * 70 + "\n")
                
            except KeyboardInterrupt:
                print("\n\n👋 Thank you for using Pizza Review Agent!")
                break
            except Exception as e:
                print(f"\n❌ Error: {str(e)}\n")


def main():
    """Main entry point for the Pizza Review Agent."""
    # Check if OpenAI API key is set
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Error: OPENAI_API_KEY not found in environment variables")
        print("\nPlease set up your OpenAI API key:")
        print("1. Copy .env.example to .env")
        print("2. Add your OpenAI API key to the .env file")
        print("3. Run the agent again")
        sys.exit(1)
    
    # Initialize agent
    agent = PizzaReviewAgent()
    
    try:
        # Load reviews and initialize RAG
        agent.load_reviews()
        agent.initialize_rag()
        
        # Check if a specific query is provided as command-line argument
        if len(sys.argv) > 1:
            question = " ".join(sys.argv[1:])
            print(f"\n❓ Question: {question}\n")
            result = agent.query(question)
            print(f"💡 Answer: {result['answer']}\n")
            print(f"📚 Based on {len(result['source_reviews'])} relevant reviews\n")
        else:
            # Run in interactive mode
            agent.interactive_mode()
            
    except FileNotFoundError:
        print(f"❌ Error: Could not find {agent.csv_path}")
        print("Please ensure the pizza reviews CSV file exists.")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    main()
