import gzip
import json
import pandas as pd
from pathlib import Path

def load_reviews_chunks(file_path, chunk_size=10_000, max_chunks=None):
    """
    Load Yelp reviews in chunks from a user-specified JSON or gzipped JSONL file.

    Args:
        file_path: Path to the JSON or JSON.GZ file
        chunk_size: Number of reviews per chunk
        max_chunks: Maximum number of chunks to load (None for all)
    """
    open_func = gzip.open if str(file_path).endswith(".gz") else open

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
