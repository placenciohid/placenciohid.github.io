---
project_id: event-prediction
layout: post
title: "Event prediction starts with the timeline"
description: "As-of features, future labels, and a training split that respects event time."
summary: "As-of features, future labels, and a training split that respects event time."
---

**Build a training row that represents what was knowable when a decision had to be made.**

This project connects a PySpark event-preparation pipeline with research scripts for imbalanced classification. Its most important modeling choice happens before a neural network: separating past events, current state, and future outcomes.

My earlier Rio Tinto internship included blocked-order prediction and model-data pipelines. This portfolio collects related technical work, with original research scripts and a runnable reference that makes the time logic inspectable.

## The question behind a training row

For a record observed on date `t`, the target asks whether a new event begins in `(t, t + 7 days]`. Features describe the record at `t` and the history up to that date. A later resolution may help establish a label or outcome, but it must not be used to describe a past state before it was known.

| Information | Allowed in an input at date t? | Reason |
| --- | --- | --- |
| Starts recorded on or before t | Yes | Part of observed history |
| Last known resolution on or before t | Yes | Helps establish current state |
| A new start three days after t | Target only | It is the event being predicted |
| A resolution arriving next week | No | It was not available at the decision date |

In a production source, event time and data-availability time can differ. This reference assumes same-day availability; a delayed source would need a separate availability timestamp and an as-of join using that field.

## Runnable implementation

[demo.py](https://github.com/placenciohid/Resume/blob/main/projects/event-prediction/demo.py) retains the record's required fields, resolves start and resolution events on one timeline, and derives `event_count`, `last_resolve_date`, and `currently_blocked`. Future starts affect only `target_event_flag`.

The fixture makes the distinction visible. Record A has a past start followed by a resolution, then another start after its snapshot. It is **currently unblocked with a positive future-event label**. Combining “ever blocked” and “blocked now” would lose that distinction.

```python
past = [e for e in history if date.fromisoformat(e['date']) <= cutoff]
future = [e for e in history
          if cutoff < date.fromisoformat(e['date']) <= cutoff + timedelta(days=horizon)]
```

The split also rejects training rows whose outcome window reaches validation. Otherwise, even chronological snapshots can share future label information across the boundary. Scaling is fitted on training rows: the saved mean is 15 despite validation values of 100 and 200. Tests perturb validation values to verify that they cannot change the fitted transformation.

## Three original implementations, three review questions

| Source | What to inspect | What needs attention before reuse |
| --- | --- | --- |
| [PySpark preparation](https://github.com/placenciohid/Resume/blob/main/projects/event-prediction/legacy/Data_PipeLine_for_Event_Prediction.py) | Event histories, joins, and feature construction | Required columns, as-of filtering, and the split/preprocessing order |
| [GEV/Gumbel-activation neural model](https://github.com/placenciohid/Resume/blob/main/projects/event-prediction/legacy/GEV-NN-Model.py) | Autoencoder features and an asymmetric hidden activation | Calibration, rare-event metrics, and comparison with a simple baseline |
| [Graph-model ensemble](https://github.com/placenciohid/Resume/blob/main/projects/event-prediction/legacy/GNN-INCM_with_HSKDM.py) | Graph construction, imbalance handling, and averaged model probabilities | Which nodes/edges may exist at inference and which labels enter resampling |

The neural script's fixed `exp(-exp(-x))` hidden activation is a Gumbel CDF, the zero-shape limit of the generalized extreme-value family. Its final output is sigmoid. It does not estimate a free GEV shape parameter. [The architecture notes](https://github.com/placenciohid/Resume/blob/main/projects/event-prediction/model-notes.md) explain both models, the actual ensemble training loop, and the evaluation boundary.

For the graph approach, a useful review asks whether the intended setting is inductive or transductive. Connections created from future observations can make a model look stronger offline while changing the problem it will face in operation. The original scripts are retained for inspection; their input training datasets are not included, so no historical accuracy is asserted here.

## Evaluate against the operational decision

Rare-event accuracy can be high simply by predicting that nothing happens. A stronger evaluation would compare a simple baseline, precision–recall performance, probability calibration, and recall at the number of cases a team can review. That last measure connects the model to an actual work queue.

## Reproduce

```bash
python projects/event-prediction/demo.py
python -m unittest discover -s tests -v
```

Python 3.10+, standard library only. [results.json](https://github.com/placenciohid/Resume/blob/main/projects/event-prediction/results.json) contains the two training and two validation rows. This compact fixture verifies the data contract; it prepares modeling data rather than presenting four rows as a predictive benchmark.

[Data preparation article](https://placenciohid.github.io/2024/10/26/EventDataPipeline.html) · [Train-only preprocessing guidance](https://scikit-learn.org/stable/common_pitfalls.html)
