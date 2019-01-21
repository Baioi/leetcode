class Node(object):
    def __init__(self, v, n):
        self.node = n
        self.visited = v[:]
class Solution(object):
    
    def findRoot(self):
        for i in range(self.nx):
            for j in range(self.ny):
                if self.grid[i][j] == 1:
                    root = (i, j)
                if self.grid[i][j] != -1:
                    self.p += 1
        return root
    def findVal(self, node):
        val = []
        if node.node[0] == 0:
            x = [1]
        elif node.node[0] == self.nx-1:
            x = [self.nx-2]
        else:
            x = [node.node[0]+1, node.node[0]-1]
        if self.nx == 1:
            x = []
        if node.node[1] == 0:
            y = [1]
        elif node.node[1] == self.ny-1:
            y = [self.ny-2]
        else:
            y = [node.node[1]+1, node.node[1]-1]
        if self.ny == 1:
            y = []
        for xi in x:
            if self.grid[xi][node.node[1]] != -1 and not (xi, node.node[1]) in node.visited:
                    val.append((xi, node.node[1]))
        for yi in y:
            if self.grid[node.node[0]][yi] != -1 and not (node.node[0], yi) in node.visited:
                    val.append((node.node[0], yi))
        return val
    def search(self, node):
        # print(node.node, node.visited)
        node.visited.append(node.node)
        val = self.findVal(node)
        #print(val)
        if not val:
            print('empty val', node.node, node.visited)
            return
        for v in val:
            if self.grid[v[0]][v[1]] == 2:
                if len(node.visited) == self.p-1:
                    print("succeed!", node.visited)
                    self.count += 1
            else:
                newNode = Node(node.visited, v)
                self.search(newNode)

    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.grid = grid
        self.nx = len(grid)
        self.ny = len(grid[0])
        self.count = 0
        self.p = 0
        root = Node([], self.findRoot())
        self.search(root)
        print(self.p)
        print(self.count)
        return self.count