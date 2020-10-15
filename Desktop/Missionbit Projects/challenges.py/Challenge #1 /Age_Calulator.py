def calculate_age(current_year, brith_year):
    age = current_year - brith_year 
    return age 
my_age = calculate_age(2049, 2003)
dads_age = calculate_age(2049, 1953)
print("I am " + str(my_age) + " and my dad is " + str(dads_age) + " years old" )

