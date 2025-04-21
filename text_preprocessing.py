import spacy
import re

nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    """Cleans and preprocesses text using NLP."""
    
    # Step 1: Remove extra spaces and convert to lowercase
    text = re.sub(r'\s+', ' ', text).lower()
    
    # Step 2: Process text with spaCy
    doc = nlp(text)
    
    # Step 3: Filter words (remove stopwords, keep only alphabetic words)
    filtered_tokens = []
    for token in doc:
        if not token.is_stop and token.is_alpha:
            filtered_tokens.append(token.lemma_)  # Store lemmatized word
    
    # Step 4: Join words into a clean string
    return " ".join(filtered_tokens)
