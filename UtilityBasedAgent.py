# So, instead of adhereing strictly to a goal, we are looking to maximize utlity, in this case comfort and energy efficiency.
# We need to be willing to have trade-offs -- rarely is any one utlity going to be perfect
# But we can have a state of "closest to perfect", which is what this agent aims to do. 

class ThermostatUtilityBasedAgent:
    def __init__(self, ideal_temp_range=(68, 72)):
        self.ideal_temp_range = ideal_temp_range
        self.current_temp = None
    
    def update_state(self, new_temp):
        self.current_temp = new_temp
    
    def utility_function(self, temp):
        # Calculate comfort utility
        if self.ideal_temp_range[0] <= temp <= self.ideal_temp_range[1]:
            comfort_utility = 100  # Max utility for being in the ideal range
        else:
            comfort_utility = max(0, 100 - 10 * abs(min(min(self.ideal_temp_range) - temp, temp - max(self.ideal_temp_range))))
        
        # Simulate energy efficiency utility (higher for less drastic changes)
        energy_efficiency_utility = 100 - abs(self.current_temp - temp)
        
        # Total utility combines both aspects
        total_utility = comfort_utility + energy_efficiency_utility
        
        return total_utility
    
    def decide_action(self):
        potential_actions = {
            "Heat": self.current_temp + 1,
            "Cool": self.current_temp - 1,
            "Maintain temperature": self.current_temp
        }
        
        # Evaluate the utility for each action's resulting temperature
        utilities = {action: self.utility_function(temp) for action, temp in potential_actions.items()}
        # Choose the action with the highest utility
        best_action = max(utilities, key=utilities.get)
        
        return best_action

agent = ThermostatUtilityBasedAgent()
agent.update_state(70)  # Initial temperature setting
print(agent.decide_action())
agent.update_state(65)  # New temperature reading
print(agent.decide_action())
