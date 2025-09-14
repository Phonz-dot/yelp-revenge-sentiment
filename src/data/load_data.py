import gzip
import json
import pandas as pd
from pathlib import Path
from src.config import Config

def load_reviews_chunks(file_path, chunk_size=10_000, max_chunks=None):
    """
    Load Yelp data in chunks from a user-specified JSON or gzipped JSONL file.
    Automatically selects feature set and index label based on file type.

    Args:
        file_path: Path to the JSON or JSON.GZ file
        chunk_size: Number of records per chunk
        max_chunks: Maximum number of chunks to load (None for all)
    """
    open_func = gzip.open if str(file_path).endswith(".gz") else open

    # Detect file type and set features + index label
    if "review" in str(file_path).lower():
        features = Config.REVIEW_FEATURES
        index_label = "review_index"
    elif "business" in str(file_path).lower():
        features = Config.BUSINESS_FEATURES
        index_label = "business_index"
    else:
        raise ValueError("Unknown file type. Expected 'review' or 'business' in filename.")

    chunks = []
    chunk_count = 0
    line_index = 0

    with open_func(file_path, 'rt', encoding='utf-8') as file:
        chunk = []
        indexes = []
        for line in file:
            chunk.append(json.loads(line))
            indexes.append(line_index)
            line_index += 1

            if len(chunk) >= chunk_size:
                df = pd.DataFrame(chunk)
                df[index_label] = indexes
                chunks.append(df[features + [index_label]])
                chunk = []
                indexes = []
                chunk_count += 1

                if max_chunks and chunk_count >= max_chunks:
                    break

        if chunk:
            df = pd.DataFrame(chunk)
            df[index_label] = indexes
            chunks.append(df[features + [index_label]])

    return pd.concat(chunks, ignore_index=True)
