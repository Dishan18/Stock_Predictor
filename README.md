# Stock Predictor and Sentiment Analysis

ML Project to predict stock prices

-Scrape recent news data about a stock using beautifulsoup and requests pacakge and perform sentiment analysis on it using the FinBERT model by HuggingFace.

-Used real time Stock data as Dataset by API calls.

-Developed a Stock prediction Model which consists of two LSTM layers with 64 units each, followed by dropout layers for regularization, and ends with two dense layers (25 units and 1 unit) for output, resulting in Mean absolute error on test set: 2.87% and R2 score: 0.96
