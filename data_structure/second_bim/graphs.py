from django.db.migrations import graph
from pip._vendor.requests.packages.urllib3.connectionpool import xrange

__author__ = 'rene_'

from pythonds.graphs import PriorityQueue, Vertex

######################
##### chapter 8 ######
######################

######################
#####    BFS    ######
######################
def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited


def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None

######################
#####    DFS    ######
######################
def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        #print(vertex)
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


def dfs_recursive(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    #print(start)
    for next in graph[start] - visited:
        dfs_recursive(graph, next, visited)
    return visited


def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


def dfs_paths_recursive(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for next in graph[start] - set(path):
        yield from dfs_paths_recursive(graph, next, goal, path + [next])


######################
##### chapter 9 ######
######################

#===================

######################
####### Tarjan #######
######################

points = []
marked_stack = []
marked = []

g = None

def dfs_cycles(graph, static_vertice, vertice, flag):
    global g, points, marked, marked_stack
    points.append(vertice)
    marked_stack.append(vertice)
    marked[vertice] = True

    print('points input = ', points)
    print('marked_stack input = ', marked_stack)
    print('marked input = ', marked)

    for w in graph[vertice][:]:
        print('w = ', w, ' s = ', static_vertice)
        if w < static_vertice:
            print('w < static_vertice = ', graph[vertice])
            graph[vertice].pop(graph[vertice].index(w))
            print('w < static_vertice = pop()', graph[vertice])
        elif w == static_vertice:
            print(points)
            flag = True
        elif marked[w] == False:
            print('marked[w] == False', marked[w])
            if flag == g and flag == False:
                flag = False
            else:
                flag = True
            print("recursao dentro com flag = ", flag, "e flag g = ", g)
            dfs_cycles(graph, static_vertice, w, g)

    g = flag
    print("flag fora = ", flag)
    if flag == True:
        u = marked_stack.pop()
        while (u != vertice):
            marked[u] = False
            u = marked_stack.pop()
        #v is now deleted from mark stacked,
        # and has been called u unmark v
        marked[u] = False
    print("points = ", points)
    points.pop(points.index(vertice))
    print("points.pop = ", points)

def tarjan_cycles(graph):
    global points, marked_stack, marked
    size = len(graph)

    for i in xrange(0,size):
        marked.append(False)

    for i in xrange(0,size):
        points = []
        #print("i = ", i)
        dfs_cycles(graph,i,i, False)
        while (len(marked_stack) > 0):
            u = marked_stack.pop()
            marked[u] = False
        print('SAIU')

    print('points = ', points)

#===================
expl = []
comp = []
edges = {}
ce = 0
cc = 0

def tarjan_edges(graph):
    global expl,comp
    size = len(graph)

    for vertex in xrange(0, size):
        expl.append(0)
        comp.append(0)

    for vertex in xrange(0, size):
        if expl[vertex] == 0:
            dfs_edges(graph, vertex)

    print("edges = ", edges)
    return edges

def dfs_edges(graph, vertex):
    global ce,cc,expl,comp, edges
    ce += 1
    expl[vertex] = ce

    for w in graph[vertex][:]:
        if expl[w] == 0:
            edges[(vertex,w)] = 'tree'
            dfs_edges(graph, w)
        else:
            if expl[w] > expl[vertex]:
                edges[(vertex, w)] = 'forward'
            else:
                if comp[w] > 0:
                    edges[(vertex, w)] = 'cross'
                else:
                    edges[(vertex, w)] = 'back'
    cc+=1
    comp[vertex] = cc

#===================
expl2 = []
comp2 = []
sort_stack = []
ce2 = 0
cc2 = 0

def tarjan_topological_sort(graph):
    global cc2,ce2,expl2,comp2,sort_stack
    topological_sort = []
    size = len(graph)

    for vertex in xrange(0, size):
        expl2.append(0)
        comp2.append(0)

    for vertex in xrange(0, size):
        if expl2[vertex] == 0:
            dfs_topological_sort(graph, vertex)

    for vertex in xrange(0,size):
        topological_sort.append(sort_stack.pop())
        #ord.append(size-comp2[vertex]+1)
    print('topological_sort = ', topological_sort)
    return topological_sort

def dfs_topological_sort(graph, vertex):
    global ce2, cc2, expl2, comp2, sort_stack
    ce2 += 1
    expl2[vertex] = ce2

    for w in graph[vertex][:]:
        if expl2[w] == 0:
            dfs_topological_sort(graph, w)
    cc2 += 1
    comp2[vertex] = cc2
    sort_stack.append(vertex)

#===================
expl3 = []

def tarjan_coloring(graph):
    global expl3
    topological_sort = []
    size = len(graph)

    for vertex in xrange(0, size):
        expl3.append(0)

    for vertex in xrange(0, size):
        if expl3[vertex] == 0:
            if dfs_coloring(graph, vertex, 2) == 0:
                print('ERROR COLORING')
                return 0 #ERROR
    print('SUCCESS COLOR')
    return 1 #SUCCESS

def dfs_coloring(graph, vertex, color):
    global expl3
    c = (color % 2) + 1
    expl3[vertex] = c
    for w in graph[vertex]:
        if expl3[w] == 0:
            if dfs_coloring(graph, w, c) == 0:
                return 0
        else:
            if expl3[w] == c:
                return 0
    return 1

#===================

scc_stack = []
scc = []
expl4 = []
ce4 = 0

def tarjan_scc(graph):
    global stack, ce4, expl4,scc
    stack = []

    size = len(graph)

    for vertex in xrange (0,size):
        expl4.append(0)
        scc.append(0)

    for vertex in xrange(0, size):
        if expl4[vertex] == 0:
            dfs_scc(graph, vertex)

    print('ssc = ', scc)
    return scc

def dfs_scc(graph, vertex):
    global scc_stack, expl4, ce4, scc
    ce4 += 1
    expl4[vertex] = ce4
    scc_stack.append(vertex)
    scc[vertex] = expl4[vertex]

    for w in graph[vertex][:]:
        print('w - ', w)
        if expl4[w] == 0:
            dfs_scc(graph, w)
            scc[vertex] = min(scc[vertex], scc[w])
            print('min(scc[vertex], scc[w])', min(scc[vertex], scc[w]))
        else:
            print('else')
            for i in scc_stack:
                print('i', i, 'w', w)
                if w is i:
                    scc[vertex] = min(scc[vertex], expl4[w])
                    print('min(scc[vertex], expl4[w])', min(scc[vertex], expl4[w]))
                    break
    if scc[vertex] == expl4[vertex]:
        print('clean stack')
        while True:
            x = scc_stack.pop()
            print('x = ', x , 'vertex = ', vertex)
            if x == vertex:
                break


#===================

cut_vertex = []
n_kids = []
dad = []
expl5 = []
m = []
ce5 = 0

def tarjan_cut_vertex(graph, start):
    global ce5, expl5, dad, n_kids, cut_vertex
    size = len(graph)

    for i in xrange (0,size):
        expl5.append(0)
        dad.append(0)
        n_kids.append(0)
        cut_vertex.append(False)
        m.append(0)

    dfs_cut_vertex(graph, start)
    cut_vertex[start] = (n_kids[start] > 1)

    for vertex in xrange(0,size):
        if vertex not in graph[start]:
            print(dad, dad[vertex])
            p = dad[vertex]
            cut_vertex[p] = cut_vertex[p] or (m[vertex]>=expl5[p])

    for vertex in xrange(0,size):
        if cut_vertex[vertex]:
            print('cut = ', vertex)

def dfs_cut_vertex(graph, vertex):
    global expl5, ce5, m, dad,n_kids
    ce5 += 1
    expl5[vertex] = ce5
    m[vertex] = expl5[vertex]

    for w in list(graph[vertex]):
        if expl5[w] == 0:
            dad[w] = vertex
            n_kids[vertex] += 1
            dfs_cut_vertex(graph, w)
            m[vertex] = min(m[vertex], m[w])
        else:
            print('aresta de retorno')
            if w != dad[vertex]:
                m[vertex] = min(m[vertex], expl5[w])

#===================

expl6 = []
dad6 = []
m6 =[]
edges6 = {}
ce6 = 0

def tarjan_cut_edge(graph, start):
    global ce6, dad6, expl6, m6

    size = len(graph)

    for i in xrange(0,size):
        expl6.append(0)
        dad6.append(None)
        m6.append(0)

    return dfs_cut_edge(graph, start)

def dfs_cut_edge(graph, vertex):
    global ce6, expl6, m6, edges6
    ce6+=1
    expl6[vertex] = ce6
    m6[vertex] = expl6[vertex]

    for w in list(graph[vertex]):
        if expl6[w] == 0:
            dad6[w] = vertex
            dfs_cut_edge(graph, w)
            m6[vertex] = min(m6[vertex], m6[w])
            if m6[w] == expl6[w]:
                print('aresta de corte', vertex, ":", w)
                edges6[(vertex, w)] = 'cut_edge'
        else:
            if w != dad6[vertex]:
                m6[vertex] = min(m6[vertex], expl6[w])
    return edges6

######################
##### dijkstra  ######
#from: http://www.thedatagent.com/2015/12/10/dijkstras-algorithm-python/
######################

def dijkstra(graph_dict, start, end):
    """
    This function implements Dijkstra's Shortest Path

    It takes as its inputs:
        i. a graph represented by a "dictionary
           of dictionaries" structure,
           i.e. {node: {neighbour: weight};
        ii. a starting node in that graph; and
        iii. an ending node for that graph

    The algorithm returns:
     i. the shortest path with
     ii. its associated cost
    """
    # empty dictionary to hold distances
    distances = {}
    # list of vertices in path to current vertex
    predecessors = {}

    # get all the nodes that need to be assessed
    to_assess = graph_dict.keys()

    # set all initial distances to infinity
    #  and no predecessor for any node
    for node in graph_dict:
        distances[node] = float('inf')
        predecessors[node] = None

    # set the initial collection of
    # permanently labelled nodes to be empty
    sp_set = []

    # set the distance from the start node to be 0
    distances[start] = 0

    # as long as there are still nodes to assess:
    while len(sp_set) < len(to_assess):

        # chop out any nodes with a permanent label
        still_in = {node: distances[node]\
                    for node in [node for node in\
                    to_assess if node not in sp_set]}

        # find the closest node to the current node
        closest = min(still_in, key = distances.get)

        # and add it to the permanently labelled nodes
        sp_set.append(closest)

        # then for all the neighbours of
        # the closest node (that was just added to
        # the permanent set)
        for node in graph_dict[closest]:
            # if a shorter path to that node can be found
            if distances[node] > distances[closest] +\
                       graph[closest][node]['weight']:

                # update the distance with
                # that shorter distance
                distances[node] = distances[closest] +\
                       graph[closest][node]['weight']

                # set the predecessor for that node
                predecessors[node] = closest

    # once the loop is complete the final
    # path needs to be calculated - this can
    # be done by backtracking through the predecessors
    path = [end]
    while start not in path:
        path.append(predecessors[path[-1]])

    # return the path in order start -> end, and it's cost
    return path[::-1], distances[end]


def kruskal():
    return ""

def prim():
    return ""


def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    # if not graph.has_key(start):
    #     return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None
