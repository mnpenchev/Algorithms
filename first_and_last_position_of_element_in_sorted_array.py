""" [10, 11, 12, 12, 12, 13, 14] should return index 2 and index 4 """


class Solution:
    def get_left(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                if mid - 1 >= 0 and nums[mid-1] != target or mid == 0:
                    return mid
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return None

    def get_right(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right)//2
            if nums[mid] == target:
                if mid + 1 < len(nums) and nums[mid + 1] != target or mid == len(nums) - 1:
                    return mid
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return None

    def range(self, nums, target):
        left = self.get_left(nums, target)
        right = self.get_right(nums, target)
        return [left, right]


s = Solution()
answer = s.range([10, 11, 12, 12, 12, 13, 14], 12)
print(answer)
