

number_list = [1, 4, 6, 7, 10, 19, 22, 23, 30, 35, 39, 46, 49, 50, 52, 55, 61, 67, 70, 71]


def binary_search(l, x):
    n = len(l)
    left = 0
    right = n-1
    while left <= right:
        mid = (left+right) // 2
        if l[mid] == x:
            return mid
        if l[mid] >= x:
            right = right-1
        else:
            left = left + 1
    return -1
# print(binary_search(number_list, 100))



#
if __name__ == '__main__':
    L = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for x in range(1, 11):
        position = binary_search(L, x)
        if position == -1:
            if x in L:
                print(x, "is in l, but function returned -1")
            else:
                print(x, 'not in list')
        else:
            if L[position] == x:
                print(x, 'found in correct position')
            else:
                print('binary search returend, ', position, 'for', x, 'which is incorrect')
                print('program terminated')

#
# print(binary_search(number_list, 70))



# number_list = [1, 4, 6, 7, 10, 19, 22, 23, 30, 35, 39, 46, 49, 50, 52, 55, 61, 67, 70, 71]
#
# def binary_search(l, x):
#     n = len(l)
#     left = 0
#     right = n-1
#     for i in range(left, right):
#         mid = left + right // 2
#         if l[mid] == x:
#             return mid
#         if l[mid] > x:
#             right = right-1
#         else:
#             left = left+1
#     return -1
#
# print(binary_search(number_list, 70))


