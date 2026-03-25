list = [10, 20, 30, 40, 50, 60, 70, 80]

print("Accessing:", list[3]) #Accessing
print("Slicing:", list[2:5]) #Slicing

list.append(90) #Adding
print("Adding:", list)

list.remove(90) #Removing
print("Removing:", list)

sorted(list) #Sorting
print("Sorting:", list)

list.sort(reverse=True) #Reverse/Descending Sorting
print("Descending:", list)

list.reverse() #Reversing List
print("Reversing:", list)

reversed_list = list[::-1] #Slicing Technique
print("Slicing Technique:", reversed_list)
