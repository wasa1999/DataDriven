import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import networkx as nx
from scipy import stats

weightData = pd.DataFrame(pd.read_csv('/Users/Tomoya_Iwasaki/Desktop/data/resultA1_E1.csv'));
edgeData = np.array([1,2,3,4]);
Graph = nx.DiGraph();
color_map = []
q1,q2,q3 = 0,0,0;


def addEdges(wd):

    buffer = [];
    for i in range(edgeData.size):
        for j in range(edgeData.size):
            if (i == j):
                break;
            else:
                print(weightData.iloc[i][j])
                buffer.append(weightData.iloc[i][j]);

    q1 = stats.scoreatpercentile(buffer, 25);
    q2 = np.median(buffer);
    q3 = stats.scoreatpercentile(buffer, 75);


    for i in range(edgeData.size):
        for j in range(edgeData.size):

            if (weightData.iloc[i,j] == 0):
                color_map.append('white');
                Graph.add_weighted_edges_from([(i+1 ,j+1 , weightData.iloc[i,j])]);


            elif (weightData.iloc[i,j] > 0 and weightData.iloc[i,j] <= q1):
                color_map.append('black');
                Graph.add_weighted_edges_from([(i+1 ,j+1 , weightData.iloc[i,j])]);


            elif (weightData.iloc[i,j] > q1 and weightData.iloc[i,j] <= q2):
                color_map.append('blue');
                Graph.add_weighted_edges_from([(i+1,j+1,weightData.iloc[i,j])]);

            elif (weightData.iloc[i,j] > q2 and weightData.iloc[i,j] <= q3):
                color_map.append('green');
                Graph.add_weighted_edges_from([(i+1,j+1,weightData.iloc[i,j])]);


            elif (weightData.iloc[i,j] > q3):
                color_map.append('red');
                Graph.add_weighted_edges_from([(i+1,j+1,weightData.iloc[i,j])]);



            # if (i == j or weightData.iloc[i,j] == 0):
            #     Graph.remove_edge(i,j);






if __name__ == '__main__':

    for i in range(0,edgeData.size):
        Graph.add_node(i+1);
    addEdges(weightData);



    nx.draw(Graph, edge_color=color_map, with_labels = True)
    plt.title("A1からA10の人間関係")
    plt.show();

    # print(weightData.iloc[9][9]);
