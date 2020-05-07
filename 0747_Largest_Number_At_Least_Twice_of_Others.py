class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m_idx, m = -1, float('-inf')
        for i, num in enumerate(nums):
            if num > m:
                m = num
                m_idx = i
        for i, num in enumerate(nums):
            if i == m_idx:
                continue
            if num * 2 > m:
                return -1
        return m_idx