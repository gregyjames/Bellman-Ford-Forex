from forex_python.converter import CurrencyRates
import math

c = CurrencyRates()

# Python program for Bellman-Ford's single source
# shortest path algorithm.

from collections import defaultdict

# Class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.V = vertices # No. of vertices
        self.graph = [] # default dictionary to store graph

    # function to add an edge to graph
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    # utility function used to print the solution
    def printArr(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("% d \t\t % d" % (i, dist[i]))

    def BellmanFord(self, src):
        dist = [float("Inf")] * self.V
        dist[src] = 0
        for i in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print "Graph contains negative weight cycle"
                break

        self.printArr(dist)

#0 -> USD
#1 -> EUR
#2 -> JPY
#3 -> CAD
#4 -> INR

USD = c.get_rates('USD')
EUR = c.get_rates('EUR')
JPY = c.get_rates('JPY')
CAD = c.get_rates('CAD')
INR = c.get_rates('INR')

g = Graph(5)
g.addEdge(0, 1, -1*math.log(USD["EUR"]))
g.addEdge(0, 2, -1*math.log(USD["JPY"]))
g.addEdge(0, 3, -1*math.log(USD["CAD"]))
g.addEdge(0, 4, -1*math.log(USD["INR"]))

g.addEdge(1, 0, -1*math.log(EUR["USD"]))
g.addEdge(1, 2, -1*math.log(EUR["JPY"]))
g.addEdge(1, 3, -1*math.log(EUR["CAD"]))
g.addEdge(1, 4, -1*math.log(EUR["INR"]))

g.addEdge(2, 0, -1*math.log(JPY["USD"]))
g.addEdge(2, 1, -1*math.log(JPY["EUR"]))
g.addEdge(2, 3, -1*math.log(JPY["CAD"]))
g.addEdge(2, 4, -1*math.log(JPY["INR"]))

g.addEdge(3, 0, -1*math.log(CAD["USD"]))
g.addEdge(3, 1, -1*math.log(CAD["EUR"]))
g.addEdge(3, 2, -1*math.log(CAD["JPY"]))
g.addEdge(3, 4, -1*math.log(CAD["INR"]))

g.addEdge(4, 0, -1*math.log(INR["USD"]))
g.addEdge(4, 1, -1*math.log(INR["EUR"]))
g.addEdge(4, 2, -1*math.log(INR["JPY"]))
g.addEdge(4, 3, -1*math.log(INR["CAD"]))

# Print the solution
g.BellmanFord(0)
# This code is contributed by Neelam Yadav
