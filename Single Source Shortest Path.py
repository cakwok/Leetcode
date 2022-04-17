'''
CS5800 HW6 Question 4 Bellman Ford for problem 2
'''
class Graph:

	def __init__(self, vertices):
		self.numofVertices = vertices # No. of vertices
		self.graph = []

	#add edges into graph
	def addEdge(self, u, v, weight):
		self.graph.append([u, v, weight])

	# utility function used to print the solution
	def printArr(self, distance):
		print("Vertex Distance from Source")
		for i in range(1, self.numofVertices + 1):
			print("{0}\t\t{1}".format(i, distance[i]))

	# The main function that finds shortest distances from src to
	# all other vertices using Bellman-Ford algorithm. The function
	# also detects negative weight cycle
	def BellmanFord(self, source):

		# Step 1: Initialize distances from src to all other vertices
		# as INFINITE
		distance = [float("Inf")] * (self.numofVertices + 1)
		distance[source] = 0


		# Step 2: Relax all edges |V| - 1 times. A simple shortest
		# path from src to any other vertex can have at-most |V| - 1
		# edges
		for i in range(self.numofVertices -1 ):
			# Update dist value and parent index of the adjacent vertices of
			# the picked vertex. Consider only those vertices which are still in
			# queue
			for u, v, weight in self.graph:
				if distance[u] != float("Inf") and distance[u] + weight < distance[v]:
						distance[v] = distance[u] + weight

		# Step 3: check for negative-weight cycles. The above step
		# guarantees shortest distances if graph doesn't contain
		# negative weight cycle. If we get a shorter path, then there
		# is a cycle.

		for u, v, weight in self.graph:
				if distance[u] != float("Inf") and distance[u] + weight < distance[v]:
						print("Graph contains negative weight cycle")
						return

		# print all distance
		self.printArr(distance)

'''
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
'''
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
