import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from grc import grc

# n = 10
# G = nx.random_tree(n=n)

G = nx.read_gexf('data/G10_tree.gexf')

pos = nx.spring_layout(G, seed=73)

signal = 1 + np.random.randint(10, size=(10,))
signal[1] = 20
signal[6] = 20

I_grc_signal = grc(G, signal=signal)


#%% Visualization of results

reds = plt.get_cmap('Greens')

newcolors = reds(np.linspace(0.25, 1.0, 256))
cmap = ListedColormap(newcolors)

plt.figure()
nx.draw_networkx(G, pos, with_labels=False, node_size=200,
                  node_color=signal, cmap=cmap)
plt.savefig('results/tree_signal.pdf', bbox_inches='tight')
#plt.savefig('results/tree_signal.eps', bbox_inches='tight')
plt.show()

plt.figure()
nx.draw_networkx(G, pos, with_labels=False, node_size=200,
                  node_color=list(I_grc_signal.values()), cmap=cmap)
plt.savefig('results/tree_smooth_signal.pdf', bbox_inches='tight')
#plt.savefig('results/tree_smooth_signal.eps', bbox_inches='tight')
plt.show()
