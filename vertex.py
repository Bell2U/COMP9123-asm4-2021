"""
Vertex
=======

Represents a vertex in the maze, holds the information about other
connected vertices, and checks whether this vertex has food.
"""


class Vertex:
    """
    Vertex represents a location in the quokka's quest to find food.
    It contains the relevant information surrounding the location.

    Attributes:
        * self.has_food (bool) - indicates whether this location has food.
        * self.edges (List[Vertex]) - list of connected vertices.

    Functions:
        * add_edge(self, v) - connects 'v' to this vertex by adding an edge.
        * rm_edge(self, v) - removes the vertex 'v' from this vertex's edges,
            breaking the connection between this vertex and 'v'.
    """

    def __init__(self, has_food: bool) -> None:
        """
        Initialises this vertex, by setting the attribute whether it has food.

        :param has_food - boolean indicating whether this location has food.
        """

        self.has_food = has_food
        self.edges = []
        self.Dijkstra_parent = None
        self.Dijkstra_distance = None
        self.destination = False
        self.extra_food = None
        self.heap_counter = None    # to fix this problem: https://stackoverflow.com/questions/43477958/typeerror-not-supported-between-instances-python

    def add_edge(self, v: 'Vertex') -> None:
        """
        Add an edge between this vertex and vertex 'v'.

        :param v - The vertex to add an edge between.
        """
        # TODO implement me please!
        if isinstance(v, Vertex) and v not in self.edges:
            if v != self:
                self.edges.append(v)
                v.edges.append(self)

    def rm_edge(self, v: 'Vertex') -> None:
        """
        Removes the edge between this vertex and 'v'.

        :param v - The vertex to remove from edges.
        """
        # TODO implement me please!
        if isinstance(v, Vertex) and v in self.edges:
            self.edges.remove(v)
            v.edges.remove(self)
    
    def did_we_eat_here(self) -> bool:
        """Did quokkas have a meal on this vertex?

        Returns:
            bool: True: yes! this vertex had food, or we consumed extra food.
                  False: no, quokkas ate nothing on this vertex
        """ 
        if self.has_food or self.Dijkstra_parent == "<root>":
            return True
        elif self.extra_food + 1 == self.Dijkstra_parent.extra_food:
            return True
        else:
            return False

    def will_survive(self, k: int) ->bool:
        """To find out if quokkas will survive when they reach this vertex, consume extra food
            if necessary.
        Args:
            k (int): The maximum number of hops between locations with food, the same arg as 
            it in find_path() method.

        Returns:
            bool:  True: will survive
                   False: will strave
        """
        # no input validity check for the argument k, since it has been checked in graph.find_path()

        walk = 0
        current_vertex = self

        while walk < k:
            if current_vertex.did_we_eat_here():
                return True
            else:
                walk += 1
                current_vertex = current_vertex.Dijkstra_parent
        
        if self.extra_food != 0:
            self.extra_food -= 1
            return True
        else:
            return False
