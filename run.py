import argparse
from src.graph import add_parameters
from src.percolation import largest_component_evolution
from src.plotting import plot_func

def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--n",
        type=int,
        default=100,
        help="Grid side length"
    )

    args = parser.parse_args()

    n = args.n

    print(f"Running simulation with n={n}")

    edges = list(add_parameters(n))

    result = largest_component_evolution(n, edges)

    plot_component_fraction(result, n)

if __name__ == "__main__":
    main()
