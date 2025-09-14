# Detecting Revengeful Sentiment in Yelp Reviews Using Large Language Models

## Description
This project aims to detect and analyze revenge-driven sentiment in Yelp reviews using large language models (LLMs). Unlike traditional sentiment analysis, which focuses on polarity (positive/negative), this approach seeks to uncover emotionally charged reviews motivated by retaliation, personal vendettas, or exaggerated negativity. The goal is to build a pipeline that can identify these nuanced signals and support deeper understanding of user intent.

## Setup
1. Clone the repository:<br>
    `git clone https://github.com/your-username/yelp-revenge-sentiment.git`<br>
    `cd yelp-revenge-sentiment`
2. Create virtual environment:<br>`python -m venv venv`
3. Activate environment:<br>`.\venv\Scripts\activate`
4. Install dependencies:<br>`pip install -r requirements.txt`

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
