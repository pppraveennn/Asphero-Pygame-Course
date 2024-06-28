def empty2DArray(size):
    count = 0
    array = []
    for i in range(size):
        row = []
        for j in range(size):
            count += 1
            row.append(count)
        array.append(row)
    return array

def print2DGrid(array):
    for row in array:
        print(row)

print2DGrid(empty2DArray(5))