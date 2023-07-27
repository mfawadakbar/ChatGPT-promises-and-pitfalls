Sure! Here's an example of a Python script that uses the Natural Language Toolkit (NLTK) library to determine the sentiment of an Amazon product review.

```python
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

def get_review_sentiment(review):
    nltk.download('vader_lexicon')  # Download required dataset for SentimentIntensityAnalyzer
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(review)
    compound_score = sentiment_scores['compound']

    # Determine sentiment based on compound score
    if compound_score >= 0.05:
        return "Positive"
    elif compound_score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# Get user input for the Amazon product review
review = input("Enter your Amazon product review: ")

# Get the sentiment of the review
sentiment = get_review_sentiment(review)

# Output the sentiment
print(f"The sentiment of the review is: {sentiment}")
```

To run the script, save it to a file (e.g., `task.py`) and execute it using the command `python task.py` in your terminal. The script will prompt you to enter your Amazon product review, and it will then determine and display the sentiment of the review.

Note: The script uses the VADER (Valence Aware Dictionary and sEntiment Reasoner) sentiment analysis tool from the NLTK library. It is a rule-based approach specifically designed for sentiment analysis of social media texts.