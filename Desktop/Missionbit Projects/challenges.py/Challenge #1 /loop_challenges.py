#----------------------------------------------------------
# Challenge 1 - Divisible by Ten
#----------------------------------------------------------
# Create a function named divisible_by_ten() that takes a list of numbers named nums as a parameter.

# Return the count of how many numbers in the list are divisible by 10.

#Write your function here
#def divisible_by_ten(nums):
    #count = 0
    #for num in nums:
        #if nums %10 == 0:
            #count += 1
    #return count


#Uncomment the line below when your function is done
#print(divisible_by_ten([20, 25, 30, 35, 40]))

#----------------------------------------------------------
# Challenge 2 - Greetings
#----------------------------------------------------------
# Create a function named add_greetings() which takes a list of strings named names as a parameter.

# In the function, create an empty list that will contain each greeting. Add the string "Hello, " in front of each name in names and append the greeting to the list.

# Return the new list containing the greetings.

#Write your function here

#def add_greetings(names):
    #greetings = []
    #for name in names:

       # greetings.append("Hello," + name)
        #return greetings

#Uncomment the line below when your function is done
#print(add_greetings(["Owen", "Max", "Sophie"]))


#----------------------------------------------------------
# Challenge 3 - Delete Starting Even Numbers
#----------------------------------------------------------

# Write a function called delete_starting_evens() that has a parameter named lst.
#def delete_starting_evens(lst):
    #while len(lst) > 0 and lst[0] %2 == 0:
        #num = lst.pop(index)
        #print("popped: " + str(num))
    
    #return lst
# The function should remove elements from the front of lst until the front of the list is not even. The function should then return lst.

# For example if lst started as [4, 8, 10, 11, 12, 15], then delete_starting_evens(lst) should return [11, 12, 15].

# Make sure your function works even if every element in the list is even!

#Write your function here


#Uncomment the lines below when your function is done
 #print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
 #print(delete_starting_evens([4, 8, 10]))


#Uncomment the line below when your function is done
# print(odd_indices([4, 3, 7, 10, 11, -2]))

#----------------------------------------------------------
# Challenge 4 - Odd Indices
#----------------------------------------------------------

# Create a function named odd_indices() that has one parameter named lst.

# The function should create a new empty list and add every element from lst that has an odd index. The function should then return this new list.

# For example, odd_indices([4, 3, 7, 10, 11, -2]) should return the list [3, 10, -2].

#Write your function here
#def odd_indices(lst)
    #newlst = []
    #for index in range(len(lst)):
        #if index %2 == 0:
            #continue
        #newlst.append(lst(append[index])
    #return newlst

#Uncomment the line below when your function is done
# print(odd_indices([4, 3, 7, 10, 11, -2]))

#----------------------------------------------------------
# Challenge 7 - Over 9000
#----------------------------------------------------------

# Create a function named over_nine_thousand() that takes a list of numbers named lst as a parameter.

# The function should sum the elements of the list until the sum is greater than 9000. When this happens, the function should return the sum. If the sum of all of the elements is never greater than 9000, the function should return total sum of all the elements. If the list is empty, the function should return 0.

# For example, if lst was [8000, 900, 120, 5000], then the function should return 9020.

#Write your function here
def over_nine_thousand(lst):
    sum = 0
    for num in lst:
    while(sum < 9000 and index < len(lst)):
        sum += lst[index]
        index += 1
    return sum

#Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))



#----------------------------------------------------------
# Challenge 8 - Max Num
#----------------------------------------------------------

# Create a function named max_num() that takes a list of numbers named nums as a parameter.

# The function should return the largest number in nums

#Write your function here


#Uncomment the line below when your function is done
# print(max_num([50, -10, 0, 75, 20]))

