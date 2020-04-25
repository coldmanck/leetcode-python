'''
Time:       32      ms
Space:      13.7    MB  python3
'''

class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        # time O(N) or O(logk) for traversing the tree of depth N
        # space O(N) or O(logk) for the recursive call stack
        if N == 1:
            return 0
        trans = {'0': '01', '1': '10'}
        if K % 2:
            last_row = K // 2 + 1  
            cur_element_idx = 0
        else:
            last_row = K // 2
            cur_element_idx = 1
        return int(trans[str(self.kthGrammar(N-1, last_row))][cur_element_idx])