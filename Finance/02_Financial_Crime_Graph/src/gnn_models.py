"""Model definitions for Elliptic AML graph tasks."""
from __future__ import annotations

import torch
import torch.nn.functional as F
from torch import nn
from torch_geometric.nn import SAGEConv


class GraphSAGE(nn.Module):
    """Two-layer GraphSAGE for inductive transaction classification.

    Why GraphSAGE over GCN:
    - GCN aggregates with a fixed normalized adjacency and is inherently transductive; new nodes at test time
      require retraining. GraphSAGE learns an aggregation function over neighbors, making it inductive and better
      suited to evolving transaction graphs where new wallets appear.
    - SAGE sampling scales to large, sparse graphs; ideal for institutional AML pipelines.
    """

    def __init__(self, in_dim: int, hidden_dim: int, out_dim: int, dropout: float = 0.5):
        super().__init__()
        self.conv1 = SAGEConv(in_dim, hidden_dim)
        self.conv2 = SAGEConv(hidden_dim, out_dim)
        self.dropout = dropout

    def forward(self, x, edge_index):  # pylint: disable=arguments-differ
        h = self.conv1(x, edge_index)
        h = F.relu(h)
        h = F.dropout(h, p=self.dropout, training=self.training)
        h = self.conv2(h, edge_index)
        return h


__all__ = ["GraphSAGE"]
