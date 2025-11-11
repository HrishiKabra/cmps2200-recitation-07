from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    while len(frontier) != 0:
        current = frontier.pop() # pop the last node from the frontier
        for neighbor in graph[current]: # for each neighbor of the current node
            if neighbor not in result:
                result.add(neighbor) # add the neighbor to the result set
                frontier.add(neighbor) # add the neighbor to the frontier
    return result





def connected(graph):
    if not graph: # if the graph is empty - return True
        return True
    start_node = next(iter(graph)) # get the first node in the graph
    return len(reachable(graph, start_node)) == len(graph) # check if graph is connected or not




def n_components(graph):
    """
    Returns:
      the number of connected components in an undirected graph
    """
    unvisited = set(graph.keys())
    components = 0
    while unvisited:
        start_node = next(iter(unvisited))
        visited = reachable(graph, start_node)
        unvisited -= visited
        components += 1
    return components

