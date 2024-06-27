def check(array):
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in array:
        try:
            nums.remove(i)
            print(nums)
        except:
            return False
    return len(nums) == 0

print(check([5, 4, 1, 7, 8, 9, 2, 3, 6]))