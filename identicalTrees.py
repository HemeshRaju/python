class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def is_same_tree(p: TreeNode, q: TreeNode):
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.right = TreeNode(3)
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
print(is_same_tree(root1,root2))