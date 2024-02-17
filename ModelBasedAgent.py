class ThermostatModelBasedAgent:
    def __init__(self, target_range=(68, 72)):
        self.target_range = target_range
        self.current_temp = None
        self.temp_trend = 'stable'  # Could be 'increasing', 'decreasing', or 'stable'

  # In the real world we would take the new_temp from sensor readings in a funtion probably called "get_new_temp". 
  # update_state keeps a record of the state of the environment -- a simple example. 
    def update_state(self, new_temp): 
        if self.current_temp is not None:
            if new_temp > self.current_temp:
                self.temp_trend = 'increasing'
            elif new_temp < self.current_temp:
                self.temp_trend = 'decreasing'
            else:
                self.temp_trend = 'stable'
        self.current_temp = new_temp
    
    def decide_action(self):
        if self.current_temp < self.target_range[0]:
            if self.temp_trend == 'increasing':
                return "Wait and monitor"
            else:
                return "Increase heating"
        elif self.current_temp > self.target_range[1]:
            if self.temp_trend == 'decreasing':
                return "Wait and monitor"
            else:
                return "Decrease heating"
        else:
            return "Maintain temperature"

agent = ThermostatModelBasedAgent()
agent.update_state(70)  # Again, in the real world we would find this out through sensors. 
print(agent.decide_action())
agent.update_state(69)
print(agent.decide_action())
