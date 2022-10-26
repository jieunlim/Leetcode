class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nestedList = nestedList
        self.values = []
        self.position = -1
        
        def helper(nestedList):
            for nestedInteger in nestedList:
                if nestedInteger.isInteger(): 
                    self.values.append(nestedInteger.getInteger())
                else:
                    helper(nestedInteger.getList())
        helper(nestedList)
    
    def next(self) -> int:
        self.position += 1
        return self.values[self.position]
    
    def hasNext(self) -> bool:
        return self.position + 1 < len(self.values)
        
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
