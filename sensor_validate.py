def within_safe_range(value, nextValue, maxDelta): 
  if nextValue - value > maxDelta:                                      
    return False
  return True

def validate_soc_reading(values):
    return process_sensor_reading(values,maxDelta = 0.05)

def validate_current_reading(values):
    return process_sensor_reading(values,maxDelta = 0.1) 
  
def process_sensor_reading(values,maxDelta):
    if values is not None:
        return validate_reading(values,maxDelta)
    else:
        return False  

def validate_reading(values,maxDelta):                                    
    last_but_one_reading = len(values) - 1                                  
    for i in range(last_but_one_reading):                                   
        if(not within_safe_range(values[i], values[i + 1], maxDelta)):
            return False                                                         
    return True
