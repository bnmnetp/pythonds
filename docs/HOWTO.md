# Install

```> python -m pip install pythonds3```

# Use

## Introduction to OOP

### Class Fraction
```python
>>> import pythonds3.intro as intro
>>> f1 = intro.Fraction(2, 3)
>>> f1
Fraction(2, 3)
>>> print(f1)
2/3
>>> f1.numer
2
>>> f1.denom
3
>>> f1.get_denom()
3
>>> f2 = intro.Fraction(4, 6)
>>> f2
Fraction(2, 3)
>>> f1 == f2
True
>>> f1 + f2
Fraction(4, 3)
>>> 
```

## Basic Data Structures

### Stack
```python
>>> import pythonds3.basic as bds
>>> s = bds.Stack()
>>> s.is_empty()
True
>>> s.size()
0
>>> s.push('Aardvark')
>>> s.push('Beaver')
>>> s.size()
2
>>> s.peek()
'Beaver'
>>> s.pop()
'Beaver'
>>> s.peek()
'Aardvark'
>>> s.is_empty()
False
>>> s.size()
1
>>> 
```

### Queue
```python
>>> import pythonds3.basic as bds
>>> q = bds.Queue()
>>> q.is_empty()
True
>>> q.size()
0
>>> q.enqueue('Aardvark')
>>> q.enqueue('Beaver')
>>> q.size()
2
>>> q.dequeue()
'Aardvark'
>>> q.is_empty()
False
>>> q.size()
1
>>> 
```

### Deque
```python
>>> import pythonds3.basic as bds
>>> dq = bds.Deque()
>>> dq.is_empty()
True
>>> dq.size()
0
>>> dq.add_front('Aardvark')
>>> dq.add_front('Beaver')
>>> dq.size()
2
>>> dq.add_rear('Cheetah')
>>> dq.size()
3
>>> dq.remove_front()
'Beaver'
>>> dq.remove_rear()
'Cheetah'
>>> dq.is_empty()
False
>>> dq.size()
1
>>> 
```

### Unordered Linked List
```python
>>> import pythonds3.basic as bds
>>> ull = bds.UnorderedList()
>>> ull.is_empty()
True
>>> ull.size()
0
>>> ull.add('Aardvark')
>>> ull.add('Beaver')
>>> ull.size()
2
>>> ull.search('Beaver')
True
>>> ull.search('Cheetah')
False
>>> len(ull)
2
>>> print(ull)
[Beaver, Aardvark]
>>> ull.remove('Beaver')
>>> print(ull)
[Aardvark]
>>> ull.is_empty()
False
>>> ull.size()
1
>>> 
```

### Ordered Linked List
```python
>>> import pythonds3.basic as bds
>>> oll = bds.OrderedList()
>>> oll.is_empty()
True
>>> oll.size()
0
>>> len(oll)
0
>>> oll.add('Beaver')
>>> oll.add('Aardvark')
>>> oll.add('Cheetah')
>>> print(oll)
[Aardvark, Beaver, Cheetah]
>>> oll.is_empty()
False
>>> oll.size()
3
>>> 
```

## Searching

### Class HashTable
```python
>>> import pythonds3.searching as search
>>> ht = search.HashTable(4)
>>> len(ht)
0
>>> ht[0] = 'Aardvark'
>>> ht[0]
'Aardvark'
>>> ht.put(100, 'Beaver')
>>> ht.get(100)
'Beaver'
>>> len(ht)
2
>>> 100 in ht
True
>>> 200 in ht
False
>>> 
```

## Sorting

### Bubble sort
```python
>>> import pythonds3.sorting as sorta
>>> lst = [30, 40, 20, 50, 10]
>>> lst
[30, 40, 20, 50, 10]
>>> sorta.bubble_sort(lst)
>>> lst
[10, 20, 30, 40, 50]
>>> 
```

