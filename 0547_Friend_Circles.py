class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        from collections import deque
        queue = deque()
        visited = set()
        ans = 0
        for i in range(len(M)): # for all student
            if i not in visited: # if haven't form a circle
                ans += 1
                visited.add(i)
                queue.append(i)
                while queue:
                    j = queue.popleft()
                    for k in range(len(M[0])): # for the rels between this student and other students
                        if not k in visited and M[j][k] == 1:
                            queue.append(k)
                            visited.add(k)
        return ans