def leap(year):
    #Years that are evenly divisible by 4
    if(year%4 == 0):
                #case of leap years less than year 100
        if(year < 100):
            return "leap year"
                #case of years greater than 100 -- possible leap year
        elif(year%100 == 0):    

            #years that are evenly divisible by 100 -- no leap year
            return "NOT a leap year"  
        
    #Years that are NOT evenly divisible by 4            
    else:
        return "NOT a leap year"
  