class Graph:
 
    def __init__(self, row, col, g):
        self.ROW = row
        self.COL = col
        self.graph = g
        self.islands = 0
 
    def MarkVisit(self, i, j): 
        self.graph[i][j] = "2"
        if i-1 >= 0 and self.graph[i-1][j] == "1":
            return self.MarkVisit(i-1, j)
        if j-1 >= 0 and self.graph[i][j-1] == "1":
            return self.MarkVisit(i, j-1)
        if i+1 < self.ROW and self.graph[i+1][j] == "1":
            return self.MarkVisit(i+1, j)
        if j+1 < self.COL and self.graph[i][j+1] == "1":
            return self.MarkVisit(i, j+1)

        if i-1 >= 0 and j-1 >= 0 and self.graph[i-1][j-1] == "1":
            return self.MarkVisit(i-1, j-1)
        if j-1 >= 0 and i+1 < self.ROW and self.graph[i+1][j-1] == "1":
            return self.MarkVisit(i+1, j-1)
        if i+1 < self.ROW and j+1 < self.COL and self.graph[i+1][j+1] == "1":
            return self.MarkVisit(i+1, j+1)
        if j+1 < self.COL and i-1 >= 0 and self.graph[i-1][j+1] == "1":
            return self.MarkVisit(i-1, j+1)
        return
 
    def countIslands(self):        
        for i in range(self.ROW):
            for j in range(self.COL):
                if self.graph[i][j] == "1":
                    self.MarkVisit(i, j)                    
                    self.islands += 1        
 

# graph = [[1, 1],
#          [1, 1]]

graph = [["1","1","0","0","0"],
         ["1","1","0","0","0"],
         ["0","0","1","0","0"],
         ["0","0","0","1","1"]]

# graph = [["1","1","1","1","0"],
#          ["1","1","0","1","0"],
#          ["1","1","0","0","0"],
#          ["0","0","0","0","0"]]

# graph = [[1, 1, 1, 0, 0],
#          [0, 1, 0, 0, 1],
#          [1, 0, 0, 1, 1],
#          [0, 0, 0, 0, 0],
#          [1, 0, 1, 0, 1]]
 
 
row = len(graph)
col = len(graph[0])
 
g = Graph(row, col, graph)
 
print("Number of islands is:")
g.countIslands()
print(g.islands)