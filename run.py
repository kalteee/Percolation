import argparse
from src.graph import add_parameters
from src.percolation import largest_component_evolution
from src.plotting import plot_func

def main() -> None:
    """Interface for the percolation simulation"""
    parser = argparse.ArgumentParser(description="2D grid percolation simulation")

    parser.add_argument(
        "--n",
        type=int,
        default=100,
        help="size of the side of the grid (initially: 100)"
    )

    args = parser.parse_args()
    n = args.n

    print(f"Starting simulation with n={n}... (Grid size: {n}x{n})")
    

    plot_func(n)
    print("Simulation terminated succesfully.")

if __name__ == "__main__":
    main()
