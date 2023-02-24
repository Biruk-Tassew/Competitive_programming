class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        seen = set()
        que = deque([beginWord])
        alphas = [chr(i) for i in range(97, 123)]
        words = set(wordList)
        level = 0
        
        while que:
            for _ in range(len(que)):
                node = que.popleft()
                
                if node == endWord:
                    return level + 1
                
                for i in range(len(node)):
                    for char in alphas:
                        n_word = node[:i] + char + node[i+1:]
                        
                        if n_word in words and n_word not in seen:
                            que.append(n_word)
                            seen.add(n_word)
                            
            level += 1
            
        return 0