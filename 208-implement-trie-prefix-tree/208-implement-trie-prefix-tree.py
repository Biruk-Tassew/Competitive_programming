class TrieNode:
    def __init__(self, char):
        self.char = char
        self.is_end = False
        self.children = {}
        
class Trie:

    def __init__(self):
        self.root = TrieNode("")
    
    def insert(self, word: str) -> None:
        node = self.root
        
        for i in word:
            if i in node.children:
                node = node.children[i]
            else:
                n_node = TrieNode(i)
                node.children[i] = n_node
                node = n_node
                
        node.is_end = True
        
    def dfs(self, node, parent):
        if node.is_end:
            return True
        
        for i in node.children.values():
            self.dfs(i, parent + node.char)
            
    def search(self, word: str) -> bool:
        node = self.root
        for i in word:
            if i in node.children:
                node = node.children[i]
            else:
                return False
            
        self.search_res = []
        return self.dfs(node, word[:-1])
        

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        
        for i in prefix:
            if i not in node.children:
                return False
            node = node.children[i]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)