class Solution:
    def frequencySort(self, s: str) -> str:
        # time O(n + nlogn) space O(n)
        from collections import Counter
        return ''.join([key * value for key, value in Counter(s).most_common()])