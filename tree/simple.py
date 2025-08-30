class TreeNode:
    def __init__(self, data, children = []):
        self.data = data
        self.children = children

    def addChild(self, TreeNode):
        self.children.append(TreeNode)

tree = TreeNode("Drinks", [])
cold = TreeNode("Cold", [])
hot = TreeNode("Hot", [])
tree.addChild(cold)
tree.addChild(hot)
print(tree)