
from src.graph import generate_edges

def test_generate_edges() -> None:
    """Small test for the number of edges and edge-duplication"""
    n = 5
    edges = list(generate_edges(n))
    unique_edges = set(edges)
    expected_edge_count = 2 * n * (n - 1)

    assert len(edges) == expected_edge_count, f"Expected number of edges: {expected_edge_count}, actual: {len(edges)}"
    assert len(edges) == len(unique_edges), "There are duplicate generated edges."
