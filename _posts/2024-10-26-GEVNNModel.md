---
project_id: gev-nn
layout: post
title: "Autoencoder features and a Gumbel activation"
description: "Reading the architecture and evaluation choices behind the rare-event neural model."
summary: "Reading the architecture and evaluation choices behind the rare-event neural model."
---

The research scripts explore representation learning and graph-based classification. Their input training files are not included. These notes explain the architecture that is actually present, identify the evaluation questions it raises, and connect it to the runnable [event-data contract](https://github.com/placenciohid/Resume/blob/main/projects/event-prediction/README.md).

## Autoencoder features and a Gumbel activation

The [GEV-NN script](https://github.com/placenciohid/Resume/blob/main/projects/event-prediction/legacy/GEV-NN-Model.py) combines three representations: a softmax-weighted copy of the input, an autoencoder's compressed representation, and two reconstruction summaries. A feed-forward classifier receives their concatenation.

The reconstruction summaries are mean squared reconstruction error and cosine similarity. The latter is named `cos_dist` in the script, but the formula calculates similarity, not `1 - similarity`. Preserving that distinction avoids reversing the interpretation of a diagnostic feature.

```python
euclid_dist = torch.mean((x - decoded) ** 2, dim=1, keepdim=True)
final_input = torch.cat((euclid_dist, cos_dist, selected_input, encoded), dim=1)
prediction = self.mlp(final_input)
```

The hidden layers use `exp(-exp(-x))`, a Gumbel CDF activation. The output layer uses a sigmoid. This is not a fitted generalized extreme-value distribution with a learned shape parameter. Likewise, softmax feature weights make a representation adaptive but do not establish causal feature importance or implement a full fuzzy inference system simply because of a class label.

The training objective adds one quarter of the autoencoder reconstruction loss to class-weighted binary cross-entropy. That encourages reconstruction and prediction jointly. An ablation would test whether the autoencoder, weighting branch, and asymmetric activation each improve performance over a smaller classifier. Their inclusion alone does not establish an advantage.

Before operational use, I would evaluate probabilities on forward-held-out observations, inspect calibration, and choose a decision threshold on validation data against an explicit review capacity. The rare-event precision–recall curve and the number of false alerts matter alongside ROC AUC. A reconstruction feature can detect unusual records without necessarily identifying the specific event the business cares about.
