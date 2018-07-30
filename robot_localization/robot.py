class Robot:
    def __init__(self, sensor_accuracy_constants, moving_accuracy_constants):
        pUndershoot = moving_accuracy_constants["pUndershoot"]
        pOvershoot = moving_accuracy_constants["pOvershoot"]
        pAccurate = 1 - (pUndershoot + pOvershoot)
        
        self.moving_accuracy_constants = {
        "pUndershoot": pUndershoot,
        "pOvershoot": pOvershoot,
        "pAccurate": pAccurate
        }
        
        self.sensor_accuracy_constants = {
            "pHit": sensor_accuracy_constants["pHit"],
            "pMiss": sensor_accuracy_constants["pMiss"]
        }
            
    def sense(self, grid, sensor_readings):
        for reading in sensor_readings:
            grid.evaluate_posterior_probabilities(reading, self.sensor_accuracy_constants)
            grid.normalize_probabilities()
            
        return grid.get_state("probability")
        
    def move(self, grid, steps):
        if steps == 0:
            return grid.get_state("probability") 
        
        compiled_distribution = [0] * grid.size
        for cell in grid.cells:
            if cell.probability == 0:
                continue
            
            specific_cell_distribution = [0] * grid.size
            
            target_index = (cell.index + steps) % grid.size
            undershot_index = (target_index - 1) % grid.size
            overshot_index = (target_index + 1) % grid.size
            
            specific_cell_distribution[target_index] = cell.probability * self.moving_accuracy_constants["pAccurate"]
            specific_cell_distribution[undershot_index] = cell.probability * self.moving_accuracy_constants["pUndershoot"]
            specific_cell_distribution[overshot_index] = cell.probability * self.moving_accuracy_constants["pOvershoot"]
            
            compiled_distribution = [x+y for x,y in zip(compiled_distribution, specific_cell_distribution)]
        
        return grid.set_state("probability", compiled_distribution)
        