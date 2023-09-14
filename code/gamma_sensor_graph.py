import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from grc import grc

disp_information = False

n = 500

if n == 500:
    kappa = 0.08
if n == 1000:
    kappa = 0.15

G = nx.random_geometric_graph(n, kappa, seed=896803)
pos = nx.get_node_attributes(G, "pos")

#print("Graphh connected:", nx.is_connected(G))

plt.figure()
nx.draw_networkx(G, pos=pos, with_labels=False, node_size=50)
plt.show()

reds = plt.get_cmap('Reds')

newcolors = reds(np.linspace(0.25, 1.0, 256))
cmap = ListedColormap(newcolors)

for gamma in [0.1,1,10]:
    I_grc = grc(G, gamma=gamma)
    
    # names = ["GRC"]
    # centralities = [I_grc]
    
    # i=0
        
    plt.figure()
    if disp_information:
        plt.title('gamma='+str(gamma))
    nx.draw_networkx(G, pos, node_color=list(I_grc.values()), node_size=50,
                      with_labels=False, cmap=cmap)
    #plt.axis("equal")
    plt.savefig('results/sensor_GRC_gamma_'+str(gamma)+'.pdf', bbox_inches='tight')
    #plt.savefig('results/sensor_GRC_gamma_'+str(gamma)+'.eps', bbox_inches='tight')
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
    plt.xticks([])
    plt.plot(range(len(G)), height, 'k', lw=1.2, zorder=1)
    plt.scatter(range(len(G)), height, s=25, c=height, cmap=cmap, zorder=2)
    plt.savefig('results/sensor_GRC_signature_gamma_'+str(gamma)+'.pdf',bbox_inches='tight')
    #plt.savefig('results/sensor_GRC_signature_gamma_'+str(gamma)+'.eps',bbox_inches='tight')
    plt.show()
