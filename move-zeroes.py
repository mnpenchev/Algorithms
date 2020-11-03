""" move all the zeroes in the list to the end of the list
by moving all the number to the end and track their count
Time complexity = O(2*) loop 2 times trough the list = O(N)
space complexity = O(1) """


def moveZeroes(nums):
    j = 0
    for num in nums:
        if num != 0:
            nums[j] = num
            j += 1

    for x in range(j, len(nums)):
        nums[x] = 0
    return nums


print(moveZeroes([None, 0, False, 0, 3, "a", 5, 4, 0]))


def move_zeros_alltypesdata(array):
    new = []
    zeros = []

    for i in range(len(array)):
        if array[i] == 0 or array[i] == 0.0:
            if type(array[i]) == int or type(array[i]) == float:
                zeros.append(array[i])
            else:
                new.append(array[i])
        else:
            new.append(array[i])

    return new + zeros


print(move_zeros_alltypesdata([None, 0, False, 0, 3, "a", 5, 4, 0]))
