from util import Stack, Queue  # These may come in handy

class Graph:

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):

        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):

        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError('vertex does not exist')

    def get_neighbors(self, vertex_id):

        return self.vertices[vertex_id]

    def bft(self, starting_vertex):

        q = Queue()
        # store starting vertex
        q.enqueue(starting_vertex)

        visited = set()

        while q.size():
            # dequeue the first vertex
            v = q.dequeue()

            # if the vertex is not in visited set
            if v not in visited:
                # add to visited
                visited.add(v)
                print(v)

                # add the neighbors to the queue
                neighbors = self.get_neighbors(v)
                for neighbor in neighbors:
                    q.enqueue(neighbor)

    def dft(self, starting_vertex):

        s = Stack()
        # add starting vertex to the stack
        s.push([starting_vertex])
        visited = set()
        path = []
        while s.size() > 0:
            path = s.pop()
            current_vertex = path[-1]
            # if this vertex is not in visited set
            if current_vertex not in visited:
                # add it to visited
                visited.add(current_vertex)

                # add the neighbors to the stack 
                for neighbor in self.get_neighbors(current_vertex):
                    path.append(neighbor)
                    s.push(path)
        return path

    def dft_recursive(self, starting_vertex, visited=None):

        # create visited set if instantiated at None
        if visited is None:
            visited = set()

        # check if starting index is in visited
        if starting_vertex not in visited:
            # add to visited
            visited.add(starting_vertex)
            print(starting_vertex)

            # call recursively for each neighbor of the starting index
            for vrtx in self.get_neighbors(starting_vertex):
                self.dft_recursive(vrtx, visited)

    def bfs(self, starting_vertex, destination_vertex):

        visited = set()
        q = Queue()
        # add starting vertex to the queue as a list
        q.enqueue([starting_vertex])

        while q.size():
            # dequeue the current path
            path = q.dequeue()
            # store the last vertex in the path
            node = path[-1]

            # check if it is in visited
            if node not in visited:
                # add to visited
                visited.add(node)
                # check for target, return path
                if node == destination_vertex:
                    return path
                else:
                    # enqueue the path to each neighbor
                    for neighbor in self.get_neighbors(node):
                        q.enqueue(path + [neighbor])

        return None

    def dfs(self, sv, dv):

        if sv not in dv:
            return []

        s = Stack()
        s.push([sv])

        visited = []

        while s.size():
            path = s.pop()

            # Get the last vertex in the path
            v = path[-1]

            # mark visited
            if v not in visited:
                visited.append(v)

            # add path to parents to the stack
            # if the vertex has no parents, it sets dict value to empty list
            for parent in dv.get(v, []):
                s.push(path + [parent])

        # return the last visited vertex, this will be the highest level parent
        return visited[-1]

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=set(), path=[]):

        if path == []:
            path = [starting_vertex]

        # base case, if we have visited all nodes we will not recurse
        if starting_vertex not in visited:
            visited.add(starting_vertex)

            if starting_vertex == destination_vertex:
                return path

            # loop over neighbors
            for neighbor in self.get_neighbors(starting_vertex):
                # store the depth first path of the starting vertex, recursively call passing in visited and the new path including the neighbor
                result = self.dfs_recursive(
                    neighbor, destination_vertex, visited, path + [neighbor])
                # if our recursive call returns a path, it will be returned here
                if result:
                    return result

        return None

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
