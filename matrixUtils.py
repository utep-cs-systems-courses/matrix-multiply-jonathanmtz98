#!/usr/bin/env python3
#Jonathan Martinez
#Parallel Computing

import argparse
import numpy as np

def genMatrix(size, value):
    # genMatrix function will generate a 2d square matrix of a specific size. Here I will use a 256 matrix with values of 1
    matrix = [[value for col in range(0, size)] for row in range(0, size)]
    return matrix

def genMatrix2(size, value):
    # The same thing happens here. Here, we create the second 2d square matrix to be multiplied.
    matrix = np.asarray([np.asarray([value for col in range(0,size)]) for row in range(0,size)])

    return matrix

def printSubarray(matrix, size):
    # This function is used to printSubarray. This will be useful to print results when multiplying matrices.
    """
    Prints the upper left subarray of dimensions size x size of
    the matrix
    """

    for row in range(1, 10):
        for col in range(1, 10):
            print(f'{matrix[row][col]} ' , end='')
        print('')

def writeToFile(matrix, fileName):
    # Function that will help to write a matrix out of a file.
    """
    Writes a matrix out to a file
    """

    with open(fileName, 'w') as file:
        for row in matrix:
            for col in row:
                file.write(f'{col} ')
            file.write('\n')

def readFromFile(fileName):
    #This function is used to read a matrix from a specific file.
    """
    Reads a matrix from a file
    """

    matrix = []

    with open(fileName, 'r') as file:
        for line in file:
            row = [int(val) for val in line.split()]
            matrix.append(row)

    return matrix

def matrixMultiply(genMatrix, genMatrix2):
    #This is where matrices get multiplied. What I did first is that I generated a new matrix called result.
    #After that, I used a nested for loop that covers the length of matrix 1 and matrix 2.
    #After that, I added those results in result matrix. Finally, I just returned it.
    result = genMatrix(256,0)
    for i in range(len(genMatrix)):
        for j in range(len(genMatrix2[0])):
            for k in range(len(genMatrix2)):

                result[i][j] += genMatrix[i][k] * genMatrix2[k][j]
                return result
def main():
    """
    Used for running as a script
    """
    parser = argparse.ArgumentParser(description=
        'Generate a 2d matrix and save it to  a file.')
    parser.add_argument('-s', '--size', default=256, type=int,
        help='Size of the 2d matrix to generate')
    parser.add_argument('-v', '--value', default=3, type=int,
        help='The value with which to fill the array with')
    parser.add_argument('-f', '--filename',
        help='The name of the file to save the matrix in (optional)')

    args = parser.parse_args()

#What I did here is that I created two new matrices in order to test multiplying function.
#First, I used the one already provided.
#Then, I created a second one, called mat2.
#Then, I created a third one, called mat3.
#Finally, I just called matrixMultiply and printed the subarray.
    mat = genMatrix(args.size, args.value)
    mat2 = genMatrix2(args.size, args.value)
    mat3 = matrixMultiply(mat, mat2)
    printSubarray(mat3, args.size)

    if args.filename is not None:
        print(f'Writing matrix to {args.filename}')
        writeToFile(mat, args.filename)

        print(f'Testing file')
        printSubarray(readFromFile(args.filename))
    else:
        printSubarray(mat)

if __name__ == '__main__':
    main()
