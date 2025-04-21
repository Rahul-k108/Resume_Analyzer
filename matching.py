from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from text_preprocessing import preprocess_text

def match_resume_to_job(resume_text, job_desc):
    """Computes a similarity score between resume and job description."""
    resume_text = preprocess_text(resume_text)
    job_desc = preprocess_text(job_desc)

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([resume_text, job_desc])

    similarity_score = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])[0][0]
    return round(similarity_score * 100, 2)  # Convert to percentage
