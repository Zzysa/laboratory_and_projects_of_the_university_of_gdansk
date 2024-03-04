import random


def matrix_sum_and_odd(columns_number_first, lines_number_first, columns_number_second, lines_number_second):
    first_matrix = []
    second_matrix = []
    sum_matrix = []
    odd_matrix = []

    if columns_number_first == columns_number_second and lines_number_first == lines_number_second:
        for i in range(lines_number_first):
            first_matrix.append([])
            for j in range(columns_number_first):
                first_matrix[i].append(random.randrange(1, 10))

        for i in range(lines_number_second):
            second_matrix.append([])
            for j in range(columns_number_second):
                second_matrix[i].append(random.randrange(1, 10))

        for i in range(len(first_matrix)):
            sum_matrix.append([])
            for j in range(len(first_matrix[i])):
                sum_matrix[i].append(0)

        for i in range(len(first_matrix)):
            odd_matrix.append([])
            for j in range(len(first_matrix[i])):
                odd_matrix[i].append(0)

        for i in range(len(first_matrix)):
            for j in range(len(first_matrix[i])):
                sum_matrix[i][j] = first_matrix[i][j] + second_matrix[i][j]

        for i in range(len(first_matrix)):
            for j in range(len(first_matrix[i])):
                odd_matrix[i][j] = first_matrix[i][j] - second_matrix[i][j]

        print("First matrix:")
        for i in range(len(sum_matrix)):
            print(first_matrix[i])
        print('\n')

        print("Second matrix:")
        for i in range(len(sum_matrix)):
            print(second_matrix[i])
        print('\n')

        print("Result of sum of first and second matrices:")
        for i in range(len(sum_matrix)):
            print(sum_matrix[i])
        print('\n')

        print("Result odd of first and second matrices:")
        for i in range(len(sum_matrix)):
            print(odd_matrix[i])
        print('\n')
    else:
        print("ERROR! It is impossible to find result of sum and odd with these sizes of matrices")


matrix_sum_and_odd(2, 1, 2, 1)
