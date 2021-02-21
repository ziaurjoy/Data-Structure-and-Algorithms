



# def recursion(n):
#     if n < 0:  # এন এর মান ০ থেকে ছোট হতে পারে না
#         return None
#     if n in [0, 1]:  # ০! এর মান ১ অ্যান্ড ১! এর মান ও ১
#         return 1
#     return n * recursion(n-1)
#
# def test_recursion():
#     assert recursion(5) == 120
#     assert recursion(0) == 1
#     assert recursion(1) == 1
#
#
# print(recursion(1))



# def fibonacci(n):
#     conostant = [1, 2]
#     if n in conostant:
#         return 1
#     return fibonacci(n-2) + fibonacci(n-1)
#
# print(fibonacci(6))




# def fibonacci(n):
#     print('Trying to find fibonacci for ', n)
#     conostant = [1, 2]
#     if n in conostant:
#         return 1
#     return fibonacci(n-2) + fibonacci(n-1)
#
# print(fibonacci(6))


# def print_number(n):
#     if n == 0:
#         return
#     print(n)
#     print_number(n-1)
#
# print_number(5)



# def print_number(n):
#     if n == 0:
#         return
#
#     print_number(n-1)
#     print(n)
#
# print_number(5)





# Bynary Search

# def binary_search(l, left, right, x):
#     if left > right:
#         return -1
#
#     mid = (left+right)//2
#     if l[mid] == x:
#         return mid
#     if l[mid] < x:
#         return binary_search(l, mid+1, right, x)
#     else:
#         return binary_search(l, left, right-1, x)
# li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# left = 0
#
# print(binary_search(li, 0, len(li)-1, 1))




def binary_search(l, left, right, x):
    if left > right:
        return -1
    mid = (left+right)//2

    if l[mid] == x:
        return mid
    if l[mid] < x:
        return binary_search(l, mid+1, right, x)
    else:
        return binary_search(l, left, right-1, x)


# if __name__ == '__main__':
#     l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#     left = 0
#     right = len(l)-1
#
#     for x in range(1, 12):
#         position = binary_search(l, left, right, x)
#         if position == -1:
#             if x in l:
#                 print(x, 'is in l, but function returned -1')
#             else:
#                 print(x, 'not in list')
#         else:
#             if l[position] == x:
#                 print(x, 'found in current position')
#             else:
#                 print('binary search returned', position, 'for', x, 'which is not correct')





if __name__ == '__main__':

    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    left = 0
    right = len(l)-1

    for x in range(1, 12):
        position = binary_search(l, left, right, x)
        if l[position] == x:
            print(x, 'found in current position')
        else:
            print('binary search returned', position, 'for', x, 'which is not correct')







