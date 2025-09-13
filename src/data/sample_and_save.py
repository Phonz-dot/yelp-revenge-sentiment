import json
import pandas as pd
import numpy as np
from pathlib import Path
from src.config import Config
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_balanced_sample(input_path, n_samples=50_000, random_state=42):
    """
    Create a balanced sample of reviews stratified by rating.
    
    Args:
        input_path: Path to original JSON file
        n_samples: Total desired sample size
        random_state: Random seed for reproducibility
    """
    samples_per_rating = n_samples // 5
    samples = {i: [] for i in range(1, 6)}
    
    logger.info(f"Creating balanced sample of {n_samples:,} reviews...")
    
    with open(input_path, 'r', encoding='utf-8') as f:
        for line in f:
            review = json.loads(line)
            rating = int(review['stars'])
            
            if len(samples[rating]) < samples_per_rating:
                samples[rating].append(review)
            
            # Check if we have enough samples
            if all(len(s) >= samples_per_rating for s in samples.values()):
                break
    
    # Combine all samples
    all_samples = []
    for rating_samples in samples.values():
        all_samples.extend(rating_samples)
    
    # Shuffle samples
    np.random.seed(random_state)
    np.random.shuffle(all_samples)
    
    return pd.DataFrame(all_samples)

def save_to_json(df, output_filename='sampled_reviews.json'):
    """
    Save DataFrame to JSON file in a memory-efficient way.
    
    Args:
        df: pandas DataFrame to save
        output_filename: name of output JSON file
    """
    output_path = Config.PROCESSED_DATA_PATH / output_filename
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    logger.info(f"Saving {len(df):,} records to {output_path}")
    
    with open(output_path, 'w', encoding='utf-8') as f:
        for _, row in df.iterrows():
            json.dump(row.to_dict(), f)
            f.write('\n')
    
    file_size = output_path.stat().st_size / (1024*1024)
    logger.info(f"File saved successfully. Size: {file_size:.2f} MB")
    
    return output_path

def main():
    """Main function to create and save balanced sample."""
    # Input file path
    input_path = Config.RAW_DATA_PATH / "yelp_dataset" / "yelp_academic_dataset_review.json"
    
    # Create balanced sample
    df = create_balanced_sample(input_path, n_samples=50_000)
    
    # Display sample statistics
    logger.info("\nRating distribution:")
    logger.info(df['stars'].value_counts().sort_index())
    
    # Save to JSON
    output_path = save_to_json(df, 'balanced_reviews_sample.json')
    
    return output_path

if __name__ == "__main__":
    main()