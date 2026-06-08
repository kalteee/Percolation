import argparse
from src.graph import add_parameters
from src.plotting import plot_graph

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=7)
    args = parser.parse_args()

    edges_with_parameters = list(add_parameters(args.n))
    plot_graph(args.n, edges_with_parameters)

if __name__ == "__main__":
    main()
