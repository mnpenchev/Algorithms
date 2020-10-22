def insertion_sort(list):
    for i in range(1, len(list)):  # start the loop from the second element
        key_item = list[i]  # this is the element we want to put in the correct place
        j = i - 1  # j will be used to find the correct position of key_item
        while j >= 0 and list[j] > key_item:  # cycle trough the list to find the position of key_item
            list[j+1] = list[j]  # shift the value one position to the left
            j -= 1  # reposition j to the next element
        list[j+1] = key_item
    return list


print(insertion_sort([1,4,7,2,5,3,8]))


