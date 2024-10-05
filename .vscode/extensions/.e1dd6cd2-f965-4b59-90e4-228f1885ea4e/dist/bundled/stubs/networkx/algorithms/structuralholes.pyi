from typing import Mapping

from ..classes.graph import Graph

__all__ = ["constraint", "local_constraint", "effective_size"]

def mutual_weight(G: Graph, u, v, weight=None): ...
def normalized_mutual_weight(G: Graph, u, v, norm=..., weight=None): ...
def effective_size(G: Graph, nodes=None, weight: str | None = None) -> Mapping: ...
def constraint(G: Graph, nodes=None, weight: str | None = None) -> Mapping: ...
def local_constraint(G: Graph, u, v, weight: str | None = None) -> float: ...
