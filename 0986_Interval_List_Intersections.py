class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        from collections import deque
        A, B = deque(A), deque(B)
        ans = []
        while A and B:
            a_start, a_end, b_start, b_end = A[0][0], A[0][1], B[0][0], B[0][1]
            if max(a_start, b_start) <= min(a_end, b_end):
                ans.append([max(a_start, b_start), min(a_end, b_end)])
            if a_end <= b_end:
                A.popleft()
            else:
                B.popleft()
        return ans