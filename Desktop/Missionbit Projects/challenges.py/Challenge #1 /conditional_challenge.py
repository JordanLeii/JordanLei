#-----------------------------------------------------
# Challenge 1 - Large Power
#-----------------------------------------------------

# Create a function named large_power() that takes two parameters named base and exponent. If base raised to the exponent is greater than 5000, return True, otherwise return False

#def large_power(base, exponent):
    #if (base**exponent > 5000): 
        #return True
    #else:
        #return False

    

    

# Write your large_power function here:

# Uncomment these function calls to test your large_power function:
#print(large_power(2, 13))
# should print True
#print(large_power(2, 12))
# should print False

#-----------------------------------------------------
# Challenge 2 - Over Budget
#-----------------------------------------------------

# Create a function called over_budget that has five parameters named budget, food_bill, electricity_bill, internet_bill, and rent. The function should return True if budget is less than the sum of the other four parameters — you’ve gone over budget! Return False otherwise.
def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
    if (food_bill + electricity_bill + internet_bill + rent) > budget:
        return True
    else:
        return False

# Write your over_budget function here:

# Uncomment these function calls to test your over_budget function:
print(over_budget(100, 20, 30, 10, 40))
 #should print False
print(over_budget(80, 20, 30, 10, 30))
 #should print True

#-----------------------------------------------------
# Challenge 3 - Twice As Large
#-----------------------------------------------------

# Create a function named twice_as_large() that has two parameters named num1 and num2. Return True if num1 is more than double num2. Return False otherwise.
def twice_as_large(num1, num2): 
    if (num1 > 2*num2):
        return True
    if (num1 > num2):
        return False 


# Write your twice_as_large function here: #if(num1 > *2 num2):

# Uncomment these function calls to test your twice_as_large function:
print(twice_as_large(10, 5))
 #should print False
print(twice_as_large(11, 5))
 #should print True

#-----------------------------------------------------
# Challenge 4 - Divisible By Ten
#-----------------------------------------------------

# Create a function called divisible_by_ten() that has one parameter named num. The function should return True if num is divisible by 10, and False otherwise. Consider using modulo (%) to check for divisibility.
def divisible_by_ten(num):
    if (num % 10 == 0) or (num % 20 == 0):
      return True
    else: 
      return False
# Write your divisible_by_ten function here: #if n % 10 == 0:

# Uncomment these function calls to test your divisible_by_ten function:
print(divisible_by_ten(20))
# should print True
print(divisible_by_ten(25))
# should print False

#-----------------------------------------------------
# Challenge 5 - Not Equal
#-----------------------------------------------------

# Create a function named not_sum_to_ten() that has two parameters named num1 and num2. Return True if num1 and num2 do not sum to 10. Return False otherwise.
#def not_sum_to_ten(num1, num2):
#if(num1 + num2 != 10)):
 #       return: True
 #   else:
  #      return: False

# Write your not_sum_to_ten function here: #(num1 + num2 != 10)):
# Uncomment these function calls to test your not_sum_to_ten function:
#print(not_sum_to_ten(9, -1))
 #should print True
#print(not_sum_to_ten(9, 1))
 #should print False
#print(not_sum_to_ten(5,5))
 #should print False