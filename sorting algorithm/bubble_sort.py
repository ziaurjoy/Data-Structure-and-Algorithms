

def bubble_sort(l):
    n = len(l)
    for i in range(0, n):
        for j in range(0, n-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]

if __name__ == '__main__':
    L = [6, 1, 4, 9, 2]
    print('Before', L)
    bubble_sort(L)
    print('After', L)