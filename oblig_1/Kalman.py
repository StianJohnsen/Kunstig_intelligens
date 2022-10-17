class Kalman():
    def __init__(self):
        # Variables used for estimating position
        
        self.estimated_current_position = 0
        self.estimated_previous_position = 0
        self.measured_value = 0
        self.alpha = 0.05
        
        # Variables used for estimating velocity
        self.estimated_current_velocity = 0
        self.estimated_previous_velocity = 0
        self.beta = 0.05
        self.delta_time = 1
        
        self.estimate_next_position = self.estimated_current_position + self.estimated_current_velocity * self.delta_time
        
        
    def estimate_current_position_and_velocity(self, zi):




        """ Estimate current position and velocity from (noisy) position measurement """
        print(zi)
        x_current = 1
        v_current = 1
        return x_current, v_current