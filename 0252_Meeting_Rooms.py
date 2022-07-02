class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        for i, (start, end) in enumerate(sorted(intervals)):
            if i != 0 and start < prev_end:
                return False
            prev_start, prev_end = start, end
        return True