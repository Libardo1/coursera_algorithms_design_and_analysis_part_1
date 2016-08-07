import sys
sys.setrecursionlimit(100000)    # default: 1000


def read_graph(data_file, reverse=False):
    graph = {}
    max_n = 0

    with open(data_file) as inf:
        for line in inf:
            v_in, v_out = [int(_) for _ in line.split()]
            max_n = max(v_in, v_out, max_n)
            if reverse:
                if v_out not in graph:
                    graph[v_out] = [v_in]
                else:
                    graph[v_out].append(v_in)
            else:
                if v_in not in graph:
                    graph[v_in] = [v_out]
                else:
                    graph[v_in].append(v_out)
    return graph, max_n

DEBUG = False

if DEBUG:
    data_file = 'small_SCC.txt'
else:
    # data_file = 'small_SCC.txt'
    data_file = 'SCC.txt'

explored = []
entrypoints = []
fin_times = {}
fin_t = 1


def dfs(graph, i):
    """
    :param i: node i
    """
    global fin_t
    global last_vertex
    explored.append(i)
    for j in graph[i]:
        if j in graph and j not in explored:
            dfs(graph, j)
        else:
            if not i in entrypoints:
                fin_times[i] = fin_t
                fin_t += 1
                # print(fin_times)
                # print(explored)

graph, max_n = read_graph(data_file, reverse=True)
print(max_n)


if DEBUG:
    print(graph)

for i in range(max_n, 0, -1):
    if i in graph and i not in explored:
        entrypoints.append(i)
        dfs(graph, i)

        for _ in reversed(explored):
            if _ not in fin_times:
                fin_times[_] = fin_t
                fin_t += 1

if DEBUG:
    print('=' * 20)
    print(explored)
    print(fin_times)
    print(entrypoints)


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
                sccs.append(scc)
                scc = set()


graph, _ = read_graph(data_file)

if DEBUG:
    print(graph)

for (i, _) in sorted(fin_times.items(), key=lambda x: x[1], reverse=True):
    if i in graph and i not in explored:
        leaders.append(i)
        scc = set()
        dfs(graph, i)

if DEBUG:
    print('=' * 20)
    print(explored)
    print(fin_times)
    print(leaders)
    print(sccs)

print(sorted(map(lambda x: len(x), sccs), reverse=True)[:5])
