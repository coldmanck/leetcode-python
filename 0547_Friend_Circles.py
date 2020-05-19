class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        '''Union Find'''
        def find(i): # Find
            if circle[i] == i:
                return i
            circle[i] = find(circle[i])
            return circle[i]
        
        circle = {i:i for i in range(len(M))} # Make set
        for i in range(len(M) - 1):
            for j in range(i + 1, len(M)):
                i_rep, j_rep = find(i), find(j)
                if M[i][j] == 1 and i_rep != j_rep:
                    circle[i_rep] = j_rep # Union

        return sum([1 for k, v in circle.items() if k == v]) # wrong: len(set((i for i in circle.values())))
        
        '''BFS'''
        # from collections import deque
        # queue = deque()
        # visited = set()
        # ans = 0
        # for i in range(len(M)): # for all student
        #     if i not in visited: # if haven't form a circle
        #         ans += 1
        #         visited.add(i)
        #         queue.append(i)
        #         while queue:
        #             j = queue.popleft()
        #             for k in range(len(M[0])): # for the rels between this student and other students
        #                 if not k in visited and M[j][k] == 1:
        #                     queue.append(k)
        #                     visited.add(k)
        # return ans