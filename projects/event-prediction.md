---
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
