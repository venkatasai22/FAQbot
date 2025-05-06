import pandas as pd
import os
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_faqs():
    """Load FAQs from CSV with error handling"""
    try:
        if not os.path.exists('data/faqs.csv'):
            raise FileNotFoundError("FAQ file not found")
            
        faqs = pd.read_csv('data/faqs.csv')
        if faqs.empty:
            logger.warning("FAQ file is empty")
        return faqs
        
    except Exception as e:
        logger.error(f"Error loading FAQs: {str(e)}")
        return pd.DataFrame(columns=['question', 'answer'])

def save_feedback(question, feedback, faq_index=-1):
    """Save user feedback with timestamp"""
    try:
        # Create feedback directory if it doesn't exist
        os.makedirs('data', exist_ok=True)
        
        feedback_data = pd.DataFrame({
            'question': [question],
            'feedback': [feedback],
            'faq_index': [faq_index],
            'timestamp': [datetime.now().isoformat()]
        })
        
        # Write with header if file doesn't exist
        write_header = not os.path.exists('data/feedback.csv')
        feedback_data.to_csv(
            'data/feedback.csv',
            mode='a',
            header=write_header,
            index=False
        )
        logger.info("Feedback saved successfully")
        
    except Exception as e:
        logger.error(f"Error saving feedback: {str(e)}")
        raise
