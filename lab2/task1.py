def find_intersections(arr1, arr2):
    result = []
    for i in arr1:
        if i in arr2 and i not in result:
            result.append(i)
    return result

def main():
    array1 = [1, 2, 2, 1]
    array2 = [2, 2]
    answer = find_intersections(array1, array2)
    print("Пересечение двух массивов (без дубликатов):", answer)

if __name__ == "__main__":
    main()