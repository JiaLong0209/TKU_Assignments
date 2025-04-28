class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edge(self, start, end, w):
        self.graph.append([start, end, w])

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        print(f'-- union --')
        print(f'    x: subsets[{x}] | parent = {parent[x]} | rank = {rank[x]}')
        print(f'    y: subsets[{y}] | parent = {parent[y]} | rank = {rank[y]}')
        if(rank[x] <  rank[y]):
            parent[x] = y
        elif(rank[x] > rank[y]):
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1
        print(f'    x: subsets[{x}] | parent = {parent[x]} | rank = {rank[x]}')
        print(f'    y: subsets[{y}] | parent = {parent[y]} | rank = {rank[y]}')


    def show_graph(self, graph):
        for start, end, weight in graph:
            print(f'    {start} <---> {end} | weight: {weight}')
        print('')

    def kruskal_MST(self):

        result = []
        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)
            

        print(f'=== original graph ===')
        self.show_graph(self.graph)
        
        self.graph = sorted(self.graph, key=lambda items: items[2])

        print(f'=== sorted graph ===')
        self.show_graph(self.graph)

        for index, next_edge in enumerate(self.graph):
            if(len(result) == self.V-1):
                break

            x = next_edge[0] # start node
            y = next_edge[1] # end node

            x_root = self.find(parent, x)
            y_root = self.find(parent, y)

            if (x_root != y_root):
                result.append(next_edge)
                self.union(parent, rank, x_root, y_root)


        return result
            

def main():

    g = Graph(7)
    g.add_edge(0, 1, 1)
    g.add_edge(0, 2, 3)
    g.add_edge(1, 2, 3)
    g.add_edge(1, 3, 6)
    g.add_edge(2, 3, 4)
    g.add_edge(2, 4, 2)
    g.add_edge(3, 4, 5)

    result = g.kruskal_MST()
    print("\n== Result ==")
    g.show_graph(result)

main()


# output: 
# === original graph ===
#     0 <---> 1 | weight: 1
#     0 <---> 2 | weight: 3
#     1 <---> 2 | weight: 3
#     1 <---> 3 | weight: 6
#     2 <---> 3 | weight: 4
#     2 <---> 4 | weight: 2
#     3 <---> 4 | weight: 5
#
# === sorted graph ===
#     0 <---> 1 | weight: 1
#     2 <---> 4 | weight: 2
#     0 <---> 2 | weight: 3
#     1 <---> 2 | weight: 3
#     2 <---> 3 | weight: 4
#     3 <---> 4 | weight: 5
#     1 <---> 3 | weight: 6
#
# -- union --
#     x: subsets[0] | parent = 0 | rank = 0
#     y: subsets[1] | parent = 1 | rank = 0
#     x: subsets[0] | parent = 0 | rank = 1
#     y: subsets[1] | parent = 0 | rank = 0
# -- union --
#     x: subsets[2] | parent = 2 | rank = 0
#     y: subsets[4] | parent = 4 | rank = 0
#     x: subsets[2] | parent = 2 | rank = 1
#     y: subsets[4] | parent = 2 | rank = 0
# -- union --
#     x: subsets[0] | parent = 0 | rank = 1
#     y: subsets[2] | parent = 2 | rank = 1
#     x: subsets[0] | parent = 0 | rank = 2
#     y: subsets[2] | parent = 0 | rank = 1
# -- union --
#     x: subsets[0] | parent = 0 | rank = 2
#     y: subsets[3] | parent = 3 | rank = 0
#     x: subsets[0] | parent = 0 | rank = 2
#     y: subsets[3] | parent = 0 | rank = 0
#
# == Result ==
#     0 <---> 1 | weight: 1
#     2 <---> 4 | weight: 2
#     0 <---> 2 | weight: 3
#     2 <---> 3 | weight: 4
#
