class DGraph:
	def __init__(self):
		# a list of strings
		# list[str]
		self._nodes = []
		# a list of tuples that each have 2 strigns
		# list[tuple[str, str]]
		self._edges = []

	def newNode(self, n):
		self._nodes.append(n)

	def newEdge(self, s, d):
		self._edges.append((s, d))

	def getNodes(self):
		return self._nodes

	def getOut(self, n):
		"""
		returns the list of the nodes having an edge from
		the node n in the graph
		"""
		output = []

		for edge in self._edges:
			if edge[0] == n:
				output.append(edge[1])

		return output
