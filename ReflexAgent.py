def reflexAgent_thermostat(current_temp):
  lower_limit = 68
  upper_limit = 72

  # In an actual program we would capture the current temperature at a certain interval.
  # Also we would define what it means to "increase" or "decrease" temperature. 
  
  if current_temp < lower_limit:
    action = "Increase temperature"
  elif current_temp > upper_limit:
    action = "Descrease temperature"
  else: 
    action = "Maintain temperature"

  return action

current_temp = 65
print(reflexAgent_thermostat(current_temp))
