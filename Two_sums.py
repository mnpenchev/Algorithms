""" Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice. """


class Sol:
    def twoSums(self, nums, target):
        m = {}
        n = len(nums)
        for i in range(0, n):
            goal = target - nums[i]
            if goal in m:
                return [m[goal], i]
            m[nums[i]] = i


s = Sol()
a = s.twoSums([3, 2, 1, 5], 8)
b = s.twoSums([1, 2, 3, 4, 5], 7)
print(a, b)
