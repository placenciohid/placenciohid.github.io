---
project_id: event-prediction
layout: post
title: "Event prediction"
description: "Event prediction — selected work by Darío Placencio."
---


How do operational records become useful prediction data without leaking future information into training?

The original project explored a PySpark preparation pipeline, Generalized Extreme Value neural networks, and graph neural networks for imbalanced event prediction. The portfolio now includes a small standard-Python reference demonstration that can run without private data or Spark.

## Run and inspect

The synthetic example builds features as of a record date, labels events in the following seven days, and fits scaling only on training records. Checks cover event resolution, target-window boundaries, retained fields, and separation of training and validation.

**[View code, run instructions, and limitations](https://github.com/placenciohid/Resume/tree/main/projects/event-prediction)**

## Original articles

- [Data preparation pipeline](/2024/10/26/EventDataPipeline.html)
- [Generalized Extreme Value neural network](/2024/10/26/GEVNNModel.html)
- [Graph neural network](/2024/10/26/GraphicalNN.html)

The original model scripts are preserved as historical research examples. The runnable reference prepares synthetic data; it does not reproduce historical model results.


## Implementation detail

The temporal gap prevents training labels from reaching the validation period. Scaling parameters come only from training rows.

```python
def split_and_scale(rows, split_date):
    train = [dict(r) for r in rows if r['record_date'] < split_date]
    validation = [dict(r) for r in rows if r['record_date'] >= split_date]
    if len(train) < 2:
        raise ValueError('At least two training rows are needed')
    # Purge training labels whose seven-day outcome window reaches validation.
    if any(date.fromisoformat(r['record_date']) + timedelta(days=7) >= date.fromisoformat(split_date) for r in train):
        raise ValueError('Training outcome windows overlap validation; add a temporal gap')
    center = mean(r['numeric_feature'] for r in train)
    scale = stdev(r['numeric_feature'] for r in train) or 1.0
    for row in train + validation:
        row['scaled_numeric_feature'] = (row['numeric_feature'] - center) / scale
    return train, validation, {'mean': center, 'scale': scale}
```

## Reproduce the example

```bash
python projects/event-prediction/demo.py
python -m unittest discover -s tests -v
```

Python 3.10+; the standard library is sufficient. [Read the full implementation](https://github.com/placenciohid/Resume/blob/main/projects/event-prediction/demo.py) and [project notes](https://github.com/placenciohid/Resume/tree/main/projects/event-prediction).

The sample creates two training and two validation rows. The first record has a resolved past event plus a future event: its current-block flag is zero and future-event label is one. The fitted numeric mean is 15 despite much larger validation values, making train-only fitting visible in the output.
