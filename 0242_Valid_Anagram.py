# Runtime: 48 ms, faster than 60.74% of Python3 online submissions for Valid Anagram.
# Memory Usage: 14.2 MB, less than 6.25% of Python3 online submissions for Valid Anagram.

from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''O(nlogn) time O(1) space method: compare sorted strings to be equal'''
        # return sorted(s) == sorted(t)
        
        '''O(n) time O(k) space method: compare two hash table with counts to be equal'''
        # where k is the maximum number of different numbers in two strings
        if len(s) != len(t):
            return False
        c1, c2 = defaultdict(int), defaultdict(int)
        for i in range(len(s)):
            c1[s[i]] += 1
            c2[t[i]] += 1
        return c1 == c2
            