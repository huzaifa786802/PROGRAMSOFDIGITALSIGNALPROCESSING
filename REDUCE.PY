from functools import reduce
numbers=[1,2,3,4,5]
sum_of_numbers=reduce(lambda x,y:x+y,numbers)
print("The sum of the numbers is:",sum_of_numbers)