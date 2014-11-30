class Graph:
    def __init__(self, maps = [], nodenum = 0, edgenum = 0):
        self.map = maps       #ͼ�ľ���ṹ
        self.nodenum = len(maps)
        self.edgenum = edgenum
     #   self.nodenum = GetNodenum()#�ڵ���
     #  self.edgenum = GetEdgenum()#����

    def isOutRange(self, x):
        try :
            if x >= self.nodenum or x <= 0:
                raise  IndexError
        except IndexError:
            print("�ڵ��±����")

    def GetNodenum(self):
        self.nodenum = len(self.map)
        return self.nodenum

    def GetEdgenum(self):
        GetNodenum()
        self.edgenum = 0
        for i in range(self.nodenum):
            for j in range(self.nodenum):
                if self.map[i][j] is 1:
                    self.edgenum = self.edgenum + 1
        return self.edgenum

    def InsertNode(self):
        for i in range(self.nodenum):
            self.map[i].append(0)
        self.nodenum = self.nodenum + 1
        ls = [0] * self.nodenum
        self.map.append(ls)

    #��ɾ����ֻ�ǹ������
    def DeleteNode(self, x):
        for i in range(self.nodenum):
            if self.map[i][x] is 1:
                self.map[i][x] = 0
                self.edgenum = self.edgenum -1
            if self.map[x][i] is 1:
                self.map[x][i] = 0
                self.edgenum = self.edgenum - 1

    def AddEdge(self, x, y):
        if self.map[x][y] is 0:
            self.map[x][y] = 1
            self.edgenum = self.edgenum + 1

    def RemoveEdge(self, x, y):
        if self.map[x][y] is 0:
            self.map[x][y] = 1
            self.edgenum = self.edgenum + 1

    def BreadthFirstSearch(self):
        def BFS(self, i):
            print(i)
            visited[i] = 1
            for k in range(self.nodenum):
                if self.map[i][k] == 1 and visited[k] == 0:
                    BFS(self, k)

        visited = [0] * self.nodenum
        for i in range(self.nodenum):
            if visited[i] is 0:
                BFS(self, i)

    def DepthFirstSearch(self):
        def DFS(self, i, queue):

            queue.append(i)
            print(i)
            visited[i] = 1
            if len(queue) != 0:
                w = queue.pop()
                for k in range(self.nodenum):
                    if self.map[w][k] is 1 and visited[k] is 0:
                        DFS(self, k, queue)


        visited = [0] * self.nodenum
        queue = []
        for i in range(self.nodenum):
            if visited[i] is 0:
                DFS(self, i, queue)

def DoTest():
    maps = [
        [-1, 1, 0, 0],
        [0, -1, 0, 0],
        [0, 0, -1, 1],
        [1, 0, 0, -1]]
    G = Graph(maps)
    G.InsertNode()
    G.AddEdge(1, 4)
    print("������ȱ���")
    G.BreadthFirstSearch()
    print("������ȱ���")
    G.DepthFirstSearch()

if __name__ == '__main__':
    DoTest()