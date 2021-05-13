import unittest

from vertex import Vertex


def should_be_equal(got, expected, func, message="Incorrect result returned"):
    """
    Simple Assert Helper Function
    """

    assert expected == got, \
        f"[{func}] MSG: {message} [Expected: {expected}, got: {got}]"


def should_be_true(got, func, message="Incorrect result returned"):
    """
    Simple assert helper
    """

    assert got is not None, \
        f"[{func}] MSG: {message} [Expected True, but got {got}]"

    assert got is True, \
        f"[{func}] MSG: {message} [Expected True, but got {got}]"


def should_be_false(got, func, message="Incorrect result returned"):
    """
    Simple false checker
    """

    assert got is not None, \
        f"[{func}] MSG: {message} [Expected False, but got {got}]"

    assert got is False, \
        f"[{func}] MSG: {message} [Expected False, but got {got}]"


class TestSampleVertex(unittest.TestCase):

    def test_can_add_single_edge(self):
        """
        Can we add a simple edge to a vertex?
        """

        A = Vertex(True)
        B = Vertex(True)

        A.add_edge(B),

        should_be_equal(
            len(A.edges),
            1,
            "vertex.add_edge"
        )

        should_be_true(
            B in A.edges,
            "vertex.add_edge"
        )

        # Should not be able to add same edge.
        A.add_edge(B),

        should_be_equal(
            len(A.edges),
            1,
            "vertex.add_edge"
        )

    def test_can_we_rm_edge(self):
        """
        Can we remove the edge?
        """

        A = Vertex(True)
        B = Vertex(True)
        C = Vertex(True)

        A.add_edge(B),

        A.rm_edge(B)

        should_be_equal(
            len(A.edges),
            0,
            "vertex.rm_edge"
        )

        # Shouldn't be able to remove an edge that doesn't exist
        A.add_edge(C)
        A.rm_edge(B)

        should_be_equal(
            len(A.edges),
            1,
            "vertex.rm_edge"
        )