# empty list
my_list = []

# Appending 10,20,30,40 to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Inserting
my_list.insert(1, 15)

# Extending lists
my_list.extend([50, 60, 70])

# Removing last element from list
my_list.pop()

# Sorting my_list in ascending order
my_list.sort()

# Finding and printing the index of value 30
index_30 = my_list.index(30)
print("Sorted List:", my_list)
print("index of 30:", index_30)