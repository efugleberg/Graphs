from graph import Graph
from util import Stack


def earliest_ancestor(ancestors, starting_node):
    ancestor_graph = Graph()
    for i in ancestors:
        ancestor_graph.add_vertex(i[0])
        ancestor_graph.add_vertex(i[1])
    for i in ancestors:
        ancestor_graph.add_edge(i[1], i[0])

    if ancestor_graph.vertices[starting_node] == set():
        return -1
    stack = Stack()
    visited = set()
    stack.push([starting_node])
    farthest_path = [-1]
    while stack.size() > 0:
        path = stack.pop()
        vertex = path[-1]
        if vertex not in visited:
            if ancestor_graph.vertices[vertex] == set():
                if len(path) > len(farthest_path):
                    farthest_path = list(path)
                elif len(path) == len(farthest_path):
                    if path[-1] < farthest_path[-1]:
                        farthest_path = list(path)
            visited.add(vertex)
            for next_vert in ancestor_graph.vertices[vertex]:
                new_path = list(path)
                new_path.append(next_vert)
                stack.push(new_path)
    return farthest_path[-1]
