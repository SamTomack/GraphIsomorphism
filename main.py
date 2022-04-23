import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import networkx as nx
import numpy as np
import tkinter as tk
import keyboard as kb
import time

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim([0, 1])
ax.set_ylim([0, 1])

fig2 = plt.figure()
ax2 = fig2.add_subplot(111)
ax2.set_xlim([0, 1])
ax2.set_ylim([0, 1])

G1 = nx.Graph()
G2 = nx.Graph()
G1Nodes = 0
isG1NodeSelected = False
G1SelectedNode = None
G2Nodes = 0
isG2NodeSelected = False
G2SelectedNode = None

def veryClose(G ,node1, node2):
    pos1 = list(G.nodes[node1].values())
    pos2 = list(G.nodes[node2].values())
    res = tuple(np.subtract(pos1[0], pos2[0]))
    if(res[0] <= .05) & (res[0] >= -.05) & (res[1] <= .05) & (res[1] >= -.05):
        return True
    else:
        return False

def XYveryClose(G, node, xy):
    pos = list(G.nodes[node].values())
    xy = tuple(xy)
    res = tuple(np.subtract(pos, xy))
    if (res[0][0] <= .05) & (res[0][0] >= -.05) & (res[0][1] <= .05) & (res[0][1] >= -.05):
        return True
    else:
        return False

#FOR GRAPH ONE
def ondblclick(event):
    X = event.xdata
    Y = event.ydata
    global G1Nodes
    global isG1NodeSelected
    global G1SelectedNode
    if event.dblclick:
        if (G1Nodes >= 1):
            G1Nodes += 1
            G1.add_node(G1Nodes, pos=(X, Y))
            pos = nx.get_node_attributes(G1, 'pos')
            truthArr = {0}
            for i in range(1, G1Nodes):
                if (veryClose(G1, G1Nodes - i, G1Nodes)):
                    truthArr.add("T")
                else:
                    truthArr.add("F")
            if "T" not in truthArr:
                nx.draw(G1, pos, with_labels= True)
            else:
                G1.remove_node(G1Nodes)
                G1Nodes -= 1

        if(G1Nodes == 0):
            G1Nodes += 1
            G1.add_node(G1Nodes, pos = (X, Y))
            pos = nx.get_node_attributes(G1, 'pos')
            nx.draw(G1, pos , with_labels= True)

        fig.canvas.draw()

    if not event.dblclick:
        for i in range(1, G1Nodes+1):
            if XYveryClose(G1, i, (X,Y)):
                if isG1NodeSelected == False:
                    color_map = []
                    for node in G1:
                        if node == i:
                            color_map.append('blue')
                        else:
                            color_map.append('#1f78b4')
                    isG1NodeSelected = True
                    G1SelectedNode = i
                    pos = nx.get_node_attributes(G1, 'pos')
                    nx.draw(G1, pos, node_color = color_map, with_labels=True)
                else:
                    G1.add_edge(G1SelectedNode, i)
                    if G1SelectedNode == i:
                        G1.remove_edge(G2SelectedNode, i)
                    isG1NodeSelected = False
                    pos = nx.get_node_attributes(G1, 'pos')
                    nx.draw(G1, pos, with_labels=True)
            elif kb.is_pressed(' '):
                isG1NodeSelected = False
                G1SelectedNode = None
                pos = nx.get_node_attributes(G1, 'pos')
                nx.draw(G1, pos, with_labels=True)

        fig.canvas.draw()
cid = fig.canvas.mpl_connect('button_press_event', ondblclick)

#FOR GRAPH TWO
def ondblclick2(event):
    X = event.xdata
    Y = event.ydata
    global G2Nodes
    global isG2NodeSelected
    global G2SelectedNode
    if event.dblclick:
        if (G2Nodes >= 1):
            G2Nodes += 1
            G2.add_node(G2Nodes, pos=(X, Y))
            pos = nx.get_node_attributes(G2, 'pos')
            truthArr = {0}
            for i in range(1, G2Nodes):
                if (veryClose(G2, G2Nodes - i, G2Nodes)):
                    truthArr.add("T")
                else:
                    truthArr.add("F")
            if "T" not in truthArr:
                nx.draw(G2, pos, node_color = 'red', with_labels= True)
            else:
                G2.remove_node(G2Nodes)
                G2Nodes -= 1

        if(G2Nodes == 0):
            G2Nodes += 1
            G2.add_node(G2Nodes, pos = (X, Y))
            pos = nx.get_node_attributes(G2, 'pos')
            nx.draw(G2, pos, node_color = 'red', with_labels= True)

        fig2.canvas.draw()

    if not event.dblclick:
        for i in range(1, G2Nodes+1):
            if XYveryClose(G2, i, (X,Y)):
                if isG2NodeSelected == False:
                    color_map = []
                    for node in G2:
                        if node == i:
                            color_map.append('#A52A2A')
                        else:
                            color_map.append('red')
                    isG2NodeSelected = True
                    G2SelectedNode = i
                    pos = nx.get_node_attributes(G2, 'pos')
                    nx.draw(G2, pos, node_color=color_map, with_labels=True)
                else:
                    G2.add_edge(G2SelectedNode, i)
                    if G2SelectedNode == i:
                        G2.remove_edge(G2SelectedNode, i)
                    isG2NodeSelected = False
                    pos = nx.get_node_attributes(G2, 'pos')
                    nx.draw(G2, pos, node_color = 'red', with_labels=True)
            elif kb.is_pressed(' '):
                isG2NodeSelected = False
                G2SelectedNode = None
                pos = nx.get_node_attributes(G2, 'pos')
                nx.draw(G2, pos, node_color = 'red', with_labels=True)
        fig2.canvas.draw()
cid = fig2.canvas.mpl_connect('button_press_event', ondblclick2)

def isIsomorphic(G1, G2):
    if nx.is_isomorphic(G1, G2):
        print("Isomorphic")
    else:
        print("Not isomorphic")

window = tk.Tk()

frame = tk.Frame(master=window)
frame.pack()
figure1 = FigureCanvasTkAgg(fig, frame)
figure1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
figure2 = FigureCanvasTkAgg(fig2, frame)
figure2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)

button = tk.Button(master = frame, text = 'Check isomorphism', command = lambda: isIsomorphic(G1,G2))
button.pack(side = tk.LEFT)
button.place(x = 875, y = 0)

window.mainloop()
