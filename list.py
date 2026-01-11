# list is also known as an array but main deference is that list can store different data types
# for example:
new_list=[1,2.4,"hii",True]
print(new_list)

# accessing elements
access_element=new_list[2]
print("Element at index 2:",access_element)

# list slicing
sliced_list=new_list[1:3]
print("Sliced list (index 1 to 2):",sliced_list)

sliced_list2=new_list[:2]
print("Sliced list (start to index 1):",sliced_list2)

sliced_list3=new_list[2:]
print("Sliced list (index 2 to end):",sliced_list3)

sliced_list4=new_list[::-1]
print("Sliced list (reversed):",sliced_list4)

# list methods
new_list.append("geeta")
print("After append:",new_list)

new_list.remove(2.4)
print("After remove:",new_list)
new_list.insert(1,"inserted_value")

print("After insert at index 1:",new_list)

popped_element=new_list.pop()
print("Popped element:",popped_element)
print("After pop:",new_list)
new_list.sort(key=str)
print("After sort:",new_list)

new_list.reverse()
print("After reverse:",new_list)


count_of_hii=new_list.count("hii")
print("Count of 'hii':",count_of_hii)
index_of_hii=new_list.index("hii")
# list are mutable i.e we can change the value at any index
new_list[index_of_hii]="changed_value"
print("After changing 'hii' to 'changed_value':",new_list)
# listsare mur=table i.e we can change the value at any index
new_list[index_of_hii]="changed_value"
print("After changing 'hii' to 'changed_value':",new_list)

# merging two lists
another_list=[5,"hello",False]
merged_list=new_list+another_list
print("Merged list:",merged_list)

# length of list
length_of_list=len(merged_list)
print("Length of merged list:",length_of_list)

