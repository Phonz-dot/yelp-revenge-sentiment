"""
Yelp Revenge Sentiment Analysis Package
Version: 0.1.0

This package provides tools and models for analyzing revenge sentiment in Yelp reviews.
"""

from pathlib import Path
import os

# Define project root path
PROJECT_ROOT = Path(__file__).parent.parent

# Import key package components
from .config import Config

# Package level variables
__version__ = "0.1.0"
__author__ = "Alphonso Houston"

# Initialize package configuration
config = Config()