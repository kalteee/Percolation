from typing import List, Tuple
import matplotlib.pyplot as plt
from src.graph import add_parameters
from src.percolation import largest_component_evolution

def plot_graph(n: int, edges_with_parameters: List[Tuple[int, int, float]]) -> None:
    """
    Plots the grid with the id. of vertices and the weights of the edges.
    """
    vertices = [(i, j) for i in range(n) for j in range(n)]
    vertex_codes = [i * n + j for i in range(n) for j in range(n)]

    for v, code in zip(vertices, vertex_codes):
        plt.text(v[0],v[1], str(code), color='blue', ha='center', va='center', fontweight='bold')

    for edge_with_parameter in edges_with_parameters:
        edge = edge_with_parameter[:2]
        parameter = edge_with_parameter[2]
        v = (edge[0] % n, n - 1 - edge[0] // n)
        w = (edge[1] % n, n - 1 - edge[1] // n)
        
        plt.plot([v[1], w[1]], [n - 1 - v[0], n - 1 - w[0]], 'k-', lw=2)
        plt.text((v[1] + w[1]) / 2, (n - 1 - v[0] + n - 1 - w[0]) / 2, f'{parameter:.2f}', color='red', ha='center', va='center')
   
    plt.xticks(range(n))
    plt.yticks(range(n))
    plt.grid(True)
    plt.savefig("images/grid.png")
    plt.show()

def plot_func(n: int) -> None:
    """
    Runs a simulation, then plots the relative size of the maximal cardinality component (f(p))
    as a function of (p). Shows the theoretical treshold p_c = 0.5. For further information see README. 
    """
    edges_with_parameters = list(add_parameters(n))

    result_series = largest_component_evolution(n, edges_with_parameters)

    p_values, max_sizes = zip(*result_series)

    f_values = [max_size / (n**2) for max_size in max_sizes]
 
    plt.figure(figsize=(10, 6))
    plt.plot(p_values, f_values, marker='o', linestyle='-', color='b', markersize=2, label='Simulation')
 
    plt.axvline(x=0.5, color='r', linestyle='--', label='$p_c = 0.5$')
    plt.xlabel('p (Parameter / probability)')
    plt.ylabel('f(p) (ratio of largest component size)')
    plt.title(f'evolution of the size of maximal cardinality component (n={n})')
    plt.legend()
    plt.grid(True)
    plt.savefig("images/simulation.png")
    plt.show()
