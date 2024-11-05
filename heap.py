def parent(i):
    """Return the index of the parent of the node at index i.
    
    Args:
        i (int): The index of the current node.
        
     Returns:
        int: The index of the parent node.
    """
    return (i - 1) // 2

def left(i):
    """Return the index of the left child of the node at index i.
        
    Args:
        i (int): The index of the current node.
        
    Returns:
        int: The index of the left child node.
    """
    return 2 * i + 1

def right(i):
    """Return the index of the right child of the node at index i.
        
    Args:
        i (int): The index of the current node.
        
    Returns:
        int: The index of the right child node.
    """
    return 2 * i + 2

def max_heapify_iterative(A, i):
    """This function modifies the heap in place to ensure the max-heap property is maintained for the subtree at index i
        
        The property:
            the value of each parent node is greater than or equal to the values of its children

    
    Args:
        A (Heap): The heap object containing the array and its size.
        i (int): The index of the node to heapify.
    """
    while True:
        l = left(i)
        r = right(i)
        largest = i

        if l < A.heap_size and A.array[l] > A.array[largest]:
            largest = l

        if r < A.heap_size and A.array[r] > A.array[largest]:
            largest = r

        if largest != i:
            A.array[i], A.array[largest] = A.array[largest], A.array[i]
            i = largest
        else:
            break

class Heap:
    """A class for a max-heap.
    
    Attributes:
        array (list): The list of elements in the heap, representing the heap structure.
        heap_size (int): The current number of elements in the heap.
    """
    def __init__(self, array):
        """Initialize the heap with an array by converting the given array into a max-heap by calling the build_max_heap function.
        
        Args:
            array (list): The initial array to be converted into a heap.
        """
        self.array = array
        self.heap_size = len(array)

def build_max_heap(A):
    """Convert the given array into a max-heap.
    
    This function processes each non-leaf node in the array and applies max_heapify
    to ensure that the max-heap property is satisfied throughout.
    It works in a loop until the last point by decrementing by 1 each time.
    
    Args:
        A (Heap): The heap object containing the array to be heapified.
    """
    A.heap_size = len(A.array)
    for i in range((len(A.array) // 2) - 1, -1, -1):
        max_heapify_iterative(A, i)

def heap_sort(A):
    """Sort the array in ascending order using heap sort.
    
    This function first builds a max-heap from the input array, then repeatedly 
    extracts the maximum element from the heap and rebuilds the heap until the 
    array is sorted. 
    Note: It decrements the size each time 
    
    Args:
        A (Heap): The heap object containing the array to be sorted.
    """
    build_max_heap(A)
    for i in range(len(A.array) - 1, 0, -1):
        A.array[0], A.array[i] = A.array[i], A.array[0]
        A.heap_size -= 1
        max_heapify_iterative(A, 0)

A = Heap([7, 9, 10, 4, 5])
heap_sort(A)
print(A.array)  # Prints the sorted array


class Graph:
    """A class representing an undirected graph using an adjacency list.
    
    The graph is represented as a dictionary where each key is a node and 
    its value is a list of neighboring nodes.
    
    Attributes:
        adjacency_list (dict): A dictionary mapping each node to its neighbors.
    """
    def __init__(self):
        """Initialize an empty graph."""
        self.adjacency_list = {}

    def add_edge(self, source, destination):
        """Add an edge between the source and destination nodes.
        
        If either node does not exist in the graph, it is added.
        
        Args:
            source: The starting node of the edge.
            destination: The ending node of the edge.
        """
        if source not in self.adjacency_list:
            self.adjacency_list[source] = []
        if destination not in self.adjacency_list:
            self.adjacency_list[destination] = []
        self.adjacency_list[source].append(destination)
        self.adjacency_list[destination].append(source)

    def bfs(self, start, goal):
        """Implementation of the breadth-first search to find a path from a start point to a goal point.
        
        This function uses a queue to explore the graph level by level, 
        recording visited nodes and tracking the path taken. If the goal is found,
        it prints the path.If the path does not exist, it returns a not found message
        
        Args:
            start: The starting node for the search.
            goal: The target node to find.
        """
        visited = set()
        queue = [(start, [start])]

        while queue:
            current, path = queue.pop(0)
            if current in visited:
                continue
            visited.add(current)
            if current == goal:
                print("Path:", " -> ".join(path))
                return
            for neighbor in self.adjacency_list.get(current, []):
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
        print("Path not found.")

    def dfs(self, current, goal, visited=None, path=None):
        """Perform depth-first search to find a path from current to goal.
        
        This function explores as far as possible along each branch before backtracking.
        If the goal is found, it prints the path taken.
        The code uses a recursive call to itself everytime it moves to a neighbour node that is not visited.
        
        Args:
            current: The current node in the search.
            goal: The target node to find.
            visited (set): A set of visited nodes to avoid cycles.
            path (list): The current path taken while searching.
        
        """
        if visited is None:
            visited = set()
        if path is None:
            path = []

        visited.add(current)
        path.append(current)

        if current == goal:
            print("Path:", " -> ".join(path))
            return

        for neighbor in self.adjacency_list.get(current, []):
            if neighbor not in visited:
                self.dfs(neighbor, goal, visited, path)

        path.pop()  

def parse_cities_file(filename):
    """Parse a file to create a graph of cities.
    
    This function reads a file containing city connections and constructs an undirected graph
    by adding edges for each connection found in the file.
        
    Returns:
        Graph: The constructed graph containing the city connections.
    """
    graph = Graph()
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 3:
                source, destination, _ = parts
                graph.add_edge(source, destination)
    return graph

# Example to check if it works
graph = parse_cities_file('cities.txt')
graph.bfs('Oradea', 'Bucharest')  
graph.dfs('Oradea', 'Bucharest')