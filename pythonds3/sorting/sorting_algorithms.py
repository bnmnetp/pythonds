#!/usr/bin/env python3
"""
Bradley N. Miller, David L. Ranum
Problem Solving with Algorithms and Data Structures using Python
Copyright 2005
Updated by Roman Yasinovskyy, 2017
"""

import heapq


def bubble_sort(lst):
    """Bubble sort"""
    for i in range(len(lst) - 1, 0, -1):
        exchanges = False
        for j in range(i):
            if lst[j] > lst[j + 1]:
                exchanges = True
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
        if not exchanges:
            break


def select_sort(lst):
    """Selection sort"""
    for i, item in enumerate(lst):
        min_idx = len(lst) - 1
        for j in range(i, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        if min_idx != i:
            lst[min_idx], lst[i] = lst[i], lst[min_idx]


def insert_sort(lst):
    """Insertion sort"""
    for i in range(1, len(lst)):
        cur_val = lst[i]
        cur_pos = i

        while cur_pos > 0 and lst[cur_pos - 1] > cur_val:
            lst[cur_pos] = lst[cur_pos - 1]
            cur_pos = cur_pos - 1
        lst[cur_pos] = cur_val


def shell_sort(lst):
    """Shell sort"""
    sublist_count = len(lst) // 3
    while sublist_count > 0:
        for pos_start in range(sublist_count):
            _gap_insert_sort(lst, pos_start, sublist_count)
        sublist_count = sublist_count // 2


def _gap_insert_sort(lst, start, gap):
    """Shell sort helper function"""
    for i in range(start + gap, len(lst), gap):
        cur_val = lst[i]
        cur_pos = i
        while cur_pos >= gap and lst[cur_pos - gap] > cur_val:
            lst[cur_pos] = lst[cur_pos - gap]
            cur_pos = cur_pos - gap
        lst[cur_pos] = cur_val


def merge_sort(lst):
    """Merge sort"""
    if len(lst) > 1:
        mid = len(lst) // 2
        left_half = lst[:mid]
        right_half = lst[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                lst[k] = left_half[i]
                i = i + 1
            else:
                lst[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            lst[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            lst[k] = right_half[j]
            j = j + 1
            k = k + 1


def quick_sort(lst):
    """Quick sort"""
    _quick_sort_help(lst, 0, len(lst) - 1)


def _quick_sort_help(lst, mark_l, mark_r):
    """Quick sort helper"""
    if mark_l < mark_r:
        split = _quick_sort_part(lst, mark_l, mark_r)
        _quick_sort_help(lst, mark_l, split - 1)
        _quick_sort_help(lst, split + 1, mark_r)


def _quick_sort_part(lst, mark_l, mark_r):
    """Quick sort partition"""
    pivot_val = lst[mark_l]
    mark_l_cur = mark_l + 1
    mark_r_cur = mark_r
    done = False

    while not done:
        while mark_l_cur <= mark_r_cur and lst[mark_l_cur] <= pivot_val:
            mark_l_cur = mark_l_cur + 1
        while mark_l_cur <= mark_r_cur and lst[mark_r_cur] >= pivot_val:
            mark_r_cur = mark_r_cur - 1
        if mark_r_cur < mark_l_cur:
            done = True
        else:
            lst[mark_l_cur], lst[mark_r_cur] = lst[mark_r_cur], lst[mark_l_cur]
    lst[mark_l], lst[mark_r_cur] = lst[mark_r_cur], lst[mark_l]

    return mark_r_cur


def heap_sort(lst):
    """Heap sort"""
    res = []
    heapq.heapify(lst)
    while lst:
        res.append(heapq.heappop(lst))
    for i in res:
        lst.append(i)
