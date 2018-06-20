'''
Bradley N. Miller, David L. Ranum
Problem Solving with Algorithms and Data Structures using Python
Copyright 2005
Updated by Roman Yasinovskyy, 2017
'''


class BinaryHeap:
    '''Minimal Binary Heap'''
    def __init__(self):
        '''Create a heap'''
        self._heap = []

    def _perc_up(self, cur_idx):
        '''Move a node up'''
        while (cur_idx - 1) // 2 >= 0:
            parent_idx = (cur_idx - 1) // 2
            if self._heap[cur_idx] < self._heap[parent_idx]:
                self._heap[cur_idx], self._heap[parent_idx] = \
                    self._heap[parent_idx], self._heap[cur_idx]
            cur_idx = parent_idx

    def _perc_down(self, cur_idx):
        '''Move a node down'''
        while 2 * cur_idx + 1 < len(self._heap):
            min_child_idx = self._get_min_child(cur_idx)
            if self._heap[cur_idx] > self._heap[min_child_idx]:
                self._heap[cur_idx], self._heap[min_child_idx] = \
                    self._heap[min_child_idx], self._heap[cur_idx]
            else:
                return
            cur_idx = min_child_idx

    def _get_min_child(self, parent_idx):
        '''Get a smaller child'''
        if 2 * parent_idx + 2 > len(self._heap) - 1:
            return 2 * parent_idx + 1
        else:
            if self._heap[2 * parent_idx + 1] < self._heap[2 * parent_idx + 2]:
                return 2 * parent_idx + 1
            else:
                return 2 * parent_idx + 2

    def heapify(self, not_a_heap, show_details=False):
        '''Build a heap from any list'''
        self._heap = not_a_heap[:]
        cur_idx = len(self._heap) // 2 - 1
        while cur_idx >= 0:
            self._perc_down(cur_idx)
            cur_idx = cur_idx - 1
            if show_details:
                print(self._heap)

    def insert(self, item):
        '''Add a new item'''
        self._heap.append(item)
        self._perc_up(len(self._heap) - 1)

    def delete(self):
        '''Remove an item'''
        self._heap[0], self._heap[-1] = \
            self._heap[-1], self._heap[0]
        result = self._heap.pop()
        self._perc_down(0)
        return result

    def is_empty(self):
        '''Check if the heap is empty'''
        return not bool(self._heap)

    def __len__(self):
        '''Get heap size'''
        return len(self._heap)

    def __str__(self):
        '''Heap as a string'''
        return str(self._heap)

    def __contains__(self, item):
        '''__contains__in method override'''
        return item in self._heap
