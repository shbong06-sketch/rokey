# sparse_matrix.py

from scipy.sparse import csr_matrix

data = [
    [0,0,3],
    [4,0,0],
    [0,5,0]
]

sparse_matrix = csr_matrix(data)
print(sparse_matrix)