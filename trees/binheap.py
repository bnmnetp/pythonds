# Bradley N. Miller, David L. Ranum
# Introduction to Data Structures and Algorithms in Python
# Copyright 2005
# 
import unittest

# this heap takes key value pairs, we will assume that the keys are integers
class BinHeap:
    def __init__(self):
        self.heapList = []
        self.currentSize = 0

    def buildHeap(self,alist):
        self.currentSize = len(alist)
        self.heapList = alist[:]

        i = len(alist)//2 -1
        while (i >= 0):
            self.percDown(i)
            print(i, self.heapList)
            i = i - 1
                        
    def percDown(self,i):
        heapList = self.heapList
        while True:
            child = 2*i+1
            if child >= self.currentSize:
                break
            if child+1<self.currentSize and heapList[child+1] < heapList[child]:
                child += 1
            if heapList[i] > heapList[child]:
                # swap
                heapList[i],heapList[child] = heapList[child],heapList[i] 
            else:
                break
            i = child

    def percUp(self,i):
        heapList = self.heapList
        while (i-1) // 2 >= 0:
            parent = (i-1)//2
            if heapList[i] < heapList[parent]:
                heapList[i], heapList[parent] = heapList[parent],heapList[i]
            else:
                break
            i = parent

    def insert(self,k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize-1)

    def delMin(self):
        retval = self.heapList[0]
        self.heapList[0] = self.heapList[self.currentSize-1]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(0)
        return retval
        
    def isEmpty(self):
        if currentSize == 0:
            return True
        else:
            return False

class FooThing:
    def __init__(self,x,y):
        self.key = x
        self.val = y
        

    def __lt__(self,other):
        if self.key < other.key:
            return True
        else:
            return False

    def __gt__(self,other):
        if self.key > other.key:
            return True
        else:
            return False
        
    def __hash__(self):
        return self.key

class TestBinHeap(unittest.TestCase):
    def setUp(self):
        self.theHeap = BinHeap()
        self.theHeap.insert(FooThing(5,'a'))                               
        self.theHeap.insert(FooThing(9,'d'))                  
        self.theHeap.insert(FooThing(1,'x'))
        self.theHeap.insert(FooThing(2,'y'))
        self.theHeap.insert(FooThing(3,'z'))

    def testInsert(self):
        assert self.theHeap.currentSize == 5

    def testDelmin(self):
        assert self.theHeap.delMin().val == 'x'
        assert self.theHeap.delMin().val  == 'y'
        assert self.theHeap.delMin().val  == 'z'
        assert self.theHeap.delMin().val  == 'a'

    def testMixed(self):
        myHeap = BinHeap()
        myHeap.insert(9)
        myHeap.insert(1)
        myHeap.insert(5)
        assert myHeap.delMin() == 1
        myHeap.insert(2)
        myHeap.insert(7)
        assert myHeap.delMin() == 2
        assert myHeap.delMin() == 5

    def testDupes(self):
        myHeap = BinHeap()
        myHeap.insert(9)
        myHeap.insert(1)
        myHeap.insert(8)
        myHeap.insert(1)
        assert myHeap.currentSize == 4
        assert myHeap.delMin() == 1
        assert myHeap.delMin() == 1
        assert myHeap.delMin() == 8

    def testBuildHeap(self):
        myHeap = BinHeap()
        myHeap.buildHeap([9,5,6,2,3])
        f = myHeap.delMin()
        print("f = ", f)
        assert f == 2
        assert myHeap.delMin() == 3
        assert myHeap.delMin() == 5
        assert myHeap.delMin() == 6
        assert myHeap.delMin() == 9                        
        
if __name__ == '__main__':
    d = {}
    d[FooThing(1,'z')] = 10
    unittest.main()
