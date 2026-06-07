import matplotlib.pyplot as plt
def plot_graph(n, edges_with_parameters):
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
    plt.show()

def plot_func(n):
    edges_with_parameters = list(add_parameters(n))

    result_series = parameter_compsize(n, edges_with_parameters)


    p_values, max_sizes = zip(*result_series)

 
    n = 100
    f_values = [max_size / (n**2) for max_size in max_sizes]

 
    plt.plot(p_values, f_values, marker='o', linestyle='-', color='b')
    plt.xlabel('p')
    plt.ylabel('f(p)')
    plt.title('Plot of f(p) for n=100')
    plt.grid(True)
    plt.show()
