import itertools

import sys


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


def dfs_first_pass(graph, start, visited, fin_t):
    """
    # Don't use recursive dfs doesn't because it results in over 20000
    # recursions, use iterative method with a FIFO stack instead

    :param fin_t: the starting finishing time when a vertex is fully explored
    """
    fin_ts = {}
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            # http://stackoverflow.com/questions/24051386/kosaraju-finding-finishing-time-using-iterative-dfs
            stack.append(vertex)   # added it back for backtracking

            if vertex in graph: # depth first
                stack.extend(graph[vertex] - visited)
        else:
            if vertex not in fin_ts:
                fin_ts[vertex] = fin_t
                fin_t += 1
    
    return visited, fin_ts, fin_t


def dfs_second_pass(graph, start, visited):
    scc = set()
    stack = [start]
    while stack:
        vertex = stack.pop()

        # otherwise, if vertex is in visited, it could be in a SCC previously
        # explored
        if vertex not in visited:
            scc.add(vertex)
            visited.add(vertex)
            if vertex in graph:
                stack.extend(graph[vertex] - scc)
    return visited, scc


def main(data_file):
    graph, n_vertexes, n_edges = read_graph(data_file, reverse=True)
    print('finished reading graph with '
          '{0} vertexes and {1} edges'.format(n_vertexes, n_edges))

    print('===== first pass:')

    if DEBUG:
        print(graph)

    visited, fin_ts, fin_t = set(), {}, 1
    for i in range(n_vertexes, 0, -1):
        if i in graph and i not in visited:
            visited, subfin_ts, fin_t = dfs_first_pass(graph, i, visited, fin_t)
            fin_ts.update(subfin_ts)

        if i % 100000 == 0:
            print('Processing Vertex {0}. len(visited): {1}'.format(i, len(visited)))

    print('sorting vertexes by finishing times...')
    sorted_visited_items = sorted(fin_ts.items(), key=lambda x: x[1], reverse=True)
    
    if DEBUG:
        print('visited: ', visited)
        print('pairs of (vertex, finishing_time):')
        for item in sorted_visited_items:
            print(item)

    ###############################################################################

    graph, _, _ = read_graph(data_file)

    print('===== second pass:')

    if DEBUG:
        print(graph)

    # visited is equivalent of the union of all sets in sccs, but union each
    # time after a scc is returned is too slow, so keep both visited and sccs
    visited, sccs, leaders = set(), [], []
    for k, (i, _) in enumerate(sorted_visited_items):
        if i in graph:
            if i not in visited:
                leaders.append(i)
                visited, scc = dfs_second_pass(graph, i, visited)
                sccs.append(scc)
        else:    # else is important for vertexes that have only incoming edges
            leaders.append(i)
            visited.add(i)
            sccs.append(set([i]))

        if k % 100000 == 0:
            print('Processing Vertex {0}. len(visited): {1}'.format(k, len(visited)))

    if DEBUG:
        print('visited: ', visited)
        print('leaders: ', leaders)
        print('SCCs: ', sccs)

    print('sorting SCCs by size...')
    res = sorted(map(lambda x: len(x), sccs), reverse=True)[:5]

    if len(res) < 5:
        res.extend([0] * (5 - len(res)))
    sizes = (','.join(map(str, res)))
    print('sizes of largest 5 SCCs: {0}'.format(sizes))
    return sizes

DEBUG = eval(sys.argv[1])

def assertEqual(a, b):
    try:
        assert a == b
    except AssertionError as err:
        print(('{0} != {1}'.format(a, b)))


if DEBUG:
    assertEqual(main('small_SCC.txt'),  '3,3,3,0,0')
    assertEqual(main('small_SCC2.txt'),  '3,3,2,0,0')
    assertEqual(main('small_SCC3.txt'),  '3,3,3,0,0')
    assertEqual(main('small_SCC4.txt'),  '3,3,2,0,0')
    assertEqual(main('small_SCC5.txt'),  '3,3,1,1,0')
    assertEqual(main('small_SCC6.txt'),  '7,1,0,0,0')
    assertEqual(main('small_SCC7.txt'),  '6,3,2,1,0')
else:
    print(main('SCC.txt'))
