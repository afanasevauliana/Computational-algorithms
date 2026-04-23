def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    matrix2 = []
    for i in range(cols):
        matrix2.append([0] * rows)
    for i in range(rows):
        for j in range(cols):
            matrix2[j][i] = matrix[i][j] 
    return matrix2

def main():
    matrix = [[1, 2, 3], 
             [4, 5, 6]]
    answer = transpose_matrix(matrix)
    print("Транспонированная матрица:")
    for rows in answer:
        print(rows)

if __name__ == "__main__":
    main()