### Selection sort
```python
>>> import pythonds3.sorting as sorta
>>> lst = [30, 40, 20, 50, 10]
>>> lst
[30, 40, 20, 50, 10]
>>> sorta.select_sort(lst)
>>> lst
[10, 20, 30, 40, 50]
>>> 
```

### Insertion sort
```python
>>> import pythonds3.sorting as sorta
>>> lst = [30, 40, 20, 50, 10]
>>> lst
[30, 40, 20, 50, 10]
>>> sorta.insert_sort(lst)
>>> lst
[10, 20, 30, 40, 50]
>>> 
```

### Shellsort
```python
>>> import pythonds3.sorting as sorta
>>> lst = [30, 40, 20, 50, 10]
>>> lst
[30, 40, 20, 50, 10]
>>> sorta.shell_sort(lst)
>>> lst
[10, 20, 30, 40, 50]
>>> 
```

### Merge sort
```python
>>> import pythonds3.sorting as sorta
>>> lst = [30, 40, 20, 50, 10]
>>> lst
[30, 40, 20, 50, 10]
>>> sorta.merge_sort(lst)
>>> lst
[10, 20, 30, 40, 50]
>>> 
```

### Quicksort
```python
>>> import pythonds3.sorting as sorta
>>> lst = [30, 40, 20, 50, 10]
>>> lst
[30, 40, 20, 50, 10]
>>> sorta.quick_sort(lst)
>>> lst
[10, 20, 30, 40, 50]
>>> 
```

### Heapsort
```python
>>> import pythonds3.sorting as sorta
>>> lst = [30, 40, 20, 50, 10]
>>> lst
[30, 40, 20, 50, 10]
>>> sorta.heap_sort(lst)
>>> lst
[10, 20, 30, 40, 50]
>>> 
```

## Trees

### Binary Tree
```python
>>> import pythonds3.trees as trees
>>> bt = trees.BinaryTree('A')
>>> bt.root
'A'
>>> bt.insert_left('B')
>>> bt.insert_right('C')
>>> bt.preorder()
A B C
>>> bt.inorder()
B A C
>>> bt.postorder()
B C A
>>> bt.height()
1
>>> bt.size()
3
>>> len(bt)
3
>>> bt.root
'A'
>>> bt.child_left.root
'B'
>>> bt.child_right.root
'C'
>>> 
```

### Binary Search Tree
```python
>>> import pythonds3.trees as trees
>>> bst = trees.BinarySearchTree()
>>> bst[0] = 'Aardvark'
>>> bst[1] = 'Cheetah'
>>> bst[2] = 'Beaver'
>>> bst.preorder()
0 1 2
>>> bst.inorder()
0 1 2
>>> bst.postorder()
2 1 0
>>> 0 in bst
True
>>> len(bst)
3
>>> bst.delete(1)
>>> len(bst)
2
>>> bst[0]
'Aardvark'
>>> 
```

### AVL Tree
```python
>>> import pythonds3.trees as trees
>>> avlt = trees.AVLTree()
>>> avlt[0] = 'Aardvark'
>>> avlt[1] = 'Beaver'
>>> avlt[2] = 'Cheetah'
>>> avlt.size()
3
>>> avlt.inorder()
0 1 2
>>> avlt.preorder()
1 0 2
>>> avlt.postorder()
0 2 1
>>> avlt.get_root().get_key()
1
>>> 
```

### Binary Heap
```python
>>> import pythonds3.trees as trees
>>> bh = trees.BinaryHeap()
>>> bh.insert(30)
>>> bh.insert(40)
>>> bh.insert(20)
>>> bh.insert(50)
>>> bh.insert(10)
>>> print(bh)
[10, 20, 30, 50, 40]
>>> lst = [30, 40, 20, 50, 10]
>>> bh.heapify(lst)
>>> print(bh)
[10, 30, 20, 50, 40]
>>> 
```

## Graphs

### Breadth-first search
```python
```

### Depth-first search
```python
```

### Dijkstra's algorithm
```python
```
