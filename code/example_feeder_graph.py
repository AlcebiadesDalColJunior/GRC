import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from scipy import stats

from grc import grc
from gft_c import gft_c
from gravity_centrality import gravity_centrality
from EffG import EffG

disp_information = True

G = nx.Graph()

edges = [(800,802),(802,806),(806,808),(808,810),(808,812),(812,814),(814,850),
         (850,816),(816,818),(818,820),(820,822),(816,824),(824,826),(824,828),
         (828,830),(830,854),(854,856),(854,852),(852,832),(832,858),(858,864),
         (832,888),(888,890),(858,834),(834,842),(842,844),(844,846),(846,848),
         (834,860),(860,836),(836,840),(836,862),(862,838)]
         
G.add_edges_from(edges)

pos = dict()
pos[800] = (0,0)
pos[802] = (1,0)
pos[806] = (2,0)
pos[808] = (3,0)
pos[810] = (3,-1.5)
pos[812] = (4,0)
pos[814] = (5,0)
pos[850] = (6,0)
pos[816] = (7,0)
pos[818] = (7,0.5)
pos[820] = (7,1)
pos[822] = (7,1.5)
pos[824] = (8,0)
pos[826] = (9,0)
pos[828] = (8,-2.5)
pos[830] = (9,-2.5)
pos[854] = (10,-2.5)
pos[856] = (11,-2.5)
pos[852] = (10,-1.4)
pos[832] = (10,-0.7)
pos[858] = (10,0)
pos[864] = (10,0.5)
pos[888] = (11.5,-0.7)
pos[890] = (12.5,-0.7)
pos[834] = (11,0)
pos[842] = (11,0.5)
pos[844] = (11,1)
pos[846] = (11,1.5)
pos[848] = (11,2)
pos[860] = (12.5,0)
pos[836] = (14,0)
pos[840] = (15,0)
pos[862] = (14,-0.7)
pos[838] = (14,-1.7)

plt.figure()
nx.draw_networkx(G, pos=pos, node_color="lightblue", node_size=200, font_size=8)
plt.savefig('results/feeder34.pdf', bbox_inches='tight')
#plt.savefig('results/feeder34.eps', bbox_inches='tight')
plt.show()

use_grc = True
use_degree = True
use_gft_c = True
use_betweenness = True
use_closeness = True
use_eigenvector = True

use_gravity_centrality = True
use_EffG = True

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
    I_eigenvector = nx.eigenvector_centrality(G, max_iter=500)
    names.append("EC")
    centralities.append(I_eigenvector)

if use_gravity_centrality:
    I_gravity_centrality = gravity_centrality(G)
    names.append("GC")
    centralities.append(I_gravity_centrality)

if use_EffG:
    I_EffG = EffG(G, method="shortest_path_coefficient", coefficient=0.05)
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
    nx.draw_networkx(G, pos, node_color=list(centralities[i].values()), node_size=200,
                      with_labels=False, cmap=cmap)
    plt.savefig('results/feeder34_'+names[i]+'.pdf', bbox_inches='tight')
    #plt.savefig('results/feeder34_'+names[i]+'.eps', bbox_inches='tight')
    plt.show()
    
    sorted_centrality = {}
    sorted_keys = sorted(centralities[i], key=centralities[i].get)
    
    for w in sorted_keys:
        sorted_centrality[w] = centralities[i][w]
    
    sorted_nodes = []
    for node in sorted_centrality.keys():
        sorted_nodes.append(node)
    
    xticks = range(0,len(G))
    sorted_nodes_xticks = []
    for j in xticks:
        sorted_nodes_xticks.append(sorted_nodes[j])
    
    height = list(sorted_centrality.values())
    
    plt.figure()
    if disp_information:
        plt.title(names[i])
        plt.xlabel("nodes")
        plt.ylabel("centrality")
    #if i in [0,3,5]:
    #    plt.gca().yaxis.set_major_formatter(plt.FormatStrFormatter('%.2f'))
    #if i == 2:
    #    height = 10 * np.array(height)
    plt.xticks(xticks, sorted_nodes_xticks, rotation=-90)
    plt.plot(range(len(G)), height, 'k', lw=1.2, zorder=1)
    plt.scatter(range(len(G)), height, s=100, c=height, cmap=cmap, zorder=2)
    plt.savefig('results/feeder34_'+names[i]+'_signature.pdf', bbox_inches='tight')
    #plt.savefig('results/feeder34_'+names[i]+'_signature.eps', bbox_inches='tight')
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
        print(coefficient_spearmanr)
