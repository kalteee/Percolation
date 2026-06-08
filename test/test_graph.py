
from src.graph import generate_edges

def test_generate_edges():
    n = 5
    edges = set(generate_edges(n))

    assert len(edges) == 2 * n * (n - 1)
    assert len(edges) == len(set(edges)) 
