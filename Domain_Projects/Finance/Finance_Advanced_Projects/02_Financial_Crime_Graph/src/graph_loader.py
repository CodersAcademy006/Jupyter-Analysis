"""Utilities to load Elliptic transaction graph into a PyG Data object.

Steps
- load edges, features, and class labels from the provided CSVs
- map label 1 -> illicit (1), 2 -> licit (0); drop unknown (0)
- build a temporal split: train if time_step < 35, test otherwise
- return a torch_geometric.data.Data with masks
"""
from __future__ import annotations

from pathlib import Path
from typing import Tuple

import pandas as pd
import torch
from torch_geometric.data import Data

# CSV filenames expected in the data directory
EDGES_FILE = "elliptic_txs_edgelist.csv"
FEATURES_FILE = "elliptic_txs_features.csv"
CLASSES_FILE = "elliptic_txs_classes.csv"


def load_elliptic_graph(data_dir: str | Path) -> Tuple[Data, pd.DataFrame]:
    """Load Elliptic dataset and return a PyG Data object and raw labels.

    Args:
        data_dir: Directory containing the three Elliptic CSVs.

    Returns:
        data: PyG Data with x, edge_index, y, train_mask, test_mask
        labels_df: DataFrame with columns [txId, class] (filtered to known labels)
    """

    base = Path(data_dir)
    edges_path = base / EDGES_FILE
    features_path = base / FEATURES_FILE
    classes_path = base / CLASSES_FILE

    # Load
    edges_df = pd.read_csv(edges_path)
    feats_df = pd.read_csv(features_path, header=None)
    labels_df = pd.read_csv(classes_path)

    # features file schema: txId, time_step, f1, f2, ..., f165
    feats_df = feats_df.rename(columns={0: "txId", 1: "time_step"})

    # Align features to ensure sorted by txId (PyG expects feature rows aligned with y)
    feats_df = feats_df.sort_values("txId").reset_index(drop=True)

    # Filter out unknown classes (0) and remap: 1 -> illicit (1), 2 -> licit (0)
    labels_df = labels_df[labels_df["class"] != 0].copy()
    labels_df["y"] = labels_df["class"].map({1: 1, 2: 0})

    # Merge labels into features; drop rows without labels (unknowns)
    merged = feats_df.merge(labels_df[["txId", "y"]], on="txId", how="inner")

    # Build feature matrix
    feature_cols = [c for c in merged.columns if c not in {"txId", "time_step", "y"}]
    x = torch.tensor(merged[feature_cols].values, dtype=torch.float)

    # Node mapping: txId to consecutive indices
    txid_to_idx = {tx_id: idx for idx, tx_id in enumerate(merged["txId"].tolist())}

    # Filter edges to nodes present after label filtering
    edges_filtered = edges_df[edges_df["txId1"].isin(txid_to_idx) & edges_df["txId2"].isin(txid_to_idx)]

    # Build edge_index (2, E)
    edge_index = torch.tensor(
        [
            edges_filtered["txId1"].map(txid_to_idx).values,
            edges_filtered["txId2"].map(txid_to_idx).values,
        ],
        dtype=torch.long,
    )

    # Targets
    y = torch.tensor(merged["y"].values, dtype=torch.long)

    # Temporal split: train < 35, test >= 35
    time_steps = merged["time_step"].values
    train_mask = torch.tensor(time_steps < 35, dtype=torch.bool)
    test_mask = torch.tensor(time_steps >= 35, dtype=torch.bool)

    data = Data(x=x, edge_index=edge_index, y=y)
    data.train_mask = train_mask
    data.test_mask = test_mask

    return data, merged[["txId", "y", "time_step"]]


__all__ = ["load_elliptic_graph"]
