import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

from grc import grc

disp_information = False

G = nx.Graph()

edges = [(33,34),(34,35),(35,36),(36,37),(37,38),(38,39),(39,106),(32,31),(30,29),(29,31),
         (29,28),(28,114),(114,113),(113,112),(112,111),(111,117),(111,110),(110,109),
         (109,108),(108,107),(107,106),(111,116),(116,115),(115,23),(28,27),(27,26),(26,25),
         (25,24),(24,23),(23,77),(22,23),(102,101),(101,100),(100,99),(39,40),(40,105),
         (106,105),(105,98),(98,99),(77,78),(78,68),(68,79),(79,80),(80,81),(68,69),(69,70),
         (70,71),(71,72),(72,73),(73,74),(74,75),(75,76),(98,104),(104,103),(40,41),(41,42),
         (42,43),(43,120),(120,22),(22,21),(21,20),(43,20),(20,44),(44,45),(45,77),(46,45),
         (46,68),(46,47),(47,48),(48,49),(49,50),(50,51),(51,52),(52,53),(53,54),(46,67),
         (67,84),(84,83),(83,82),(54,55),(55,56),(56,57),(57,58),(58,59),(59,60),(60,61),
         (61,62),(62,63),(63,64),(64,65),(65,66),(66,67),(45,85),(85,86),(85,67),(20,19),
         (19,85),(19,18),(18,17),(17,87),(87,86),(17,88),(98,97),(97,96),(96,95),(95,94),
         (94,88),(103,96),(43,118),(119,20),(119,96),(118,19),(88,89),(89,90),(90,91),(91,92),
         (92,93),(17,16),(16,15),(15,14),(14,13),(13,12),(12,11),(11,10),(10,9),(9,7),(7,8),
         (7,6),(6,5),(5,4),(4,3),(3,2),(2,1),(22,77),(119,118)]

G.add_edges_from(edges)

pos = dict()
pos[33] = (0,0)
pos[34] = (0,1)
pos[35] = (0,2)
pos[36] = (0,3)
pos[37] = (0,4)
pos[38] = (0,5)
pos[39] = (0,6)
pos[105] = (0.1,7.4)
pos[98] = (0.1,9)
pos[104] = (0.1,10)
pos[103] = (0.1,11)
pos[106] = (0.6,6)
pos[32] = (7,0)
pos[31] = (7,1)
pos[30] = (6.5,1.5)
pos[29] = (7,2)
pos[28] = (7,3)
pos[114] = (6,3)
pos[113] = (5,3)
pos[112] = (4,3)
pos[111] = (3,3)
pos[117] = (3,2)
pos[110] = (2.5,3.5)
pos[109] = (2,4)
pos[108] = (1.5,4.5)
pos[107] = (1,5)
pos[116] = (3,4)
pos[115] = (3,5)
pos[23] = (4.5,6)
pos[27] = (7,4)
pos[26] = (6.8,4.8)
pos[25] = (6.4,5.4)
pos[24] = (5.6,5.8)
pos[102] = (-0.5-3*0.6,8.4-3*0.6)
pos[101] = (-0.5-2*0.6,8.4-2*0.6)
pos[100] = (-0.5-0.6,8.4-0.6)
pos[99] = (-0.5,8.4)
pos[77] = (5,6.6)
pos[22] = (3.2,6.6)
pos[78] = (6,6.6)
pos[68] = (7.6,6.6)
pos[79] = (9.6,6.6)
pos[80] = (11.6,6.6)
pos[81] = (13.6,6.6)
pos[69] = (12.5-7*0.6,1.5+7*0.6)
pos[70] = (12.5-6*0.6,1.5+6*0.6)
pos[71] = (12.5-5*0.6,1.5+5*0.6)
pos[72] = (12.5-4*0.6,1.5+4*0.6)
pos[73] = (12.5-3*0.6,1.5+3*0.6)
pos[74] = (12.5-2*0.6,1.5+2*0.6)
pos[75] = (12.5-0.6,1.5+0.6)
pos[76] = (12.5,1.5)
pos[40] = (0.65,7)
pos[41] = (1.1,7.55)
pos[42] = (1.6,8.05)
pos[43] = (2.2,8.35)
pos[120] = (2.5,7.5)
pos[21] = (3,7.7)
pos[20] = (3,8.5)
pos[44] = (4.5,8.5)
pos[45] = (5.5,8.5)
pos[46] = (7.6,8.5)
pos[47] = (8.6,8.5)
pos[48] = (9.6,8.5)
pos[49] = (10.6,8.5)
pos[50] = (11.6,8.5)
pos[51] = (12.6,8.5)
pos[52] = (13.6,8.5)
pos[53] = (14.6,8.5)
pos[54] = (15.6,8.5)
pos[67] = (8,9.5)
pos[84] = (9.2,9.5)
pos[83] = (10.4,9.5)
pos[82] = (11.6,9.5)
pos[55] = (15.6,9.5)
pos[56] = (15.6,10.5)
pos[57] = (15.6,11.5)
pos[58] = (15.4,12.5)
pos[59] = (14.8,13)
pos[60] = (13.8,13)
pos[61] = (12.8,13)
pos[62] = (11.8,13)
pos[63] = (10.8,13)
pos[64] = (10,12.5)
pos[65] = (9.2,12)
pos[66] = (8.6,11)
pos[85] = (5.5,9.5)
pos[86] = (5.5,10.5)
pos[19] = (3,9.5)
pos[18] = (3,10.5)
pos[17] = (3,11.5)
pos[87] = (5.3,11.5)
pos[97] = (0.5,9.5)
pos[96] = (0.9,10)
pos[95] = (1.3,10.5)
pos[94] = (1.7,11)
pos[118] = (2.3,9.45)
pos[119] = (2.55,8.75)
pos[88] = (2,11.5)
pos[89] = (2-0.7,11.5+0.7)
pos[90] = (2-2*0.7,11.5+2*0.7)
pos[91] = (2-3*0.7,11.5+3*0.7)
pos[92] = (2-4*0.7,11.5+4*0.7)
pos[93] = (2-5*0.7,11.5+5*0.7)
pos[16] = (3,12.5)
pos[15] = (3,13.5)
pos[14] = (3,14.5)
pos[13] = (3,15.5)
pos[12] = (3,16.5)
pos[11] = (3,17.5)
pos[10] = (3,18.5)
pos[9] = (3,19.5)
pos[7] = (2,20.5)
pos[8] = (3.3,20.5)
pos[6] = (1.2,20.5)
pos[5] = (0.4,20.5)
pos[4] = (-0.4,20.5)
pos[3] = (-1.2,20.5)
pos[2] = (-2,20.5)
pos[1] = (-2.8,20.5)

