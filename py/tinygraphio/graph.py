from typing import NamedTuple, NewType
from collections.abc import Iterable, Sequence


Node = NewType("Node", int)
Edge = NewType("Edge", int)

class Tinygraph(NamedTuple):
    offsets: Sequence[Edge]
    targets: Sequence[Node]

    def num_nodes(self) -> int:
        return max(0, len(self.offsets) - 1)

    def num_edges(self) -> int:
        return len(self.targets)

    def is_empty(self) -> bool:
        return self.num_nodes() == 0;

    def edges(self, n: Node) -> Iterable[Edge]:
        return [Edge(e) for e in range(self.offsets[n], self.offsets[n + 1])]

    def target(self, e: Edge) -> Node:
        return self.targets[e]

    def degree(self, n: Node) -> int:
        return self.offsets[n + 1] - self.offsets[n]

    def neighbors(self, n: Node) -> Iterable[Node]:
        return [self.target(e) for e in self.edges(n)]

    def has_node(self, n: Node) -> bool:
        return 0 <= n < self.num_nodes()

    def has_edge(self, e: Edge) -> bool:
        return 0 <= e < self.num_edges()

    def has_edge_from_to(self, s: Node, t: Node) -> bool:
        return t in set(self.neighbors(s))

    def __repr__(self) -> str:
        return f"<Tinygraph nodes={self.num_nodes()}, edges={self.num_edges()}>"
