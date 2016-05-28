__author__ = 'rene_'

######################
##### chapter 8 ######
######################

def bfs():
    return ""

def dfs():
    return ""

######################
##### chapter 9 ######
######################

def tarjan():
    return ""

def dijkstra():
    return ""

def kruskal():
    return ""

def prim():
    return ""


def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if not graph.has_key(start):
        return None
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath: return newpath
    return None
