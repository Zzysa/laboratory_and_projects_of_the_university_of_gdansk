import random


def matrix_sum_and_odd(lines_number_first, columns_number_first, lines_number_second, columns_number_second):
    first_matrix = []
    second_matrix = []
    multiplication_matrix = []
    sum = 0

    if columns_number_first == lines_number_second:
        for i in range(lines_number_first):
            first_matrix.append([])
            for j in range(columns_number_first):
                first_matrix[i].append(random.randrange(1, 10))

        for i in range(lines_number_second):
            second_matrix.append([])
            for j in range(columns_number_second):
                second_matrix[i].append(random.randrange(1, 10))

        for i in range(lines_number_first):
            multiplication_matrix.append([])
            for j in range(columns_number_second):
                multiplication_matrix[i].append(0)

        for i in range(lines_number_first):
            for j in range(columns_number_second):
                for k in range(columns_number_first):
                    print("First: ", sum)
                    sum += first_matrix[i][k] * second_matrix[k][j]
                    print("Second: ", sum)
                multiplication_matrix[i][j] = sum
                sum = 0

        print("First matrix:")
        for i in range(len(first_matrix)):
            print(first_matrix[i])
        print('\n')

        print("Second matrix:")
        for i in range(len(second_matrix)):
            print(second_matrix[i])
        print('\n')

        print("Result multiplication of first and second matrices:")
        for i in range(len(multiplication_matrix)):
            print(multiplication_matrix[i])
        print('\n')
    else:
        print("ERROR! It is impossible to find result of multiplication with these sizes of matrices")


matrix_sum_and_odd(3, 2, 2, 1)
