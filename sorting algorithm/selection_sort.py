def selection_sort(L):
    n = len(L)
    for i in range(0, n-1):
        index_min = i
        for j in range(i+1, n):
            if L[j] < L[index_min]:
                index_min = j
        if index_min != i:
            L[i], L[index_min] = L[index_min], L[i]

L = [6, 1, 4, 9, 2]
selection_sort(L)
print(L)

#
#
#
# if __name__ == '__main__':
#     L = [6, 1, 4, 9, 2]
#     print('Before', L)
#     selection_sort(L)
#     print('After', L)




# def selectionSort(array):
#     size = len(data)
#     for step in range(size):
#         min_idx = step
#
#         for i in range(step + 1, size):
#
#             # to sort in descending order, change > to < in this line
#             # select the minimum element in each loop
#             if array[i] < array[min_idx]:
#                 min_idx = i
#
#         # put min at the correct position
#
#         array[step], array[min_idx] = array[min_idx], array[step]
#
#
# data = [-2, 45, 0, 11, -9]
#
# selectionSort(data)
# print('Sorted Array in Ascending Order:')
# print(data)




# def selection_sort(l):
#     n = len(l)
#     for i in range(n):
#         index_min = i
#         for j in range(i+1, n):
#             if l[j] < l[index_min]:
#                 index_min = j
#         l[i], l[index_min] = l[index_min], l[i]
#
# data = [-2, 45, 0, 11, -9]
#
# selection_sort(data)
# print('Sorted Array in Ascending Order:')
# print(data)