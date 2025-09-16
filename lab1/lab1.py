#quesiron no 1 
# entering two strings and convert them to sets and perform union, intersection and differences operations on 
# the two sets uning python function

## create two stings 
string1 = "hello"
string2= "world"

#conver them into sets
set1= set(string1)
set2= set(string2)

#performing set operations
union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set1 = set1.difference(set2)
difference_set2 = set2.difference(set1)

# displaying the results 
print("set1:", set1)
print("set2:", set2)
print("Union:", union_set)
print("Intersetion:", intersection_set)
print("Difference (Set1 - Set2):", difference_set1)
print("Difference (Set2 -Set1):", difference_set2)

