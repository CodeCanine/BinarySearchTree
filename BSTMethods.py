# Class Methods
# Executed in main.py

from node import Node
import numpy as np


# Iterative DFS
def dfs_traversal_iter(root):
    if root is None:
        return []
    result = []
    # Start Node
    stack = [root]
    # Traversal
    while len(stack) > 0:
        current = stack.pop()
        # Adding elements to the final result array
        result.append(current.val)
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    # If no more elements in stack, return the finished array
    return result


# Recursive DFS
def dfs_traversal_rec(root):
    if root is None:
        return []
    return [root.val, *dfs_traversal_rec(root.left), *dfs_traversal_rec(root.right)]


# BFS Algorithm time complexity O(n), space complexity O(n) // no recursive, is it problematic, it uses heap
def bfs_traversal_iter(root):
    if root is None:
        return []
    result = []
    que = [root]
    while len(que) > 0:
        current = que.pop(0)
        result.append(current.val)
        if current.left:
            que.append(current.left)
        if current.right:
            que.append(current.right)
    return result


# Breadth First Traversal recursive method
# This is not as intuitive as the DFS version, as BFS uses a stack instead of que,
# and thus this algorithm becomes a deviation of a DFS algorithm.
# The nature of non-tail recursion does not completely allow the calculation to be O(n), but O(n*n)

bsf_rec = []


def bfs_traversal_rec(root, level):
    global bsf_rec
    if root is None:
        return
    if level == 0:
        return bsf_rec.append(root.val)
    elif level > 0:
        bfs_traversal_rec(root.left, level - 1)
        bfs_traversal_rec(root.right, level - 1)


# Breadth First Search iterative method
def bfs_search_iter(root, target):
    if root is None:
        return False
    que = [root]
    while que:
        current = que.pop(0)
        if current.val == target:
            return True
        if current.left:
            que.append(current.left)
        if current.right:
            que.append(current.right)
    return False


# Depth First Search recursive method
def dfs_search_rec(root, target):
    if root is None:
        return False

    # if root.val == target:
    #     return True
    # elif dfs_search_rec(root.left, target):
    #     return True
    # elif dfs_search_rec(root.right, target):
    #     return True
    # else:
    #     return False

    # One line code for above
    return True if root.val == target or dfs_search_rec(root.left, target) \
                   or dfs_search_rec(root.right, target) else False


# DFS recursive sum of tree
def tree_sum_rec(root):
    if root is None:
        return 0
    return root.val + tree_sum_rec(root.left) + tree_sum_rec(root.right)


# BFS iterative sum of tree
def tree_sum_iter(root):
    if root is None:
        return
    que = [root]
    total_sum = 0
    while que:
        current = que.pop(0)
        total_sum += current.val
        if current.left:
            que.append(current.left)
        if current.right:
            que.append(current.right)
    return total_sum


# DFS recursive minimum search for a simple Binary Tree, but works perfectly on Binary Search Trees as well
def minimum_value_rec(root):
    if root is None:
        return float('inf')
    return min(root.val, minimum_value_rec(root.left), minimum_value_rec(root.right))


# DFS iterative minimum search for a simple Binary Tree, but works perfectly on Binary Search Trees as well
def minimum_value_iter(root):
    if root is None:
        return None
    # Start Node
    stack = [root]
    smallest = float('inf')
    # Traversal
    while stack:
        current = stack.pop()
        if smallest > current.val:
            smallest = current.val
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return smallest


# BFS minimum search for a simple Binary Tree, but works perfectly on Binary Search Trees as well
def bfs_minimum_value_iter(root):
    if root is None:
        return None
    # Start Node
    que = [root]
    smallest = float('inf')
    # Traversal
    while que:
        current = que.pop(0)
        if smallest > current.val:
            smallest = current.val
        if current.left:
            que.append(current.left)
        if current.right:
            que.append(current.right)
    return smallest


