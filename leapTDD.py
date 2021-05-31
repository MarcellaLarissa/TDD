def leap(year):
    #Years that are evenly divisible by 4
    if(year%4 == 0):
                #case of leap years less than year 100
        if(year < 100):
            return "leap year"
                #case of years greater than 100 -- possible leap year
        elif(year%100 == 0):    
                        # case of years are evenly divisible by 400 -- leap year
            if(year%400 == 0):
               return "leap year"
                
            #years that are evenly divisible by 100 -- no leap year
            else:
                return "NOT a leap year"  
        
    #Years that are NOT evenly divisible by 4            
    else:
        return "NOT a leap year"
  