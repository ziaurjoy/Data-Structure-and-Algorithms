

# heap = [None] * 10
# heap[1] = 19
# heap[1*2] = 7
# heap[1*2+1] = 17
# heap[2*2] = 3
# heap[2*2+1] = 5
# heap[3*2] = 12
# heap[3*2+1] = 10
# heap[4*2] = 1
# heap[4*2+1] = 2



def left(i):
    return 2*i

def right(i):
    return 2*i+1

def parent(i):
    return i//2

def is_max_heap(H):
    n = len(H)-1
    for i in range(n, 1, -1):
        p = parent(i)
        if H[p] < H[i]:
            return False
        return True

# if __name__ == '__main__':
#     H = [None, 19, 7, 17, 3, 5, 12, 10, 1, 2]
# #    index 0    1  2  3   4  5   6  7   8  9
#     print(H, is_max_heap(H))
#     H = [None, 19, 7, 17, 3, 5, 12, 10, 1, 4]
#     print(H, is_max_heap(H))
#
#     H = [None, 1, 2, 3]
#     print(H, is_max_heap(H))
#
#     H = [None, 2, 1, 3]
#     print(H, is_max_heap(H))
#
#     H = [None, 3, 1, 2]
#     print(H, is_max_heap(H))

                        # 4      9
def max_heapify(heap, heap_size, i):
    l = left(i)
    r = right(i)
    if l <= heap_size and heap[l] > heap[i]:
        largest = l
    else:
        largest = i
    if r < heap_size and heap[r] > heap[largest]:
        largest = r
    if largest != i:
        heap[i], heap[largest] = heap[largest], heap[i]
        max_heapify(heap, heap_size, largest)

def build_max_heap(heap):
    heap_size = len(heap) - 1
    for i in range(heap_size//2, 0, -1):
        max_heapify(heap, heap_size, i)



        # BinaryTree package use

# if __name__ == '__main__':
#     heap = [None, 12, 7, 1, 3, 10, 17, 19, 2, 5]
#     print('Before building heap:')
#     print(heap)
#     build_max_heap(heap)
#     print('After building heap:')
#     print(heap)




def heap_sort(heap):
    build_max_heap(heap)
    heap_size = len(heap) - 1
    for i in range(heap_size, 1, -1):
        heap[1], heap[i] = heap[i], heap[1]
        heap_size -= 1
        max_heapify(heap, heap_size, 1)

if __name__ == '__main__':
    heap = [None, 12, 7, 1, 3, 10, 17, 19, 2, 5]
    print('Before building heap:')
    print(heap)
    heap_sort(heap)
    print('After building heap:')
    print(heap)










