# Implementation of max heap
# Programmed by Olac Fuentes
# Last modified November 18, 2019
# Only works with class Word

import matplotlib.pyplot as plt
import math
from Lab5.Word import Word


class MaxHeap(object):
    # Constructor
    def __init__(self):
        self.tree = []

    def is_empty(self):
        return len(self.tree) == 0

    def parent(self, i):
        if i == 0:
            return Word("", -math.inf)
        return self.tree[(i - 1) // 2]

    def left_child(self, i):
        c = 2 * i + 1
        if c >= len(self.tree):
            return Word("", -math.inf)
        return self.tree[c]

    def right_child(self, i):
        c = 2 * i + 2
        if c >= len(self.tree):
            return Word("", -math.inf)
        return self.tree[c]

    def insert(self, item):
        self.tree.append(item)
        self._percolate_up(len(self.tree) - 1)

    def _percolate_up(self, i):
        if i == 0:
            return

        parent_index = (i - 1) // 2

        if self.tree[parent_index] < self.tree[i]:
            self.tree[i], self.tree[parent_index] = self.tree[parent_index], self.tree[i]
            self._percolate_up(parent_index)

    def extract_max(self):
        if len(self.tree) < 1:
            return None
        if len(self.tree) == 1:
            return self.tree.pop()

        root = self.tree[0]
        self.tree[0] = self.tree.pop()

        self._percolate_down(0)

        return root

    def _percolate_down(self, i):
        if self.tree[i] >= max(self.left_child(i), self.right_child(i)):
            return

        max_child_index = 2 * i + 1 if self.left_child(i) > self.right_child(i) else 2 * i + 2

        self.tree[i], self.tree[max_child_index] = self.tree[max_child_index], self.tree[i]
        self._percolate_down(max_child_index)


    def draw(self):
        if not self.is_empty():
            fig, ax = plt.subplots()
            self.draw_(0, 0, 0, 100, 50, ax)
            ax.axis('off')
            ax.set_aspect(1.0)

            plt.show()

    def draw_(self, i, x, y, dx, dy, ax):
        if self.left_child(i) > Word("", -math.inf):
            ax.plot([x, x - dx], [y, y - dy], linewidth=1, color='k')
            self.draw_(2 * i + 1, x - dx, y - dy, dx / 2, dy, ax)
        if self.right_child(i) > Word("", -math.inf):
            ax.plot([x, x + dx], [y, y - dy], linewidth=1, color='k')
            self.draw_(2 * i + 2, x + dx, y - dy, dx / 2, dy, ax)
        ax.text(x, y, str(self.tree[i]), size=20,
                ha="center", va="center",
                bbox=dict(facecolor='w', boxstyle="circle"))

    def is_valid(self):
        if len(self.tree) == 0 or len(self.tree) == 1:
            return True
        # Check if parents are bigger
        for i in range(1, len(self.tree)):
            pi = self.parent(i)
            if self.tree[i] > self.tree[pi]:
                return False

        return True

    def second_max(self):
        if len(self.tree) == 2:
            return self.tree[0]
        return max(self.tree[1], self.tree[2])

    def print_path(self, i):
        if i == 0:
            print(self.tree[0])

        curr = i
        while curr < 0:
            print(self.tree[curr])
            curr = self.parent(curr)

    def try_replace(self, i, val):
        pi = self.parent(i)
        left_child_i = self.left_child(i)
        right_child_i = self.right_child(i)
        max_child = max(self.tree[left_child_i], self.tree[left_child_i])
        if self.tree[pi] > val and max_child < val:
            self.tree[i] == val

    def gen_gap(self):
        max_gap = Word("", -math.inf)
        for i in range(1, len(self.tree)):
            curr_gap = self.tree[self.parent(i)] - self.tree[i]
            if curr_gap > max_gap:
                max_gap = curr_gap

        return max_gap

    @staticmethod
    def max_index_heap(input_array):
        for i in range(1, len(input_array)):
            parent = input_array[(i - 1)//2]
            if input_array[i] > parent:
                return False

        return True


def heap_sort(a_lst):
    h = MaxHeap()
    for a in a_lst:
        h.insert(a)
    i = len(a_lst) - 1
    while not h.is_empty():
        a_lst[i] = h.extract_max()
        i -= 1


if __name__ == "__main__":
    plt.close("all")
    h = MaxHeap()
    a_list = [2, 6, 1, 5, 3, 8, 4, 12, 10, 11, 9, 7]
    for a in a_list:
        h.insert(a)
        print(h.tree)

    h.draw()

    while not h.is_empty():
        a = h.extract_max()
        print(h.tree)

    heap_sort(a_list)
    print(a_list)

