class ThermostatModelGoalBasedAgent:
    def __init__(self, ideal_temp):
        self.ideal_temp = ideal_temp
        self.current_temp = None
        self.temp_trend = 'stable'  # 'increasing', 'decreasing', 'stable'
        self.demerit_points = 0
    
    def update_state(self, new_temp):
        if self.current_temp is not None:
            if new_temp > self.current_temp:
                self.temp_trend = 'increasing'
            elif new_temp < self.current_temp:
                self.temp_trend = 'decreasing'
            else:
                self.temp_trend = 'stable'
        self.current_temp = new_temp
        # Update demerit points based on deviation from the ideal temperature
        self.demerit_points += abs(self.ideal_temp - new_temp)

  # This is an incredably simple model for temperature change. 
    def predict_demerits(self, action):
        predicted_temp_change = 1 if action in ["Heat", "Cool"] else 0
        if self.temp_trend == 'increasing' and action == "Cool":
            predicted_temp_change = -1
        elif self.temp_trend == 'decreasing' and action == "Heat":
            predicted_temp_change = 1
        
        predicted_temp = self.current_temp + predicted_temp_change
        predicted_demerits = abs(self.ideal_temp - predicted_temp)
        # Penalty for making an adjustment
        if action != "Maintain temperature":
            predicted_demerits += 1
        
        return predicted_demerits
    
    def decide_action(self):
        actions = ["Heat", "Cool", "Maintain temperature"]
        # Evaluate the predicted demerits for each possible action
        demerits_for_actions = {action: self.predict_demerits(action) for action in actions}
        # Choose the action with the minimum predicted demerits
        best_action = min(demerits_for_actions, key=demerits_for_actions.get)
        
        return best_action

agent = ThermostatModelGoalBasedAgent(ideal_temp=70)
agent.update_state(68)  # Example: current temperature is 68
print(agent.decide_action())
agent.update_state(72)  # Update state with new temperature
print(agent.decide_action())
