from collections import deque
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        visited = set()
        ans = 0
        for i in range(len(M)):
            if i not in visited:
                ans += 1
                queue = deque()
                queue.append(i)
                while queue:
                    s = queue.popleft()
                    visited.add(s)
                    for j in range(i, len(M)):
                        if M[s][j] == 1 and j not in visited:
                            queue.append(j)
        return ans