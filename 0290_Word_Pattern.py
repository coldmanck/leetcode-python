class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        '''Short'''
        s = str.split()
        if len(s) != len(pattern):
            return False
        return len(set(s)) == len(set(pattern)) == len(set(zip(s, pattern)))
        
        '''Two dict solution'''
        # s = str.split()
        # if len(pattern) != len(s):
        #     return False
        # s_to_pattern = {}
        # pattern_to_s = {}
        # for i in range(len(s)):
        #     if not s[i] in s_to_pattern and not pattern[i] in pattern_to_s:
        #         s_to_pattern[s[i]] = pattern[i] # dog -> a
        #         pattern_to_s[pattern[i]] = s[i] # a -> dog
        #     elif s[i] in s_to_pattern and pattern[i] in pattern_to_s:
        #         if s_to_pattern[s[i]] != pattern[i] or pattern_to_s[pattern[i]] != s[i]:
        #             return False
        #     else:
        #         return False
        # return True