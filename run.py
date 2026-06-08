from src.graph import add_parameters
from src.percolation import largest_component_evolution
from src.plotting import plot_func

def main():
    n = 100

    print(f"Running bond percolation on a {n}x{n} grid...")

    edges = list(add_parameters(n))

    result = largest_component_evolution(n, edges)

    print("Simulation finished.")
    print(f"Final largest component size: {result[-1][1]}")

    plot_component_fraction(result, n)

if __name__ == "__main__":
    main()
