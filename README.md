# Detecting Revengeful Sentiment in Yelp Reviews Using Large Language Models

## Description
 The purpose of this project is to identify and analyze instances of revenge-driven sentiment in Yelp reviews, using large language models (LLMs) to go beyond traditional sentiment analysis and uncover nuanced emotional intent, particularly when users leave reviews motivated by retaliation rather than genuine feedback.

## Setup
1. Clone the repository:
    git clone https://github.com/your-username/yelp-revenge-sentiment.git
    cd yelp-revenge-sentiment
2. Create virtual environment: `python -m venv venv`
3. Activate environment: `.\venv\Scripts\activate`
4. Install dependencies: `pip install -r requirements.txt`

## Project Structure
- `data/`: Raw and processed Yelp datasets (.json, .json.gz)
- `notebooks/`: Exploratory analysis and model development in Jupyter
- `src/`: Core source code including data loaders, preprocessing, and modeling
- `tests/`: Unit tests for key components
- `models/`: Saved model checkpoints and outputs
- `reports/`: Generated reports, visualizations, and summaries
- `.env`: Environment variables
- `requirement.txt`: Python dependencies
- `setup.py`: Project packaging and metadata
