""" Given an array of strings, group the anagrams together. You can return the answer
in any order.An Anagram is a word or phrase formed by rearranging the letters of a
different word or phrase, typically using all the original letters exactly once.
=> time is O(N*M*Log(M) N input list, M is length of longest string, M * Log(M) because we sort
each string when pass over in the loop"""


class Sol:

    def findHash(self, s):
        return ''.join(sorted(s))

    def anagrams(self, list):
        answers = []
        m = {}
        for s in list:
            hashed = self.findHash(s)
            if hashed not in m:
                m[hashed] = []
            m[hashed].append(s)
        for p in m.values():
            answers.append(p)
        return answers


s = Sol()
answer = s.anagrams(["eat","tea","tan","ate","nat","bat"])
print(answer)