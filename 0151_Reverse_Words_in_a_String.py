class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])
        
        # s_arr = s.strip().split(' ')
        # s_arr2 = []
        # for s in s_arr:
        #     if s:
        #         s_arr2.append(s)
        # s_arr2.reverse()
        # return ' '.join(s_arr2)