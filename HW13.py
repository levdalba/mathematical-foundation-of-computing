import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# Experiment with different graphs
G = nx.erdos_renyi_graph(10, 0.5, seed=1)
adjacency_matrix = nx.to_numpy_array(G)
out_degrees = np.sum(adjacency_matrix, axis=1)
markov_matrix = np.zeros(adjacency_matrix.shape)
for i in range(adjacency_matrix.shape[0]):
    for j in range(adjacency_matrix.shape[1]):
        markov_matrix[i][j] = adjacency_matrix[i][j] / out_degrees[i]
markov_matrix = np.transpose(markov_matrix)

# Initialize rank vector
pagerank = np.ones(markov_matrix.shape[0]) / markov_matrix.shape[0]

# Power iteration with damping factor
damping_factor = 0.85
epsilon = 1e-8  # Convergence threshold
delta = 1  # Change in rank vector
while delta > epsilon:
    new_pagerank = damping_factor * np.dot(markov_matrix, pagerank) + (
        1 - damping_factor
    ) / len(pagerank)
    delta = np.abs(new_pagerank - pagerank).sum()  # Calculate change
    pagerank = new_pagerank

# Normalize
pagerank /= np.sum(pagerank)

print("PageRank for Erdos-Renyi graph:", pagerank)

# Draw the graph with node sizes proportional to PageRank
plt.figure(figsize=(8, 6))
nx.draw(G, with_labels=True, node_size=[50000 * i for i in pagerank])
plt.show()
