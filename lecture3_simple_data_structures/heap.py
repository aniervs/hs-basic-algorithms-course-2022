count = 0

def parent(v):
    return (v - 1) // 2

def left(v):
    return 2 * v + 1

def right(v):
    return 2 * v + 2

class Heap:
    def __init__(self):
        self.lst = []
    def heapify_down(self) -> None:
        '''
        Swaps the value at the root as long as it's greater than its two children
        '''
        v = 0

        global count

        while v < len(self.lst):
            count += 1
            l = left(v)
            r = right(v)

            if l >= len(self.lst):
                break 
            
            idx = -1

            if r >= len(self.lst) or self.lst[l] <= self.lst[r]:
                idx = l
            else:
                idx = r
            
            if self.lst[idx] < self.lst[v]:
                self.lst[idx], self.lst[v] = self.lst[v], self.lst[idx]
                v = idx
            else:
                break 

    def heapify_up(self, v: int) -> None :
        '''
        Swap the vertex v with its ancestors as long as it is greater than them
        '''

        global count

        while v != 0:
            count += 1
            pv = parent(v)

            if self.lst[pv] > self.lst[v]:
                self.lst[pv], self.lst[v] = self.lst[v], self.lst[pv] 
                v = parent(v)
            else:
                break

    def insert(self, value: int) -> None:
        self.lst.append(value)
        self.heapify_up(len(self.lst) - 1)

    def pop(self) -> None:
        '''
        Pops the minimum value
        '''
        assert not self.empty(), 'The heap is empty, thus we cannot erase anything'

        self.lst[0], self.lst[-1] = self.lst[-1], self.lst[0]
        self.lst.pop(-1)

        if not self.empty():
            self.heapify_down()

    def size(self):
        return len(self.lst)

    def empty(self):
        return self.size() == 0


import numpy as np
from matplotlib import pyplot as plt 

x = np.array([10**i for i in range(5)])
y = []

for n in x:
    lst = np.random.randint(10000, size = n)
    count = 0
    H = Heap()
    for i in lst:
        H.insert(i)
    for _ in range(n):
        H.pop()

    y.append(count)

y = np.array(y)

plt.plot(x, y)
x = np.arange(1, 10**4 + 1, 1)
y = 1.5 * x * np.log(x)

plt.plot(x, y)

plt.show()
