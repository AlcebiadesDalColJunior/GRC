import numpy as np
import networkx as nx

from scipy.sparse.linalg import eigsh

def grc(G, gamma=1, signal=None):
    """Compute the graph regularization centrality for nodes.

    Parameters
    ----------
    G : graph
      A networkx graph

    Returns
    -------
    nodes : dictionary
       Dictionary of nodes with graph regularization centrality as the value.
    """
    
    n = len(G)
    
    L = nx.laplacian_matrix(G)
    
    gr = graph_regularization(L, gamma)
    
    centrality = np.zeros((n,))
    for i in range(n):
        fn = np.zeros((n,))
        
        if signal is None:
            fn[i] = 1
        else:
            fn[i] = 1 * signal[i]
        
        fn_smooth = gr.transform(fn)
        
        if signal is None:
            centrality[i] = 1 / fn_smooth[i]
        else:
            centrality[i] = fn_smooth[i]
        
    I_centrality = {node_i:centrality[i] for i, node_i in enumerate(G.nodes)}
    
    return(I_centrality)


class graph_regularization():
    def __init__(self, L, gamma):
        self.M = 10
        
        self.L = L.asfptype()
        self.N = (self.L).shape[0]
        
        self.lmax = eigsh(self.L, k=1, which='LA', return_eigenvectors=False,
                          tol=1e-08, maxiter=1e8)[0]
        self.alpha = self.lmax / 2
        
        self.g = filter_design(gamma)
        
        self.c = cheby_coeff(self.g, self.M, self.alpha)
        
    def transform(self, f):
        pol = cheby_pol(self.L, f, self.M, self.alpha)
        
        f0 = np.zeros((self.N,))
        for i in range(self.N):
            sm = 0
            sm += 0.5 * self.c[0] * f[i]
            
            for k in range(1,self.M):
                sm += self.c[k] * pol[k][i]

            f0[i] = sm
            
        return(f0)
    
def filter_design(gamma):
    filters = lambda x:1/(1+gamma*x)
    
    return(filters)

def cheby_coeff(g, m, alpha):
    N = m + 1
    arange = [0, 2*alpha]
    
    a1 = (arange[1]-arange[0]) / 2
    a2 = (arange[1]+arange[0]) / 2
    
    c = np.zeros((m,))
    for j in range(1,m+1):
        I = np.arange(1,N+1)
        c[j-1] = np.sum(np.multiply(g(a1*np.cos((np.pi*(I-0.5))/N)+a2),np.cos(np.pi*(j-1)*(I-0.5)/N)))*2/N
        
    return(c)

def cheby_pol(L, f, M, alpha):
    pol = []
    pol.append(f)
    pol.append((1/alpha)*L.dot(f)-f)

    for k in range(2,M):
        Lpol = L.dot(pol[k-1])
        pol.append((2/alpha)*Lpol-2*pol[k-1]-pol[k-2])

    return(pol)
