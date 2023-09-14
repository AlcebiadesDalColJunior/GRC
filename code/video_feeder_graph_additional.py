import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

import matplotlib.animation as animation

from grc import grc
from gft_c import gft_c
from gravity_centrality import gravity_centrality
from EffG import EffG

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

# Select six centralities at a time

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
    I_eigenvector = nx.eigenvector_centrality(G, max_iter=500)
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

n = len(G)

nodes = list(G.nodes())

reds = plt.get_cmap('Reds')

newcolors = reds(np.linspace(0.25, 1.0, 256))
cmap = ListedColormap(newcolors)

fig, axs = plt.subplots(2,3)

###############################################################################
i = 0

filename = 'results/centralities_feeder_graph.mp4'

sorted_centrality = {}
sorted_keys = sorted(centralities[i], key=centralities[i].get)

for w in sorted_keys:
    sorted_centrality[w] = centralities[i][w]

sorted_nodes_0 = []
for node in sorted_centrality.keys():
    sorted_nodes_0.append(node)

axs[0,0].set_title(names[i])

signal_0 = list(centralities[i].values())

vmin_0 = min(signal_0)
vmax_0 = max(signal_0)

###############################################################################
i = 1

sorted_centrality = {}
sorted_keys = sorted(centralities[i], key=centralities[i].get)

for w in sorted_keys:
    sorted_centrality[w] = centralities[i][w]

sorted_nodes_1 = []
for node in sorted_centrality.keys():
    sorted_nodes_1.append(node)

axs[0,1].set_title(names[i])

signal_1 = list(centralities[i].values())

vmin_1 = min(signal_1)
vmax_1 = max(signal_1)

###############################################################################
i = 2

sorted_centrality = {}
sorted_keys = sorted(centralities[i], key=centralities[i].get)

for w in sorted_keys:
    sorted_centrality[w] = centralities[i][w]

sorted_nodes_2 = []
for node in sorted_centrality.keys():
    sorted_nodes_2.append(node)

axs[0,2].set_title(names[i])

signal_2 = list(centralities[i].values())

vmin_2 = min(signal_2)
vmax_2 = max(signal_2)

###############################################################################
i = 3

sorted_centrality = {}
sorted_keys = sorted(centralities[i], key=centralities[i].get)

for w in sorted_keys:
    sorted_centrality[w] = centralities[i][w]

sorted_nodes_3 = []
for node in sorted_centrality.keys():
    sorted_nodes_3.append(node)

axs[1,0].set_title(names[i])

signal_3 = list(centralities[i].values())

vmin_3 = min(signal_3)
vmax_3 = max(signal_3)

###############################################################################
i = 4

sorted_centrality = {}
sorted_keys = sorted(centralities[i], key=centralities[i].get)

for w in sorted_keys:
    sorted_centrality[w] = centralities[i][w]

sorted_nodes_4 = []
for node in sorted_centrality.keys():
    sorted_nodes_4.append(node)

axs[1,1].set_title(names[i])

signal_4 = list(centralities[i].values())

vmin_4 = min(signal_4)
vmax_4 = max(signal_4)

###############################################################################
i = 5

sorted_centrality = {}
sorted_keys = sorted(centralities[i], key=centralities[i].get)

for w in sorted_keys:
    sorted_centrality[w] = centralities[i][w]

sorted_nodes_5 = []
for node in sorted_centrality.keys():
    sorted_nodes_5.append(node)

axs[1,2].set_title(names[i])

signal_5 = list(centralities[i].values())

vmin_5 = min(signal_5)
vmax_5 = max(signal_5)


node_color = ['w' for j in range(n)]

nx.draw_networkx(G, pos, node_color=node_color, node_size=20, with_labels=False, ax=axs[0,0])
nx.draw_networkx(G, pos, node_color=node_color, node_size=20, with_labels=False, ax=axs[0,1])
nx.draw_networkx(G, pos, node_color=node_color, node_size=20, with_labels=False, ax=axs[0,2])
nx.draw_networkx(G, pos, node_color=node_color, node_size=20, with_labels=False, ax=axs[1,0])
nx.draw_networkx(G, pos, node_color=node_color, node_size=20, with_labels=False, ax=axs[1,1])
nx.draw_networkx(G, pos, node_color=node_color, node_size=20, with_labels=False, ax=axs[1,2])


def func(j):
    
    ###########################################################################
    node = sorted_nodes_0[j]
    
    G_local = nx.empty_graph()
    G_local.add_node(node)
    
    signal_local_0 = signal_0[nodes.index(node)]
    
    nx.draw_networkx(G_local, pos, node_color=signal_local_0, node_size=20, vmin=vmin_0,
                     vmax=vmax_0,with_labels=False, cmap=cmap, ax=axs[0,0])
    
    ###########################################################################
    node = sorted_nodes_1[j]
    
    G_local = nx.empty_graph()
    G_local.add_node(node)
    
    signal_local_1 = signal_1[nodes.index(node)]
    
    nx.draw_networkx(G_local, pos, node_color=signal_local_1, node_size=20, vmin=vmin_1,
                     vmax=vmax_1,with_labels=False, cmap=cmap, ax=axs[0,1])
    
    ###########################################################################
    node = sorted_nodes_2[j]
    
    G_local = nx.empty_graph()
    G_local.add_node(node)
    
    signal_local_2 = signal_2[nodes.index(node)]
    
    nx.draw_networkx(G_local, pos, node_color=signal_local_2, node_size=20, vmin=vmin_2,
                     vmax=vmax_2,with_labels=False, cmap=cmap, ax=axs[0,2])
    
    ###########################################################################
    node = sorted_nodes_3[j]
    
    G_local = nx.empty_graph()
    G_local.add_node(node)
    
    signal_local_3 = signal_3[nodes.index(node)]
    
    nx.draw_networkx(G_local, pos, node_color=signal_local_3, node_size=20, vmin=vmin_3,
                     vmax=vmax_3,with_labels=False, cmap=cmap, ax=axs[1,0])
    
    ###########################################################################
    node = sorted_nodes_4[j]
    
    G_local = nx.empty_graph()
    G_local.add_node(node)
    
    signal_local_4 = signal_4[nodes.index(node)]
    
    nx.draw_networkx(G_local, pos, node_color=signal_local_4, node_size=20, vmin=vmin_4,
                     vmax=vmax_4,with_labels=False, cmap=cmap, ax=axs[1,1])
    
    ###########################################################################
    node = sorted_nodes_5[j]
    
    G_local = nx.empty_graph()
    G_local.add_node(node)
    
    signal_local_5 = signal_5[nodes.index(node)]
    
    nx.draw_networkx(G_local, pos, node_color=signal_local_5, node_size=20, vmin=vmin_5,
                     vmax=vmax_5,with_labels=False, cmap=cmap, ax=axs[1,2])
    
    return()

fig.tight_layout()

ani = animation.FuncAnimation(fig, func, range(n), repeat=False)

Writer = animation.writers['ffmpeg']
writer = Writer(fps=2)

ani.save(filename, writer=writer, dpi=250)
