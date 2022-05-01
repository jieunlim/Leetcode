from collections import defaultdict
class Node:
    def __init__(self):
        self.directory = defaultdict(lambda: Node())
        self.files = defaultdict(str)

class FileSystem:

    def __init__(self):
        self.root = Node()
        

    def ls(self, path: str) -> List[str]:
        node = self.root
        if path != "/":
            p = path.split('/')
            for i in range(1, len(p)-1):
                node = node.directory[p[i]]
            if p[-1] in node.files:
                return [p[-1]]
            node = node.directory[p[-1]]
        return sorted(list(node.directory)+(list(node.files)))

    def mkdir(self, path: str) -> None:
        node = self.root
        p = path.split('/')
        for i in range(1, len(p)):
            node = node.directory[p[i]]
            
    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self.root
        p = filePath.split('/')
        for i in range(1, len(p)-1):
            node =  node.directory[p[i]]
        node.files[p[-1]] += content


    def readContentFromFile(self, filePath: str) -> str:
        node = self.root
        p = filePath.split('/')
        for i in range(1, len(p)-1):
            node = node.directory[p[i]]
        return node.files[p[-1]]


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
