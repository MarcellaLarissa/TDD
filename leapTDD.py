def leap(year):
    #Years that are evenly divisible by 4
    if(year%4 == 0):
                #case of leap years less than year 100
        if(year < 100):
            return "leap year"
        
        
    #Years that are NOT evenly divisible by 4            
    else:
        return "NOT a leap year"
  