import numpy as np
from string import ascii_lowercase

def reduce(a, b): # takes two indices for doing Gauss/Gauss-Jordan reduction where a is kept and b is reduced
    matrix[a] = matrix[a] / matrix[a][a] # initial row is scaled
    ratio = float(matrix[b][a] / matrix[a][a]) # find the ratio between starting terms
    matrix[b] = matrix[b] - (matrix[a] * ratio) #b is reduced by ratio*a to eliminate leading term

    for i in range(len(matrix[b])):
        if (matrix[b][i] != 0):
            matrix[b] = matrix[b] / matrix[b][i]
            break
    print("Reduce:\n", matrix)

def solve(matrix):

    print("Initial Matrix:\n" + str(matrix) + "\n")
    rows = len(matrix)
    for i in range(rows): # for each row:
        if (matrix[i][i] == 0): # if current row starts with zero
            for j in range(i+1, rows): # for each row after:
                if (matrix[j][i] != 0): # find a row with a non-zero value and swap the rows
                    matrix[i], matrix[j] = matrix[j], matrix[i]
                    break
        for j in range(i+1, rows): # for each row after:
            if (matrix[j][i] != 0): # Do Gaussian Reduction
                    reduce(i, j)
    for i in range(rows-1): # For each row (starting at bottom) do Gauss-Jordan Reduction
        if(matrix[rows - i - 1][rows - i - 1] != 0):
            for j in range(i + 1, rows):
                reduce(rows - i - 1, rows - j - 1)
    #Printing result:
    print("Final Matrix:\n" + str(matrix))
    for i in range(len(matrix[0])-1):
        print(str(matrix[:, i]) +  ascii_lowercase[(23+i) % 26], end = ' ')
        if (i < len(matrix[0]) - 2):
            print('+ ', end = '')
    print(" = ", matrix[:, len(matrix[0]) - 1])

matrix = [[2.0, 3.0, -1.0, 14.0], [1.0, -1.0, 0.0, -1.0], [0.0, -3.0, 1.0, 2.0]]
matrix = np.array(matrix)

solve(matrix)