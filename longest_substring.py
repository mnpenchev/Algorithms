""" return the longest substring without repeating characters """


class Solution:
    def length(self, s):
        m = {}
        left = 0
        right = 0
        ans = 0
        n = len(s)
        while left < n and right < n:
            el = s[right]
            if el in m:
                left = max(left, m[el] + 1)
            m[el] = right
            ans = max(ans, right-left+1)
            right += 1
        return ans


s = Solution()
answer = s.length("substring")
print(answer)
