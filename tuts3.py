#List & tupple in python


numbers = [1,2,4,43,3,21]
print(numbers)
numbers.reverse()
print("Reverse of list", numbers)
numbers.sort()
print("Sorting of list", numbers)

print("Maximum number in list is", max(numbers))
print("Minimum number in list is", min(numbers))

numbers.append(12)
numbers.append(5)
numbers.append(17)
print("List after adding values", numbers)
#insert number
numbers.insert(1,100)
print("List after insert number on index 1", numbers)

#remove number from list
numbers.remove(100)
print("After removing element from list", numbers)
numbers.pop()
print("Pop from list", numbers)



#Mutable = can change
#Immutable = can't change

tp = (1,2,4,69,34,21,7,12)
print(tp)

# In tuple we can't change values
"""
tp.append(2)
print(tp)

it will throw error tuple obkect has no attribute 'append'

"""

# Swap a variable in python

a = 12
b = 100
print("value of var a", a, "\n value of variable b", b)
a, b = b,a
print("After swapping value of var a", a, "\n value of variable b", b)