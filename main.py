import Levenshtein
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.util import ngrams
import numpy as np


def calculate_similarity(candidate_list, patch_str, top_k=2):
    # 定义一个空的字典来存储每个候选补丁代码的相似度分数
    similarity_scores = {
        'levenshtein': [],
        'cosine': []
    }

    # Levenshtein Distance
    for candidate in candidate_list:
        # 由于Levenshtein距离是一个距离度量（距离越小，相似度越高），我们转换为相似度
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


# 测试函数
candidate_list = [
    "int value = value / 10;",
    "double value = value % 10;",
    "int value = value2 / 10;"
]
patch_str = "int value = value % 10;"
top_k_list = calculate_similarity(candidate_list, patch_str, top_k=1)
print(top_k_list)