""" the list have to contain increasing and decreasing sequence i.e. 12321/ 0321 /1432
time is O(N) space is O(1) linear"""
from typing import List


class Solution:
    def validMountainArray(self, A: List[int]):
        if len(A) < 3:
            return False
        i = 1
        while i < len(A) and A[i] > A[i-1]:
            i += 1
        if i == 1 or i == len(A):
            return False
        while i < len(A) and A[i] < A[i-1]:
            i += 1

        return i == len(A)


s = Solution()
answer = s.validMountainArray([1,1,2,3,1])
print(answer)