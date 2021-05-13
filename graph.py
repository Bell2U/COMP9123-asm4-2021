"""
Quokka Maze
===========

This file represents the quokka maze, a graph of locations where a quokka is
trying to find a new home.

Please help the quokkas find a path from their current home to their
destination such that they have sufficient food along the way!

*** Assignment Notes ***

This is the main file that will be interacted with during testing.
All functions to implement are marked with a `TODO` comment.

Please implement these methods to help the quokkas find their new home!
"""

from typing import List, Union

from vertex import Vertex
from math import inf, isinf
import heapq


class QuokkaMaze:
    """
    Quokka Maze
    -----------

    This class is the undirected graph class that will contain all the
    information about the locations between the Quokka colony's current home
    and their final destination.

    We _will_ be performing some minor adversarial testing this time, so make
    sure you're performing checks and ensuring that the graph is a valid simple
    graph!

    ===== Functions =====

        * block_edge(u, v) - removes the edge between vertex `u` and vertex `v`
        * fix_edge(u, v) - fixes the edge between vertex `u` and `v`. or adds an
            edge if non-existent
        * find_path(s, t, k) - find a SIMPLE path from veretx `s` to vertex `t`
            such that from any location with food along this simple path we
            reach the next location with food in at most `k` steps
        * exists_path_with_extra_food(s, t, k, x) - returns whether it’s
            possible for the quokkas to make it from s to t along a simple path
            where from any location with food we reach the next location with
            food in at most k steps, by placing food at at most x new locations

    ===== Notes ======

    * We _will_ be adversarially testing, so make sure you check your params!
    * The ordering of vertices in the `vertex.edges` does not matter.
    * You MUST check that `k>=0` and `x>=0` for the respective functions
        * find_path (k must be greater than or equal to 0)
        * exists_path_with_extra_food (k and x must be greater than or equal to
            0)
    * This is an undirected graph, so you don't need to worry about the
        direction of traversing during your path finding.
    * This is a SIMPLE GRAPH, your functions should ensure that it stays that
        way.
    * All vertices in the graph SHOULD BE UNIQUE! IT SHOULD NOT BE POSSIBLE
        TO ADD DUPLICATE VERTICES! (i.e the same vertex instance)
    """

    def __init__(self) -> None:
        """
        Initialises an empty graph with a list of empty vertices.
        """
        self.vertices = []

    def add_vertex(self, v: Vertex) -> bool:
        """
        Adds a vertex to the graph.
        Returns whether the operation was successful or not.

        :param v - The vertex to add to the graph.
        :return true if the vertex was correctly added, else false
        """
        # TODO implement me, please?   Sure!
        if isinstance(v, Vertex) and v not in self.vertices:
            self.vertices.append(v)
            return True
        else:
            return False

    def fix_edge(self, u: Vertex, v: Vertex) -> bool:
        """
        Fixes the edge between two vertices, u and v.
        If an edge already exists, then this operation should return False.

        :param u - A vertex
        :param v - Another vertex
        :return true if the edge was successfully fixed, else false.
        """

        # TODO implement me please.
        # input validity check
        if not(isinstance(u, Vertex) and isinstance(v, Vertex)):
            return False
        if u not in self.vertices or v not in self.vertices:
            return False
        if u == v:
            return False
        if u in v.edges or v in u.edges:
            return False
        
        u.add_edge(v)
        return True
        

    def block_edge(self, u: Vertex, v: Vertex) -> bool:
        """
        Blocks the edge between two vertices, u and v.
        Removes the edge if it exists.
        If not, it should be unsuccessful.

        :param u - A vertex
        :param v - Another vertex.
        :return true if the edge was successfully removed, else false.
        """

        # TODO implement me, please!
        if not(isinstance(u, Vertex) and isinstance(v, Vertex)):
            return False
        if u not in self.vertices or v not in self.vertices:
            return False
        if u == v:
            return False
        if u in v.edges:
            u.rm_edge(v)
            return True
        else:
            return False

    def find_path(
            self,
            s: Vertex,
            t: Vertex,
            k: int,
            extra_food:int=0
    ) -> Union[List[Vertex], None]:
        """
        find_path returns a SIMPLE path between `s` and `t` such that from any
        location with food along this path we reach the next location with food
        in at most `k` steps

        :param s - The start vertex for the quokka colony
        :param t - The destination for the quokka colony
        :param k - The maximum number of hops between locations with food, so
        that the colony can survive!
        :returns
            * The list of vertices to form the simple path from `s` to `t`
            satisfying the conditions.
            OR
            * None if no simple path exists that can satisfy the conditions, or
            is invalid.

        Example:
        (* means the vertex has food)
                    *       *
            A---B---C---D---E

            1/ find_path(s=A, t=E, k=2) -> returns: [A, B, C, D, E]

            2/ find_path(s=A, t=E, k=1) -> returns: None
            (because there isn't enough food!)

            3/ find_path(s=A, t=C, k=4) -> returns: [A, B, C]

        """

        # TODO implement me please
        # input validity check
        if not(isinstance(s, Vertex) and isinstance(t, Vertex) and isinstance(k, int) and isinstance(extra_food, int)):
            return None
        if s not in self.vertices or t not in self.vertices or k < 0 or extra_food < 0:
            return None
        # s != t ???

        # modified Dijstra Algorithm
        # initiation
        i = 0
        while i < len(self.vertices):
            self.vertices[i].Dijkstra_parent = None
            self.vertices[i].Dijkstra_distance = inf
            self.vertices[i].extra_food = None
            self.vertices[i].destination = False
            self.vertices[i].heap_counter = i
            i += 1
        
        s.Dijkstra_parent = "<root>"
        s.Dijkstra_distance = 0
        s.extra_food = extra_food

        t.destination = True

        pqkeys = [v.Dijkstra_distance for v in self.vertices]
        pqcounters = [v.heap_counter for v in self.vertices]
        PQ = [elem for elem in zip(pqkeys, pqcounters, self.vertices)]    # priority queue
        heapq.heapify(PQ)

        # find the path
        while PQ:
            if not isinf(PQ[0][0]):
                current_vertex = heapq.heappop(PQ)[2]
                if current_vertex.will_survive(k):
                    if current_vertex.destination:
                        # return a list
                        return_list = []
                        to_be_append = current_vertex
                        while to_be_append.Dijkstra_parent != "<root>":
                            return_list.append(to_be_append)
                            to_be_append = to_be_append.Dijkstra_parent
                        return_list.append(to_be_append)
                        return [ele for ele in reversed(return_list)]

                    # update neighbors
                    j = 0
                    while j < len(current_vertex.edges):
                        # update neighbor's key in the heap
                        # update neighbor's parent
                        # update neighbor's extra_food here
                        # reorder the heap
                        try:
                            idx = PQ.index((current_vertex.edges[j].Dijkstra_distance, current_vertex.edges[j].heap_counter, current_vertex.edges[j]))
                            if current_vertex.Dijkstra_distance + 1 < current_vertex.edges[j].Dijkstra_distance:
                                current_vertex.edges[j].Dijkstra_distance = current_vertex.Dijkstra_distance + 1
                                current_vertex.edges[j].Dijkstra_parent = current_vertex
                                current_vertex.edges[j].extra_food = current_vertex.extra_food
                                PQ[idx] = (current_vertex.edges[j].Dijkstra_distance, current_vertex.edges[j].heap_counter, current_vertex.edges[j])
                                heapq._siftdown(PQ, 0, idx)     # reorder the heap
                        except ValueError:
                            pass
                        j += 1
                else:
                    # delete k vertexs:
                    #   initilize k vertices' value
                    #   push them back to the heap
                    to_be_initialize = current_vertex
                    i1 = 0
                    while i1 < k:
                        to_be_initialize.Dijkstra_parent = None
                        to_be_initialize.Dijkstra_distance = inf
                        to_be_initialize.extra_food = None
                        heapq.heappush(PQ, (to_be_initialize.Dijkstra_distance, to_be_initialize.heap_counter, to_be_initialize))
                        i1 += 1

            else:
                return None


    def exists_path_with_extra_food(
        self,
        s: Vertex,
        t: Vertex,
        k: int,
        x: int
    ) -> bool:
        """
        Determines whether it is possible for the quokkas to make it from s to
        t along a SIMPLE path where from any location with food we reach the
        next location with food in at most k steps, by placing food at at most
        x new locations.

        :param s - The start vertex for the quokka colony
        :param t - The destination for the quokka colony
        :param k - The maximum number of hops between locations with food, so
        that the colony can survive!
        :param x - The number of extra foods to add.
        :returns
            * True if with x added food we can complete the simple path
            * False otherwise.

        Example:
        (* means the vertex has food)
                            *
            A---B---C---D---E

            1/ exists_with_extra_food(A, E, 2, 0) -> returns: False
                (because we can't get from A to E with k=2 and 0 extra food)

            2/ exists_with_extra_food(A, E, 2, 1) -> returns: True
                (Yes, if we put food on `C` then we can get to E with k=2)

            3/ exists_with_extra_food(A, E, 1, 6) -> returns: True
                (Yes, if we put food on `B`, `C`, `D` then we reach E!)

        """

        # TODO implement me please
        path = self.find_path(s, t, k, x)
        if path is None:
            return False
        else:
            return True
