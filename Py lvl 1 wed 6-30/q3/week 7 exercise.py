def checkNotValid(array):
        array = [int(x) for x in array if x != '_']
        array.sort()
        return array != [1, 2, 3, 4, 5, 6, 7, 8, 9] and len(array) == 9

print(checkNotValid([1, 1, 3, 4, 5, 6, 7, 8, 9]))