"""
Data loader module for loading and preprocessing pizza reviews from CSV.
"""
import pandas as pd
from typing import List, Dict


class PizzaReviewLoader:
    """Loads and processes pizza review data from CSV files."""
    
    def __init__(self, csv_path: str):
        """
        Initialize the loader with CSV file path.
        
        Args:
            csv_path: Path to the CSV file containing pizza reviews
        """
        self.csv_path = csv_path
        self.df = None
        
    def load_data(self) -> pd.DataFrame:
        """
        Load pizza reviews from CSV file.
        
        Returns:
            DataFrame containing the review data
        """
        self.df = pd.read_csv(self.csv_path)
        return self.df
    
    def get_documents(self) -> List[Dict[str, str]]:
        """
        Convert reviews to document format for RAG system.
        
        Returns:
            List of dictionaries containing review text and metadata
        """
        if self.df is None:
            self.load_data()
        
        documents = []
        for _, row in self.df.iterrows():
            # Create a comprehensive text representation of the review
            doc_text = (
                f"Review #{row['review_id']}: "
                f"Customer {row['customer_name']} ordered {row['pizza_type']} pizza "
                f"in {row['location']} on {row['date']}. "
                f"Rating: {row['rating']}/5 stars. "
                f"Review: {row['review_text']}"
            )
            
            documents.append({
                'text': doc_text,
                'metadata': {
                    'review_id': str(row['review_id']),
                    'customer_name': row['customer_name'],
                    'pizza_type': row['pizza_type'],
                    'rating': str(row['rating']),
                    'location': row['location'],
                    'date': row['date']
                }
            })
        
        return documents
    
    def get_statistics(self) -> Dict[str, any]:
        """
        Get basic statistics about the review dataset.
        
        Returns:
            Dictionary containing dataset statistics
        """
        if self.df is None:
            self.load_data()
        
        stats = {
            'total_reviews': len(self.df),
            'average_rating': round(self.df['rating'].mean(), 2),
            'pizza_types': self.df['pizza_type'].unique().tolist(),
            'locations': self.df['location'].unique().tolist(),
            'rating_distribution': self.df['rating'].value_counts().to_dict()
        }
        
        return stats
