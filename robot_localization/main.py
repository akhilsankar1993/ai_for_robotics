from grid import Grid
from robot import Robot
    
# Now we setup our specific example environment.

# intialize grid with 5 cells
grid = Grid(5)
grid.set_colors(["green", "red", "red", "green", "green"])

# get PRIOR state of grid
print grid.get_state("probability") 
print grid.get_state("color")

# lets suppose the robot now senses the color "red" at its current location
# the sensor has some degree of inaccuracy, and we capture this numerically using pHit and pMiss constants

# pHit = 3*pMiss signifies that:
# the robot is 3 times more likely to sense "red" and actually be located on a red cell, 
# than sense "red" and actually be located on a "green" cell.

robot = Robot({ "pHit": 0.6, "pMiss": 0.2})
 
# With this in mind, the default distribution of the grid is now multiplied by these constants 
# to determine the POSTERIOR probability distribution of the grid.

print robot.sense(grid, ["red", "green"])