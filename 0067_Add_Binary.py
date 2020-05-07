class Solution:
    def addBinary(self, a: str, b: str) -> str:
        '''Method 1: add digit-by-digit'''
        carry = 0
        pa, pb = len(a) - 1, len(b) - 1
        ans = ['x'] * (max(len(a), len(b)) + 1)
        i = len(ans) - 1
        for i in range(len(ans) - 1, -1, -1):
            ans_i = carry
            if pa >= 0 and pb >= 0:
                ans_i += int(a[pa]) + int(b[pb])
            elif pa >= 0:
                ans_i += int(a[pa])
            elif pb >= 0:
                ans_i += int(b[pb])
            
            if ans_i > 1:
                ans_i -= 2
                carry = 1
            else:
                carry = 0
            
            ans[i] = str(ans_i)
            i, pa, pb = i - 1, pa - 1, pb - 1
            
        return ''.join(ans[1:]) if ans[0] == '0' else ''.join(ans)
            
        '''Method 2: use build-in function'''
        # return bin(int(a, 2) + int(b, 2))[2:]