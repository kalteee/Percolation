from src.graph import generate_edges

def test_generate_edges(grid_size: int) -> None:
    """
    Testing the number of edges if the gridsize is given, and testing for duplicate edges.
    """
    n = grid_size
    print(f"\nruninng test with grid side size n={n}...") 

    edges = list(generate_edges(n))
    unique_edges = set(edges)

    expected_edge_count = 2 * n * (n - 1)

    assert len(edges) == expected_edge_count, f"Expected number of edges: {expected_edge_count}, actual: {len(edges)}"
    assert len(edges) == len(unique_edges), "There is duplication between the generated edges."
