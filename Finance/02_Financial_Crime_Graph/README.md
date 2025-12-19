Financial Crime Graph — Bitcoin AML (Institutional Reference)
=============================================================

Executive summary
-----------------
Production-grade reference for anti-money-laundering analytics on Bitcoin transaction graphs using graph neural networks (GNNs). Covers ingestion, graph construction, supervised and unsupervised training, embedding export, and evaluation on the Elliptic dataset. Organized for reproducibility and hand-off to platform teams.

Business value
--------------
- Detect illicit activity early to reduce downstream compliance and operational risk.
- Provide reusable graph feature and model assets for broader blockchain monitoring use cases.
- Demonstrate controls for data lineage, experiment tracking, and deployable artifacts.

Repository layout
-----------------
```
02_Financial_Crime_Graph/
├── data/
│   └── elliptic_bitcoin_dataset/
│       ├── elliptic_txs_features.csv
│       ├── elliptic_txs_edgelist.csv
│       ├── elliptic_txs_classes.csv
│       ├── gnn_embeddings.npy
│       └── unsupervised_anomaly_results.csv
├── notebooks/
│   ├── Bitcoin_AML_Analysis.ipynb        # EDA, model training, evaluation and visualizations
│   └── bitcoin_gnn_model.pth             # Example trained model checkpoint
├── src/
│   ├── __init__.py
│   ├── graph_loader.py                   # CSV -> graph data (PyG) and preprocessing
│   └── gnn_models.py                     # GNN architectures and utilities
├── run_analysis.py                       # Orchestration script for training/evaluation
├── requirements.txt                      # Reproducible environment pins
└── README.md
```

Data and provenance
-------------------
- Source: Elliptic Bitcoin transaction dataset (license required). Place CSVs under `data/elliptic_bitcoin_dataset/`.
- Files: features, edgelist, class labels, exported embeddings, unsupervised anomaly scores.
- Sensitive data: none beyond licensed dataset; no PII present.

Methodology
-----------
- Task: node classification for illicit/licit/unknown transactions; anomaly scoring as auxiliary signal.
- Models: configurable GCN/GAT variants in `src/gnn_models.py`; unsupervised embedding with Deep Graph Infomax for anomaly detection.
- Features: transaction attributes per Elliptic schema; graph structure from `elliptic_txs_edgelist.csv`.
- Training script: `run_analysis.py` orchestrates load → split → train → evaluate; accepts CLI args for model type and epochs.

Evaluation and KPIs
-------------------
- Primary: macro F1 on labeled nodes; ROC-AUC for anomaly scoring.
- Secondary: calibration (ECE), inference latency per batch, embedding quality for downstream scoring.
- Current artifact: example checkpoint `notebooks/bitcoin_gnn_model.pth`; embeddings in `data/elliptic_bitcoin_dataset/gnn_embeddings.npy`.

How to run
----------
1) `python -m venv .venv && .venv\Scripts\activate` (Windows) or `source .venv/bin/activate` (Unix).
2) `pip install -r requirements.txt`.
3) Confirm data present under `data/elliptic_bitcoin_dataset/`.
4) Train/eval example: `python run_analysis.py --model gcn --epochs 50 --batch-size 1024`.
5) Export embeddings/anomaly scores via notebook `notebooks/Bitcoin_AML_Analysis.ipynb` or scripted hooks in `run_analysis.py`.

Operational notes
-----------------
- Reproducibility: set seeds in `run_analysis.py`; deterministic PyTorch where feasible.
- Monitoring: log metrics; evaluate class imbalance impacts; validate against drift by recomputing embeddings periodically.
- Controls: track dataset version and licensing; avoid mixing unlabeled nodes in supervised validation splits.

