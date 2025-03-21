class TreeNode():
    def __init__(self, val=0):
        self.val = val
        self.children = []
    
class Solution():
    def preorder(self, root:TreeNode):
        if root == None:
            return 
        node = [root.val]
        for child in root.children:
            node.extend(self.preorder(child))
        return node
    
    # Ordered N-ary tree
    def same_tree(self, node1: TreeNode, node2: TreeNode):
        if node1 == None and node2 == None:
            return True
        if node1 == None or node2 == None:
            return False
        answer = node1.val == node2.val and len(node1.children) == len(node2.children)
        if answer is None:
            return False
        for child1, child2 in zip(node1.children,node2.children):
            if self.same_tree(child1, child2) == False:
                return False
        return True

if __name__ == '__main__':
    root = TreeNode(1)
    root.children.append(TreeNode(3))
    root.children.append(TreeNode(2))
    root.children.append(TreeNode(4))
    root.children[0].children.append(TreeNode(5))
    root.children[0].children.append(TreeNode(6))
    
    root1 = TreeNode(1)
    root1.children.append(TreeNode(3))
    root1.children.append(TreeNode(2))
    root1.children.append(TreeNode(4))
    root1.children[0].children.append(TreeNode(5))
    root1.children[0].children.append(TreeNode(6))

    soln = Solution()
    print(soln.preorder(root))

    print("Check same tree for 2 N-ary trees: ", soln.same_tree(root, root1))
