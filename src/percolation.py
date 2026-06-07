from src.unionfind import UnionFind
def largest_component_evolution(n, p_edges):
   
    p_edges = sorted(p_edges, key=lambda x: x[2])
    num_vertices = n * n
    uf = UnionFind(num_vertices)
    result = []

    for edge in p_edges:
        a, b, parameter = edge
        uf.union(a, b)
        result.append((parameter, uf.get_maxsize()))

    return result
