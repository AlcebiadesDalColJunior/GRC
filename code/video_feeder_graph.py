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

# Select only one centrality at a time

use_grc = True
use_degree = False
use_gft_c = False
use_betweenness = False
use_closeness = False
use_eigenvector = False

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

i = 0

filename = 'results/'+names[i]+'_feeder_graph.mp4'

sorted_centrality = {}
sorted_keys = sorted(centralities[i], key=centralities[i].get)

for w in sorted_keys:
    sorted_centrality[w] = centralities[i][w]

sorted_nodes = []
for node in sorted_centrality.keys():
    sorted_nodes.append(node)

fig, axs = plt.subplots(2,1)
axs[0].set_title(names[i])
axs[1].set_title("Signature")

signal = list(centralities[i].values())
height = list(sorted_centrality.values())

vmin = min(signal)
vmax = max(signal)

node_color = ['w' for j in range(n)]

nx.draw_networkx(G, pos, node_color=node_color, node_size=36, vmin=vmin, vmax=vmax,
                  with_labels=False, cmap=cmap, ax=axs[0])

axs[1].scatter(range(n), height, c='w')

def func(node):
    
    j = sorted_nodes.index(node) + 1
    
    G_local = nx.empty_graph()
    G_local.add_node(node)
    
    signal_local = signal[nodes.index(node)]
    
    nx.draw_networkx(G_local, pos, node_color=signal_local, node_size=36, vmin=vmin, vmax=vmax,
                      with_labels=False, cmap=cmap, ax=axs[0])
    
    axs[1].set_xticks([])
    axs[1].plot(range(j), height[:j], 'k', lw=1.0, zorder=1)
    axs[1].scatter(range(j), height[:j], c=height[:j], cmap=cmap, zorder=2,
                   vmin=vmin, vmax=vmax)
    
    return()

fig.tight_layout()

ani = animation.FuncAnimation(fig, func, sorted_nodes, repeat=False)

Writer = animation.writers['ffmpeg']
writer = Writer(fps=2)

ani.save(filename, writer=writer, dpi=250)
