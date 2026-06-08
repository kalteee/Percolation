from typing import List, Tuple
from src.unionfind import UnionFind

def largest_component_evolution(n: int, p_edges: List[Tuple[int, int, float]]) -> List[Tuple[float, int]]:
    """
    Simulate the evolution of largest component with adding new edges
    
    Args:
        n (int): The number of vertices on one side of the square.
        p_edges (List[Tuple[int, int, float]]): list of edges, where each edge is a  
                                                 (vertex1, vertex2, probability) tuple.
                                                
    Returns:
        List[Tuple[float, int]]: list of (p_value, max_component_size) size.
    """
    p_edges = sorted(p_edges, key=lambda x: x[2])
    num_vertices = n * n
    uf = UnionFind(num_vertices)
    result = []

    for edge in p_edges:
        a, b, parameter = edge
        uf.union(a, b)
        result.append((parameter, uf.get_maxsize()))

    return result
