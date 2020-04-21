# Runtime: 52 ms, faster than 63.85% of Python3 online submissions for Rotting Oranges.
# Memory Usage: 13.6 MB, less than 16.67% of Python3 online submissions for Rotting Oranges.

from collections import deque
class Solution:
    '''BFS approach'''
    def orangesRotting(self, grid: List[List[int]]) -> int:
        nb_fresh_orange = 0
        queue = deque() # for rotten orange
        
        height, width = len(grid), len(grid[0])
        # initialize queue and nb_fresh_orange
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    nb_fresh_orange += 1
        
        # put a mark for each timestamp after the first level in queue
        queue.append((-1, -1))
        
        # start rotting
        time = -1
        neighbor_direction = ((1, 0), (-1, 0), (0, 1), (0, -1))
        while queue:
            i, j = queue.popleft()
            if i == -1: # finish a level
                time += 1
                if queue: # only add one more mark if the queue is not empty
                    queue.append((-1, -1))
            else:
                for a, b in neighbor_direction:
                    i2, j2 = i + a, j + b
                    if 0 <= i2 < height and 0 <= j2 < width:
                        if grid[i2][j2] == 1:
                            grid[i2][j2] = 2
                            queue.append((i2, j2))
                            nb_fresh_orange -= 1
        
        return time if nb_fresh_orange == 0 else -1

'''
Time Complexity: O(N), where N is the size of the grid.

First, we scan the grid to find the initial values for the queue, which would take O(N) time.

Then we run the BFS process on the queue, which in the worst case would enumerate all the cells in the grid once and only once. Therefore, it takes O(N) time.

Thus combining the above two steps, the overall time complexity would be O(N)+O(N)=O(N)

Space Complexity: O(N), where N is the size of the grid.

In the worst case, the grid is filled with rotten oranges. As a result, the queue would be initialized with all the cells in the grid.
'''