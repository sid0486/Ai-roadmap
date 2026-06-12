import math 

print("="*50)
print("VECTORS - FROM SCRATCH")
print("="*50)


v = [3,4]
print("Vector:",v)

# vector addition:
v1 = [1,2]
v2 = [3,4]

result = [
    v1[0] + v2[0],
    v1[1] + v2[1]
]

print(result)

def vector_add(a,b):
    return [a[i] + b[i] for i in range(len(a))]

def vector_subtract(a,b):
    return [a[i] - b[i] for i in range(len(a))]

a = [2,5,-1]
b = [3,-2,4]
print(vector_add(a,b))
print(vector_subtract(a,b))

king= [1.0,0.9]
man = [0.9,0.2]
woman = [0.1,0.8]
result = vector_add(vector_subtract(king,man),woman)
print(result)

# vector subtraction:
v1 = [5,7]
v2 = [2,3]

result = [
    v1[0] - v2[0],
    v1[1] - v2[1]
]
print(result)


# scalar multipication
v = [3,4]
result = [
    2*v[0],
    2*v[1]
]
print(result)


def scalar_multiply(c,v):
    return [c*x for x in v ]
print(scalar_multiply(4,[2,-1,3]))
print(scalar_multiply(-2,[2,-1,3]))

# magnitude:

import math 

v = [3,4]
magnitude  = math.sqrt(
    v[0]**2 + v[1]**2
)
print(magnitude)

def magnitude(v):
    return math.sqrt(sum(x**2 for x in v ))
print("Magnitude:", magnitude(v))

def euclidean_distance(a,b):
    return math.sqrt(sum((a[i] - b[i])**2 for i in range(len(a))))

a = [1,2]
b = [4,6]
print("Euclidean:",euclidean_distance(a,b))

def euclidean_distance(a, b):
    total = 0
    for i in range(len(a)):
        gap = a[i] - b[i]
        total += gap ** 2
    return math.sqrt(total)

print(euclidean_distance([1, 2], [4, 6]))

# dot product :
v1 = [1,2]
v2 = [3,4]

dot_product = (
    v1[0] * v2[0]) + (
    v1[1] * v2[1])

print(dot_product)

def dot_product(a,b):
    return sum(a[i] * b[i] for i in range(len(a)))

a = [1,2,3]
b = [4,5,6]
print(dot_product(a,b))

x_axis = [1,0]
y_axis = [0,1]
print(dot_product(x_axis,y_axis))

w = [0.5,-0.3,0.8]
x = [2.0,1.5,3.0]
b = 0.1
z = dot_product(w,x) + b 
print(f"Neuron output: {z}")

def cosine_similarity(a,b):
    return dot_product(a,b) / (magnitude(a) * magnitude(b))
print(cosine_similarity([1,2,3],[4,5,6]))


a = [1, 2, 3]
b = [4, 5, 6]

# Calculate dot product without numpy
def dot_product(a,b):
    return sum(a*b for a,b in zip(a,b))

result = dot_product(a,b)
print(result)





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


# # from sentence_transformers import SentenceTransformer
# # import numpy as np

# # model = SentenceTransformer('all-MiniLM-L6-v2')

# # sentences = [
# #     "I love machine learning",
# #     "I enjoy deep learning",
# #     "FastAPI is a web framework",
# #     "Python is great for AI",
# #     "I like pizza"
# # ]

# # # 1. Get embeddings for all sentences
# # embeddings = model.encode(sentences)

# # # 2. Use your cosine_similarity function from earlier
# # def cosine_similarity(a, b):
# #     return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

# # # 3. Compare every sentence with every other sentence
# # for i in range(len(sentences)):
# #     for j in range(i+1, len(sentences)):
# #         score = cosine_similarity(embeddings[i], embeddings[j])
# #         print(f"{sentences[i]!r} vs {sentences[j]!r} → {score:.3f}")



def l1_norm(v):
    return sum(abs(x) for x in v)
    
def l2_norm(v):
    return math.sqrt(sum(x**2 for x in v ))   


v = [3, 4]
print("L1:", l1_norm(v))
print("L2:", l2_norm(v))

def projection(a,b):
    scalar = dot_product(a,b)/ dot_product(b,b)
    return scalar_multiply(scalar,b)

a = [1,2]
b = [1,0]
print(projection(a,b))

def projection(a,b):
    scalar = dot_product(a,b)/dot_product(b,b)
    return scalar_multiply(scalar,b)

a = [3,4]
b = [1,1]
print(projection(a,b))



# def matrix_multiply(A,B):
#     rows_A = len(A)
#     cols_B = len(B[0])
#     cols_A = len(A[0])

#     result = 

def matrix_multiply(A, B):
    rows_A = len(A)
    cols_B = len(B[0])
    cols_A = len(A[0])
    
    result = [[0] * cols_B for _ in range(rows_A)]
    
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

A = [[2, 0], [1, 3]]
B = [[1, 4], [2, 5]]
print(matrix_multiply(A, B))
# expected: [[2, 8], [7, 19]]



def transpose(A):
    rows = len(A)
    cols = len(A[0])

    result = [[0] * rows for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = A[i][j]

    return result

A = [[1, 2, 3],
     [4, 5, 6]]
print(transpose(A))
# expected: [[1, 4], [2, 5], [3, 6]]

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

result = [[0] * len(A[0]) for _ in range(len(A))]

for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j] * B[i][j]

print(result)























