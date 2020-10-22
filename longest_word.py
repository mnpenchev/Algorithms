""" Output should be the length of the longest word, as a number."""


def find_longest(strng):
    return max(len(a) for a in strng.split())


print(find_longest("welcome to the jungle"))