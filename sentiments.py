import tkinter as tk
from tkinter import messagebox
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
import matplotlib.pyplot as plt
from PIL import Image, ImageTk
import io
import nltk

nltk.download('vader_lexicon')

# -----------------------------
# Sentiment Analysis Functions
# -----------------------------
def analyze_sentiment_vader(text):
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(text)
    compound_score = sentiment_scores['compound']
    if compound_score >= 0:
        sentiment_label = 'Positive'
    else:
        sentiment_label = 'Negative'
    return sentiment_label, compound_score

def analyze_sentiment_textblob(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        sentiment_label = 'Positive'
    elif polarity < 0:
        sentiment_label = 'Negative'
    else:
        sentiment_label = 'Neutral'
    return sentiment_label, abs(polarity)

# -----------------------------
# GUI Application
# -----------------------------
def analyze_text():
    input_text = text_entry.get("1.0", tk.END).strip()
    if not input_text:
        messagebox.showwarning("Input Error", "Please enter some text.")
        return

    # Analyze
    vader_label, vader_score = analyze_sentiment_vader(input_text)
    textblob_label, textblob_score = analyze_sentiment_textblob(input_text)

    # Display results
    result_label.config(
        text=f"VADER: {vader_label} ({vader_score:.2f})\nTextBlob: {textblob_label} ({textblob_score:.2f})"
    )

    # Sentiment counts for pie chart
    counts = {'Positive': 0, 'Negative': 0, 'Neutral': 0}
    counts[vader_label] += 1
    counts[textblob_label] += 1

    # Pie Chart
    labels = list(counts.keys())
    sizes = list(counts.values())
    colors = ['lightgreen', 'lightcoral', 'lightgray']

    plt.figure(figsize=(4, 4))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title('Sentiment Distribution')
    plt.axis('equal')

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    chart_img = Image.open(buf)
    chart_img = chart_img.resize((200, 200))
    photo = ImageTk.PhotoImage(chart_img)
    chart_label.config(image=photo)
    chart_label.image = photo
    plt.close()

# -----------------------------
# Tkinter Window Setup
# -----------------------------
root = tk.Tk()
root.title("Sentiment Analysis")
root.geometry("500x500")

tk.Label(root, text="Enter a sentence:").pack(pady=10)
text_entry = tk.Text(root, height=4, width=50)
text_entry.pack()

tk.Button(root, text="Analyze", command=analyze_text).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

chart_label = tk.Label(root)
chart_label.pack(pady=10)

root.mainloop()
