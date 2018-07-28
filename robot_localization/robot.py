class Robot:
    def __init__(self, sensor_accuracy_constants):
        self.constants = {
            "pHit": sensor_accuracy_constants["pHit"],
            "pMiss": sensor_accuracy_constants["pMiss"]
        }
            
    def sense(self, target_grid, sensor_readings):
        for reading in sensor_readings:
            target_grid.evaluate_posterior_probabilities(reading, self.constants)
            target_grid.normalize_probabilities()
            
        return target_grid.get_state("probability")