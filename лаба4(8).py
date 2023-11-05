import numpy as np

A = np.array([[14, 4, 6],
              [5, -3, 2],
              [10, -11, 5]])

B = np.array([30, 15, 36])

det_A = np.linalg.det(A)

A1 = A.copy()
A2 = A.copy()
A3 = A.copy()

A1[:, 0] = B
A2[:, 1] = B
A3[:, 2] = B

x1 = np.linalg.det(A1) / det_A
x2 = np.linalg.det(A2) / det_A
x3 = np.linalg.det(A3) / det_A

print(f'Розв\'язок методом Крамера:')
print(f'x = {x1}')
print(f'y = {x2}')
print(f'z = {x3}')

result = np.linalg.solve(A, B)
print(f'Розв\'язок з використанням solve(): x = {result[0]}, y = {result[1]}, z = {result[2]}')






