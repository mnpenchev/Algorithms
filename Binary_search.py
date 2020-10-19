""" works with sorted lists, search by value to return the index """


def binarySearch(arr, target):
    """ set two pointer 1st is at the beginning, second at the end of the list """
    left = 0
    right = len(arr)-1

    while left <= right:
        mid = (left + right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return None


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 6

result = binarySearch(arr, target)

if result is not None:
    print("Element is present at index ", result)
else:
    print("Element is not present in the array")
