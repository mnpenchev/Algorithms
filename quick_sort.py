from random import randint


def quicksort(list):
    if len(list)<2:
        return list
    low, same, high = [], [], []
    pivot = list[randint(0, len(list) - 1)]
    for i in list:
        if i < pivot:
            low.append(i)
        elif i == pivot:
            same.append(i)
        elif i > pivot:
            high.append(i)

    return quicksort(low) + same + quicksort(high)


print(quicksort([3,4,7,1,2,6,5,9,8]))
