import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from grc import grc

disp_information = False

# n = 10
# G = nx.random_tree(n=n, seed=57)

G = nx.read_gexf('data/G10_tree.gexf')

pos = nx.spring_layout(G, seed=73)

plt.figure()
nx.draw_networkx(G, pos=pos, node_color="lightblue")
plt.show()

reds = plt.get_cmap('Reds')

newcolors = reds(np.linspace(0.25, 1.0, 256))
cmap = ListedColormap(newcolors)

for gamma in [0.1,1,10]:
    
    I_grc = grc(G, gamma=gamma)
    
    plt.figure()
    if disp_information:
        plt.title('gamma='+str(gamma))
    nx.draw_networkx(G, pos, with_labels=False, node_size=200,
                     node_color=list(I_grc.values()), cmap=cmap)
    plt.savefig('results/tree_GRC_gamma_'+str(gamma)+'.pdf', bbox_inches='tight')
    #plt.savefig('results/tree_GRC_gamma_'+str(gamma)+'.eps', bbox_inches='tight')
    plt.show()
    
    sorted_centrality = {}
    sorted_keys = sorted(I_grc, key=I_grc.get)
    
    for w in sorted_keys:
        sorted_centrality[w] = I_grc[w]
    
    sorted_nodes = []
    for node in sorted_centrality.keys():
        sorted_nodes.append(node)
    
    height = list(sorted_centrality.values())
    
    plt.figure()
    if disp_information:
        plt.title('gamma='+str(gamma))
        plt.xlabel("nodes")
        plt.ylabel("centrality")
    plt.xticks(range(len(G)), sorted_nodes)
    plt.plot(range(len(G)), height, 'k', lw=1.2, zorder=1)
    plt.scatter(range(len(G)), height, s=100, c=height, cmap=cmap, zorder=2)
    #plt.grid("on")
    plt.savefig('results/tree_GRC_signature_gamma_'+str(gamma)+'.pdf', bbox_inches='tight')
    #plt.savefig('results/tree_GRC_signature_gamma_'+str(gamma)+'.eps', bbox_inches='tight')
    plt.show()
