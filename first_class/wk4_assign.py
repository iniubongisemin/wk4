def highest_number(num:list):
    highest = []
    num = list_num.sort()
    num.append(highest)
    print(highest)
    # return num

answer = highest_number(list_num)
print(answer)


#1b
def even_odd(first_list:list, second_list:list):
    even_num = []
    odd_num = []
    for x in first_list, second_list:
        if x % 2 == 0:
            x.append(even_num)
        else:
            x.append(odd_num)
    print(even_num)
    print(odd_num)

# even_odd(list_1, list_2)

#2a.
def reverse_func(str):

    # rev_str = str[-1::0]
    rev_str = reversed(str)
    print(rev_str)
    # return rev_str

strg = '1234abcd'
rev = reverse_func(strg)
print(rev)
