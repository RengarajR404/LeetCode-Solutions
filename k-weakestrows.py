class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
    def __eq__(self, a):
        if(a.key == self.key and a.val ==self.val):
            return True
        else:
            return False
    
    def __lt__(self, a):
        if (self.key < a.key or (self.key==a.key and self.val < a.val)):
            return True
        else:
            return False
    
    def __gt__(self, a):
        if (self.key > a.key or (self.key==a.key and self.val > a.val)):
            return True
        else:
            return False
    
class MinHeap:
    def __init__(self):
        self.heap=[]
        self.size = 0

    def peek(self):
        if not self.heap:
            return False
        return self.heap[0]

    def push(self, data):
        self.heap.append(data)
        self.heapify_up()
        self.size=+1

    def heapify_up(self):
        child=len(self.heap)-1
        while child >0:
            if(self.heap[child] < self.heap[(child-1)//2]):
                self.heap[child], self.heap[(child-1)//2] = self.heap[(child-1)//2], self.heap[child]
            child = (child-1)//2

    def pop(self):
        if not self.heap:
            return False
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        data = self.heap.pop()
        self.heapify_down()
        return data

    def heapify_down(self):
        i = 0
        while (2*i+1) < len(self.heap):  
            smaller_idx = 2*i+1
            if (2*i+2) < len(self.heap) and self.heap[2*i+2] < self.heap[2*i+1]:
                smaller_idx = 2*i+2
            if self.heap[smaller_idx] > self.heap[i]:
                return
            self.heap[smaller_idx], self.heap[i] = self.heap[i], self.heap[smaller_idx]
            i = smaller_idx
class Solution:
    def kWeakestRows(self, mat, k: int):
        h = MinHeap()
        c =0
        arr=[]
        arr2=[]
        for i in mat:
            h.push(Node(sum(i), c))
            c=c+1
        for i in range(k):
            arr.append(h.pop())
        arr.sort()
        for i in arr:
            arr2.append(i.val)
        return arr2
s= Solution()
print(s.kWeakestRows([[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]]
,3))