import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

import time

from grc import grc
from gft_c import gft_c
from gravity_centrality import gravity_centrality
from EffG import EffG

n = 500

n_iter = 100

use_grc = True
use_degree = True
use_gft_c = True
use_betweenness = True
use_closeness = True
use_eigenvector = True

use_gravity_centrality = False
use_EffG = False

names = []
times = []
times_mean = []

if use_grc:
    t_grc_current = []
    names.append("GRC")

if use_degree:
    t_degree_current = []
    names.append("DC")

if use_gft_c:
    t_gft_c_current = []
    names.append("GFT-C")

if use_betweenness:
    t_betweenness_current = []
    names.append("BC")

if use_closeness:
    t_closeness_current = []
    names.append("CC")

if use_eigenvector:
    t_eigenvector_current = []
    names.append("EC")

if use_gravity_centrality:
    t_gravity_centrality_current = []
    names.append("GC")

if use_EffG:
    t_EffG_current = []
    names.append("EffG")

#t_gravity_centrality_current = list(np.load("results/tree_GC.npy"))
#t_EffG_current = list(np.load("results/tree_EffG.npy"))

for i in range(n_iter):
    
    #print("Iteration:",i)
    
    G = nx.random_tree(n=n)
    
    if use_grc:
        start = time.time()
        grc(G)
        t_grc_current.append(time.time()-start)
    
    if use_degree:
        start = time.time()
        nx.degree_centrality(G)
        t_degree_current.append(time.time()-start)
    
    if use_gft_c:
        start = time.time()
        gft_c(G)
        t_gft_c_current.append(time.time()-start)
    
    if use_betweenness:
        start = time.time()
        nx.betweenness_centrality(G)
        t_betweenness_current.append(time.time()-start)
    
    if use_closeness:
        start = time.time()
        nx.closeness_centrality(G)
        t_closeness_current.append(time.time()-start)
        
    if use_eigenvector:
        start = time.time()
        nx.eigenvector_centrality(G, max_iter=500, tol=1e-04)
        t_eigenvector_current.append(time.time()-start)
    
    if use_gravity_centrality:
        start = time.time()
        I_gravity_centrality = gravity_centrality(G)
        t_gravity_centrality_current.append(time.time()-start)
    
    if use_EffG:
        start = time.time()
        I_EffG = EffG(G, method="shortest_path")
        t_EffG_current.append(time.time()-start)

if use_grc:
    t_grc = np.mean(t_grc_current)
    times.append(t_grc_current)
    times_mean.append(t_grc)

if use_degree:
    t_degree = np.mean(t_degree_current)
    times.append(t_degree_current)
    times_mean.append(t_degree)

if use_gft_c:
    t_gft_c = np.mean(t_gft_c_current)
    times.append(t_gft_c_current)
    times_mean.append(t_gft_c)

if use_betweenness:
    t_betweenness = np.mean(t_betweenness_current)
    times.append(t_betweenness_current)
    times_mean.append(t_betweenness)

if use_closeness:
    t_closeness = np.mean(t_closeness_current)
    times.append(t_closeness_current)
    times_mean.append(t_closeness)

if use_eigenvector:
    t_eigenvector = np.mean(t_eigenvector_current)
    times.append(t_eigenvector_current)
    times_mean.append(t_eigenvector)

if use_gravity_centrality:
    t_gravity_centrality = np.mean(t_gravity_centrality_current)
    times.append(t_gravity_centrality_current)
    times_mean.append(t_gravity_centrality)

if use_EffG:
    t_EffG = np.mean(t_EffG_current)
    times.append(t_EffG_current)
    times_mean.append(t_EffG)

print()


#%% Visualization of results

#names = ["GRC", "DC", "GFT-C", "BC", "CC", "EC", "GC", "EffG"]

n_names = len(names)

plt.figure()
plt.title("Tree")
plt.boxplot(times)
plt.xticks(list(range(1,n_names+1)), names)
plt.savefig('results/tree_time.pdf', bbox_inches='tight')
plt.show()

for i in range(n_names):
    if i < n_names-1:
        print(names[i],end =" & ")
    else:
        print(names[i])

for i in range(n_names):
    times_mean[i] = round(times_mean[i], 4)
    
    if i < n_names-1:
        print(times_mean[i], end = " & ")
    else:
        print(times_mean[i], end = "")

#np.save("results/tree_GC",np.array(t_gravity_centrality_current))
#np.save("results/tree_EffG",np.array(t_EffG_current))
