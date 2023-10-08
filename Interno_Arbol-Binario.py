class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return TreeNode(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def inorder_traversal(root):
    result = []
    if root:
        result = inorder_traversal(root.left)
        result.append(root.val)
        result = result + inorder_traversal(root.right)
    return result

def tree_sort(arr):
    root = None
    for item in arr:
        root = insert(root, item)
    
    return inorder_traversal(root)

# Ejemplo de uso:
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    sorted_arr = tree_sort(arr)
    print("Arreglo ordenado:")
    for item in sorted_arr:
        print(item)
