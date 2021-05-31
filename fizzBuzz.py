def fb(nums):
    if (nums > 100):
        return None
    if ((nums % 5 == 0) and (nums % 3 == 0)):
        return "fizzbuzz"
    
    if (nums % 3 == 0):
        return "fizz"
    
    if (nums % 5 == 0):
        return "buzz"

    else:
        return nums
    
    
nums = 1
fb(nums)