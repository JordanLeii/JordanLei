#names = ["tyler" , "jack", "ramiro", "jon", "alex"]
#print("tyler" in names)
#names[0] makes no sense

#looping through sets with for loop: for name in names:
#want to add to set use: thiset.add("what the thing is") and thisset.update(lst) to add multiple 
#to remove something use: names.remove("what you want to remove")
#to find length of set use: 

#joining 2 sets
set1 = {"buff", "angel", "Noob"}
set2 = {"tyler", "andrew",}
set3 = set1.union(set2)
print(set3)

#this set combining wont work the sets wont have duplicates of something
names1 = {"tyler" , "jack", "ramiro", "jon", "alex"}
names2 = {"tyler" , "jack", "ramiro", "jon", "alex"}
names3 = names1.union(names2)
print(names3)

#intersection prints the things that arent overlaped
names.intersection = names1.intersection(names2)
print(names.intersection)
