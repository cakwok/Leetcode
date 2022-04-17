'''
CS5800 HW6 Q4 Bellman Ford Implementation
'''
class Graph:

	def __init__(self, vertices):
		self.numofVertices = vertices 	# No. of vertices
		self.graph = []					#list of list of edges

	#add edges to graph
	def addEdge(self, u, v, weight):
		self.graph.append([u, v, weight])

	# print out distance of vertex to source
	def print_SingleSourceShortestPath(self, distance, source):
		print("Vertex\t Distance to Source")
		for i in range(source, self.numofVertices + source):	# "source" to tailer printout index.  sometimes source is S which is 0, sometimes it's A, of which is intrintively 1
			print("{0}\t\t{1}".format(i, distance[i]))
		print("\n")

	#Implement Bellman Ford to find single source shortest path, and detection of negative weight cycle
	def BellmanFord(self, source):

		distance = [float("Inf")] * (self.numofVertices + 1)
		distance[source] = 0

		# Edge relaxation
		for i in range(self.numofVertices - 1):
			for u, v, weight in self.graph:
				#print ("u, v, weight", u, v, weight)
				#print("distance[u] + weight, u ", distance[u], weight )
				if distance[u] != float("Inf") and distance[v] > distance[u] + weight  :
						distance[v] = distance[u] + weight
						#print ("v", v, "distance[v]", distance[v], "\n")

		# Detect negative weight cycle.  Parent distance + weight shouldn't be less than child distance
		for u, v, weight in self.graph:
				if distance[u] != float("Inf") and distance[v] > distance[u] + weight:
						print(u, v, "in negative weight cycle", "\n")
						return

		# print all distance
		self.print_SingleSourceShortestPath(distance, source)

		return

#-----------------
print("4a. Graph for problem 2")

g = Graph(8)  #create 8 vertexes into the graph

g.addEdge(1, 2, 1)  #create edges and run in this sequence
g.addEdge(1, 5, 4)
g.addEdge(1, 6, 8)
g.addEdge(2, 3, 2)
g.addEdge(2, 6, 6)
g.addEdge(2, 7, 6)
g.addEdge(3, 4, 1)
g.addEdge(3, 7, 2)
g.addEdge(4, 7, 1)
g.addEdge(4, 8, 4)
g.addEdge(5, 6, 5)
g.addEdge(7, 6, 1)
g.addEdge(7, 8, 1)

g.BellmanFord(1)    # Run BellmanFord with "1" as source

#-----------------
print("4b.  Graph for Figure 4.14 P124 DPV")

g = Graph(8)

g.addEdge(0, 1, 10)
g.addEdge(0, 7, 8)
g.addEdge(1, 5, 2)
g.addEdge(2, 1, 1)
g.addEdge(2, 3, 1)
g.addEdge(3, 4, 3)
g.addEdge(4, 5, -1)
g.addEdge(5, 2, -2)
g.addEdge(6, 1, -4)
g.addEdge(6, 5, -1)
g.addEdge(7, 6, 1)

g.BellmanFord(0)

#-----------------
print("4c.  Graph for Figure 24.4 P652 CLRS")

g = Graph(5)

g.addEdge(1, 2, 6)
g.addEdge(1, 4, 7)
g.addEdge(2, 3, 5)
g.addEdge(2, 4, 8)
g.addEdge(2, 5, -4)
g.addEdge(3, 2, -2)
g.addEdge(4, 3, -3)
g.addEdge(4, 5, 9)
g.addEdge(5, 1, 2)
g.addEdge(5, 3, 7)

g.BellmanFord(1)

#-----------------
print("4d.  Graph for Figure 24.1 P646 CLRS i")

g = Graph(11)

g.addEdge(0, 1, 3)
g.addEdge(0, 3, 5)
g.addEdge(0, 5, 2)
g.addEdge(1, 2, -4)
g.addEdge(2, 7, 4)
g.addEdge(3, 4, 6)
g.addEdge(4, 3, -3)
g.addEdge(4, 7, 8)
g.addEdge(5, 6, 3)
g.addEdge(6, 5, -6)
g.addEdge(6, 7, 7)

g.BellmanFord(0)

#-----------------
print("4e.  Graph for Figure 24.1 P646 CLRS ii")

g = Graph(3)

g.addEdge(1, 2, 2)
g.addEdge(2, 3, 3)
g.addEdge(3, 1, -8)

g.BellmanFord(1)