for i in pos.keys():
    (a,b) = pos[i]
    pos[i] = (1.1 * a,1.1 * b)

plt.figure()
#nx.draw_networkx(G, pos=pos, node_color="lightblue", node_size=35, font_size=3.6)
nx.draw_networkx(G, pos=pos, node_color="lightblue", node_size=80, font_size=6)
plt.show()

reds = plt.get_cmap('Reds')

newcolors = reds(np.linspace(0.25, 1.0, 256))
cmap = ListedColormap(newcolors)

for gamma in [0.1,1,10]:
    
    I_grc = grc(G, gamma=gamma)
    
    plt.figure()
    if disp_information:
        plt.title('gamma='+str(gamma))
    nx.draw_networkx(G, pos, with_labels=False, node_size=50,
                      node_color=list(I_grc.values()), cmap=cmap)
    # nx.draw_networkx_labels(G, pos=pos_labels, labels=labels, font_size=12)
    plt.savefig('results/Taipei_GRC_gamma_'+str(gamma)+'.pdf', bbox_inches='tight')
    #plt.savefig('results/Taipei_GRC_gamma_'+str(gamma)+'.eps', bbox_inches='tight')
    plt.show()
    
    sorted_centrality = {}
    sorted_keys = sorted(I_grc, key=I_grc.get)
    
    for w in sorted_keys:
        sorted_centrality[w] = I_grc[w]
    
    sorted_nodes = []
    for node in sorted_centrality.keys():
        sorted_nodes.append(node)
    
    print("Larger centralities","GRC")
    for j in range(-2,0):
        print("node:",sorted_nodes[j],"centrality",sorted_centrality[sorted_nodes[j]])
    print("")
    
    xticks = [len(G)-1]
    sorted_nodes_xticks = []
    for j in xticks:
        sorted_nodes_xticks.append(sorted_nodes[j])
    
    height = list(sorted_centrality.values())
    
    plt.figure()
    if disp_information:
        plt.title('gamma='+str(gamma))
        plt.xlabel("nodes")
        plt.ylabel("centrality")
    #plt.xticks(xticks, sorted_nodes_xticks, rotation=-90)
    plt.xticks([])
    plt.plot(range(len(G)), height, 'k', lw=1.2, zorder=1)
    plt.scatter(range(len(G)), height, s=25, c=height, cmap=cmap, zorder=2)
    plt.savefig('results/Taipei_GRC_signature_gamma_'+str(gamma)+'.pdf', bbox_inches='tight')
    #plt.savefig('results/Taipei_GRC_signature_gamma_'+str(gamma)+'.eps', bbox_inches='tight')
    plt.show()
        