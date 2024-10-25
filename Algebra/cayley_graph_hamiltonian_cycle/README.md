# Cayley Graph Visualizer and Analyzer

This Python script provides tools to generate, visualize, and analyze Cayley graphs, particularly focusing on properties such as Hamiltonian cycles. Cayley graphs are useful in group theory for studying the structure and relationships of elements within a group. The script also allows you to visualize generator paths and verify the existence of Hamiltonian cycles.

## Algorithm Definition

The Cayley graph generation algorithm in this script is designed to construct a graph that represents the structure of a group based on a set of generators. Here is a detailed step-by-step explanation of how it works, with references to the corresponding code:

### Cayley Graph Generation (`cayley_graph(group, generators)`)
1. **Initialize Nodes and Edges**:
   - In the function `cayley_graph(group, generators)`, a dictionary `G` is created where each key represents an element of the group, and the value is an empty list that will store the neighbors of that node. Another dictionary, `edges_by_generator`, is initialized to keep track of edges for each generator. This setup can be seen in the following lines of code:
     ```python
     G = {g: [] for g in group}  # save neighbors for each node
     edges_by_generator = {gen: [] for gen in generators}  # edges
     ```

2. **Add Edges Using Generators**:
   - The script iterates over each element (`g`) in the group and applies each generator (`s`) to determine the neighboring element (`h`). The operation `(g + s) % len(group)` ensures that the resulting element stays within the group, creating a circular structure. If the neighbor (`h`) is not already present in the list of neighbors for `g`, it is added to avoid duplicates. This is shown in the following code snippet:
     ```python
     for g in group:
         for s in generators:
             h = (g + s) % len(group)  # mod +
             if h not in G[g]:
                 G[g].append(h)
             if (g, h) not in edges_by_generator[s] and (h, g) not in edges_by_generator[s]:
                 edges_by_generator[s].append((g, h))  # save edges
     ```
   - This ensures that each node is connected to its neighbors based on the given generators, and that each edge is recorded only once for each generator.

3. **Avoid Duplicate Edges**:
   - To avoid creating duplicate edges, the script checks if an edge already exists between two nodes before adding it to `edges_by_generator`. This prevents redundant connections and ensures that each edge is represented only once in the graph.

### Hamiltonian Cycle Detection (`has_hamiltonian_cycle(G)`)
The Hamiltonian cycle detection algorithm is implemented using a backtracking approach. Here is how it works:

1. **Define the Backtracking Function**:
   - The function `has_hamiltonian_cycle(G)` defines a nested function `backtrack(path)` which recursively attempts to construct a path that visits every node exactly once. The initial call starts with each possible node in the graph:
     ```python
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
     ```

2. **Recursive Exploration**:
   - The `backtrack` function keeps adding nodes to the current path until all nodes are visited. If the path returns to the starting node, forming a cycle, it prints the Hamiltonian cycle. If no valid cycle is found from the current path, it backtracks and tries a different route.

3. **Start from Each Node**:
   - The function attempts to start the Hamiltonian cycle from each node in the graph (`for start_node in nodes:`). If a cycle is found, it returns `True`, otherwise, it continues until all nodes have been tried:
     ```python
     for start_node in nodes:
         if backtrack([start_node]):
             return True
     print("No Hamiltonian cycle found.")
     return False
     ```

This backtracking approach, while simple and intuitive, is not the most efficient for large graphs as the number of possible paths grows exponentially with the size of the graph. However, it works well for small groups and provides a clear method for determining whether a Hamiltonian cycle exists.

### Summary
- **Graph Construction**: Nodes represent group elements, and edges are formed by applying generators.
- **Edge Coloring**: Each generator defines a distinct set of edges, which are stored separately and visualized with unique colors.
- **Cycle Detection**: The Hamiltonian cycle detection uses backtracking to explore all possible paths, ensuring that each node is visited exactly once before returning to the start.
- **Code References**: The core functions are `cayley_graph(group, generators)` for graph generation and `has_hamiltonian_cycle(G)` for cycle detection, with each step carefully designed to construct and analyze the Cayley graph effectively.

The Cayley graph generation algorithm in this script takes a group and a set of generators as input, and constructs a graph where each node represents an element of the group. The edges represent the application of generators to the group elements. Specifically:

1. **Initialize Nodes and Edges**: Create nodes for each element of the group, and initialize empty lists to store neighbors and edges for each generator.
2. **Add Edges Using Generators**: For each group element, apply each generator to determine the neighboring element, using modulo operations to ensure all elements remain within the group. This results in the graph edges connecting group elements.
3. **Avoid Duplicate Edges**: Ensure that edges are not duplicated by checking if an edge already exists between two nodes.

The Hamiltonian cycle detection is performed using a backtracking approach, which attempts to visit all nodes exactly once, starting from each node in the graph and recursively exploring potential paths until a cycle is found or all options are exhausted.

## Features

1. **Cayley Graph Generation**: The function `cayley_graph(group, generators)` generates the Cayley graph for a given group and its generators.
2. **Graph Visualization with Colored Edges**: The function `draw_graph_with_colored_edges(G, edges_by_generator)` visualizes the Cayley graph using `matplotlib` and `networkx`, with edges colored according to their corresponding generators.
3. **Generator Path Representation**: The function `print_generator_paths_text(generators, group_size)` prints a textual representation of the paths generated by each generator.
4. **Hamiltonian Cycle Detection**: The function `has_hamiltonian_cycle(G)` checks if a Hamiltonian cycle exists in the given Cayley graph and displays the result.

## Requirements

- Python 3.x
- `matplotlib`
- `networkx`

You can install the dependencies using the following command:

```sh
pip install matplotlib networkx
```

## Usage

1. **Define the Group and Generators**: Define a group as a list of elements and the corresponding generators. For example:

    ```python
    group = list(range(4))  # Group elements: 0, 1, 2, 3
    generators = [1, 2]  # Generators
    ```

2. **Generate the Cayley Graph**: Use the `cayley_graph(group, generators)` function to generate the graph representation.

3. **Visualize the Graph**: Call `draw_graph_with_colored_edges(G, edges_by_generator)` to draw the Cayley graph with different colors for each generator's edges.

4. **Print Generator Paths**: Use `print_generator_paths_text(generators, len(group))` to print the paths generated by each generator.

5. **Hamiltonian Cycle Detection**: Use `has_hamiltonian_cycle(G)` to check if a Hamiltonian cycle exists in the graph.

## Example

The following example demonstrates how to use the script:

```python
# Define the group and generators
group = list(range(4))  # Group elements: 0, 1, 2, 3
generators = [1, 2]  # Generators

# Generate Cayley graph
G, edges_by_generator = cayley_graph(group, generators)

# Visualize Cayley graph with colored edges
draw_graph_with_colored_edges(G, edges_by_generator)

# Print generator paths
print_generator_paths_text(generators, len(group))

# Check for Hamiltonian cycle
has_hamiltonian_cycle(G)
```

## Output

- **Graph Visualization**: A circular graph with nodes and edges is drawn, with different colors representing different generators.
- **Generator Paths**: Textual representation of each generator's path through the group.
- **Hamiltonian Cycle Detection**: Prints whether a Hamiltonian cycle exists, along with the cycle itself if found.

## Notes

- This script currently works with additive groups modulo the size of the group. You can modify the group operations as needed for different types of groups.
- The Hamiltonian cycle detection is implemented using a backtracking algorithm, which may not be efficient for large groups.

## License

This project is licensed under the MIT License. Feel free to modify and use it for your own projects.

## Contributions

Contributions, issues, and feature requests are welcome! Feel free to open an issue or create a pull request.

