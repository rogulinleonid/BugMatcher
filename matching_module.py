from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_bugs(student_bugs, reference_bugs):
    results = []
    
    for student_bug in student_bugs:
        best_match = None
        best_score = 0
        
        for bug_id, ref_bug in reference_bugs.items():
            # Векторизация текстов
            vectorizer = TfidfVectorizer()
            tfidf = vectorizer.fit_transform([
                student_bug['description'], 
                ref_bug['description']
            ])
            
            # Расчёт схожести
            similarity = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
            
            if similarity > best_score:
                best_score = similarity
                best_match = bug_id
        
        results.append({
            'student': student_bug['student'],
            'ticket_id': student_bug['id'],
            'found_bug': best_match,
            'confidence': best_score
        })
    
    return results
