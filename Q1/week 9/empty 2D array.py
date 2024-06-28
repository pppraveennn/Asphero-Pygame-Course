def empty2DArray(size):
    array = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(0)
        array.append(row)
    return array

print(empty2DArray(5))

def print2DGrid(array):
    for row in array:
        print(row)

print2DGrid(empty2DArray(5))