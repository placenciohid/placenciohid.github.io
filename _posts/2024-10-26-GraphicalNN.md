---
project_id: gnn
layout: post
title: "Graph-based rare-event classification"
description: "Similarity graphs, focal-loss ensembles, and the boundary between validation and testing."
summary: "Similarity graphs, focal-loss ensembles, and the boundary between validation and testing."
---

**What makes a graph useful for rare-event classification—and what can its evaluation really establish?**

## A graph built from feature similarity

The [graph script](https://github.com/placenciohid/Resume/blob/main/projects/event-prediction/legacy/GNN-INCM_with_HSKDM.py) creates separate train, validation, and test graphs using nearest neighbors in standardized feature space. Nodes are records, and edges reflect similarity rather than a supplied customer, equipment, or transaction relationship.

```python
dist = torch.cdist(X_tensor, X_tensor)
_, indices = dist.topk(k + 1, largest=False)
edge_index = torch.stack([row.reshape(-1), indices[:, 1:].reshape(-1)])
```

The GNN stacks configurable convolution layers with batch normalization, ELU, dropout, and training-time edge dropout. Training uses focal loss, while three independently trained networks contribute probabilities that are averaged for evaluation. Although the historical class is named `HSKDM`, the implemented training loop uses independent focal-loss updates; it contains no teacher–student distillation loss.

That implementation raises two practical questions. First, should predictions be made for a batch of unseen records that can connect to one another, or for a single arriving record with access only to the historical graph? Separate test-graph construction assumes the former. Second, `torch.cdist` materializes all pairwise distances, so graph creation requires quadratic memory before nearest neighbors are selected. It is an inspectable prototype, not a scalable neighbor-search service.

The script applies SMOTE and undersampling within training. Because interpolation affects feature geometry, its effect on graph neighborhoods deserves an ablation against weighting alone. Graph similarity also needs a business rationale: nearby feature vectors need not share the same event-generating process.

## The evaluation boundary

The historical graph script chooses a decision threshold using test labels. That consumes the test set for selection. A revised benchmark should choose the threshold on validation data and evaluate it once on an untouched test period. Its random split also answers a different question from the temporal event-preparation reference.

I would begin with a time-aware linear or boosted-tree baseline, use an approximate-neighbor index for larger graphs, and compare precision at a fixed review workload. Those experiments would establish whether graph context earns its computational and operational cost.

The runnable [demo.py](https://github.com/placenciohid/Resume/blob/main/projects/event-prediction/demo.py), its saved [results](https://github.com/placenciohid/Resume/blob/main/projects/event-prediction/results.json), and the temporal-control tests provide a concrete starting point for that evaluation. They isolate a prerequisite that applies to either architecture: features must describe the past and labels must describe the specified future window.
