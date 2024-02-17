# In this example we use the concept of demerit points as a consequence. 
# The goal is to maintain the optimal temprature while reducing demerit points for poor performance. 
class ThermostatGoalBasedAgent:
    def __init__(self, ideal_temp):
        self.ideal_temp = ideal_temp
        self.current_temp = None
        self.demerit_points = 0
    
    def update_state(self, new_temp):
        self.current_temp = new_temp
        # Update demerit points based on deviation from the ideal temperature
        self.demerit_points += abs(self.ideal_temp - new_temp)
    
    def predict_demerits(self, action):
        # Hypothetical change in temperature based on action
        if action == "Heat":
            predicted_temp = self.current_temp + 1
        elif action == "Cool":
            predicted_temp = self.current_temp - 1
        else:  # "Maintain current setting"
            predicted_temp = self.current_temp
        
        # Predict demerits for the action
        predicted_demerits = abs(self.ideal_temp - predicted_temp)
        # Assume each adjustment action also adds a fixed demerit for changing the status
        if action != "Maintain temperature":
            predicted_demerits += 1  # Penalty for making an adjustment
        
        return predicted_demerits
    
    def decide_action(self):
        actions = ["Heat", "Cool", "Maintain temperature"]
        # Evaluate the predicted demerits for each possible action
        demerits_for_actions = {action: self.predict_demerits(action) for action in actions}
        # Choose the action with the minimum predicted demerits
        best_action = min(demerits_for_actions, key=demerits_for_actions.get)
        
        return best_action

agent = ThermostatGoalBasedAgent(ideal_temp=70)
agent.update_state(68)  # Example: current temperature is 68
print(agent.decide_action())
agent.update_state(72)  # Update state with new temperature
print(agent.decide_action())
