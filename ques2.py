# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 16:32:15 2023

@author: vvrav
"""

class TreeNode(object):
    
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def solution(root):
    
    if not root:
        return 0

    left_depth = solution(root.left)
    right_depth = solution(root.right)

    # Return the maximum depth among the left and right subtrees plus 1 for the current node.
    return max(left_depth, right_depth) + 1

a15 = TreeNode(15)
a7 = TreeNode(7)
a20 = TreeNode(20)
a9 = TreeNode(9)
a3 = TreeNode(3)
a20.left = a15
a20.right = a7
a3.left = a9
a3.right = a20

print(solution(a3))
