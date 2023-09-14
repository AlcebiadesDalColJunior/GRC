import numpy as np
import networkx as nx

def gravity_centrality(G):
    """Compute the gravity centrality for nodes.

    Parameters
    ----------
    G : graph
      A networkx graph

    Returns
    -------
    nodes : dictionary
       Dictionary of nodes with gravity centrality as the value.
    """
    
    n = len(G)
    
    degrees = nx.degree_centrality(G)
    
    for key in degrees:
        degrees[key] *= (n-1)
    
    centrality = np.zeros((n,))
    for i,nodei in enumerate(G.nodes):
        for nodej in G.nodes:
            if nodei != nodej:
                dij = nx.shortest_path_length(G, source=nodei, target=nodej)
                centrality[i] += (degrees[nodei] * degrees[nodej]) / (dij * dij)
        
    I_centrality = {node_i:centrality[i] for i, node_i in enumerate(G.nodes)}
    
    return(I_centrality)
