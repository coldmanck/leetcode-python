class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        '''Hashmap: time O(n) space O(n)'''
        if not trust:
            return 1
        trust_cache = {} # key of person, value of [n_trust_others, n_trusted]
        for i, j in trust:
            if not i in trust_cache:
                trust_cache[i] = [1, 0]
            else:
                trust_cache[i][0] += 1
            if not j in trust_cache:
                trust_cache[j] = [0, 1]
            else:
                trust_cache[j][1] += 1
        for person, (n_trust_others, n_trusted) in trust_cache.items():
            if n_trust_others == 0 and n_trusted == N - 1:
                return person
        return -1