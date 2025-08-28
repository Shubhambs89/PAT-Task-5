# 1. use lambda functions to filter out the people under 18 and then map the remaining peoples name to new list 
voters = [{"name" : "Rahul", "age": 21}, {"name" : "Amit", "age": 16}, {"name" : "Abhi", "age": 22}, {"name" : "Pavan", "age": 30}, {"name" : "Krishna", "age": 28}, {"name" : "Ashish", "age": 12}, {"name" : "Manu", "age": 34}]
voters_eigible = list(filter(lambda age: age["age"] >= 18, voters))

eligible_candidates = list(map(lambda candidates : candidates['name'], voters_eigible))
print(eligible_candidates)

# 2. Given a list of numbers use the reduce function and a lambda expression to calculate the product of all the numbers in the list 
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
product_of_numbers= 1
for num in nums:
     product_of_numbers = (lambda x, y: x * y)(product_of_numbers, num)
print(product_of_numbers)

# 3. Write a list comprehension that creates a new list of squares of even numbers from a given list, using a lambda function to check for even numbers 
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)
sq_evens = list(map(lambda x: x**2,evens))
print(sq_evens)

# 4. write a lambda function to check if a given string is a number
import re
text = "My Phone number is 9008044594"
pattern = r"\d{10}"
match = re.search(pattern, text)
if match:
    print("Phone number found: ", match.group())

# 5. use a lambda function to extract the year, month and day from a datetime object 
from datetime import datetime

dt= datetime (1994, 10, 21)
extract_date = (lambda dt_obj: (dt_obj.year, dt_obj.month, dt_obj.day))

year, month, day = extract_date(dt)
print(f"year: {year}, month: {month}, Day: {day}")

# 6. Create a lambda function to generate a Fibnacci series upto n terms.

fibonacci_series = lambda n: [0, 1][:n] if n <= 2 else [0, 1] + [sum([0, 1]) for i in range(2, n)]

n = 10
print(fibonacci_series(n))
