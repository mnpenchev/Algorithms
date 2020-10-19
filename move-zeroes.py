""" move all the zeroes in the list to the end of the list
by moving all the number to the end and track their count
Time complexity = O(2*) loop 2 times trough the list = O(N)
space complexity = O(1) """
from typing import List


class Solution:
    def moveZeroes(self, nums : List[int]):
        j = 0
        for num in nums:
            if num != 0:
                nums[j] = num
                j += 1

        for x in range(j, len(nums)):
            nums[x] = 0
        print(nums)


s = Solution()
s.moveZeroes([0, 3, 0, 5, 4, 0])


