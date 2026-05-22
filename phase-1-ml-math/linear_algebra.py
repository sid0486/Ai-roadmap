# v = [3,4]
# print(v)

# # vector addition:
# v1 = [1,2]
# v2 = [3,4]

# result = [
#     v1[0] + v2[0],
#     v1[1] + v2[1]
# ]

# print(result)

# # vector subtraction:
# v1 = [5,7]
# v2 = [2,3]

# result = [
#     v1[0] - v2[0],
#     v1[1] - v2[1]
# ]
# print(result)

# # scalar multipication
# v = [3,4]
# result = [
#     2*v[0],
#     2*v[1]
# ]
# print(result)


# # magnitude:

# import math 

# v = [3,4]
# magnitude  = math.sqrt(
#     v[0]**2 + v[1]**2
# )
# print(magnitude)

# # dot product :
# v1 = [1,2]
# v2 = [3,4]

# dot_product = (
#     v1[0] * v2[0]) + (
#     v1[1] * v2[1])

# print(dot_product)



# a = [1, 2, 3]
# b = [4, 5, 6]

# # Calculate dot product without numpy
# def dot_product(a,b):
#     return sum(a*b for a,b in zip(a,b))

# result = dot_product(a,b)
# print(result)



# A = [[1, 2], [3, 4]]
# B = [[5, 6], [7, 8]]

# def magnitude(a):
#     return sum(x**2 for x in a) ** 0.5

# def cosine_similarity(a, b):
#     result = dot_product(a, b) / (magnitude(a) * magnitude(b))
#     return result

# print(cosine_similarity(a,b))



# i = [1,0]
# j = [0,1]

# v = [
#     3 * i[0] + 2 * j[0],
#     3 * i[1] + 2 * j[1]
# ]
# print(v)


# v = [1,2]
# w = [3,4]
# a = 2
# b = 3 

# result=[
#     a * v[0] + b * w[0],
#     a * v[1] + b * w[1]
# ]
# print(result)

# v = [1,2]

# for a in range(-5,6):
#     result = [ 
#         a * v[0],
#         a * v[1]
#     ]
#     print(result)

# v1 = [3,6]
# v2 = [4,8]
# a = 3
# b = 2 
# result = [
#     a * v1[0] + a * v2[0],
#     b * v1[1] + b * v2[1],
# ]
# print(result)
# 5

# def linear_combination(v1,v2,a,b):
#     result = [
#         a * v1[0] + b * v2[0],
#         a * v1[1] + b * v2[1],
#     ]
#     return result
# print(linear_combination([3,6], [4,8], 3, 2))
# print(linear_combination([1,2,3], [4,5,6], 2, 3)) 



# i = [1,0]
# j = [0,1]
 
# result = linear_combination(i,j,5,7)
# print(result)

# result = linear_combination(i,j,3,-2)
# print(result)


# v1 = [1,1]
# v2 = [1,-1]
# result = linear_combination(v1,v2,4,2)
# print(result)


from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

sentences = [
    "I love machine learning",
    "I enjoy deep learning",
    "FastAPI is a web framework",
    "Python is great for AI",
    "I like pizza"
]

# 1. Get embeddings for all sentences
embeddings = model.encode(sentences)

# 2. Use your cosine_similarity function from earlier
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# 3. Compare every sentence with every other sentence
for i in range(len(sentences)):
    for j in range(i+1, len(sentences)):
        score = cosine_similarity(embeddings[i], embeddings[j])
        print(f"{sentences[i]!r} vs {sentences[j]!r} → {score:.3f}")