class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {len(s): ['']}
        def sentences(i):
            if i in memo:
                return memo[i]
            memo[i] = []
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in wordDict:
                    for tail in sentences(j):
                        tail_ans = tail if tail == '' else ' ' + tail
                        memo[i].append(s[i:j] + tail_ans)
            return memo[i]
        ans = sentences(0)
        return ans