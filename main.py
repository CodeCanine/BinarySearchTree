# This project is a practice of the BST data structure implementation and it's methods.
# 3 Separate Classes to define the Nodes (node.py), defining the methods (BSTMethods.py), and execution (main.py)

# n = number of nodes
# Time complexity: O(n)
# Space complexity: O(n)

# Binary Search Tree is a node-based binary tree data structure which has the following properties:

# - The left subtree of a node contains only nodes with keys lesser than the node’s key.
# - The right subtree of a node contains only nodes with keys greater than the node’s key.
# - The left and right subtree each must also be a binary search tree.


from BSTMethods import *
from node import *
import random

# Manual Tests below, feel free to use them directly, or leave them commented out.
if __name__ == '__main__':
    # Manual test #1
    #     a
    #    / \
    #   b   c
    #  / \    \
    # d   e    f

    # a = Node('a')
    # b = Node('b')
    # c = Node('c')
    # d = Node('d')
    # e = Node('e')
    # f = Node('f')
    # a.left = b
    # a.right = c
    # b.left = d
    # b.right = e
    # c.right = f

    # Manual test #2
    #      10
    #    /    \
    #   2     60
    #  / \
    # 1   3
    #      \
    #       5

    # a1 = Node('10')
    # b1 = Node('2')
    # c1 = Node('60')
    # d1 = Node('1')
    # e1 = Node('3')
    # f1 = Node('5')
    # a1.left = b1
    # a1.right = c1
    # b1.left = d1
    # b1.right = e1
    # c1.right = f1

    # Manual test with insert method
    #      50
    #    /    \
    #   30     70
    #  / \    /  \
    # 20  40 60  80

    # root = None
    # root = insert(root, 50)
    # root = insert(root, 30)
    # root = insert(root, 20)
    # root = insert(root, 40)
    # root = insert(root, 70)
    # root = insert(root, 60)
    # root = insert(root, 80)

    # Same as above code, just shorter
    # root = None
    # # node_list = [50, 30, 20, 40, 70, 60, 80]
    # node_list = [50, 30, 20, 40]
    # for element in node_list:
    #     root = insert(root, element)

    # Testing for random values
    # Initializing Root Node
    root = None
    # Initializing list for elements of the Tree
    random_list = []
    # Including 0, to test no root cases as well
    # Below code will append 5-10 Numbers between 1-30 to the previously initialized list (can be scaled infinitely).
    N = random.randint(5, 10)
    for i in range(0, N):
        random_list.append(random.randint(1, 30))
    # Checking the list of elements
    print(random_list)

    # For debugging:
    # print(set(sorted(random_list)))

    # Creating and adding Nodes to the BST from the previously filled list
    for element in random_list:
        root = insert(root, element)

    # Visual representation of the BST
    PrintTree(root)
    print("\nNumber of Nodes:")
    print(count(root))
    print("\nHeight of tree:")
    print(height(root))
    print("\nDFS traversal iterative approach:")
    print(dfs_traversal_iter(root))
    print("\nDFS traversal recursive approach:")
    print(dfs_traversal_rec(root))
    print("\nBFS traversal iterative approach:")
    print(bfs_traversal_iter(root))
    print("\nBFS traversal recursive approach:")

    # BFS Recursive Traversal works differently than Iterative, must be nested in loop
    for i in range(0, height(root)):
        bfs_traversal_rec(root, i)
    print(*bsf_rec)

    # BFS Search will return True if Node is present in tree, otherwise it will return False
    print("\nBFS search iterative approach:")
    print(bfs_search_iter(root, 0))
    print("\nSum of tree iterative approach:")
    print(tree_sum_iter(root))
    print("\nSum of tree recursive approach:")
    print(tree_sum_rec(root))
    print("\nDFS Minimum value iterative approach:")
    print(minimum_value_iter(root))
    print("\nBFS Minimum value iterative approach:")
    print(bfs_minimum_value_iter(root))
    print("\nMinimum value recursive approach:")
    print(minimum_value_rec(root))
    print("\nMinimum value getmin approach:")
    print(get_min(root))
    print("\nMax path sum recursive:")
    print(max_path_sum_rec(root))
    print("\nMin path sum recursive:")
    print(min_path_sum_rec(root))
    # Testing insert before deletion
    root = insert(root, 11)
    root = insert(root, 0)
    print("\nAfter Insertion:")
    PrintTree(root)
    # For debugging checking current state
    # print(*dfs_traversal_iter(root))

    # Deletion
    # All 3 types of deletion (Root, Leaf, Middle) are working properly.
    delete(root, postorder(root)[-1])
    print("\nAfter deleting root node:")
    PrintTree(root)
    print(*dfs_traversal_iter(root))
    print("\nAfter deleting mid node:")
    delete(root, 11)
    PrintTree(root)
    print(*dfs_traversal_iter(root))
    print("\nAfter deleting end node:")
    delete(root, 0)
    PrintTree(root)
    print(*dfs_traversal_iter(root))

    # Orderings working properly
    print("\n\nPreorder")
    preorder(root)
    print("\n\nInorder")
    inorder(root)
    print("\n\nPostorder")
    print(*postorder(root))
