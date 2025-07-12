Sentiment Analysis Desktop App (Tkinter + VADER + TextBlob)

A simple and interactive desktop GUI application built with Python Tkinter that analyzes the sentiment of user-input text using two popular NLP tools:  
VADER (Valence Aware Dictionary and sEntiment Reasoner)  
TextBlob
The interface visualizes the result with a pie chart, making it easy to understand how positive, negative, or neutral your text is.

Features
1)Simple Tkinter interface  
2)Real-time sentiment analysis  
3)Dual sentiment engines: VADER + TextBlob  
4)Pie chart visualization using Matplotlib  
5)Fully offline desktop app — no server or internet needed  

Technologies Used
- Python 3
- Tkinter – for GUI
- NLTK (VADER) – sentiment analysis
- TextBlob – sentiment scoring
- Matplotlib – chart plotting
- Pillow – to display charts in GUI

Installation
1. Clone the Repository
git clone https://github.com/your-username/sentiment-analysis-tkinter.git
cd sentiment-analysis-tkinter
2. Install Required Packages
pip install nltk textblob matplotlib pillow
Also run the following once to download the VADER lexicon:
import nltk
nltk.download('vader_lexicon')
Run the App
python sentiment_gui.py
