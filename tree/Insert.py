import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'queue_linked_list')))
from dequeue import Queue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftChild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    q = Queue()
    q.enqueue(rootNode)

    while not (q.is_empty()):
        root = q.dequeue()
        print(root.value.data)
        if root.value.leftChild:
            q.enqueue(root.value.leftChild)
        if root.value.rightChild:
            q.enqueue(root.value.rightChild)

def search(rootNode, value):
    if not rootNode:
        return "The BT does not exist"
    q = Queue()
    q.enqueue(rootNode)

    while not (q.is_empty()):
        root = q.dequeue()
        if root.value.data == value:
            return True
        if root.value.leftChild:
            q.enqueue(root.value.leftChild)
        if root.value.rightChild:
            q.enqueue(root.value.rightChild)
    return False

def insert(rootNode, newNode):
    if not rootNode:
        rootNode  = newNode
    else:
        q = Queue()
        q.enqueue(rootNode)

        while not q.is_empty():
            root = q.dequeue()
            if root.value.leftChild:
                q.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return True
            if root.value.rightChild:
                q.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return True
    return False

newTree = TreeNode("Drinks")
hot = TreeNode("Hot")
cold = TreeNode("Cold")
newTree.leftChild = hot
newTree.rightChild = cold
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
hot.leftChild = tea
hot.rightChild = coffee
fanta = TreeNode("Fanta")
cold.leftChild = fanta
preOrderTraversal(newTree)
inOrderTraversal(newTree)
postOrderTraversal(newTree)
print("***********level order**************")
levelOrderTraversal(newTree)
print("Searching: ", search(newTree, "Hot"))
newNode = TreeNode("Cola")
print("Inserting: ", insert(newTree, newNode))
print("***********level order**************")
preOrderTraversal(newTree)
