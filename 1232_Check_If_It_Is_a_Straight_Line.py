class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # compute y = ax + b using the first two coordinates
        if coordinates[0][0] - coordinates[1][0] != 0:
            a = (coordinates[0][1] - coordinates[1][1]) / (coordinates[0][0] - coordinates[1][0])
            b = coordinates[0][1] - a * coordinates[0][0]
            for c in coordinates:
                if c[1] != a * c[0] + b:
                    return False
            return True
        else:
            x = coordinates[0][0]
            for c in coordinates:
                if c[0] != x:
                    return False
            return True