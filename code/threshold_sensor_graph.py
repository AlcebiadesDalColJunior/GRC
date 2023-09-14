import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from grc import grc
from gft_c import gft_c
from gravity_centrality import gravity_centrality
from EffG import EffG

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
#plt.savefig('results/sensor.pdf', bbox_inches='tight')
#plt.savefig('results/sensor.eps', bbox_inches='tight')
plt.show()

use_grc = True
use_degree = True
use_gft_c = True
use_betweenness = True
use_closeness = True
use_eigenvector = True

use_gravity_centrality = False
use_EffG = False

names = []
centralities = []

if use_grc:
    I_grc = grc(G)
    names.append("GRC")
    centralities.append(I_grc)

if use_degree:
    I_degree = nx.degree_centrality(G)
    names.append("DC")
    centralities.append(I_degree)

if use_gft_c:
    I_gft_c = gft_c(G)
    names.append("GFT-C")
    centralities.append(I_gft_c)

if use_betweenness:
    I_betweenness = nx.betweenness_centrality(G)
    names.append("BC")
    centralities.append(I_betweenness)

if use_closeness:
    I_closeness = nx.closeness_centrality(G)
    names.append("CC")
    centralities.append(I_closeness)

if use_eigenvector:
    I_eigenvector = nx.eigenvector_centrality(G)
    names.append("EC")
    centralities.append(I_eigenvector)

if use_gravity_centrality:
    I_gravity_centrality = gravity_centrality(G)
    names.append("GC")
    centralities.append(I_gravity_centrality)

if use_EffG:
    I_EffG = EffG(G)
    names.append("EffG")
    centralities.append(I_EffG)


#%% Visualization of results

n_names = len(names)

reds = plt.get_cmap('Reds')

newcolors = reds(np.linspace(0.25, 1.0, 256))
cmap = ListedColormap(newcolors)

th = 450

node_color = ['w' for j in range(n)]

for i in range(n_names):
    
    sorted_centrality = {}
    sorted_keys = sorted(centralities[i], key=centralities[i].get)
    
    for w in sorted_keys:
        sorted_centrality[w] = centralities[i][w]
    
    sorted_nodes = []
    for node in sorted_centrality.keys():
        sorted_nodes.append(node)
    
    height = list(sorted_centrality.values())
    
    vmin = min(height)
    vmax = max(height)
    
    plt.figure()
    if disp_information:
        plt.title(names[i])
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
    plt.savefig('results/sensor_'+names[i]+'_threshold_'+str(500-th)+'_signature.pdf', bbox_inches='tight')
    #plt.savefig('results/sensor_'+names[i]+'_threshold_'+str(500-th)+'_signature.eps', bbox_inches='tight')
    plt.show()
    
    G_th = nx.empty_graph()
    G_th.add_nodes_from(sorted_nodes[th:])
    #G_th.add_nodes_from(sorted_nodes[:th])
    
    plt.figure()
    if disp_information:
        plt.title(names[i])
    nx.draw_networkx(G, pos, node_color=node_color, node_size=20, with_labels=False, cmap=cmap)
    nx.draw_networkx(G_th, pos, node_color=height[th:], node_size=20, vmin=vmin, vmax=vmax, with_labels=False, cmap=cmap)
    #nx.draw_networkx(G_th, pos, node_color=height[:th], node_size=20,vmin=vmin, vmax=vmax, with_labels=False, cmap=cmap)
    plt.axis('equal')
    plt.savefig('results/sensor_'+names[i]+'_threshold_'+str(500-th)+'.pdf', bbox_inches='tight')
    #plt.savefig('results/sensor_'+names[i]+'_threshold_'+str(500-th)+'.eps', bbox_inches='tight')
    plt.show()
    