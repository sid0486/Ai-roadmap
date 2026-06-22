import math 
print("="*50)
print("Vectors - From scratch")
print("="*50)


v1 = [1,2]
v2 = [3,4]

result = [
    v1[0] + v2[0],
    v1[1] + v2[1]
]
print("Vector_add:",result)

def vector_add(a,b):
    return[a[i] + b[i] for i in range(len(a))]

def vector_subtract(a,b):
    return[a[i] - b[i] for i in range(len(a))]

a = [2,5,-1]
b = [3,-2,4]
print("Vector_add:",vector_add(a,b))
print("Vector_sub:",vector_subtract(a,b))

v1 = [5,7]
v2 = [2,3]

result = [
    v1[0] - v2[0],
    v1[1] - v2[1]
]
print("Vector_sub:",result)

v = [3,4]
result = [
    2*v[0],
    2*v[1]
]
print("Scalar_multiplication:",result)

def scalar_multiply(c,v):
    return [c*x for x in v]

print("Scalar multiply function (4 * [2,-1,3]):", scalar_multiply(4,[2,-1,3]))
print("Scalar multiply function (-2 * [2,-1,3]):", scalar_multiply(-2,[2,-1,3]))

v = [3,4]
magnitude = math.sqrt(v[0]**2 + v[1]**2)
print("Magnitude:",magnitude)

def magnitude(v):
    return math.sqrt(sum(x**2 for x in v))
print("Magnitude:",magnitude(v))

def euclidean_distance(a,b):
    return math.sqrt(sum((a[i] - b[i])**2 for i in range(len(a))))

a = [1,2]
b = [4,6]
print("Euclidean distance (list comprehension):", euclidean_distance(a,b))

def euclidean_distance(a,b):
    total = 0 
    for i in range(len(a)):
        gap = a[i] - b[i]
        total += gap**2
    return math.sqrt(total)
print(euclidean_distance([1,2],[4,6]))

v1 = [1,2]
v2 = [3,4]

dot_product = (
    v1[0] * v2[0],
    v1[1] * v2[1]
)
print(dot_product)

def dot_product(a,b):
        return sum(a[i]*b[i] for i in range(len(a)))

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
print(f"Neuron output:{z}")


def cosine_similarity(a,b):
    return dot_product(a,b)/(magnitude(a)*magnitude(b))
print("Cosine similarity:",cosine_similarity([1,2,3],[4,5,6]))


def mean_center(data):
    mean = sum(data)/len(data)
    return [x - mean for x in data]
data = [2,4,6,8,10]
centered = mean_center(data)
print("Mean centered:",centered)
print("Sum of centered:",sum(centered))

def l1_norm(v):
    return sum(abs(x) for x in v )

v = [3,4]
print("L1 norm:", l1_norm(v))

def l2_norm(v):
    return math.sqrt(sum(x**2 for x in v))

print("L2 norm:",l2_norm(v))

def projection(a,b):
    scalar = dot_product(a,b)/dot_product(b,b)
    return scalar_multiply(scalar,b)

a = [1,2]
b = [1,0]
print("Projection of [1,2] onto [1,0]:",projection(a,b))

a = [3,4]
b = [1,1]
print("Projection of [3,4] onto [1,1]:", projection(a,b))


def linear_combination(a,b,scalar_a,scalar_b):
    return [scalar_a*a[i] + scalar_b*b[i] for i in range(len(a))]

v1 = [1, 2]
v2 = [3, 4]
scalar_1 = 2
scalar_2 = 3
print(linear_combination(v1,v2,scalar_1,scalar_2))
print(linear_combination([1,2], [3,4], 3, 2))

i = [1,0]
j = [0,1]
result = linear_combination(i,j,5,7)
print(result)

def linear_combination_any(vectors,scalars):
    if len(vectors) != len(scalars):
        print("Mismatch")
        return None 

    result = [0] * len(vectors[0])
    for i in range(len(vectors)):
        for j in range(len(result)):
            result[j] += scalars[i] * vectors[i][j]
    return result

