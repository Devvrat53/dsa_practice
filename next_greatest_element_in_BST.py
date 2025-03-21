# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    def inorder_successor_BST(self, root, prev):
        greatest = None
        while root:
            if prev >= root.val:
                root = root.right
            else:
                greatest = root
                root = root.left
        return greatest

    def greatest_element_BST(self, root, prev):
        greatest = -float("inf") 
        if root == None:
            return 0
        self.greatest_element_BST(root.left, prev)
        if greatest == prev:
            print(root.val)
        greatest = root.val
        self.greatest_element_BST(root.right, prev)

if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    soln = Solution()

    # print("Next greatest element:", soln.inorder_successor_BST(root, 15))
    # print("Next greatest element:", soln.greatest_element_BST(root, 15))