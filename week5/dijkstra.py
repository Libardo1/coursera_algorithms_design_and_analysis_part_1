import sys


def read_graph(data_file, reverse=False):
    graph = {}
    vertexes = set()
    n_edges = 0

    with open(data_file) as inf:
        for line in inf:
            sl = line.split()
            v_from = int(sl[0])
            vertexes.add(v_from)

            if v_from not in graph:
                # could've been added before for undirected edge
                graph[v_from] = {}

            for r in sl[1:]:
                v_to, dist = [int(_) for _ in r.split(',')]
                vertexes.add(v_to)
                graph[v_from][v_to] = dist
                n_edges += 1

                # add the edge to the adjacency list of v_to, too
                if v_to not in graph:
                    graph[v_to] = {v_from: dist}
                else:
                    graph[v_to][v_from] = dist

    # /2 : because edges are undirected
    return graph, len(vertexes), n_edges


def get_crossing_edges(graph, X):
    """
    This function should be improved, once a vertex is added to X, all edges
    from other vertexes in X to it doesn't need to be concerned anymore
    """
    for v_from in X:
        for (v_to, dist) in graph[v_from].items():
            if v_to not in X:
                yield v_from, v_to, dist


def dijkstra(graph, start):
    # stores explored vertexes
    X = set()
    # stores shortest distance from start to any vertex
    dists = {start: 0}
    # stores the corresponding shortest path from start to any vertex
    paths = {start: [start]}

    X.add(start)

    all_vertexes = len(graph)
    while len(X) < all_vertexes:
        min_v_from, min_v_to, min_greedy_score = None, None, 10000000
        for (v_from, v_to, dist) in get_crossing_edges(graph, X):
            greedy_score = dists[v_from] + dist
            if greedy_score < min_greedy_score:
                min_greedy_score = greedy_score
                min_v_to = v_to
                min_from_to = v_from
        dists[min_v_to] = min_greedy_score
        paths[min_v_to] = paths[min_from_to] + [min_v_to]
        X.add(min_v_to)
    return dists, paths



def assertEqual(a, b):
    try:
        assert a == b
    except AssertionError as err:
        print(('{0} != {1}'.format(a, b)))



def test0():
    data_file = 'testData0.txt'
    graph, n_vertexes, n_edges = read_graph(data_file)
    print('finished reading graph with '
          '{0} vertexes and {1} edges'.format(n_vertexes, n_edges))

    dists, paths = dijkstra(graph, 1)
    assertEqual(dists, {1: 0, 2: 1, 3: 3, 4: 6})
    assertEqual(paths, {1: [1], 2: [1, 2], 3: [1, 2, 3], 4: [1, 2, 3, 4]})


def test1():
    data_file = 'testData1.txt'
    graph, n_vertexes, n_edges = read_graph(data_file)
    print('finished reading graph with '
          '{0} vertexes and {1} edges'.format(n_vertexes, n_edges))

    dists, paths = dijkstra(graph, 1)
    assertEqual(dists, {1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 4, 7: 3, 8: 2})
    assertEqual(paths, {
        1: [1],
        2: [1, 2],
        3: [1, 2, 3],
        4: [1, 2, 3, 4],
        5: [1, 2, 3, 4, 5],
        6: [1, 8, 7, 6],
        7: [1, 8, 7],
        8: [1, 8]
    })


def test3():
    data_file = 'testData3.txt'
    graph, n_vertexes, n_edges = read_graph(data_file)
    print('finished reading graph with '
          '{0} vertexes and {1} edges'.format(n_vertexes, n_edges))

    dists, paths = dijkstra(graph, 1)
    assertEqual(dists, {1:0, 2:1, 3:4, 4:5, 5:3, 6:4, 7:3, 8:2, 9:3, 10:6, 11:5})


def test4():
    data_file = 'testData4.txt'
    graph, n_vertexes, n_edges = read_graph(data_file)
    print('finished reading graph with '
          '{0} vertexes and {1} edges'.format(n_vertexes, n_edges))

    dists, paths = dijkstra(graph, 1)
    assertEqual(dists, {1:0, 2:1, 3:2, 4:3, 5:5})


def test5():
    data_file = 'testData5.txt'
    graph, n_vertexes, n_edges = read_graph(data_file)
    print('finished reading graph with '
          '{0} vertexes and {1} edges'.format(n_vertexes, n_edges))
    # print(graph)
    # for i in graph:
    #     for j in graph[i].keys():
    #         if i > j:
    #             print('{0} -> {1}'.format(i, j))

    dists, paths = dijkstra(graph, 1)
    assertEqual(dists, {1: 0, 2: 1, 3: 4, 4: 3, 5: 11, 6: 7, 7: 2, 8: 8, 9: 10, 10: 9})

def test6():
    data_file = 'testData6.txt'
    graph, n_vertexes, n_edges = read_graph(data_file)
    print('finished reading graph with '
          '{0} vertexes and {1} edges'.format(n_vertexes, n_edges))

    dists, paths = dijkstra(graph, 1)
    assertEqual(dists, {1:0, 2:3, 3:2, 4:4, 5:5, 6:5})

DEBUG = eval(sys.argv[1])

if DEBUG:
    test0()
    test1()
    # test2()                     # test2 doesn't have ground truth in the forum
    test3()
    test4()
    test5()
    test6()

else:
    data_file = 'dijkstraData.txt'
    graph, n_vertexes, n_edges = read_graph(data_file)
    print('finished reading graph with '
          '{0} vertexes and {1} edges'.format(n_vertexes, n_edges))
    starting_vertex = 1
    dists, paths = dijkstra(graph, starting_vertex)

    # generate answer
    ans = []
    for i in [7, 37, 59, 82, 99, 115, 133, 165, 188, 197]:
        if i in dists:
            ans.append(dists[i])
        else:
            ans.append(1000000)
    print(','.join(map(str, ans)))
