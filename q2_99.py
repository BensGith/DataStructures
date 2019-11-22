### Exercise 3 - q2: Graphs ###

### Template ###

#import libraries:
import pandas as pd
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
#Load  data:
df_edges_raw = pd.read_csv('edges.csv')
df_name_id = pd.read_csv('name_id_data.csv')

#Handle data:
def set_id_instead_names(df_name_id, df_edges):
    df_edges_copy = df_edges.copy()
    for char_id in df_name_id['id']:
        char_name = df_name_id.iloc[char_id]['name']
        df_edges_copy.loc[df_edges_copy['Source']==char_name, 'Source'] = char_id
        df_edges_copy.loc[df_edges_copy['Target']==char_name, 'Target'] = char_id
    return df_edges_copy

#please note that this function might take few seconds to finish
df_edges = set_id_instead_names(df_name_id, df_edges_raw)
edges=[tuple(x) for x in df_edges.to_records(index=False)]

#a. create adjacency matrix
#Build function for creating adjacency matrix:
def creat_adjacency_matrix(edges):
    max_val = 0
    for t in edges:  # getting max value to determine matrix size
        if max_val < max(t[0],t[1]):
            max_val = max(t[0],t[1])
    mat = np.zeros((max_val + 1, max_val + 1))
    for t in edges:
        mat[t[0],t[1]], mat[t[1], t[0]] = 1, 1  # assign value of 1 to each connection
    return mat



#Use adjacency matrix function on data:
print(creat_adjacency_matrix(edges))

#b. create adjacency dictionary
#Build function for creating adjacency dict:
def creat_adjacency_dict(edges):
    dict = {}
    for t in edges:
        if t[0] in dict:
            dict[t[0]].append(t[1])
        if t[1] in dict:
            dict[t[1]].append(t[0])
        if t[0] not in dict:
            dict[t[0]] = [t[1]]
        if t[1] not in dict:
            dict[t[1]] = [t[0]]
    return dict


#Use adjacency dict function on data:
print(creat_adjacency_dict(edges))

#c. BFS
#Build class Queue:
class Queue():
    def __init__(self):
        self.lst = []

    def empty(self):
        if len(self.lst) == 0:
            return True
        return False

    def enqueue(self, x):
        self.lst.append(x)

    def dequeue(self):
        if not self.empty():
            return self.lst.pop(0)


#Build BFS function:
def BFS(edges,v):
    queue = Queue()
    adj_dict = creat_adjacency_dict(edges)  # creating dictionary to quickly add neighbors to queue
    visited = [v]  # add first city visited
    queue.enqueue(v)  # add person v to queue for visiting neighbors
    while not queue.empty():
        el = queue.dequeue()  # pulling person from queue and visiting his neighbors
        for person in adj_dict[el]:  # for each neighbor of el
            if person not in visited:
                visited.append(person)  # add person to visited list
                queue.enqueue(person)  # add person to queue to be visited
    return visited

#Use BFS function on data, start as v=1:
print (BFS(edges,1))
#d. DFS
#Build DFS function:
def DFS(edges=list):
    visited = []
    def visit(u):
        colors[u] = "gray"
        visited.append(u)  # appending visited node to visited list
        for person in adj_dict[u]:
            if colors[person] == "white":
                visit(person)
            colors[u] = "black"
    adj_dict = creat_adjacency_dict(edges)
    colors = {}  # dictionary for coloring vertexes
    for v in adj_dict.keys():  # for every node
        colors[v] = "white"  # adding vertexes to color dictionary, coloring all vertexes white
    for v in adj_dict.keys():
        if colors[v] == "white":  # if node is white, visit it
            visit(v)
    return visited  # return visited vertexes list


#Use DFS function on data:
print(DFS(edges))

#Bonus Section:


def visual():

    G = nx.Graph()
    for e in range(50):  # running on first 50 values
        G.add_edge(edges[e][0], edges[e][1])  # adding edges to graph
    pos = nx.spring_layout(G,k=1.00,scale=2.0,iterations=20)
    plt.figure(num=None, figsize=(30, 30), dpi=80)
    plt.axis('off')
    nx.draw(G,pos,fontsize =6,with_labels=True)
    plt.show()


visual()
