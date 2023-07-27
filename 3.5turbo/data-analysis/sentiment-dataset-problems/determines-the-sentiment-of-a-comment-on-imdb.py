Sure! Here is a Python script that uses the NLTK library to determine the sentiment of a comment on IMDb:

```python
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

def get_sentiment(comment):
    # Initialize SentimentIntensityAnalyzer
    sia = SentimentIntensityAnalyzer()

    # Get sentiment scores
    sentiment_scores = sia.polarity_scores(comment)

    # Determine sentiment label
    if sentiment_scores['compound'] >= 0.05:
        sentiment = 'Positive'
    elif sentiment_scores['compound'] <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    return sentiment

def main():
    # Get comment from user
    comment = input('Enter a comment: ')

    # Determine sentiment
    sentiment = get_sentiment(comment)

    # Print sentiment
    print('Sentiment:', sentiment)

if __name__ == '__main__':
    main()
```

To run this script, save it as `task.py` and execute it using the command `python task.py`. The script will prompt you to enter a comment, and then it will determine the sentiment of the comment using the SentimentIntensityAnalyzer from the NLTK library. The sentiment will be outputted as either "Positive", "Negative", or "Neutral".