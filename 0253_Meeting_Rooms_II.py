from collections import deque
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        '''
        Method: Two Sorting + two queues, record the maximum nb of rooms needed only when a new meeting start

        Runtime: 88 ms, faster than 21.92% of Python3 online submissions for Meeting Rooms II.
        Memory Usage: 17 MB, less than 5.41% of Python3 online submissions for Meeting Rooms II.
        '''
        q1 = deque(sorted([i[0] for i in intervals]))
        q2 = deque(sorted([i[1] for i in intervals]))
        
        cur_room = max_room = 0
        while q1: # only need to check when there's still a meeting to be held
            if q1[0] == q2[0]:
                q1.popleft()
                q2.popleft()
            elif q1[0] < q2[0]:
                q1.popleft()
                cur_room += 1
                max_room = max(cur_room, max_room)
            else:
                q2.popleft()
                cur_room -= 1
        return max_room