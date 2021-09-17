#Jonathan Martinez
import argparse
import numpy as np
import time

def genMatrix(size, value):
    """
    Generates a 2d square matrix of the specified size with the specified values
    """
    matrix = [[value for col in range(0,size)] for row in range(0,size)]
    return matrix

def genMatrix2(size, value):
    """
    Generates a 2d square matrix of the specified size with the specified values
    """
    matrix = np.asarray([ np.asarray([value for col in range(0,size)]) for row in range(0,size)])
    return matrix

def matrixMultiply(matrix1,matrix2):
    #Fixed matrixMultiply
    matrix = genMatrix2(128,0)
    with pymp.Parallel() as p:#Added pymp to make matrix multiplier run in parallel.
        for i in range(len(matrix1)):
            for j in range(len(matrix2[0])):
                for k in range(len(matrix2)):
                    matrix[i][j] = ((matrix1[i][k]) * (matrix2[k][j]))
    return matrix

def printSubarray(matrix, size=10):
    """
    Prints the upper left subarray of dimensions size x size of
    the matrix
    """
    for row in range(1, 10):
        for col in range(1, 10):
            print(f'{matrix[row][col]} ' , end='')
        print('')

def writeToFile(matrix, fileName):
    """
    Writes a matrix out to a file
    """
    with open(fileName, 'w') as file:
        for row in matrix:
            for col in row:
                file.write(f'{col} ')
            file.write('\n')

def readFromFile(fileName):
    """
    Reads a matrix from a file
    """
    matrix = []
    with open(fileName, 'r') as file:
        for line in file:
            row = [int(val) for val in line.split()]
            matrix.append(row)
    return matrix

def main():
    """
    Used for running as a script
    """
    parser = argparse.ArgumentParser(description=
        'Generate a 2d matrix and save it to  a file.')
    parser.add_argument('-s', '--size', default=128, type=int,
        help='Size of the 2d matrix to generate')
    parser.add_argument('-v', '--value', default=2, type=int,
        help='The value with which to fill the array with')
    parser.add_argument('-f', '--filename',
        help='The name of the file to save the matrix in (optional)')
    args = parser.parse_args()
    matrix1 = genMatrix2(args.size, args.value)
    matrix2 = genMatrix2(args.size, args.value)
    matrix3 = genMatrix2(128,0)
    finalTime = 0
    for i in range(3):#Number of times the program will make the process of multiplying
        timeS = time.time()#Start
        matrix3 = matrixMultiply(matrix1,matrix2)#Call function
        runningtime = time.time() - timeS
        finalTime += runningtime#Total time
        printSubarray(matrix3)
        print(f'Running Time: '+str(runningtime)+' secs')#Print the total running time

if __name__ == '__main__':
    # execute only if run as a script
    main()
