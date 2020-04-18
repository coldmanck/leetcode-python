def infectious_rabbit(grid):
    nb_of_timestamp = 0
    neighbors = [[1,0],[-1,0],[0,1],[0,-1]]
    updated = True
    while updated:
        updated = False # assume that after this infection there's no more neighbor rabbit to infect
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1: # for each healthy rabbit see if there's infectious rabbits nearby
                    for nb in neighbors: # for each of its neighbors
                        x = i + nb[0]
                        y = j + nb[1]
                        if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                            if grid[x][y] == 2: # check if there's a infectious rabbit (2) nearby
                                grid[i][j] = 3 # mark it as 3 so that we won't infect more than one neighbor
                                updated = True # set updated=True if there's a update process
        for i in range(len(grid)): 
            for j in range(len(grid[0])):
                if grid[i][j] == 3: # change all 3 back to 2 for next timestamp's infection process
                    grid[i][j] = 2 
        nb_of_timestamp += 1

    # check if there's an uninfected rabbit
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1: 
                return -1

    return nb_of_timestamp - 1

def test():
    grid = [[2,1,0,2,1], [1,0,1,2,1], [1,0,0,2,1]]
    print(infectious_rabbit(grid))