# Specific Binary Search Tree method, as the minimum value must be on the furthermost left side of the tree
def get_min(root):
    if root is None:
        return None
    current = root
    while current.left:
        current = current.left
    return current.val


# Specific Binary Search Tree method, as the maximum value must be on the furthermost left side of the tree
def get_max(root):
    if root is None:
        return None
    current = root
    while current.right is not None:
        current = current.right
    return current.val


# Max of path sums
def max_path_sum_rec(root):
    if root is None:
        return float('-inf')
    if root.left is None and root.right is None:
        return root.val
    return root.val + max(max_path_sum_rec(root.left), max_path_sum_rec(root.right))


# Min of path sums
def min_path_sum_rec(root):
    if root is None:
        return float('inf')
    if root.left is None and root.right is None:
        return root.val
    return root.val + min(min_path_sum_rec(root.left), min_path_sum_rec(root.right))


# Recursive method to insert nodes into the BST
def insert(root, val):
    # If the tree is empty, return a new node
    if root is None:
        return Node(val)

    # Otherwise, recur down the tree
    if val < root.val:
        root.left = insert(root.left, val)
    elif val > root.val:
        root.right = insert(root.right, val)
    else:
        return root
        # return the (unchanged) node pointer
    return root


def preorder(root):
    if root is None:
        return "BST is empty!"
    print(root.val, end=" ")
    if root.left:
        preorder(root.left)
    if root.right:
        preorder(root.right)


def inorder(root):
    if root is None:
        return "BST is empty!"
    if root.left:
        inorder(root.left)
    print(root.val, end=" ")
    if root.right:
        inorder(root.right)


def postorder(root):
    # result = []
    result = np.array([])
    if root is None:
        return "BST is empty!"
    if root.left:
        result = np.append(result, postorder(root.left))
    if root.right:
        result = np.append(result, postorder(root.right))
    result = np.append(result, root.val)
    result = result.flatten().astype(int)
    return result


def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1


def successor(root):
    root = root.right
    while root.left:
        root = root.left
    return root.val


def predecessor(root):
    root = root.left
    while root.right:
        root = root.right
    return root.val


def delete(root, val):
    if not root:
        return None
    self = root
    if val > root.val:
        root.right = delete(root.right, val)
    elif val < root.val:
        root.left = delete(root.left, val)
    else:
        if not (root.left or root.right):
            root = None
        elif root.right:
            root.val = successor(root)
            root.right = delete(root.right, root.val)
        else:
            root.val = predecessor(root)
            root.left = delete(root.left, root.val)

    return root


def count(root):
    if root is None:
        return 0
    return 1 + count(root.left) + count(root.right)


# Below method is not written by me, I have found it on Stackoverflow.com
def PrintTree(root):
    nlevels = height(root)
    width = pow(2, nlevels)

    q = [(root, 0, width, 'c')]
    levels = []

    while q:
        node, level, x, align = q.pop(0)
        if node:
            if len(levels) <= level:
                levels.append([])

            levels[level].append([node, level, x, align])
            seg = width // (pow(2, level + 1))
            q.append((node.left, level + 1, x - seg, 'l'))
            q.append((node.right, level + 1, x + seg, 'r'))

    for i, l in enumerate(levels):
        pre = 0
        preline = 0
        linestr = ''
        pstr = ''
        seg = width // (pow(2, i + 1)) - 1
        for n in l:
            valstr = str(n[0].val)
            if n[3] == 'r':
                linestr += ' ' * (n[2] - preline - 1 - seg - seg // 2) + '¯' * (seg + seg // 2) + '\\'
                preline = n[2]
            if n[3] == 'l':
                linestr += ' ' * (n[2] - preline - 1) + '/' + '¯' * (seg + seg // 2)
                preline = n[2] + seg + seg // 2
            pstr += ' ' * (n[2] - pre - len(valstr)) + valstr  # correct the position according to the number size
            pre = n[2]
        print(linestr)
        print(pstr)
