# -*- coding:utf-8 -*-

"""

题目描述
输入一个链表，从尾到头打印链表每个节点的值。
输入描述:

输入为链表的表头

输出描述:

输出为需要打印的“新链表”的表头


"""


class ListNode:
    # 限定Node实例的属性
    __slots__ = ['val', 'next']

    def __init__(self, x):
        self.val = item
        # Node的指针部分默认指向None
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def __init__(self):
        self.data = []

    def printListFromTailToHead(self, listNode):
        if not listNode:
            return self.data

        while listNode.next:
            self.data.insert(0, listNode.val)
            listNode = listNode.next

        self.data.insert(0, listNode.val)

        return self.data
