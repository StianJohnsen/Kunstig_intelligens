class Kalman():
    def __init__(self):
        # Variables used for estimating position
        self.value_lst = []

        self.alpha = 0.05
        self.beta = 0.04
        self.gamma = 0.01

        self.delta_time = 1

        self.current_estimated_position = 0
        self.current_estimated_velocity = 0
        self.current_estimated_acceleration = 0

        self.next_estimated_position = self.current_estimated_position + self.current_estimated_velocity * self.delta_time + self.current_estimated_acceleration * 1/2 * self.delta_time ** 2
        self.next_estimated_velocity = self.current_estimated_velocity + self.current_estimated_acceleration * self.delta_time
        self.next_estimated_acceleration = self.current_estimated_acceleration
 


        
        
    def estimate_current_position_and_velocity(self, zi):
        self.value_lst.append(zi)
        '''Calculating current estimate using State Update Equations'''
        #self.alpha = 1/len(self.value_lst)
        #self.beta = 1/len(self.value_lst)
        #self.gamma = 1/len(self.value_lst)
        self.current_estimated_position = self.next_estimated_position + self.alpha*(zi-self.next_estimated_position)
        self.current_estimated_velocity = self.next_estimated_velocity + self.beta * ((zi-self.next_estimated_position)/self.delta_time)
        self.current_estimated_acceleration = self.next_estimated_acceleration + self.gamma * ((zi-self.next_estimated_position)/0.5*self.delta_time**2)

        '''Calculating the next state estimate using the State Extrapolation Equations'''
        
        self.next_estimated_position = self.current_estimated_position+self.current_estimated_velocity*self.delta_time+self.current_estimated_acceleration*0.5*self.delta_time**2
        self.next_estimated_velocity = self.current_estimated_velocity+self.current_estimated_acceleration*self.delta_time
        self.next_estimated_acceleration = self.current_estimated_acceleration

        return self.current_estimated_position,self.current_estimated_velocity   