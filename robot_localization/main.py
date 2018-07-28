from grid import Grid

# intialize grid with 5 cells
grid = Grid(5)
grid.set_colors(["green", "red", "red", "green", "green"])

# get PRIOR state of grid
print grid.get_state("probability") 
print grid.get_state("color")


# lets suppose the robot now senses the color "red" at its current location
# the sensor has some degree of inaccuracy, and we capture this numerically using pHit and pMiss constants
constants = { "pHit": 0.6, "pMiss": 0.2}

# pHit = 3*pMiss signifies that the robot is 3 times more likely to sense "red" and actually be 
# located on a red cell, that sense "red" erroneously and actually be located on a "green" cell.
 
# With this in mind, the default distribution of the grid is now multiplied by these constants 
# to determine the POSTERIOR probability distribution of the grid.

# Here we are just writing a wrapper function to match the Udacity 'sense' function contract
def sense(target_grid, sensor_reading):
    target_grid.evaluate_posterior_probabilities(sensor_reading, constants)
    target_grid.normalize_probabilities()
    return target_grid.get_state("probability")

# This is the expected output to match Udacity's function
# => [0.11..., 0.33..., 0.33..., 0.11..., 0.11...] which should add up to 1
print sense(grid, "red")