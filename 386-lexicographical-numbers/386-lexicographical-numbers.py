class TrieNode:
    def __init__(self, dig):
        self.dig = dig
        self.is_end = False
        self.children = {}
        
class Solution:
    def __init__(self):
        self.root = TrieNode("")
        
    def insert(self, num):
        node = self.root
        
        for i in num:
            if i in node.children:
                node = node.children[i]
            else:
                n_node = TrieNode(i)
                node.children[i] = n_node
                node = n_node
            
        node.is_end = True
        
    def dfs(self, node, pre):
        if node.is_end:
            self.res.append(pre)
            
        for i in node.children.values():
            self.dfs(i, pre + i.dig)    
            
    def lexicalOrder(self, n: int) -> List[int]:
        for i in range(1, n+1):
            self.insert(str(i))
            
        self.res = []
        self.dfs(self.root, "")
        return self.res
        
         
        
                    
                    
            
    