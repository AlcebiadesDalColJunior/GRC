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
#print()

plt.figure()
nx.draw_networkx(G, pos=pos, with_labels=False, node_size=20)
plt.axis('equal')
plt.show()

reds = plt.get_cmap('Reds')

newcolors = reds(np.linspace(0.25, 1.0, 256))
cmap = ListedColormap(newcolors)

th = 450

node_color = ['w' for j in range(n)]

for gamma in [0.1,1,10]:
    
    I_grc = grc(G, gamma=gamma)
    
    sorted_centrality = {}
    sorted_keys = sorted(I_grc, key=I_grc.get)
    
    for w in sorted_keys:
        sorted_centrality[w] = I_grc[w]
    
    sorted_nodes = []
    for node in sorted_centrality.keys():
        sorted_nodes.append(node)
    
    height = list(sorted_centrality.values())
    
    vmin = min(height)
    vmax = max(height)
    
    plt.figure()
    if disp_information:
        plt.title("GRC"+'  gamma='+str(gamma))
        plt.xlabel("nodes")
        plt.ylabel("centrality")
    #if i == 0:
    #    plt.gca().yaxis.set_major_formatter(plt.FormatStrFormatter('%.1f'))
    #if i == 1:
    #    height = 10 * np.array(height)
    #if i == 2:
    #    height = 100 * np.array(height)
    plt.xticks([])
    plt.plot(range(len(G)), height, 'k', lw=1.2, zorder=1)
    #plt.scatter(range(len(G)), height, s=20, c='w', cmap=cmap, zorder=2)
    plt.scatter(range(th,len(G)), height[th:], s=20, c=height[th:], vmin=vmin, vmax=vmax, cmap=cmap, zorder=2)
    #plt.scatter(range(th), height[:th], s=20, c=height[:th], cmap=cmap, zorder=2)
    plt.savefig('results/sensor_GRC_threshold_'+str(500-th)+'_gamma_'+str(gamma)+'_signature.pdf', bbox_inches='tight')
    #plt.savefig('results/sensor_GRC_threshold_'+str(500-th)+'_gamma_'+str(gamma)+'_signature.eps', bbox_inches='tight')
    plt.show()
    
    G_th = nx.empty_graph()
    G_th.add_nodes_from(sorted_nodes[th:])
    #G_th.add_nodes_from(sorted_nodes[:th])
    
    vmin = min(height)
    vmax = max(height)
    
    plt.figure()
    if disp_information:
        plt.title("GRC"+'  gamma='+str(gamma))
    nx.draw_networkx(G, pos, node_color=node_color, node_size=20, with_labels=False, cmap=cmap)
    nx.draw_networkx(G_th, pos, node_color=height[th:], node_size=20,vmin=vmin, vmax=vmax, with_labels=False, cmap=cmap)
    #nx.draw_networkx(G_th, pos, node_color=height[:th], node_size=20,vmin=vmin, vmax=vmax, with_labels=False, cmap=cmap)
    plt.axis('equal')
    plt.savefig('results/sensor_GRC_threshold_'+str(500-th)+'_gamma_'+str(gamma)+'.pdf', bbox_inches='tight')
    #plt.savefig('results/sensor_GRC_threshold_'+str(500-th)+'_gamma_'+str(gamma)+'.eps', bbox_inches='tight')
    plt.show()
    