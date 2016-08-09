
def read_graph(data_file, reverse=False):
    graph = {}
    vertexes = set()
    n_edges = 0

    with open(data_file) as inf:
        for line in inf:
            sl = line.split()
            v_from = int(sl[0])
            vertexes.add(v_from)

            graph[v_from] = {}

            for r in sl[1:]:
                v_to, dist = [int(_) for _ in r.split(',')]
                vertexes.add(v_to)
                graph[v_from][v_to] = dist
                n_edges += 1

    # /2 : because edges are undirected
    return graph, len(vertexes), int(n_edges / 2)


def dijkstra(graph, start):
    queue = [(start, v_to, dist) for (v_to, dist) in graph[start].items()]
    current_vertex = start
    while queue:
        v_from, v_to, dist = queue.pop(0)
        X.add(v_from)

        if v_from != current_vertex:
            current_vertex = v_from

        new_dist =  A[v_from] + dist
        if v_to in A:
            if new_dist < A[v_to]:
                A[v_to] = new_dist
        else:
            A[v_to] = new_dist

        queue.extend([(v_to, v_to_next, dist)
                      for (v_to_next, dist) in graph[v_to].items()
                      if v_to_next not in X])
        
DEBUG = True

data_file = 'testData1.txt'

graph, n_vertexes, n_edges = read_graph(data_file)
print('finished reading graph with '
      '{0} vertexes and {1} edges'.format(n_vertexes, n_edges))

if DEBUG:
    print(graph)

all_vertexes = graph.keys()
starting_vertex = 1
X = set()
A = {starting_vertex: 0}
B = {starting_vertex: [starting_vertex]}

dijkstra(graph, 1)
print(A)
