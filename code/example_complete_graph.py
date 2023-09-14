import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from grc import grc
from gft_c import gft_c
from gravity_centrality import gravity_centrality
from EffG import EffG

disp_information = False

n = 6

G = nx.complete_graph(n)

pos = nx.spring_layout(G, seed=0)

plt.figure()
nx.draw_networkx(G, pos=pos, node_color="lightblue")
plt.savefig('results/complete.pdf', bbox_inches='tight')
#plt.savefig('results/complete.eps', bbox_inches='tight')
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

for i in [0,2]:
    for j in range(len(G)):
        centralities[i][j] = np.round(centralities[i][j], 12)
    
    plt.figure()
    if disp_information:
        plt.title(names[i])
    nx.draw_networkx(G, pos, with_labels=False, node_size=200,
                     node_color=list(centralities[i].values()), cmap=cmap)
    plt.savefig('results/complete_'+names[i]+'.pdf', bbox_inches='tight')
    #plt.savefig('results/complete_'+names[i]+'.eps', bbox_inches='tight')
    plt.show()
    
    sorted_centrality = {}
    sorted_keys = sorted(centralities[i], key=centralities[i].get)
    
    for w in sorted_keys:
        sorted_centrality[w] = centralities[i][w]
    
    sorted_nodes = []
    for node in sorted_centrality.keys():
        sorted_nodes.append(node)
    
    height = list(sorted_centrality.values())
    
    plt.figure()
    if disp_information:
        plt.title(names[i])
        plt.xlabel("nodes")
        plt.ylabel("centrality")
    plt.xticks(range(len(G)), sorted_nodes)
    plt.plot(range(len(G)), height, 'k', lw=1.2, zorder=1)
    plt.scatter(range(len(G)), height, s=100, c=height, cmap=cmap, zorder=2)
    plt.savefig('results/complete_'+names[i]+'_signature.pdf', bbox_inches='tight')
    #plt.savefig('results/complete_'+names[i]+'_signature.eps', bbox_inches='tight')
    plt.show()
