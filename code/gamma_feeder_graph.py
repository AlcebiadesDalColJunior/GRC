import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from grc import grc

disp_information = False

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
plt.show()

reds = plt.get_cmap('Reds')

newcolors = reds(np.linspace(0.25, 1.0, 256))
cmap = ListedColormap(newcolors)

for gamma in [0.1,1,10]:
    
    I_grc = grc(G, gamma=gamma)
        
    plt.figure()
    if disp_information:
        plt.title('gamma='+str(gamma))
    nx.draw_networkx(G, pos, node_color=list(I_grc.values()), node_size=200,
                      with_labels=False, cmap=cmap)
    plt.savefig('results/feeder_GRC_gamma_'+str(gamma)+'.pdf', bbox_inches='tight')
    #plt.savefig('results/feeder_GRC_gamma_'+str(gamma)+'.eps', bbox_inches='tight')
    plt.show()
    
    sorted_centrality = {}
    sorted_keys = sorted(I_grc, key=I_grc.get)
    
    for w in sorted_keys:
        sorted_centrality[w] = I_grc[w]
    
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
        plt.title('gamma='+str(gamma))
        plt.xlabel("nodes")
        plt.ylabel("centrality")
    plt.xticks(xticks, sorted_nodes_xticks, rotation=-90)
    plt.plot(range(len(G)), height, 'k', lw=1.2, zorder=1)
    plt.scatter(range(len(G)), height, s=100, c=height, cmap=cmap, zorder=2)
    plt.savefig('results/feeder_GRC_signature_gamma_'+str(gamma)+'.pdf',bbox_inches='tight')
    #plt.savefig('results/feeder_GRC_signature_gamma_'+str(gamma)+'.eps',bbox_inches='tight')
    plt.show()
        