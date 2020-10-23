class Solution:
    def fourSum(self, A, B, C, D):
        m = {}
        ans = 0

        for i in range(0, len(A)):
            x = A[i]
            for j in range(0, len(B)):
                y = B[j]
                if x + y not in m:
                    m[x + y] = 0
                m[x + y] += 1

        for i in range(0, len(C)):
            x = C[i]
            for j in range(0, len(D)):
                y = D[j]
                target = -(x + y)
                if target in m:
                    ans += m[target]

        return ans


s = Solution()
answer = s.fourSum([-1, 1], [-2, 2], [1, -3], [-1, 3])
print(answer)