#1a. write a python function to get the largest number from a list of numbers. your function will accept a list of numbers as argument and return the largest number as its value
list_num = [10, 134, 29, 31, 79, 34]

def highest_number(nums):
  nums.sort(reverse=True)
  return nums[0]

list_num = [10, 134, 29, 31, 79, 34]
answer = highest_number(list_num)
print(answer)

#1b. given a list of numbers, write a function to count the even and odd numbers in the list and print the result.
list_1 = [2, 7, 5, 32, 14]
list_2 = [12, 15, 16, 84, 3, 9]

def count_even_odd(nums):
  
  even_count = 0
  odd_count = 0 
  for num in nums:
    if num % 2 == 0:
      even_count += 1
    else:
      odd_count += 1
  return even_count, odd_count

# Calling the function with individual lists
even_1, odd_1 = count_even_odd(list_1)
even_2, odd_2 = count_even_odd(list_2)

print("List 1: Even_numbers:", even_1, "Odd_numbers:", odd_1)
print("List 2: Even_numbers:", even_2, "Odd_numbers:", odd_2)

#2a. write a python function to reverse a string "1234abcd"
def reverse_func(str):
  return str[::-1]

strg = '1234abcd'
rev = reverse_func(strg)
print(rev)

# 2b. rewrite the function below using anonymous function
def cube(n):
    return n ** 3

c = cube(5)
print(c)

# using lambda function
cube = lambda n : n ** 3
print(cube(5))

