import networkx as nx
from itertools import product
import sys
import matplotlib.pyplot as plt

# Increase recursion limit for larger graphs
sys.setrecursionlimit(1000000)

# Group orders
group_orders = (8, 3, 5)

# Generate group members
group = list(product(range(8), range(3), range(5)))

# Generators
generators = [
    (1, 0, 0),  # Generator for Z8
    (0, 1, 0),  # Generator for Z3
    (0, 0, 1)   # Generator for Z5
]

# Function to construct Cayley graph
def cayley_graph(group, generators, group_orders):
    G = nx.Graph()
    edges_by_generator = {gen: [] for gen in generators}
    for g in group:
        for s in generators:
            h = tuple(( (g_i + s_i) % n_i for g_i, s_i, n_i in zip(g, s, group_orders)))
            if g != h:  # Avoid self-loops
                G.add_edge(g, h)
                edges_by_generator[s].append((g, h))
    return G, edges_by_generator

# Construct Cayley graph
G, edges_by_generator = cayley_graph(group, generators, group_orders)

# Function to construct Hamiltonian cycle using a full backtracking approach
def hamiltonian_cycle_full_backtracking(G, start):
    path = [start]
    visited = set([start])

    def backtrack(current):
        if len(path) == len(G.nodes()):
            if G.has_edge(path[-1], start):
                path.append(start)
                return True
            else:
                return False

        for neighbor in G.neighbors(current):
            if neighbor not in visited:
                visited.add(neighbor)
                path.append(neighbor)

                if backtrack(neighbor):
                    return True

                # Backtrack to previous state
                visited.remove(neighbor)
                path.pop()

        return False

    if backtrack(start):
        return path
    else:
        return None

# Use full backtracking to find Hamiltonian cycle
start_node = (0, 0, 0)
hamiltonian_cycle = hamiltonian_cycle_full_backtracking(G, start_node)

# Verify and save Hamiltonian cycle
if hamiltonian_cycle and len(hamiltonian_cycle) == len(G.nodes()) + 1:
    print("Hamiltonian cycle found and verified.")

    # Print detailed stages of the cycle for better understanding
    print("Start of the cycle:")
    previous_x = hamiltonian_cycle[0][0]
    for idx, node in enumerate(hamiltonian_cycle):
        print(f"{idx + 1}. {node}")
        if idx < len(hamiltonian_cycle) - 1:
            next_x = hamiltonian_cycle[idx + 1][0]
            if next_x != previous_x:
                print(f"Continuation for x = {next_x}:")
            previous_x = next_x

    # Save cycle to file
    with open("hamiltonian_cycle.txt", "w") as f:
        for node in hamiltonian_cycle:
            f.write(f"{node}\n")

    print("Hamiltonian cycle saved to 'hamiltonian_cycle.txt'.")

    # Draw the entire graph
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray')
    nx.draw_networkx_edges(G, pos, edgelist=[(hamiltonian_cycle[i], hamiltonian_cycle[i + 1]) for i in range(len(hamiltonian_cycle) - 1)], edge_color='r', width=2)
    plt.title("Cayley Graph with Hamiltonian Cycle Highlighted")
    plt.show()
else:
    print("No Hamiltonian cycle exists.")
