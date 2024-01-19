import Levenshtein
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.util import ngrams
import numpy as np


def calculate_similarity(candidate_list, patch_str, top_k=2):
    similarity_scores = {
        'levenshtein': [],
        'cosine': []
    }

    # Levenshtein Distance
    for candidate in candidate_list:
        similarity_scores['levenshtein'].append(
            (candidate, 1 - Levenshtein.distance(patch_str, candidate) / max(len(patch_str), len(candidate)))
        )

    # Cosine Similarity
    vectorizer = TfidfVectorizer().fit(candidate_list + [patch_str])
    vectors = vectorizer.transform(candidate_list + [patch_str])
    cosine_similarities = cosine_similarity(vectors[-1], vectors[:-1]).flatten()
    for candidate, similarity in zip(candidate_list, cosine_similarities):
        similarity_scores['cosine'].append((candidate, similarity))

    similarity_method = 'cosine'
    similarity_scores[similarity_method].sort(key=lambda x: x[1], reverse=True)

    top_k_list = [item[0] for item in similarity_scores[similarity_method][:top_k]]
    return top_k_list
