# FAQ Chatbot with Feedback Loop

An NLP-based chatbot that answers user questions by matching them to FAQs using TF-IDF and cosine similarity, with a feedback mechanism for continuous improvement.

## Features

- Natural language processing for question matching
- Feedback collection for model improvement
- Simple web interface
- Data stored in CSV files

## Installation

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application:
```bash
python app.py
```

Then open `http://localhost:5000` in your browser.

## Configuration

- Add FAQs in `data/faqs.csv`
- Feedback is stored in `data/feedback.csv`

## Tech Stack

- Python
- Flask
- Scikit-learn
- Pandas
