""" in a given array every numbers is present twice and there is just on number present only once, find the number """


class Sol:
    def find(self, li):
        return 2*sum(set(li)) - sum(li)


s = Sol()
a = s.find([1,1,2,2,3,4,4,5,5])
print(a)