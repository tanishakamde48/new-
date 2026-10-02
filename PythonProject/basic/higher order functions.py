
# map()
# applies function to every item.
marks = [10,20,30]
result = list(map(lambda x: x*2, marks))
print(result)


age = [ 40,50,60,20]
result = list(map(lambda x: x*2,age))
print(result)

# filter()
# keeps only matching values.

numbers  = [1,2,3,4,5,6,7,8,9,10]
result = list(filter(lambda x: x%2 == 0,numbers))
print(result)

# reduce()
# reduce() combines values into one result
from functools import reduce
numbers = [1,2,3,4,5,6,7,8,9,10]
result = reduce(lambda a,b: a+b,numbers)
print(result)
