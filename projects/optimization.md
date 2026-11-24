---
project_id: optimization
layout: post
title: "Optimization"
description: "Optimization — selected work by Darío Placencio."
---


Optimization makes a decision explicit: what are we trying to improve, which choices can we make, and what limits must we respect?

## A runnable example

The scheduling demonstration assigns eight synthetic procedures to two rooms with four hours of capacity each. It compares a first-fit baseline with an exact search that maximizes total priority while respecting the capacity limit.

**[View code, run instructions, and limitations](https://github.com/placenciohid/Resume/tree/main/projects/optimization)**

This is a small capacity-allocation example. It does not model clinical priorities, staff availability, or a real hospital workflow. The original operating-room Pyomo and Julia puzzle notebooks are retained alongside it as earlier work.

[Read the original Julia constraint-programming article](/2023/07/13/Julia_Optimization.html).


## Implementation detail

Each procedure has three choices: deferred, room one, or room two. The complete search evaluates 6,561 assignments, rejects capacity violations, and retains the maximum score.

```python
def solve(procedures=PROCEDURES, capacity=4):
    best = (-1, (), [])
    # Each procedure is either deferred (0), or assigned to room 1 or 2.
    for assignment in product((0,1,2), repeat=len(procedures)):
        result = objective(assignment, procedures, capacity)
        if result != -1 and result[0] > best[0]:
            best = (result[0], assignment, result[1])
    return best
```

## Reproduce the example

```bash
python projects/optimization/demo.py
python -m unittest discover -s tests -v
```

Python 3.10+; the standard library is sufficient. [Read the full implementation](https://github.com/placenciohid/Resume/blob/main/projects/optimization/demo.py) and [project notes](https://github.com/placenciohid/Resume/tree/main/projects/optimization).

The executed synthetic schedule increases the dimensionless priority score from **24** under first fit to **28** under exact search. Both rooms use four hours, with no capacity violation. The score is not money, clinical benefit, or a real operational result.
