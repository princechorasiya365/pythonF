import random


def generate_edges(num_nodes, num_edges):
    edges = set()

    while len(edges) < num_edges:
        a = random.randint(1, num_nodes)
        b = random.randint(1, num_nodes)

        if a != b and (a, b) not in edges and (b, a) not in edges:
            edges.add((a, b))

    return edges


num_nodes = 1000  # Change this to the desired number of nodes
num_edges = 2000  # Change this to the desired number of edges

edges = generate_edges(num_nodes, num_edges)

for edge in edges:
    print(f'{{{edge[0]},{edge[1]}}}')
