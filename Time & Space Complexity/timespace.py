


# Time and space complexity

# first_number = 10 # Assignment 10
# second_number = 20 # Assignment 20
# result = first_number + second_number # 2 number addition and Assignment Time and space complexity O(1)

# n = int(input('Number : '))
# result = n * (n+1)/2 # addition -> multiplacation -> division -> assignment time and space complexity O(1)
# print(result)

# n = int(input('Number : '))
# sum = 0
# for i in range(1, n+1): # run time n O(n)
#     sum = i+sum # space complexity n O(n)
# print(sum)

# n = int(input('Number : '))
# if n % 2 == 0: # time and space complexity O(1)
#     print('Even Number ')
# else:
#     print('Odd Number ')


# n = 100
# even = [False] * (n+1)
# for i in range(0, n+1, 2):
#     even[i] = True
# print(even[4])
# print(even[1])



# count = 0
# n = int(input('Enter Number : '))
# for i in range(1, n+1):
#     for j in range(1, n+1):   # complexity O(n^2)
#         count += 1
# print('number N : ', n, 'Count : ', count)



# count = 0
# n = int(input('Enter Number : '))
# for i in range(1, n+1):  # Complexity O(n)
#     count += 1
#
# print('number N : ', n, 'Count : ', count)


# loop1 = 0
# loop2 = 0
# loop3 = 0
# n = int(input('Enter Number : '))
# for i in range(1, n+1):
#     loop1 += 1
#     for j in range(1, n+1):
#         loop2 += 1
#         for k in range(1, n+1):   # complexity O(n^3)
#             loop3 += 1
#
# print('loop1 : ', loop1, 'loop2 : ', loop2, 'loop3 : ', loop3)




