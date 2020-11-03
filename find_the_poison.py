""" The King of a small country invites 1000 senators to his annual party. As a tradition, each senator brings the King a bottle of wine. Soon after, the Queen discovers that one of the senators is trying to assassinate the King by giving him a bottle of poisoned wine. Unfortunately, they do not know which senator, nor which bottle of wine is poisoned, and the poison is completely indiscernible.

However, the King has 10 lab rats. He decides to use them as taste testers to determine which bottle of wine contains the poison. The poison when taken has no effect on the rats, until exactly 24 hours later when the infected rats suddenly die. The King needs to determine which bottle of wine is poisoned by tomorrow, so that the festivities can continue as planned.

Hence he only has time for one round of testing, he decides that each rat tastes multiple bottles, according to a certain scheme.

Your Task
You receive an array of integers (0 to 9), each of them is the number of a rat which died after tasting the wine bottles. Return the number of the bottle (1..1000) which is poisoned. """


def find(r):
    pr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in r:
        pr[i] = 1
    pr.reverse()
    string = int(''.join(str(e) for e in pr), 2)

    return string


def find1(r):
    return sum(2**i for i in r)


print(find([0, 3, 5, 4, 9, 8]))  # 825
print(find([0, 1, 9, 3, 5]))  # 555
print(find([0, 1, 2, 3, 4, 6]))  # 95
print(find([0, 1, 3, 4]))  # 27

print(find1([0, 3, 5, 4, 9, 8]))  # 825
print(find1([0, 1, 9, 3, 5]))  # 555
print(find1([0, 1, 2, 3, 4, 6]))  # 95
print(find1([0, 1, 3, 4]))  # 27
