# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.main_list = []
        self.cur_idx = 0
        
        for i in nestedList:
            if i.isInteger():
                self.main_list.append(i.getInteger())
            else:
                inner_list = []
                n_itr = NestedIterator(i.getList())
                
                while n_itr.hasNext():
                    inner_list.append(n_itr.next())
                
                self.main_list += inner_list
    
    def next(self) -> int:
        self.cur_idx += 1
        return self.main_list[self.cur_idx-1]
        
    
    def hasNext(self) -> bool:
        return self.cur_idx < len(self.main_list)
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())