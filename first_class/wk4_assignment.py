#1a. write a python function to get the largest number from a list of numbers. your function will accept a list of numbers as argument and return the largest number as its value
list_num = [10, 134, 29, 31, 79, 34]

# def highest_number(num:list):
#     num = list_num.sort()
#     print(num[-1])
        
# answer = highest_number(list_num)
# print(answer)

#1b. given a list of numbers, write a function to count the even and odd numbers in the list and print the result.
list_1 = [2, 7, 5, 32, 14]
list_2 = [12, 15, 16, 84, 3, 9]

#2a. write a python function to reverse a string
def reverse_func(str):

    # rev_str = str[-1::0]
    rev_str = reversed(str)
    print(rev_str)
    # return rev_str

strg = '1234abcd'
rev = reverse_func(strg)
print(rev)

#2b. def cube(n):
            # return n ** 3
# rewrite the function above using anonymous function