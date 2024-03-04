import random


def matrix_transposition(columns_number, lines_number):
    matrix = []
    for i in range(lines_number):
        matrix.append([])
        for j in range(columns_number):
            matrix[i].append(random.randrange(1, 10))

    new_matrix = []

    for i in range(len(matrix[0])):
        new_matrix.append([])
        for j in range(len(matrix)):
            new_matrix[i].append(0)

    for i in range(len(matrix)):
        print(matrix[i])
 
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            new_matrix[j][i] = matrix[i][j]

    print('\n')

    for i in range(len(new_matrix)):
        print(new_matrix[i])


matrix_transposition(1, 4)
