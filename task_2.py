def method_find_island(data, row_index, column_index):
    # finish if element (row_index, j) in not within the matrix or is not equal 1
    if row_index < 0 or column_index < 0 or row_index >= len(data) or column_index >= len(data[0]) \
            or data[row_index][column_index] != 1:
        return
    # Mark the current element (use number 2)
    data[row_index][column_index] = 2

    method_find_island(data, row_index - 1, column_index)  # up
    method_find_island(data, row_index + 1, column_index)  # down
    method_find_island(data, row_index, column_index - 1)  # left
    method_find_island(data, row_index, column_index + 1)  # right


def count_islands(data):
    count_of_islands = 0
    for i in range(len(data)):
        for j in range(len(data[0])):
            if data[i][j] == 1:
                count_of_islands += 1
                method_find_island(data, i, j)
    return count_of_islands


n = int(input("Enter n: "))
m = int(input("Enter m: "))
matrix = []
for i in range(n):
    row = []
    for j in range(m):
        value = int(input(f"Enter value for matrix[{i}][{j}]: "))
        row.append(value)
    matrix.append(row)

print(count_islands(matrix))
