from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def process_query(user_question):
    try:
        # Load FAQs with error handling
        faqs = pd.read_csv('data/faqs.csv')
        if len(faqs) == 0:
            return "No FAQs available. Please try again later.", -1
            
        # Initialize and fit vectorizer
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform(faqs['question'].tolist() + [user_question])
        
        # Calculate similarity
        cosine_sim = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
        closest_faq_index = cosine_sim.argsort()[0][-1]
        
        # Get threshold for minimum similarity
        max_similarity = cosine_sim[0][closest_faq_index]
        if max_similarity < 0.3:  # Threshold for considering a match
            return "I'm not sure I understand. Could you rephrase your question?", -1
            
        answer = faqs.iloc[closest_faq_index]['answer']
        return answer, closest_faq_index
        
    except Exception as e:
        logger.error(f"Error processing query: {str(e)}")
        return "Sorry, I encountered an error processing your request.", -1
