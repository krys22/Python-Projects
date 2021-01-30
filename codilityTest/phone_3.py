N = 4
A = [1,2,4,4,3]
B = [2,3,1,4,1]


class Graph:
     
    def __init__(self, number):
         
        self.number = number
        self.graph = [[0 for j in range(self.number + 1)]
                     for i in range(self.number + 1)]
     
        for i in range(self.number + 1):
            self.graph[i][i] = 1
 
    def addEdges(self, first_array, second_array):
        self.graph[first_array][second_array] = 1
        self.graph[second_array][first_array] = 1
 
    def computePathsBetweenNodes(self):
        for k in range(1, self.number + 1):
            for i in range(1, self.number + 1):
                for j in range(1, self.number + 1):
                    self.graph[i][j] = (self.graph[i][j] | (self.graph[i][k] and self.graph[k][j]))
                     
    def isConnected(self, first, second):
 
        if (self.graph[first][second] == 1):
            return True
        else:
            return False

if __name__=='__main__':
 
    _g = Graph(4)
    _g.addEdge(1, 2)
    _g.addEdge(2, 3)
    _g.addEdge(1, 4)
    _g.computePaths()
 
    u = 4
    v = 3
     
    if (_g.isReachable(u, v)):
        print('Yes')
    else:
        print('No')



def solution(N,A,B):