Next steps
----------
- Add experiment tracking (MLflow/W&B) hooks.
- Provide packaged inference service (FastAPI) with model loading and feature validation.
- Extend to multi-chain graphs and cross-exchange entity resolution.
   - `elliptic_txs_edgelist.csv`: directed transaction edges (sender -> receiver).
   - `elliptic_txs_classes.csv`: per-node labels (licit / illicit / unknown) used for supervised experiments.
   - `gnn_embeddings.npy`: precomputed node embeddings (artifact produced by runs).
   - `unsupervised_anomaly_results.csv`: results from unsupervised scoring experiments.

Architecture & approach
-----------------------
- Graph construction: `src/graph_loader.py` converts CSVs into PyTorch Geometric Data objects, applies feature normalization, and produces time-sliced train/validation/test splits to avoid temporal leakage.
- Model families: `src/gnn_models.py` contains implementations (configurable) of GraphSAGE / GCN / GAT style layers with classifier heads for node classification and a projection head for embedding extraction.
- Training: `run_analysis.py` orchestrates experiments, handles hyperparameter arguments, checkpointing, and metric logging (precision/recall/F1/AUC where applicable).

Reproducible quickstart
----------------------
1. Create a Python environment (recommended Python 3.8+).

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
pip install --upgrade pip
pip install -r requirements.txt
```

2. Place the Elliptic CSV files in `data/elliptic_bitcoin_dataset/`.

3. Run a short training/evaluation experiment (example):

```powershell
python run_analysis.py \\
   --data_dir data/elliptic_bitcoin_dataset \\
   --epochs 30 \\
   --batch_size 1024 \\
   --hidden_dim 128 \\
   --device cpu
```

4. Open the analytical notebook for deep-dive analysis and visualizations:

```powershell
jupyter lab notebooks/Bitcoin_AML_Analysis.ipynb
```

Outputs & artifacts
-------------------
- Model checkpoints: `notebooks/bitcoin_gnn_model.pth` (example) or checkpoints saved by `run_analysis.py`.
- Embeddings: `data/elliptic_bitcoin_dataset/gnn_embeddings.npy` — reusable for downstream clustering, scoring, or feature stores.
- Evaluation results: `data/elliptic_bitcoin_dataset/unsupervised_anomaly_results.csv` and standard classification metrics logged to the console.

Evaluation guidance
-------------------
- Use time-aware train/test splits to avoid look-ahead bias (split on discrete timesteps present in the dataset).
- Report per-class precision, recall, and F1 — emphasize illicit-class performance and false positive rate for operational feasibility.
- For unsupervised detection, provide ROC-AUC and precision@k (top-K alerting) to simulate analyst workload.

Security, privacy & governance
------------------------------
- This repository is intended for research and internal prototyping. Do not deploy model outputs to production without a full model risk assessment and data governance review.
- Ensure licensing compliance for the Elliptic dataset and treat any sensitive transaction-derived data according to your organisation's policies.

Limitations & intended use
--------------------------
- The Elliptic dataset is a proxy for historic Bitcoin flows and may not fully represent live network characteristics.
- GNN models are data-hungry and sensitive to class imbalance; operational deployment requires alert tuning and analyst-in-the-loop validation.

Next steps (engineering + research)
----------------------------------
- Integrate model outputs into a feature store and scalable scoring pipeline (stream / batch).
- Evaluate robustness across adversarial obfuscation tactics (mixing, chain-hopping).
- Add end-to-end tests and CI for model training, and containerize for reproducible deployments.

Contact & contribution
----------------------
If you are working from this repository in a team, please open issues or PRs for suggested improvements. For questions or hand-over, contact the repository owner.

Acknowledgements
----------------
- Elliptic dataset authors and maintainers.
- PyTorch Geometric and the open-source graph ML community.

License
-------
This repository does not include a license file by default. Apply your organisation's preferred license and confirm dataset redistribution permissions before sharing externally.

Glossary (quick)
-----------------
- AML: Anti-Money Laundering.
- GNN: Graph Neural Network.
- PyG: PyTorch Geometric.

----
Produced for internal technical review and engineering hand-off.

