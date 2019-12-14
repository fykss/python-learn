# https://leetcode.com/problems/range-sum-of-bst/
# TODO range sum of BST

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def rangeSumBST(root: TreeNode, L: int, R: int) -> int:
    root.left = L
    print(root.left)
    return 0


root = [10, 5, 15, 3, 7, 18]
L = 7
R = 15
tree_node = TreeNode(L)

tree_node.left = 1
print(tree_node.left)
print(tree_node.right)

rangeSumBST(root, L, R)