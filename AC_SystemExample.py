# Example agent program for the implementation of an A/C system. 
def adjust_temperature(T_current, T_pref):
    # Define the temperature change per action
    Delta_T = 1  # Assuming 1 degree change per action for simplicity
    
    # Determine the action based on the current and preferred temperatures
    if T_current > T_pref:
        action = 'C'  # Cooling
    elif T_current < T_pref:
        action = 'H'  # Heating
    else:
        action = 'I'  # Idle
    
    # Apply the action to adjust the temperature
    if action == 'C':
        T_new = T_current - Delta_T  # Cooling decreases the temperature
    elif action == 'H':
        T_new = T_current + Delta_T  # Heating increases the temperature
    else:
        T_new = T_current  # Idle keeps the temperature unchanged
    
    return T_new

# Example usage
T_current = 68  # Current temperature
T_pref = 70     # Preferred temperature

# Adjust the temperature until it matches the preferred temperature
while T_current != T_pref:
    T_current = adjust_temperature(T_current, T_pref)
    print(f"Adjusted temperature to {T_current}°F")

print("Desired temperature reached.")
