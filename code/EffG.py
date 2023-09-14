import numpy as np
import networkx as nx

def EffG(G, method="original", use_shortest_path=False, coefficient=0.05):
    """Compute the effective distance gravity centrality for nodes.

    Parameters
    ----------
    G : graph
      A networkx graph

    Returns
    -------
    nodes : dictionary
       Dictionary of nodes with effective distance gravity centrality as the value.
    """
    
    n = len(G)
    
    degrees = nx.degree_centrality(G)
    
    for key in degrees:
        degrees[key] *= (n-1)
    
    A = nx.adjacency_matrix(G)
    
    nodes = list(G.nodes)
    
    D = np.zeros((n,n))
    
    # Directly connected nodes
    for edge in G.edges:
        node0 = edge[0]
        node1 = edge[1]
        
        i = nodes.index(node0)
        j = nodes.index(node1)
        
        pij = A[j,i] / degrees[node1]
        D[i,j] = 1 - (np.log(pij)/np.log(2))
        
        pji = A[i,j] / degrees[node0]
        D[j,i] = 1 - (np.log(pji)/np.log(2))
        
    # Indirectly connected nodes
    for i,nodei in enumerate(G.nodes):
        for j,nodej in enumerate(G.nodes):
            if i != j:
                if (nodei,nodej) not in G.edges:
                    if method == "original":
                        paths = list(nx.all_simple_paths(G, source=nodei, target=nodej))
                        
                        distances = np.zeros((len(paths),))
                        for k,path in enumerate(paths):
                            for l in range(len(path)-1):
                                distances[k] += D[nodes.index(path[l]),nodes.index(path[l+1])]
                        
                        D[i,j] = np.min(distances)
                    if method == "shortest_path":
                        path = nx.shortest_path(G, source=nodei, target=nodej)
                        
                        for l in range(len(path)-1):
                                D[i,j] += D[nodes.index(path[l]),nodes.index(path[l+1])]
                    if method == "shortest_path_coefficient":
                        dij = nx.shortest_path_length(G, source=nodei, target=nodej)
                        cutoff = int((1+coefficient) * dij)
                        paths = list(nx.all_simple_paths(G, source=nodei, target=nodej, cutoff=cutoff))
                        
                        distances = np.zeros((len(paths),))
                        for k,path in enumerate(paths):
                            for l in range(len(path)-1):
                                distances[k] += D[nodes.index(path[l]),nodes.index(path[l+1])]
                        
                        D[i,j] = np.min(distances)
    
    centrality = np.zeros((n,))
    for i,nodei in enumerate(G.nodes):
        for j,nodej in enumerate(G.nodes):
            if i != j:
                centrality[i] += (degrees[nodei] * degrees[nodej]) / (D[j,i] * D[j,i])
    
    I_centrality = {node_i:centrality[i] for i, node_i in enumerate(G.nodes)}
    
    return(I_centrality)

if __name__ == "__main__":
    G = nx.Graph()

    edges = [(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),
             (2,5),(3,5),(4,5),(4,6)]
    
    G.add_edges_from(edges)
    
    #nx.draw_networkx(G, with_labels=True)
    
    A = nx.adjacency_matrix(G).toarray()
    print("A")
    print(A)
    print("")
    
    I_EffG = EffG(G)
    print("I_EffG")
    print(I_EffG)
    
    