class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Time O(len(ransomNote) + len(magazine))
        # Space O(len(magazine))
        from collections import Counter
        mag = Counter(magazine)
        for ch in ransomNote:
            if not ch in mag or not mag[ch]:
                return False
            mag[ch] -= 1
        return True