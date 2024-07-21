class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        graph_row = defaultdict(set)
        graph_col = defaultdict(set)
        
        for row in rowConditions:
            graph_row[row[0]].add(row[1])

        for col in colConditions:
            graph_col[col[0]].add(col[1])
        
        order_row = list()
        order_col = list()
        visited_row = defaultdict(bool)
        visited_col = defaultdict(bool)
        
        def dfs(i,v,o,g):
            if i in v:
                return v[i]

            v[i] = True
            for n in g[i]:
                if dfs(n,v,o,g):
                    return True
            v[i] = False
    
            o.append(i)

        for i in range(1,k+1):
            if dfs(i,visited_row, order_row,graph_row):
                return []

        for i in range(1,k+1):
            if dfs(i,visited_col,order_col ,graph_col):
                return []

        order_row.reverse() 
        order_col.reverse() 

        pos = [[0,0] for i in range(k+1)]

        for i,v in enumerate(order_row):
            pos[v][0] = i
        for i,v in enumerate(order_col):
            pos[v][1] = i
        
        res = [[0 for i in range(k)] for j in range(k)]

        for i,p in enumerate(pos):
            if i == 0:
                continue
            res[p[0]][p[1]] = i

        return res