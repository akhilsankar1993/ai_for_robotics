from functools import reduce
from cell import Cell

class Grid:
    def __init__(self, size = 1):
        self.size = size
        self.cells = []
        base_probability = 1./self.size
        
        for i in range(size):
            new_cell = Cell(i, base_probability)
            self.cells.append(new_cell)
    
    def set_colors(self, cell_colors):
        for i, cell in enumerate(self.cells):
            cell.color = cell_colors[i]
            
    def get_state(self, attribute):
        return [getattr(cell, attribute) for cell in self.cells]
        
    def evaluate_posterior_probabilities(self, sensor_reading, constants):
        for cell in self.cells:
            if cell.color == sensor_reading:
                cell.probability *= constants["pHit"] 
            else:
                cell.probability *= constants["pMiss"]
                
    def normalize_probabilities(self):
        total = sum(self.get_state("probability"))
        
        for cell in self.cells:
            cell.probability /= total
        