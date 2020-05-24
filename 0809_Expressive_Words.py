class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        from collections import Counter
        set_S = set(S)
        counter_S = Counter(S)
        ans = 0
        for word in words:
            if set_S == set(word):
                i = j = 0
                print(word)
                while i < len(S) and j < len(word):
                    if S[i] != word[j]:
                        break
                    count_s = 1
                    while i < len(S) - 1 and S[i + 1] == S[i]:
                        i += 1
                        count_s += 1
                    count_w = 1
                    while j < len(word) - 1 and word[j + 1] == word[j]:
                        j += 1
                        count_w += 1
                    if count_s < count_w or (count_s > count_w and count_s == 2):
                        break
                    i, j = i + 1, j + 1
                ans = ans + 1 if i == len(S) and j == len(word) else ans
        return ans