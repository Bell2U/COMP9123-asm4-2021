# Python Implementation
## Assignment 4: Quokka Survival Strategies
All submitted work must be done individually without consulting someone else's solutions in accordance with the University's Academic Dishonesty and Plagiarism policies.

## Story
A small quokka colony in Western Australia is migrating and since these creatures are vulnerable, we've been tasked with helping them make their way to their new home. For safety reasons, the quokka colony travels together at all times and can only travel between specific locations. We model these locations as the vertices of a simple undirected graph and two vertices are connected by an edge if the colony can travel from one location to the other.

Since the quokkas need to eat every so often, every vertex has the additional information whether sufficient food is available at a certain location. The colony can move through a number of locations before needing food and we assume that the intended destination has food. All other locations may or may not have food.

Please help the quokkas find a path from their current home to their destination such that they have sufficient food along the way.

Informally, our implementation should support the following operations:

`find_path(s, t, k)`
The main operation consists of finding a path from vertex s to vertex t such that from any location with food along this path we reach the next location with food in at most k steps.

Implement find_path(s, t, k) returning the list of vertices used in the path, or None if no path exists.

```fix_edge(u, v)
block_edge(u, v)```
We may need to update the graph sometimes when a certain edge is blocked or becomes accessible again. Implement the block_edge(u, v) and fix_edge(u, v) functions that removes an existing edge (if exists), or adds a new edge to the graph (if doesn't exist yet).

`exists_path_with_extra_food(s, t, k, x)`
We also want to help the quokkas by placing some extra food ourselves. Implement a method exists_path_with_extra_food(s, t, k, x) that returns whether it is possible for the quokkas to make it from s to t along a path where from any location with food we reach the next location with food in at most k steps, by placing food at at most x new locations. In other words, is it possible to place food at x new locations such that afterwards find_path(s, t, k) can find a path?

### Note

This assignment was inspired by Hamster Obstacle Mazes and Quokkas. No quokkas or hamsters were harmed in the production of this assignment. Credit to André for the assignment creation.

Visual Example
Given a graph:
```
        *       *
A---B---C---D---E
```
The find_path(A, E, 2) is a valid, achievable path, because between A and C there are 2 hops, and C and E are two hops, so the quokkas will survive. This will then return: [A, B, C, D, E].

On the other hand find_path(A, E, 1) cannot find a path, because A to B is 1 hop, and the quokkas will need food. So this returns None.

exists_path_with_extra_food(A, E, 1, 3) returns True, because adding 3 extra food to (at least) B and D will make the path [A, B, C, D, E] achievable as there is food at least 1 hop away for each vertex.

### ORDER MATTERS IN THE PATH RETURNED, IT SHOULD BE A SEQUENCE.

About the code
You are asked to implement 2 major files, vertex.py and graph.py.

vertex.py
The Vertex class provides the information of the vertex in the graph.

__Properties__

* `has_food` - [Boolean] indicates whether the vertex has food or not.

* `edges` - [List[Vertex]] the list of vertices connected to this vertex, forming edges in the graph.

Functions
`add_edge(v)`
Adds an edge between this vertex and the Vertex v.

`rm_edge(v)`
Removes the edge between this vertex and the Vertex v.

graph.py
This QuokkaMaze class provides the implementation of the graph for the quokkas to traverse.

__Properties__

* vertices - [List[Vertex]] the list of vertices in the graph.

Functions
`add_vertex(v) -> bool`
Adds the Vertex v to the graph, returning True if the operation was successful, False if it was not, or it was invalid.

`fix_edge(u, v) -> bool`
Fixes an edge between two vertices, u and v. If an edge already exists, or the edge is invalid, then this operation should return False. Else, if the operation succeeds, return True.

Example: If an edge between u and v already exists or is invalid, fix_edge(u, v) should return False.

`block_edge(u, v) -> bool`
Blocks the edge between two vertices, u and v. Removes the edge if it exists, and returns True if the operation was successful. If the edge does not exist or is invalid, it should be unsuccessful and return False.

`find_path(s, t, k) -> List[Vertex] or None`
Find a SIMPLE PATH between Vertex s and Vertex t such that from any location with food along this path we reach the next location with food in at most k steps.

This function returns: The list of vertices to form the simple path from s to t which satisfies the condition, or, None if there is no path that exists in the graph.

If there are invalid aspects (invalid path, invalid input), then this function returns `None`.

`exists_path_with_extra_food(s, t, k, x) -> bool`
Determines whether it is possible for the quokkas to make it from Vertex s to Vertex t along a SIMPLE path where from any location with food we reach the next location with food in at most k steps, by placing food at at most x new locations.

This function returns True if we can complete the simple path with at most x additional food, else it returns False.

If there are invalid aspects (invalid path, invalid input), then this function returns False.

## IMPORTANT INFORMATION
* We will be performing minor adversarial testing, which means:

  * CHECK YOUR PARAMS, for example: 

    * k should always be >= 0 for find_path() and exists_path_with_extra_food().

    * x should always be >= 0 for find_path() and exists_path_with_extra_food().

  * You must be careful for ALL functions.

* DO NOT MODIFY THE has_food PROPERTY OF THE VERTICES - we are running multiple tests on the same graph, and if you corrupt your graph by modifying the vertices then you may achieve an unwanted result and fail the tests.

* BE CAREFUL WITH copy and deepcopy - we are using equality on the vertices to check paths, this does a direct comparison with the vertex object, so any modifications and copies will be incorrect.

* List of Vertices as edges in a vertex are unordered, but when we fix an edge between two vertices, it should update both!

* The list of vertices returned by path functions (such as find_path) IS ORDERED, which means you return the sequence to form the path.
