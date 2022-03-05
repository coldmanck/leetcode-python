from functools import lru_cache

class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        # use dp because of finding minimal difficulty of a list of jobs
        # dp(i, day) returns the mimimal difficulty of jobs starting jD[i:] and on the 'day'
        # recurrence relation: 
        #   for j in range(day, len(jD) - (d - day)):
        #       hardest = max(hardest, jD[j])
        #       min_diff =  min(hardest + dp(i + 1, day + 1))
        # base cases: happen when day = d
        #   hardest = 0
        #   base_cases = [0] * len(jD)
        #   for i in range(len(jD) - 1, -1, -1):
        #       hardest = max(hardest, jD[i])
        #       base_cases[i] = hardest
        # answer: return dp(0, 1)
        jD = jobDifficulty
        if len(jD) < d:
            return -1
        
        # base cases
        hardest = 0
        base_cases = [0] * len(jD)
        for i in range(len(jD) - 1, -1, -1):
            hardest = max(hardest, jD[i])
            base_cases[i] = hardest
        
        # recurrence relation
        @lru_cache(None)
        def dp(i, day):
            if day == d:
                return base_cases[i]
            hardest = 0
            min_diff = float('inf')
            for j in range(i, len(jD) - (d - day)):
                hardest = max(hardest, jD[j])
                min_diff = min(min_diff, hardest + dp(j + 1, day + 1))
            return min_diff
        
        return dp(0, 1)
        