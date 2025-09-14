import gzip
import json
import pandas as pd
from pathlib import Path

def load_reviews_chunks(chunk_size=10_000, max_chunks=None):
    """
    Load Yelp reviews in chunks from either a plain or gzipped JSONL file.

    Args:
        chunk_size: Number of reviews per chunk
        max_chunks: Maximum number of chunks to load (None for all)
    """
    # Define both file paths
    json_path = Config.RAW_DATA_PATH / "yelp_dataset" / "yelp_academic_dataset_review.json"
    gz_path = Config.RAW_DATA_PATH / "yelp_dataset" / "yelp_academic_dataset_review.json.gz"

    # Use .gz if it exists, otherwise fallback to .json
    file_path = gz_path if gz_path.exists() else json_path
    open_func = gzip.open if file_path.suffix == ".gz" else open

    chunks = []
    chunk_count = 0

    with open_func(file_path, 'rt', encoding='utf-8') as file:
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

        if chunk:
            df = pd.DataFrame(chunk)
            chunks.append(df[Config.REVIEW_FEATURES])

    return pd.concat(chunks, ignore_index=True)
