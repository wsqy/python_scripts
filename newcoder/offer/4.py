# -*- coding:utf-8 -*-
"""
重建二叉树

题目描述
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，
则重建二叉树并返回。

"""


class Solution:
    # 返回构造的TreeNode根节点
    def __init__(self):
        self.data = []

    def reConstructBinaryTree(self, pre, tin):
        if len(pre) == 0:
            return None
        val = pre[0]
        self.data.append(val)
        for i in range(0, len(tin)):
            if tin[i] == val:
                break
        left = self.reConstructBinaryTree(pre[1:1+i], tin[:i])
        right = self.reConstructBinaryTree(pre[1+i:], tin[1+i:])
        return self.data

if __name__ == '__main__':
    pre_order = [1, 2, 4, 7, 3, 5, 6, 8]
    mid_order = [4, 7, 2, 1, 5, 3, 8, 6]
    s = Solution()
    root = s.reConstructBinaryTree(pre_order, mid_order)
    print(root)
