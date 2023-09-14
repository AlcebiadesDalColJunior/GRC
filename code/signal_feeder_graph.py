import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from grc import grc

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

n = len(G)

nodes = list(G.nodes())

# signal = 1 + np.random.randint(10, size=(n,))
# signal[nodes.index(808)] = 30
# signal[nodes.index(802)] = 30

signal = np.zeros((n,))
signal[nodes.index(800)] = 1.0500
signal[nodes.index(802)] = 1.0475
signal[nodes.index(806)] = 1.0457
signal[nodes.index(808)] = 1.0136
signal[nodes.index(810)] = 1.0294
signal[nodes.index(812)] = 0.9763
signal[nodes.index(814)] = 0.9467
signal[nodes.index(850)] = 1.0176
signal[nodes.index(816)] = 1.0172
signal[nodes.index(818)] = 1.0163
signal[nodes.index(820)] = 0.9926
signal[nodes.index(822)] = 0.9895
signal[nodes.index(824)] = 1.0082
signal[nodes.index(826)] = 1.0156
signal[nodes.index(828)] = 1.0074
signal[nodes.index(830)] = 0.9894
signal[nodes.index(854)] = 0.9890
signal[nodes.index(852)] = 0.9581
signal[nodes.index(832)] = 1.0359
signal[nodes.index(858)] = 1.0336
signal[nodes.index(834)] = 1.0309
signal[nodes.index(842)] = 1.0309
signal[nodes.index(844)] = 1.0307
signal[nodes.index(846)] = 1.0309
signal[nodes.index(848)] = 1.0310
signal[nodes.index(860)] = 1.0305
signal[nodes.index(836)] = 1.0303
signal[nodes.index(840)] = 1.0303
signal[nodes.index(862)] = 1.0303
signal[nodes.index(838)] = 1.0285
signal[nodes.index(864)] = 1.0336
signal[nodes.index(888)] = 0.9996
signal[nodes.index(890)] = 0.9167
signal[nodes.index(856)] = 0.9977

I_grc_signal = grc(G, gamma=0.03, signal=signal)


#%% Visualization of results

reds = plt.get_cmap('Greens')

newcolors = reds(np.linspace(0.25, 1.0, 256))
cmap = ListedColormap(newcolors)

vmin=np.min(signal)
vmax=np.max(signal)

plt.figure()
nx.draw_networkx(G, pos, with_labels=False, node_size=50, vmin=vmin, vmax=vmax,
                  node_color=signal, cmap=cmap)
plt.savefig('results/feeder_signal.pdf', bbox_inches='tight')
#plt.savefig('results/feeder_signal.eps', bbox_inches='tight')
plt.show()

plt.figure()
nx.draw_networkx(G, pos, with_labels=False, node_size=50, vmin=vmin, vmax=vmax,
                  node_color=list(I_grc_signal.values()), cmap=cmap)
plt.savefig('results/feeder_smooth_signal.pdf', bbox_inches='tight')
#plt.savefig('results/feeder_smooth_signal.eps', bbox_inches='tight')
plt.show()
