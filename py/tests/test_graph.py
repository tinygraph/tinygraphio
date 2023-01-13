import unittest

from tinygraphio.graph import Tinygraph


class GraphTestCase(unittest.TestCase):
    def test_simple_graph(self):
        # (0 -> 1)
        # (0 -> 2)
        # (1 -> 0)
        # (1 -> 2)
        # (2 -> 1)
        g1 = Tinygraph(offsets=[0, 2, 4, 5], targets=[1, 2, 0, 2, 1])

        self.assertFalse(g1.is_empty())
        self.assertEqual(g1.num_nodes(), 3)
        self.assertEqual(g1.num_edges(), 5)

        self.assertEqual(g1.edges(0), [0, 1])
        self.assertEqual(g1.edges(1), [2, 3])
        self.assertEqual(g1.edges(2), [4])

        self.assertEqual(g1.target(0), 1)
        self.assertEqual(g1.target(1), 2)
        self.assertEqual(g1.target(2), 0)
        self.assertEqual(g1.target(3), 2)
        self.assertEqual(g1.target(4), 1)

        self.assertEqual(g1.degree(0), 2)
        self.assertEqual(g1.degree(1), 2)
        self.assertEqual(g1.degree(2), 1)

        self.assertEqual(g1.neighbors(0), [1, 2])
        self.assertEqual(g1.neighbors(1), [0, 2])
        self.assertEqual(g1.neighbors(2), [1])

        self.assertTrue(g1.has_node(0))
        self.assertFalse(g1.has_node(-1))
        self.assertFalse(g1.has_node(3))

        self.assertTrue(g1.has_edge(0))
        self.assertFalse(g1.has_edge(-1))
        self.assertFalse(g1.has_edge(5))

        self.assertTrue(g1.has_edge_from_to(0, 1))
        self.assertTrue(g1.has_edge_from_to(2, 1))
        self.assertFalse(g1.has_edge_from_to(2, 0))
        self.assertFalse(g1.has_edge_from_to(-1, 1))
        self.assertFalse(g1.has_edge_from_to(0, -1))
        self.assertFalse(g1.has_edge_from_to(-1, -1))


if __name__ == "__main__":
    unittest.main()
