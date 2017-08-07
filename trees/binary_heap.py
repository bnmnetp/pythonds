'''
Bradley N. Miller, David L. Ranum
Introduction to Data Structures and Algorithms in Python
Copyright 2005
Updated by Roman Yasinovskyy, 2017
'''


class BinaryHeap:
    '''Minimal Binary Heap'''
    def __init__(self):
        '''Create a heap'''
        self.__heap = []

    def __perc_up(self, cur_idx):
        '''Move a node up'''
        while (cur_idx - 1) // 2 >= 0:
            parent_idx = (cur_idx - 1) // 2
            if self.__heap[cur_idx] < self.__heap[parent_idx]:
                self.__heap[cur_idx], self.__heap[parent_idx] = \
                    self.__heap[parent_idx], self.__heap[cur_idx]
            cur_idx = parent_idx

    def __perc_down(self, cur_idx):
        '''Move a node down'''
        while 2 * cur_idx + 1 < len(self.__heap):
            min_child_idx = self.__get_min_child(cur_idx)
            if self.__heap[cur_idx] > self.__heap[min_child_idx]:
                self.__heap[cur_idx], self.__heap[min_child_idx] = \
                    self.__heap[min_child_idx], self.__heap[cur_idx]
            else:
                return
            cur_idx = min_child_idx

    def __get_min_child(self, parent_idx):
        '''Get a smaller child'''
        if 2 * parent_idx + 2 > len(self.__heap) - 1:
            return 2 * parent_idx + 1
        else:
            if self.__heap[2 * parent_idx + 1] < self.__heap[2 * parent_idx + 2]:
                return 2 * parent_idx + 1
            else:
                return 2 * parent_idx + 2

    def heapify(self, not_a_heap, show_details=False):
        '''Build a heap from any list'''
        self.__heap = not_a_heap[:]
        cur_idx = len(self.__heap) // 2 - 1
        while cur_idx >= 0:
            self.__perc_down(cur_idx)
            cur_idx = cur_idx - 1
            if show_details:
                print(self.__heap)

    def insert(self, item):
        '''Add a new item'''
        self.__heap.append(item)
        self.__perc_up(len(self.__heap) - 1)

    def delete(self):
        '''Remove an item'''
        self.__heap[0], self.__heap[-1] = \
            self.__heap[-1], self.__heap[0]
        result = self.__heap.pop()
        self.__perc_down(0)
        return result

    def is_empty(self):
        '''Check if the heap is empty'''
        return len(self.__heap) == 0

    def __len__(self):
        '''Get heap size'''
        return len(self.__heap)

    def __str__(self):
        '''Heap as a string'''
        return str(self.__heap)
