import matplotlib.pyplot as plt
import networkx as nx

# cayley graph
def cayley_graph(group, generators):
    G = {g: [] for g in group}  # save neighbors for each node
    edges_by_generator = {gen: [] for gen in generators}  #edges
    for g in group:
        for s in generators:
            h = (g + s) % len(group)  # mod +
            if h not in G[g]:
                G[g].append(h)
            if (g, h) not in edges_by_generator[s] and (h, g) not in edges_by_generator[s]:
                edges_by_generator[s].append((g, h))  # save edges
    return G, edges_by_generator

# draw graph with colored edges
def draw_graph_with_colored_edges(G, edges_by_generator):
    plt.figure(figsize=(8, 6))
    pos = nx.circular_layout(G)
    colors = ['red', 'green', 'blue', 'purple', 'orange']
    nx_G = nx.Graph()
    for node, neighbors in G.items():
        for neighbor in neighbors:
            nx_G.add_edge(node, neighbor)
    
    # draw network nodes with different colors
    nx.draw(nx_G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=15)
    
    # draw network edges with different colors based on generators
    for i, (gen, edges) in enumerate(edges_by_generator.items()):
        nx.draw_networkx_edges(nx_G, pos, edgelist=edges, edge_color=colors[i % len(colors)], width=2, label=f'Generator {gen}')
    
    plt.show()

# print generator paths in textual representation
def print_generator_paths_text(generators, group_size):
    print("Generator paths (Textual representation):")
    for gen in generators:
        path = []
        current = 0  # start form Zer0
        for _ in range(group_size):
            next_node = (current + gen) % group_size
            path.append(f"{current}+{gen} > {next_node}")
            current = next_node
        path_representation = " > ".join(path)
        print(f"Generator {gen}: {path_representation}")

# Check if there exists a Hamiltonian cycle in the given Cayley graph.
def has_hamiltonian_cycle(G):
    nodes = list(G.keys())
    def backtrack(path):
        if len(path) == len(nodes):
            if path[0] in G[path[-1]]:
                print("Hamiltonian cycle exists:", path + [path[0]])
                return True
            return False
        current = path[-1]
        for neighbor in G[current]:
            if neighbor not in path:
                if backtrack(path + [neighbor]):
                    return True
        return False

    for start_node in nodes:
        if backtrack([start_node]):
            return True
    print("No Hamiltonian cycle found.")
    return False

# example usage
group = list(range(4))  
generators = [1 , 2]  

G, edges_by_generator = cayley_graph(group, generators)

draw_graph_with_colored_edges(G, edges_by_generator)

print_generator_paths_text(generators, len(group))

has_hamiltonian_cycle(G)
