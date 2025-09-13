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
    
    # Model settings
    MODEL_NAME = os.getenv('MODEL_NAME', 'bert-base-uncased')
    BATCH_SIZE = int(os.getenv('BATCH_SIZE', 32))
    
    # Training settings
    RANDOM_SEED = int(os.getenv('RANDOM_SEED', 42))
    NUM_EPOCHS = int(os.getenv('NUM_EPOCHS', 5))