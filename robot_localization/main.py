from grid import Grid

# intialize grid with 5 cells
grid = Grid(5)
grid.set_colors_for_cells(["red", "green", "green", "red", "green"])

# display PRIOR state of grid
print grid.all_cells_state_for_attr("probability")
print grid.all_cells_state_for_attr("color")