import sys
sys.setrecursionlimit(100000)    # default: 1000


def read_graph(data_file, reverse=False):
    graph = {}
    vertexes = set()
    n_edges = 0

    with open(data_file) as inf:
        for line in inf:
            v_in, v_out = [int(_) for _ in line.split()]
            vertexes.add(v_in)
            vertexes.add(v_out)
            if reverse:
                if v_out not in graph:
                    graph[v_out] = {v_in}
                else:
                    graph[v_out].add(v_in)
            else:
                if v_in not in graph:
                    graph[v_in] = {v_out}
                else:
                    graph[v_in].add(v_out)
            n_edges += 1
    return graph, len(vertexes), n_edges


DEBUG = eval(sys.argv[1])

if DEBUG:
    data_file = 'small_SCC.txt'
    # data_file = 'small_SCC2.txt'
else:
    # data_file = 'small_SCC.txt'
    data_file = 'SCC.txt'

# recursive dfs doesn't because it results in over 20000 recursions, use FIFO

# explored = []
# entrypoints = []
# fin_times = {}
# fin_t = 1

# def dfs(graph, i):
#     """
#     :param i: node i
#     """
#     global fin_t
#     explored.append(i)
#     for j in graph[i]:
#         if j not in explored and j in graph:
#             dfs(graph, j)
#         else:
#             if not i in entrypoints:
#                 fin_times[i] = fin_t
#                 fin_t += 1


def dfs(graph, start, visited=None, fin_ts=None, fin_t=0):
    """
    :param fin_t: the time when a vertex is fully explored
    """
    if visited is None:
        visited = set()

    if fin_ts is None:
        fin_ts = {}

    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            if vertex in graph:
                stack.extend(graph[vertex] - visited)
        fin_t += 1
        fin_ts[vertex] = fin_t
    return visited, fin_ts, fin_t

graph, n_vertexes, n_edges = read_graph(data_file, reverse=True)
print('finished reading graph with '
      '{0} vertexes and {1} edges'.format(n_vertexes, n_edges))

print('===== first pass:')

if DEBUG:
    print(graph)

visited = set()
fin_ts = {}
fin_t = 0
entrypoints = []
for i in range(n_edges, 0, -1):
    if i in graph and i not in visited:
        entrypoints.append(i)
        visited, fin_ts, fin_t = dfs(graph, i, visited, fin_ts, fin_t)

#         for _ in reversed(explored[explored.index(i):]):
#             if _ not in fin_times:
#                 fin_times[_] = fin_t
#                 fin_t += 1

#     if i % 100000 == 0:
#         print('Processing Vertex {0}'.format(i))


if DEBUG:
    print('explored: ', visited)

# if DEBUG:
#     print('explored: ', explored)
#     print('finishing times: ', fin_times)
#     print('entrypoints: ', entrypoints)


sys.exit()


###############################################################################


explored = []
leaders = entrypoints = []
sccs = []

def dfs(graph, i):
    """
    :param i: node i
    """
    global scc
    explored.append(i)
    scc.add(i)
    for j in graph[i]:
        if j in graph and j not in explored:
            dfs(graph, j)
        else:
            if i not in leaders:
                print(i, scc)
                sccs.append(scc)
                scc = set()

graph, _, _ = read_graph(data_file)

print('===== second pass:')

if DEBUG:
    print(graph)

for (i, _) in sorted(fin_times.items(), key=lambda x: x[1], reverse=True):
    if i in graph and i not in explored:
        leaders.append(i)
        scc = set()
        dfs(graph, i)

if DEBUG:
    print('explored: ', explored)
    print('leaders: ', leaders)
    print('SCCs: ', sccs)
    # assert sccs == [{1, 4, 7}, {9, 3, 6}, {8, 2, 5}]

print(sorted(map(lambda x: len(x), sccs), reverse=True)[:5])
