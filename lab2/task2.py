def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix)
    matrix2 = [[0] * rows for i in range(cols)]
    return matrix2

def main():
    matrix = [[1, 2, 3], [4, 5, 6, 8, 7]]
    answer = transpose_matrix(matrix)
    print(answer)

if __name__ == "__main__":
    main()