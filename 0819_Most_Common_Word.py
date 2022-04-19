# Runtime: 45 ms, faster than 65.43% of Python3 online submissions for Most Common Word.
# Memory Usage: 13.9 MB, less than 40.74% of Python3 online submissions for Most Common Word.
import string
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        from collections import defaultdict
        word_count = defaultdict(int)
        max_count = i = 0
        banned = set(banned)
        while i != len(paragraph):
            while i != len(paragraph) and paragraph[i] not in string.ascii_letters:
                i += 1
            if i == len(paragraph):
                break
            word = []
            while i != len(paragraph) and paragraph[i] in string.ascii_letters:
                word.append(paragraph[i])
                i += 1
            word = ''.join(word).lower()
            if word in banned:
                continue
            word_count[word] += 1
            if word_count[word] > max_count:
                ans = word
                max_count = word_count[word]
        return ans