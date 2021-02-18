3
# foor loop

# def linear_search(l, x):
#     for i in l:
#         if l[i] == x:
#             return i
#     return -1
# my_list = [1, 2, 3, 4, 5]
# print(linear_search(my_list, 3))


# while loop

# def linear_search(l, x):
#     i = 0
#     while i < len(l):
#         if l[i] == x:
#             return i
#         i += 1
#     return -1
#
# my_list = [1, 2, 3, 4, 5]
# print(linear_search(my_list, 3))



# def binary_search(l, x):
#     # le = [1, 2, 3, 4, 5]
#     left = 0
#     right = len(l)-1
#     while left <= right:
#         mid = (left + right)//2
#         if l[mid] == x:
#             return mid
#         if l[mid] < x:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1
#
# le = [1, 2, 3, 4, 5]
# print(binary_search(le, 5))



# def binary_search(l, x):
#     left = 0
#     right = len(l) - 1
#     while left <= right:
#         mid = (left + right)//2
#         if l[mid] == x:
#             return mid
#         if l[mid] < x:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1
#
# li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(binary_search(li, 2))


# foor loop

# def binary_search(l, x):
#     left = 0
#     right = len(l)
#     for i in range(left, right):
#         mid = (left+right)//2
#         if l[mid] == x:
#             return mid
#         if l[mid] < x:
#             left = mid+1
#         else:
#             right = mid-1
#     return -1

# print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],9))





def linear_search(l, x):
    n = len(l)
    for i in range(n):
        if l[i] == x:
            return i
    return -1

print(linear_search([1, 2, 3, 4, 5], 4))


def test_linear_search():
    l = [1, 2, 3, 4, 5]
    excepted_result = 3





