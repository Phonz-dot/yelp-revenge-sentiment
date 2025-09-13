import pandas as pd
import json
from pathlib import Path
from src.config import Config

def load_reviews_chunks(chunk_size=10_000, max_chunks=None):
    """
    Load Yelp reviews in chunks to manage memory.
    
    Args:
        chunk_size: Number of reviews per chunk
        max_chunks: Maximum number of chunks to load (None for all)
    """
    review_path = Config.RAW_DATA_PATH / "yelp_dataset" / "yelp_academic_dataset_review.json"
    
    chunks = []
    chunk_count = 0
    
    with open(review_path, 'r', encoding='utf-8') as file:
        chunk = []
        for line in file:
            chunk.append(json.loads(line))
            if len(chunk) >= chunk_size:
                df = pd.DataFrame(chunk)
                chunks.append(df[Config.REVIEW_FEATURES])
                chunk = []
                chunk_count += 1
                
                if max_chunks and chunk_count >= max_chunks:
                    break
    
    return pd.concat(chunks, ignore_index=True)