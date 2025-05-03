class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def add_edges(self, edges):
        for edge in edges:
            self.graph.append(edge)

    def add_edge(self, start, end, w):
        self.graph.append([start, end, w])

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        print(f'  {i} ----- parent = {parent[i]}')
        return parent[i]

    def union(self, parent, rank, x, y):
        print(f'\n-- union --')
        print(f'    x: node[{x}] | parent = {parent[x]} | rank = {rank[x]} | parent_rank = {rank[parent[x]]}')
        print(f'    y: node[{y}] | parent = {parent[y]} | rank = {rank[y]} | parent_rank = {rank[parent[y]]}')
        if(rank[x] <  rank[y]):
            parent[x] = y
        elif(rank[x] > rank[y]):
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1
        print(f'    x: node[{x}] | parent = {parent[x]} | rank = {rank[x]} | parent_rank = {rank[parent[x]]}')
        print(f'    y: node[{y}] | parent = {parent[y]} | rank = {rank[y]} | parent_rank = {rank[parent[y]]}')


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
            print(f'\n==== edge_index = {index} | x: {x}  y: {y} ====')


            print(f'-- find x_root --')
            x_root = self.find(parent, x)

            print(f'-- find y_root --')
            y_root = self.find(parent, y)

            if (x_root != y_root):
                result.append(next_edge)
                self.union(parent, rank, x_root, y_root)

        print(f'\nAll nodes: ')
        for i in range(len(result)):
            print(f"---- node: {i} | parent: {parent[i]} | rank: {rank[i]}")

        return result
            

def main():

    
    edges_1 = [[0, 1, 1], [0, 2, 3], [1, 2, 3], [1, 3, 6], [2, 3, 4], [2, 4, 2], [3, 4, 5] ] 
    # g.add_edges(edges_1)

    edges_2 = [
            [3, 4, 2],
            [1, 4, 6],
            [0, 2, 8],
            [1, 2, 3],
            [3, 5, 2],
            [2, 3, 3],
            [4, 5, 5],
            [2, 4, 4],
            [0, 1, 7],
            # [1, 3, 1],
            ]

    g = Graph(6)
    g.add_edges(edges_2)

    result = g.kruskal_MST()
    print("\n== Result ==")
    g.show_graph(result)


main()

# output 
# === original graph ===
#     3 <---> 4 | weight: 2
#     1 <---> 4 | weight: 6
#     0 <---> 2 | weight: 8
#     1 <---> 2 | weight: 3
#     3 <---> 5 | weight: 2
#     2 <---> 3 | weight: 3
#     4 <---> 5 | weight: 5
#     2 <---> 4 | weight: 4
#     0 <---> 1 | weight: 7
#
# === sorted graph ===
#     3 <---> 4 | weight: 2
#     3 <---> 5 | weight: 2
#     1 <---> 2 | weight: 3
#     2 <---> 3 | weight: 3
#     2 <---> 4 | weight: 4
#     4 <---> 5 | weight: 5
#     1 <---> 4 | weight: 6
#     0 <---> 1 | weight: 7
#     0 <---> 2 | weight: 8
#
#
# ==== edge_index = 0 | x: 3  y: 4 ====
# -- find x_root --
#   3 ----- parent = 3
# -- find y_root --
#   4 ----- parent = 4
#
# -- union --
#     x: node[3] | parent = 3 | rank = 0 | parent_rank = 0
#     y: node[4] | parent = 4 | rank = 0 | parent_rank = 0
#     x: node[3] | parent = 3 | rank = 1 | parent_rank = 1
#     y: node[4] | parent = 3 | rank = 0 | parent_rank = 1
#
# ==== edge_index = 1 | x: 3  y: 5 ====
# -- find x_root --
#   3 ----- parent = 3
# -- find y_root --
#   5 ----- parent = 5
#
# -- union --
#     x: node[3] | parent = 3 | rank = 1 | parent_rank = 1
#     y: node[5] | parent = 5 | rank = 0 | parent_rank = 0
#     x: node[3] | parent = 3 | rank = 1 | parent_rank = 1
#     y: node[5] | parent = 3 | rank = 0 | parent_rank = 1
#
# ==== edge_index = 2 | x: 1  y: 2 ====
# -- find x_root --
#   1 ----- parent = 1
# -- find y_root --
#   2 ----- parent = 2
#
# -- union --
#     x: node[1] | parent = 1 | rank = 0 | parent_rank = 0
#     y: node[2] | parent = 2 | rank = 0 | parent_rank = 0
#     x: node[1] | parent = 1 | rank = 1 | parent_rank = 1
#     y: node[2] | parent = 1 | rank = 0 | parent_rank = 1
#
# ==== edge_index = 3 | x: 2  y: 3 ====
# -- find x_root --
#   1 ----- parent = 1
#   2 ----- parent = 1
# -- find y_root --
#   3 ----- parent = 3
#
# -- union --
#     x: node[1] | parent = 1 | rank = 1 | parent_rank = 1
#     y: node[3] | parent = 3 | rank = 1 | parent_rank = 1
#     x: node[1] | parent = 1 | rank = 2 | parent_rank = 2
#     y: node[3] | parent = 1 | rank = 1 | parent_rank = 2
#
# ==== edge_index = 4 | x: 2  y: 4 ====
# -- find x_root --
#   1 ----- parent = 1
#   2 ----- parent = 1
# -- find y_root --
#   1 ----- parent = 1
#   3 ----- parent = 1
#   4 ----- parent = 1
#
# ==== edge_index = 5 | x: 4  y: 5 ====
# -- find x_root --
#   1 ----- parent = 1
#   4 ----- parent = 1
# -- find y_root --
#   1 ----- parent = 1
#   3 ----- parent = 1
#   5 ----- parent = 1
#
# ==== edge_index = 6 | x: 1  y: 4 ====
# -- find x_root --
#   1 ----- parent = 1
# -- find y_root --
#   1 ----- parent = 1
#   4 ----- parent = 1
#
# ==== edge_index = 7 | x: 0  y: 1 ====
# -- find x_root --
#   0 ----- parent = 0
# -- find y_root --
#   1 ----- parent = 1
#
# -- union --
#     x: node[0] | parent = 0 | rank = 0 | parent_rank = 0
#     y: node[1] | parent = 1 | rank = 2 | parent_rank = 2
#     x: node[0] | parent = 1 | rank = 0 | parent_rank = 2
#     y: node[1] | parent = 1 | rank = 2 | parent_rank = 2
#
# All nodes: 
# ---- node: 0 | parent: 1 | rank: 0
# ---- node: 1 | parent: 1 | rank: 2
# ---- node: 2 | parent: 1 | rank: 0
# ---- node: 3 | parent: 1 | rank: 1
# ---- node: 4 | parent: 1 | rank: 0
#
# == Result ==
#     3 <---> 4 | weight: 2
#     3 <---> 5 | weight: 2
#     1 <---> 2 | weight: 3
#     2 <---> 3 | weight: 3
#     0 <---> 1 | weight: 7
#
