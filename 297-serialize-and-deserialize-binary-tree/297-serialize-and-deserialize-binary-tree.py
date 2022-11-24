# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "#"
        
        return ",".join([str(root.val), str(self.serialize(root.left)), str(self.serialize(root.right))])
     
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        self.data = data
        if self.data[0] == "#":
            return None
        
        node = TreeNode(data[:self.data.find(",")])
        node.left = self.deserialize(self.data[self.data.find(",")+1:])
        node.right = self.deserialize(self.data[self.data.find(",")+1:])
        
        return node
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))