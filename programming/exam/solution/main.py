from DGraph import DGraph

## 1
def allIn(n ,g: DGraph):
	"""
	n: node
	g: graph
	returns a list of the nodes that are the source
	of the edges directed to the given node in the graph
	"""

	# list of nodes(string)
	# list[str]
	source_nodes = []

	for node in g.getNodes():
		if n in g.getOut(node):
			source_nodes.append(node)

	return source_nodes


## 2
graph = DGraph()

graph.newNode('a')
graph.newNode('b')
graph.newNode('c')
graph.newNode('d')

graph.newEdge('a', 'b')
graph.newEdge('a', 'd')
graph.newEdge('a', 'c')
graph.newEdge('b', 'd')
graph.newEdge('c', 'd')


## 3
print(graph.getOut('a'))


## 4
print(graph.getNodes())


## 5
print(allIn('d', graph))
