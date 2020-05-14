class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # Stack: time O(n) space O(n)
        if len(num) == k:
            return '0'
        
        length = len(num) - k
        num = list(num)
        stack = [num[0]]
        i = 1
        while i < len(num) and k > 0:
            while k > 0 and stack and int(num[i]) < int(stack[-1]):
                stack.pop()
                k -= 1
            stack.append(str(num[i]))
            i += 1
        ans = (stack + num[i:])[:length]
        return str(int(''.join(ans)))
        
        # Recursion: Time Limit Exceeded
        '''
        if len(num) == k:
            return '0'
        num = [ch for ch in num]
        target_n_digits = len(num) - k
        
        def remove_k_digits(idx, num, cur_ans, ans):
            if len(cur_ans) == target_n_digits: # 4
                if int(''.join(cur_ans)) < int(''.join(ans)):
                    ans = cur_ans
                return ans
            for i in range(idx, len(num)):
                ans = remove_k_digits(i + 1, num, cur_ans + [num[i]], ans)
            return ans
        
        return str(int(''.join(remove_k_digits(0, num, [], num))))
        '''