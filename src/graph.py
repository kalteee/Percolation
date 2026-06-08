from typing import Iterator, Tuple
import numpy as np
def generate_edges(n: int) ->Iterator[Tuple[int, int]]:
    """
    Generating function for the edges of the grid. 
    Args:
        n (int): the size of the side of the grid. 
    Yields:
        Iterator[Tuple[int, int]]: edge as a pair of (vertex_id_1, vertex_id_2), where vertex_id_1 < vertex_id_2.
    """
    vertices = [(i, j) for i in range(n) for j in range(n)]
    visited = set()
    for v in vertices:
        v_code = v[0] * n + v[1]
        neighbors = [(v[0] + 1, v[1]), (v[0] - 1, v[1]), (v[0], v[1] + 1), (v[0], v[1] - 1)]
        for w in neighbors:
            if 0 <= w[1] < n and 0 <= w[0] < n:
                w_code = w[0] * n + w[1]
                edge = (min(v_code, w_code), max(v_code, w_code))  
                if edge not in visited:
                    visited.add(edge)
                    yield edge

def add_parameters(n: int) -> Iterator[Tuple[int, int, float]]:
    """
    Maps a uniformly distributed random value from [0,1) to every edge of the grid.

    Args:
        n (int): size of the side of the grid.
    Yields:
        Iterator[Tuple[int, int, float]]: A (vertex_id_1, vertex_id_2, probability) tuple.
    """
    edges_generator = generate_edges(n)
    for edge in edges_generator:
        parameter = np.random.uniform(0, 1)
        yield edge + (parameter,)
