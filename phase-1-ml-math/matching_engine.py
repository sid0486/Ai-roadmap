from linear_algebra import cosine_similarity, dot_product, magnitude

candidate_1 = [9, 8, 6, 7]
candidate_2 = [3, 2, 1, 9]
candidate_3 = [8, 9, 8, 3]

job_1 = [8, 8, 7, 5]
job_2 = [4, 3, 2, 9]

candidates = [candidate_1, candidate_2, candidate_3]
jobs = [job_1, job_2]

for job in jobs:
    results = []
    for candidate in candidates:
        score = cosine_similarity(candidate, job)
        results.append((candidate, score))
    
    sorted_results = sorted(results, key=lambda x: x[1], reverse=True)
    print(f"Job: {job}")
    for candidate, score in sorted_results:
        print(f"  {candidate} -> {score}")
   


















