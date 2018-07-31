from grid import Grid
from robot import Robot
    
# Now we setup our specific example environment.

# intialize grid with 5 cells
# grid = Grid(5)
# grid.set_colors(["green", "red", "red", "green", "green"])

# get PRIOR state of grid
# print grid.get_state("probability") 
# print grid.get_state("color")

# lets suppose the robot now senses the color "red" at its current location
# the sensor has some degree of inaccuracy, and we capture this numerically using pHit and pMiss constants

# pHit = 3*pMiss signifies that:
# the robot is 3 times more likely to sense "red" and actually be located on a red cell, 
# than sense "red" and actually be located on a "green" cell.

robot = Robot(
    { "pHit": 0.6, "pMiss": 0.2}, 
    { "pUndershoot": 0.1, "pOvershoot": 0.1 }
)
 
# With this in mind, the default distribution of the grid is now multiplied by these constants 
# to determine the POSTERIOR probability distribution of the grid.
    
# print robot.sense(grid, ["red", "green"])

# Now we can test our robot's move method, by creating a new grid and passing it in to the method

# move_grid = Grid(5)
# move_grid.set_state("probability", [1, 0, 0, 0, 0])
# 
# for i in range(1000):
#     robot.move(move_grid, 1)
# 
# print move_grid.get_state("probability")

# Now we can test the sense_and_move approach, where we do multiple sense and movement cycles and then perform a posterior 
# distribution calculation

sense_and_move_grid = Grid(5)
sense_and_move_grid.set_state("probability", [0.2, 0.2, 0.2, 0.2, 0.2])
sense_and_move_grid.set_colors(["green", "red", "red", "green", "green"])

measurements = ["red", "green"]
movements = [1,1]
print robot.sense_and_move(sense_and_move_grid, measurements, movements)
