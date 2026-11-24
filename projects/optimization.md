---
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
