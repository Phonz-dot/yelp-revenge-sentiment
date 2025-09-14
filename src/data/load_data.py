import json
import gzip
import pandas as pd

def load_reviews_chunks(file, chunk_size=10_000, max_chunks=None):
    """Load Yelp reviews in chunks to manage memory."""
    # Choose open function based on file extension
    open_func = gzip.open if str(file).endswith('.gz') else open
    
    chunks = []
    chunk_count = 0
    
    with open_func(file, 'rt', encoding='utf-8') as f:
        chunk_data = []
        
        for line in f:
            try:
                chunk_data.append(json.loads(line))
                
                # Process chunk when full
                if len(chunk_data) >= chunk_size:
                    df = pd.DataFrame(chunk_data)
                    chunks.append(df[Config.REVIEW_FEATURES])
                    chunk_data = []
                    chunk_count += 1
                    
                    # Stop if we have enough chunks
                    if max_chunks and chunk_count >= max_chunks:
                        break
                        
            except json.JSONDecodeError:
                continue  # Skip bad lines
        
        # Handle remaining data
        if chunk_data:
            df = pd.DataFrame(chunk_data)
            chunks.append(df[Config.REVIEW_FEATURES])
    
    return pd.concat(chunks, ignore_index=True)