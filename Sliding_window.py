""" find maximum window sum 'K' is the size of the window 'N' is size of the array """


def maxSum(arrAy, WindowSize):
    arraySize = len(arrAy)
    if arraySize <= WindowSize:
        print("invalid operation")
        return None

    window_sum = sum(arrAy[i] for i in range(WindowSize))
    max_sum = window_sum

    for i in range(arraySize-WindowSize):
        window_sum = window_sum - arrAy[i] + arrAy[i + WindowSize]
        max_sum = max(window_sum, max_sum)

    return max_sum


arrAy = [60, -20, 30, 70, 95, 60]
k = 3
answer = maxSum(arrAy, k)
print(answer)
