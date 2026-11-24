---
project_id: ml-from-scratch
layout: post
title: "Machine learning from scratch"
description: "Machine learning from scratch — selected work by Darío Placencio."
---


Implementing a model without a machine-learning library makes its decisions easier to inspect.

## A runnable example

This demonstration implements k-nearest neighbors, logistic regression, and a depth-one decision tree. Each model uses the same synthetic training set and is evaluated on a held-out set, with a fixed seed for reproducibility.

**[View code, run instructions, and limitations](https://github.com/placenciohid/Resume/tree/main/projects/ml-from-scratch)**

The output reports accuracy on a deliberately simple synthetic problem. It is an implementation example, not evidence of performance on operational data. The original coursework notebook is preserved separately and requires its original datasets.

[Read the original machine-learning article](/2023/07/12/MLScratch.html).


## Implementation detail

The gradient is averaged over training rows, an intercept is included, and the sigmoid is clipped for numerical stability. The test set does not enter fitting.

```python
def fit_logistic(xs, ys, steps=1200, rate=0.2):
    weights = [0.0] * (len(xs[0]) + 1)
    for _ in range(steps):
        gradient = [0.0] * len(weights)
        for x, y in zip(xs, ys):
            features = [1.0] + list(x)
            error = sigmoid(sum(a*b for a,b in zip(weights, features))) - y
            gradient = [g + error*f for g,f in zip(gradient, features)]
        weights = [w - rate*g/len(xs) for w,g in zip(weights, gradient)]
    return weights
```

## Reproduce the example

```bash
python projects/ml-from-scratch/demo.py
python -m unittest discover -s tests -v
```

Python 3.10+; the standard library is sufficient. [Read the full implementation](https://github.com/placenciohid/Resume/blob/main/projects/ml-from-scratch/demo.py) and [project notes](https://github.com/placenciohid/Resume/tree/main/projects/ml-from-scratch).

## Held-out synthetic evaluation

| Classifier | Accuracy on 60 held-out rows |
| --- | ---: |
| knn | 98.33% |
| logistic regression | 100.00% |
| decision stump | 88.33% |

These are simple synthetic-boundary results, not operational accuracy. The original coursework notebook remains available separately.
