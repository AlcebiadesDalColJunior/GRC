import numpy as np
import networkx as nx

from numpy.linalg import eigh

def gft_c(G):
    """Compute the graph Fourier transform centrality for nodes.

    Parameters
    ----------
    G : graph
      A networkx graph

    Returns
    -------
    nodes : dictionary
       Dictionary of nodes with graph Fourier transform centrality as the value.
    """
    
    # graph Fourier transform
    
    n = len(G)
    
    L = nx.linalg.laplacianmatrix.laplacian_matrix(G, weight=None)
    
    Lambda, U = eigh(L.toarray(), UPLO='U')
    
    centrality = np.zeros((n,))
    
    for i, node_i in enumerate(G.nodes):
        fn = np.zeros((n,))
        
        cost = nx.shortest_path_length(G, source=node_i, weight='weight')
        
        for j, node_j in enumerate(G.nodes):
            if j != i:
                fn[j] = 1/cost[node_j]
        
        fn /= np.sum(fn)
        
        fn[i] = 1
        
        fn_hat = np.matmul(U.T,fn)
        
        for j in range(n):
            centrality[i] += w(Lambda[j]) * np.abs(fn_hat[j]) 
    
    centrality /= np.sum(centrality)
    
    I_centrality = {node_i:centrality[i] for i, node_i in enumerate(G.nodes)}
    
    return(I_centrality)


def w(lambda_ell, k = 0.1):
    
    return(np.exp(k * lambda_ell) - 1)