class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals)
        start, end = sorted_intervals[0]
        ans = []
        for left, right in sorted_intervals:
            if left <= end:
                if right > end:
                    end = right
            else:
                ans.append([start, end])
                start, end = left, right
        ans.append([start, end])
        return ans
    
    # time complexity: O(nlogn)
    # space complexity: O(logn) (for in-place sorting) or O(n) 