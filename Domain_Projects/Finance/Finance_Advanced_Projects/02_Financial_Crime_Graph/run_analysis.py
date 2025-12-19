"""End-to-end training script for Elliptic AML GraphSAGE.

Usage:
    python run_analysis.py --data_dir ./data --epochs 20 --hidden_dim 128
"""
from __future__ import annotations

import argparse
import random
from pathlib import Path

import numpy as np
import torch
import torch.nn.functional as F
from sklearn.metrics import precision_recall_fscore_support
from torch.optim import Adam
from torch_geometric.loader import NeighborLoader

from src.graph_loader import load_elliptic_graph
from src.gnn_models import GraphSAGE


def set_seed(seed: int) -> None:
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)


def train_one_epoch(model, loader, optimizer, device):
    model.train()
    total_loss = 0.0
    for batch in loader:
        batch = batch.to(device)
        optimizer.zero_grad()
        out = model(batch.x, batch.edge_index)
        loss = F.cross_entropy(out[batch.train_mask], batch.y[batch.train_mask])
        loss.backward()
        optimizer.step()
        total_loss += loss.item() * batch.num_graphs
    return total_loss / len(loader.dataset)


def evaluate(model, data, device):
    model.eval()
    with torch.no_grad():
        out = model(data.x.to(device), data.edge_index.to(device))
        pred = out.argmax(dim=1).cpu()
        y_true = data.y.cpu()

    # Focus metrics on illicit class (label=1)
    precision, recall, f1, support = precision_recall_fscore_support(
        y_true[data.test_mask.cpu()],
        pred[data.test_mask.cpu()],
        labels=[1],
        average=None,
        zero_division=0,
    )

    return {
        "precision_illicit": float(precision[0]),
        "recall_illicit": float(recall[0]),
        "f1_illicit": float(f1[0]),
        "support_illicit": int(support[0]),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_dir", type=str, default="./data")
    parser.add_argument("--epochs", type=int, default=20)
    parser.add_argument("--hidden_dim", type=int, default=128)
    parser.add_argument("--dropout", type=float, default=0.5)
    parser.add_argument("--lr", type=float, default=1e-3)
    parser.add_argument("--batch_size", type=int, default=1024)
    parser.add_argument("--num_neighbors", type=int, default=25)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()

    set_seed(args.seed)

    data, _ = load_elliptic_graph(Path(args.data_dir))


    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    print(f"data.x shape: {getattr(data.x, 'shape', None)}")
    print(f"data.y shape: {getattr(data.y, 'shape', None)}")
    print(f"num_node_features: {getattr(data, 'num_node_features', None)}")
    print(f"num_classes: {int(data.y.max().item()) + 1 if hasattr(data.y, 'max') else None}")

    model = GraphSAGE(
        in_dim=getattr(data, 'num_node_features', None),
        hidden_dim=args.hidden_dim,
        out_dim=int(data.y.max().item()) + 1 if hasattr(data.y, 'max') else None,
        dropout=args.dropout,
    ).to(device)

    optimizer = Adam(model.parameters(), lr=args.lr)

    # NeighborLoader for mini-batching; mask filtering keeps temporal split intact
    train_indices = torch.nonzero(data.train_mask, as_tuple=False).view(-1)
    train_loader = NeighborLoader(
        data,
        num_neighbors=[args.num_neighbors, args.num_neighbors],
        batch_size=args.batch_size,
        input_nodes=train_indices,
        shuffle=True,
    )

    for epoch in range(1, args.epochs + 1):
        loss = train_one_epoch(model, train_loader, optimizer, device)
        metrics = evaluate(model, data.to(device), device)
        print(
            f"Epoch {epoch:02d} | Loss: {loss:.4f} | "
            f"P@1: {metrics['precision_illicit']:.4f} "
            f"R@1: {metrics['recall_illicit']:.4f} "
            f"F1@1: {metrics['f1_illicit']:.4f} "
            f"Support: {metrics['support_illicit']}"
        )


if __name__ == "__main__":
    main()
