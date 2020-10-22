""" Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the
array, and it should return false if every element is distinct.
method 1 - sort the list, if 2 consecutive elements have the same value, return the value
method 2 - add elements in a set compare the set and list size, if they are the same return true
method 3 - utilize hashmap - Space O(N)"""
from collections import defaultdict


class Sol:
    def dup(self, list):
        m = defaultdict(int)
        for n in list:
            if m[n]:
                return True
            m[n] += 1
        return False


s = Sol()
answer = s.dup([5, 3, 2, 4, 1, 1])
print(answer)
