""" save people with less possible boats, boats have weight limit
a boat can carry only 2 people
time complexity O(N logN) because the use of sorting of the input array, looping over sorted array is O(N)
space complexity O(N) same reason"""

from typing import List


class Solution:
    def numRescueBoats(self, people:List[int], limit:int):
        people.sort()
        n = len(people)
        left = 0
        right = len(people) - 1
        boat_number = 0

        while left <= right:
            if left == right:
                boat_number +=1
                break

            if people[left] + people[right] <= limit:
                left +=1

            right -= 1
            boat_number += 1

        return boat_number


s = Solution()
answer = s.numRescueBoats([5, 3, 2, 4, 1, 6], 6)
print(answer)
