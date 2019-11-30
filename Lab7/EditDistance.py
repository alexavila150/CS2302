def edit_distance(str1, str2):
    # Create Matrix
    matrix = []
    for i in range(len(str1) + 1):
        matrix.append([-1] * (len(str2) + 1))

    # Fill first column and first row
    for i in range(len(str1) + 1):
        matrix[i][0] = i

    for i in range(len(str2) + 1):
        matrix[0][i] = i

    # Traverse the matrix to calculate every value
    for i in range(1, len(matrix)):  # str1
        for j in range(1, len(matrix[i])):  # str2
            if str1[i - 1] == str2[j - 1]:
                print(str1[i - 1] + " " + str2[j - 1])
                matrix[i][j] = matrix[i - 1][j - 1]
            else:
                matrix[i][j] = min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + 1

    print(matrix)
    return matrix[-1][-1]


edit_distance("santa", "ant")