vectors = [[1, 2, 0], [3, 4, 5]]  # Now both length 3
scalars = [2, 3]
result = linear_combination_any(vectors, scalars)
print(result)


# ============ MATRIX OPERATIONS ============

print("\n" + "="*50)
print("MATRICES - FROM SCRATCH")
print("="*50)

def get_order(A):
    rows = len(A)
    cols = len(A[0])
    return rows , cols

A = [[1,2],[3,4],[5,6]]
print("Matrix order:",get_order(A))

def print_matrix(A):
    row = len(A)
    col = len(A[0])
    for i in range(row):
        print(*A[i])

A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
print("Print matrix:")
print_matrix(A)


def add_matrices(A,B):
    if get_order(A) != get_order(B):
        print("Matrix mismatch")
        return None
    rows,cols = get_order(A)
    C = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(A[i][j] + B[i][j])
        C.append(row)
    return C

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

print("Matrix addition:")
C = add_matrices(A, B)
print_matrix(C)


def subtract_matrices(A,B):
    if get_order(A) != get_order(B):
        Print("Mismatch")
        return None

    rows,cols = get_order(A)
    C = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(A[i][j] - B[i][j])
        C.append(row)
    return C

A = [[4,5],[7,8]]
B = [[9,10],[11,12]]
C = subtract_matrices(A,B)
print_matrix(C)

def transpose(A):
    rows = len(A)
    cols = len(A[0])
    result = [[0]*rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            result[j][i] = A[i][j]
    return result

A = [[1, 2, 3],
     [4, 5, 6]]
print("Transpose:")
print(transpose(A))


def matrix_vector_multiply(A,v):
    result = []
    for row in A:
        value = 0 
        for i in range(len(v)):
            value += row[i] * v[i]
        result.append(value)
    return result


A = [
    [0, -1],
    [1, 0]
]
v = [1, 0]
print("Matrix-vector multiplication:", matrix_vector_multiply(A, v))


def matrix_multiply(A, B):
    rows_A = len(A)          # Number of rows in A
    cols_B = len(B[0])       # Number of columns in B
    cols_A = len(A[0])       # Number of columns in A (must equal rows of B)
    
    # Create result matrix filled with zeros
    result = [[0] * cols_B for _ in range(rows_A)]
    
    # Triple nested loops!
    for i in range(rows_A):          # For each row in A
        for j in range(cols_B):      # For each column in B
            for k in range(cols_A):  # For each element in the row/column
                result[i][j] += A[i][k] * B[k][j]
    
    return result

A = [[2, 0], [1, 3]] 
B = [[1, 4], [2, 5]] 
print("Matrix multiplication (2x2):", matrix_multiply(A, B))

A = [[1, 2, 3], [4, 5, 6]]
B = [[7, 8], [9, 10], [11, 12]]
print("Matrix multiplication (2x3 * 3x2):", matrix_multiply(A, B))


def determinant_2x2(matrix):
    result = matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    return result 

matrix = [[2,4],[5,8]]
print("Determinant:", determinant_2x2(matrix))


def inverse_2x2(A):
    det = determinant_2x2(A)
    if det == 0 :
        raise ValueError("Matrix is singular, no inverse exists")

    a = A[0][0]
    b = A[0][1]
    c = B[1][0]
    d = B[1][1]
    new_matrix = [
        [d/det,-b/det],
        [-c/det,a/det]
    ]
    return new_matrix

A = [[4, 7], [2, 6]]
print("Inverse:", inverse_2x2(A))


print("\n" + "="*50)
print("ADDITIONAL TESTS")
print("="*50)

king = [1.0,0.9]
man = [0.9,0.2]
woman = [0.1,0.8]
result = vector_add(vector_subtract(king,man),woman)
print("Word embedding analogy (king - man + woman):", result)

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

result = [[0] * len(A[0]) for _ in range(len(A))]

for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j] = A[i][j] * B[i][j]

print("Element-wise matrix multiplication:", result)



























