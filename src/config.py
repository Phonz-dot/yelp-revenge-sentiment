from dotenv import load_dotenv
import os
from pathlib import Path

# Load environment variables from .env file
load_dotenv()

class Config:
    """Project configuration class."""
    
    # Database
    DB_HOST = os.getenv('DB_HOST')
    DB_PORT = int(os.getenv('DB_PORT', 5432))
    DB_NAME = os.getenv('DB_NAME')
    
    # Paths
    DATA_PATH = Path(os.getenv('DATA_PATH', './data'))
    MODELS_PATH = Path(os.getenv('MODELS_PATH', './models/trained'))
    
    # Settings
    DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
    ENVIRONMENT = os.getenv('ENVIRONMENT', 'development')
    
    @classmethod
    def validate(cls):
        """Validate required environment variables."""
        required = ['DB_HOST', 'DB_NAME']
        missing = [var for var in required if not getattr(cls, var)]
        if missing:
            raise ValueError(f"Missing required environment variables: {', '.join(missing)}")