import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from grc import graph_regularization

# n = 20
# G = nx.random_tree(n=n)

G = nx.read_gexf('data/G20_tree.gexf')

pos = nx.spring_layout(G, seed=22)

n = len(G)

Fn_smooth = np.zeros((n,n))

signal = None

n = len(G)

L = nx.laplacian_matrix(G)

gr = graph_regularization(L, gamma=1)

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
    
    Fn_smooth[:,i] = fn_smooth
    
I_centrality = {node_i:centrality[i] for i, node_i in enumerate(G.nodes)}


#%% Visualization of results

vmin = 0
vmax = 1

cmap = plt.get_cmap('Greens')
colors = cmap(np.linspace(0.1, 1.0, 256))
cmap = ListedColormap(colors)

for i in [1,0]:
    fn = np.zeros((n,))
    
    fn[i] = 1
    
    plt.figure()
    nx.draw_networkx(G, pos, node_color=fn, node_size=200, vmin=vmin, vmax=vmax,
                     with_labels=False, cmap=cmap)
    plt.savefig('results/tree_delta_'+str(i)+'.pdf', bbox_inches='tight')
    #plt.savefig('results/tree_delta_'+str(i)+'.eps', bbox_inches='tight')
    plt.show()

    
    plt.figure()
    nx.draw_networkx(G, pos, node_color=Fn_smooth[:,i], node_size=200, vmin=vmin,
                      vmax=vmax, with_labels=False, cmap=cmap)
    plt.savefig('results/tree_smooth_delta_'+str(i)+'.pdf', bbox_inches='tight')
    #plt.savefig('results/tree_smooth_delta_'+str(i)+'.eps', bbox_inches='tight')
    plt.show()
    
print("Importance of node i:",round(I_centrality[str(1)], 4))
print("Importance of node j:",round(I_centrality[str(0)], 4))

