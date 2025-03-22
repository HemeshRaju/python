class Node:
    def __init__(self,key):
        self.val=key
        self.left=None
        self.right=None
def insert(root, key):
    if root is None:
        return Node(key)
    if root.val == key:
            return root
    if root.val < key:
            root.right = insert(root.right, key)
    else:
            root.left = insert(root.left, key)
    return root

list=[]
def inorder(root):
    global list
    if root:
        inorder(root.left)
        list.append(root.val)
        print(root.val, end=" ")
        inorder(root.right)
r=Node(5)
r=insert(r,3)
r=insert(r,6)
r=insert(r,2)
r=insert(r,4)
r=insert(r,7)
k=int(input("Kth smallest value:"))
inorder(r)
print()
print(list)
print(f"{k}th smallest value is",list[k-1])
