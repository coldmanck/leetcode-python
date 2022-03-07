class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        left, right = 0, 1
        max_len = 0
        cur_set = set([s[left]])
        while right < len(s):
            while s[right] in cur_set:
                cur_set.remove(s[left])
                left += 1                
            cur_set.add(s[right])
            max_len = max(max_len, right - left + 1)
            right += 1
        return max_len
    
        # time complexity: O(2n)
        # space complexity: O(n_possble_charactures)