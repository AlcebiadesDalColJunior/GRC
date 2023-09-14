import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from scipy import stats

from grc import grc
from gft_c import gft_c
from gravity_centrality import gravity_centrality
from EffG import EffG

disp_information = False

G = nx.Graph()

nodelist = [i for i in range(21)]

G.add_nodes_from(nodelist)

edges = [(0,1),(0,2),(0,3),(0,4),
         (1,2),(1,4),
         (2,3),
         (3,4),
         (4,5),(5,6),(6,7),(7,8),(8,9),
         (9,10),(9,11),(9,12),
         (10,11),(10,12),
         (11,12),
         (12,13),(13,14),(14,15),(15,16),(16,17),
         (17,18),(17,19),(17,20),
         (18,19),(18,20),
         (19,20)]
         
G.add_edges_from(edges)
         
pos = dict()
pos[0] = (2.5,4.6)
pos[1] = (3,4)
pos[2] = (2,4)
pos[3] = (2,3)
pos[4] = (3,3)
pos[5] = (4,3)
pos[6] = (5,3)
pos[7] = (6,3)
pos[8] = (7,3)
pos[9] = (7,2)
pos[10] = (6,2)
pos[11] = (7,1)
pos[12] = (6,1)
pos[13] = (5,1)
pos[14] = (4,1)
pos[15] = (3,1)
pos[16] = (2,1)
pos[17] = (1,1)
pos[18] = (0,1)
pos[19] = (1,0)
pos[20] = (0,0)

plt.figure()
nx.draw_networkx(G, pos=pos, node_color="lightblue")
plt.savefig('results/unweighted_graph_II.pdf', bbox_inches='tight')
#plt.savefig('results/unweighted_graph_II.eps', bbox_inches='tight')
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
    I_eigenvector = nx.eigenvector_centrality(G, max_iter=200, tol=1e-04)
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

for i in range(n_names):
    plt.figure()
    if disp_information:
        plt.title(names[i])
    nx.draw_networkx(G, pos, with_labels=False, node_size=200,
                     node_color=list(centralities[i].values()), cmap=cmap)
    plt.savefig('results/unweighted_graph_II_'+names[i]+'.pdf', bbox_inches='tight')
    #plt.savefig('results/unweighted_graph_II_'+names[i]+'.eps', bbox_inches='tight')
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
    plt.savefig('results/unweighted_graph_II_'+names[i]+'_signature.pdf', bbox_inches='tight')
    #plt.savefig('results/unweighted_graph_II_'+names[i]+'_signature.eps', bbox_inches='tight')
    plt.show()

print("Spearman correlation coefficient with respect to GRC:")
print()

for i in range(1,n_names):
    if i < n_names-1:
        print(names[i],end =" & ")
    else:
        print(names[i])

for i in range(1,n_names):
    coefficient_spearmanr = stats.spearmanr(list(I_grc.values()),list(centralities[i].values()))
    coefficient_spearmanr = coefficient_spearmanr[0]
    
    coefficient_spearmanr = round(coefficient_spearmanr, 2)
    
    if i < n_names-1:
        print(coefficient_spearmanr,end =" & ")
    else:
        print(coefficient_spearmanr,end ="")
