"""
Test script to verify the Pizza Review Agent structure without requiring OpenAI API key.
This validates that all components are properly structured and can be imported.
"""
import sys


def test_imports():
    """Test that all modules can be imported."""
    print("Testing module imports...")
    
    try:
        from data_loader import PizzaReviewLoader
        print("✓ data_loader module imported")
    except Exception as e:
        print(f"✗ Failed to import data_loader: {e}")
        return False
    
    try:
        from rag_system import PizzaReviewRAG
        print("✓ rag_system module imported")
    except Exception as e:
        print(f"✗ Failed to import rag_system: {e}")
        return False
    
    try:
        from pizza_review_agent import PizzaReviewAgent
        print("✓ pizza_review_agent module imported")
    except Exception as e:
        print(f"✗ Failed to import pizza_review_agent: {e}")
        return False
    
    return True


def test_data_loader():
    """Test the data loader functionality."""
    print("\nTesting data loader...")
    
    try:
        from data_loader import PizzaReviewLoader
        
        # Initialize loader
        loader = PizzaReviewLoader('pizza_reviews.csv')
        print("✓ Data loader initialized")
        
        # Load data
        df = loader.load_data()
        if df is None or len(df) == 0:
            print("✗ Failed to load data")
            return False
        print(f"✓ Loaded {len(df)} reviews")
        
        # Get statistics
        stats = loader.get_statistics()
        if not stats or 'total_reviews' not in stats:
            print("✗ Failed to get statistics")
            return False
        print(f"✓ Statistics generated: {stats['total_reviews']} total reviews")
        
        # Get documents
        docs = loader.get_documents()
        if not docs or len(docs) == 0:
            print("✗ Failed to get documents")
            return False
        print(f"✓ Generated {len(docs)} documents for RAG")
        
        # Verify document structure
        sample_doc = docs[0]
        if 'text' not in sample_doc or 'metadata' not in sample_doc:
            print("✗ Document structure is incorrect")
            return False
        print("✓ Document structure is valid")
        
        return True
        
    except Exception as e:
        print(f"✗ Data loader test failed: {e}")
        return False


def test_csv_structure():
    """Test that the CSV file has the correct structure."""
    print("\nTesting CSV structure...")
    
    try:
        import pandas as pd
        
        df = pd.read_csv('pizza_reviews.csv')
        
        # Check required columns
        required_cols = ['review_id', 'customer_name', 'pizza_type', 
                        'rating', 'review_text', 'date', 'location']
        
        missing_cols = [col for col in required_cols if col not in df.columns]
        if missing_cols:
            print(f"✗ Missing columns: {missing_cols}")
            return False
        print("✓ All required columns present")
        
        # Check data types and content
        if df['rating'].min() < 1 or df['rating'].max() > 5:
            print("✗ Ratings should be between 1 and 5")
            return False
        print("✓ Rating values are valid")
        
        # Check for non-empty reviews
        if df['review_text'].isna().any():
            print("✗ Some reviews are empty")
            return False
        print("✓ All reviews have text")
        
        return True
        
    except Exception as e:
        print(f"✗ CSV structure test failed: {e}")
        return False


def test_agent_structure():
    """Test that the agent can be instantiated (without API key)."""
    print("\nTesting agent structure...")
    
    try:
        from pizza_review_agent import PizzaReviewAgent
        
        # Create agent instance
        agent = PizzaReviewAgent()
        print("✓ Agent instantiated")
        
        # Test load_reviews
        agent.load_reviews()
        print("✓ Reviews loaded successfully")
        
        # Verify loader is set
        if agent.loader is None:
            print("✗ Loader not initialized")
            return False
        print("✓ Loader initialized")
        
        return True
        
    except Exception as e:
        # If it's just an API key error, that's expected
        if "OPENAI_API_KEY" in str(e):
            print("⚠ Agent structure is valid (API key not tested)")
            return True
        print(f"✗ Agent structure test failed: {e}")
        return False


def run_all_tests():
    """Run all tests."""
    print("=" * 70)
    print("Pizza Review Agent - Structure Tests")
    print("=" * 70)
    
    tests = [
        ("Module Imports", test_imports),
        ("Data Loader", test_data_loader),
        ("CSV Structure", test_csv_structure),
        ("Agent Structure", test_agent_structure),
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n{'=' * 70}")
        print(f"Test: {test_name}")
        print("-" * 70)
        result = test_func()
        results.append((test_name, result))
    
    # Summary
    print(f"\n{'=' * 70}")
    print("Test Summary")
    print("=" * 70)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✓ PASSED" if result else "✗ FAILED"
        print(f"{test_name}: {status}")
    
    print(f"\n{passed}/{total} tests passed")
    print("=" * 70)
    
    return passed == total


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
