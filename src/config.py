from dotenv import load_dotenv
import os
from pathlib import Path

# Load environment variables from .env file
load_dotenv()

class Config:
    """Configuration for Yelp sentiment analysis project."""
    
    # Paths
    PROJECT_ROOT = Path(__file__).parent.parent
    DATA_PATH = PROJECT_ROOT / 'data'
    RAW_DATA_PATH = DATA_PATH / 'raw'
    PROCESSED_DATA_PATH = DATA_PATH / 'processed'
    MODEL_PATH = PROJECT_ROOT / 'models' / 'trained'

    REVIEW_FILE = PROCESSED_DATA_PATH / "sampled_reviews.json"
    BUSINESS_FILE = RAW_DATA_PATH / "yelp_dataset" / "yelp_academic_dataset_business.json.gz"



    # Model settings
    MODEL_NAME = os.getenv('MODEL_NAME', 'bert-base-uncased')
    BATCH_SIZE = int(os.getenv('BATCH_SIZE', 32))
    
    # Training settings
    RANDOM_SEED = int(os.getenv('RANDOM_SEED', 42))
    NUM_EPOCHS = int(os.getenv('NUM_EPOCHS', 5))

    # Data processing settings
    CHUNK_SIZE = 10_000  # Number of records to process at a time
    REVIEW_FEATURES = ['review_id', 'user_id', 'business_id', 'stars', 'text', 'date', 'useful']
    BUSINESS_FEATURES = ['business_id', 'name', 'address', 'city', 'state', 'postal_code', 'latitude', 'longitude', 'stars', 'review_count', 'is_open', 'categories']

    #Sampling settings
    SAMPLE_SIZE = 100_000  # Number of reviews to sample for initial analysis