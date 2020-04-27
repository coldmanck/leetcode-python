# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        
        def clean_room(cell, d): # d for direction
            robot.clean()
            visited.add(cell)
            for i in range(4):
                new_d = (d + i) % 4
                new_cell = (cell[0] + move[new_d][0], cell[1] + move[new_d][1])
                if not new_cell in visited and robot.move():
                    clean_room(new_cell, new_d)
                    robot.turnRight()
                    robot.turnRight()
                    robot.move()
                    robot.turnLeft()
                else:
                    robot.turnRight()
            return True
        
        move = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()
        clean_room((0, 0), 0)
        
# Time complexity : \mathcal{O}(4^{N - M}), where N is a number of cells in the room and M is a number of obstacles, because for each cell the algorithm checks 4 directions.

# Space complexity : \mathcal{O}(N - M), where N is a number of cells in the room and M is a number of obstacles, to track visited cells.