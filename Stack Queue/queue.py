


class Queue:
    def __init__(self, size):
        self.items = [0] * size
        self.max_size = size
        self.head = 0
        self.tail = 0
        self.size = 0

    def enqueue(self, item):
        if self.is_full():
            print('Queue is full')
            return
        print('Inserting', item)
        self.items[self.tail] = item
        self.tail = (self.tail+1) % self.max_size
        self.size += 1

    def dequeue(self):
        item = self.items[self.head]
        self.head = (self.head+1) % self.max_size
        self.size -= 1
        return item



    def is_empty(self):
        if self.size == 0:
            return True
        return False

    def is_full(self):
        if self.size == self.max_size:
            return True
        return False


# q = Queue(3)
# q.enqueue('Joy')
# q.enqueue('Ziaur')
# q.enqueue('Imam')
# print(q.items)
# print(q.tail)
# print(q.head)

if __name__ == '__main__':
    q = Queue(3)
    q.enqueue('Joy')
    q.enqueue('Ziaur')
    q.enqueue('Imam')

    while not q.is_empty():
        persion = q.dequeue()
        print(persion)
    q.enqueue('Subeen')
    q.enqueue('Alu')
    print(q.items)
    print('Head:', q.head)
    print('tail:', q.tail)

