class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        root = 0
        for i in range(len(graph)):
            if graph[i]:
                root = i
                break
                
        
        for i in range(len(graph)):
            color = defaultdict(set)
            stack = [(i, "red")]
            while stack:
                node, exp_color = stack.pop()
                color[exp_color].add(node)
                for child in graph[node]:
                    if child not in color["blue"] and child not in color["red"]:
                        if exp_color == "red":
                            stack.append((child, "blue"))
                        else:
                            stack.append((child, "red"))
                    else:
                        if child in color[exp_color]:
                            return False
                 
                    
        return True
                        
        