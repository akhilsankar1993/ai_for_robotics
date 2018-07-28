from cell import Cell

class Grid:
    def __init__(self, size = 1):
        self.size = size
        self.cells = []
        base_probability = 1./self.size
        
        for i in range(size):
            new_cell = Cell(i, base_probability)
            self.cells.append(new_cell)
    
    def set_colors_for_cells(self, cell_colors):
        for i, cell in enumerate(self.cells):
            cell.color = cell_colors[i]
            
    def all_cells_state_for_attr(self, attribute):
        all_probabilities = []
        for cell in self.cells:
            all_probabilities.append(getattr(cell, attribute))
        
        return all_probabilities
        