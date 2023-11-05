import numpy as np

# Задаємо розмірність матриці
N = 5  # Кількість рядків
M = 4  # Кількість стовпців

# Генеруємо випадкову матрицю
A = np.random.rand(N, M)

# Знаходимо середні значення для кожного рядка
row_means = np.mean(A, axis=1)

# Знаходимо найнижче середнє значення
min_row_mean = np.min(row_means)

# Знаходимо індекс рядка з найнижчим середнім значенням
min_row_index = np.argmin(row_means)

# Виводимо матрицю та результати
print("Матриця A:")
print(A)
print("\nСередні значення для кожного рядка:")
print(row_means)
print(f"\nНайнижче середнє значення: {min_row_mean} (знаходиться в рядку {min_row_index})")
ult[1], z = {result[2]}










