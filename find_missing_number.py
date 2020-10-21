""" find missing number in a given array """


class Solution:
    def find_number(self, arr):
        return sum(arr) - len(arr)*(len(arr)+1)//2


s = Solution()
an = s.find_number([1, 2, 4, 5, 6])
print(an)