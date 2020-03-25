# Runtime: 112 ms, faster than 36.31% of Python3 online submissions for Group Anagrams.
# Memory Usage: 18.9 MB, less than 11.32% of Python3 online submissions for Group Anagrams.

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        for str1 in strs:
            atoz = [0] * 26
            for cha in str1:
                atoz[ord(cha)-97] += 1
            anagram_dict[tuple(atoz)].append(str1)
        return list(anagram_dict.values())