class Kalman():
    def __init__(self):
        # Variables used for estimating position
        self.value_lst = []

        #self.alpha = 0.0365 # Prøv å eksperimetere videre
        #self.beta = 0.00249 # Prøv å eksperimetere videre
        #self.gamma = 0.00000632 # Prøv å eksperimetere videre

        self.damping = 0.995        
        self.alpha = 1-self.damping**3
        self.beta = 1.5*(1-self.damping)**2 *(1+self.damping)
        self.gamma = (1-self.damping)**3

        self.delta_time = 1

        self.current_estimated_position = 0#200
        self.current_estimated_velocity = 0#0.4
        self.current_estimated_acceleration = 0#0.003

        self.next_estimated_position = self.current_estimated_position + self.current_estimated_velocity * self.delta_time + self.current_estimated_acceleration * 0.5 * self.delta_time ** 2
        self.next_estimated_velocity = self.current_estimated_velocity + self.current_estimated_acceleration * self.delta_time
        self.next_estimated_acceleration = self.current_estimated_acceleration
 


        
        
    def estimate_current_position_and_velocity(self, zi):
        self.value_lst.append(zi)
        '''Calculating current estimate using State Update Equations'''
        self.current_estimated_position = self.next_estimated_position + self.alpha*(zi-self.next_estimated_position)
        self.current_estimated_velocity = self.next_estimated_velocity + self.beta * ((zi-self.next_estimated_position)/self.delta_time)
        self.current_estimated_acceleration = self.next_estimated_acceleration + self.gamma * ((zi-self.next_estimated_position)/0.5*self.delta_time**2)

        '''Calculating the next state estimate using the State Extrapolation Equations'''
        
        self.next_estimated_position = self.current_estimated_position+self.current_estimated_velocity*self.delta_time+self.current_estimated_acceleration*0.5*self.delta_time**2
        self.next_estimated_velocity = self.current_estimated_velocity+self.current_estimated_acceleration*self.delta_time
        self.next_estimated_acceleration = self.current_estimated_acceleration

        return self.current_estimated_position,self.current_estimated_velocity   