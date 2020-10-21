import math


class Solution:
    def count(self, n):
        if n < 2:
            return 0
        isPrime = [True] * n
        isPrime[0] = isPrime[1] = False

        for i in range(2, int(math.ceil(math.sqrt(n)))):
            if isPrime[i]:
                for multiples_of_i in range(i*i, n, i):
                    isPrime[multiples_of_i] = False
        return sum(isPrime)


s = Solution()
a = s.count(12)
print(a)
