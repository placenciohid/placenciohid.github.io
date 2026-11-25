---
project_id: restaurant-reviews
layout: post
title: "Restaurant reviews: a defensible comparison"
description: "Sampling, word frequencies, and the difference between a rating and a sentiment label."
summary: "Sampling, word frequencies, and the difference between a rating and a sentiment label."
---

**A frequent word is a starting point for investigation, not an explanation of customer satisfaction.**

This exploratory project compares review language for highly rated and poorly rated restaurants. The [original notebook](https://github.com/placenciohid/Resume/blob/main/projects/yelp-reviews/legacy/Text%20Analytics%20-%20Yelp%20Reviews.ipynb) joins restaurant-level ratings with review text, examines common words, and computes TextBlob polarity and subjectivity. It is an analysis notebook, rather than a trained sentiment-classification benchmark.

## What the original analysis contains

Four source tables separate restaurant summaries from review text for the top- and bottom-rated groups. The restaurant summary includes 100 businesses in each group. A join on `business_id` brings review text together with the restaurant's average rating; one saved joined table contains 21,131 review rows for the highly rated group.

The filtered high-rating vocabulary includes “fresh,” “friendly,” “service,” and “staff.” The low-rating vocabulary includes “order,” “service,” and “time.” Those overlaps matter: service can be discussed positively or negatively, so its frequency alone cannot tell which experience occurred.

## Three decisions determine what the comparison means

**Sampling.** Selecting extreme-rated restaurants gives a useful contrast, but it does not represent the full restaurant population. Restaurants with many reviews can dominate token totals unless the analysis deliberately reweights at restaurant level.

**Normalization.** Raw counts depend on the total number of tokens and reviews. A fair comparison would report normalized frequencies and uncertainty, or a contrast statistic such as a smoothed log-odds ratio. The original raw counts should not be interpreted as differences in complaint rates.

**Label definition.** The notebook labels sentiment from the restaurant's average rating, while TextBlob computes polarity from individual review text. These are distinct variables. Calling agreement between them a review-level sentiment accuracy would conflate a business-level label with an individual text judgment.

## A concrete improvement to the visualization

The notebook constructs a word cloud from a joined list of unique words after counting them. That discards the already-computed frequency weights. A revised visualization should use those weights directly:

```python
frequencies = dict(zip(word_counts['word'], word_counts['count']))
wordcloud.generate_from_frequencies(frequencies)
```

This is a suggested correction to the historical workflow. It changes what the word sizes represent; it does not solve sampling or interpretation on its own.

## What a useful operational output would look like

I would present a small number of themes with normalized prevalence, examples reviewed in context, and a clear definition of the sampled population. “Service” should be split into an actionable issue—such as waiting, order accuracy, or staff interaction—before recommending a process change. A team can act on an interpretable issue and trace it to the source; an attractive word cloud is insufficient.

## Inspect and reproduce the historical work

The notebook contains the preprocessing, counts, joins, and saved outputs. The four original CSV extracts (`top_best_100.csv`, `top_worst_100.csv`, `top_best_text.csv`, and `top_worst_text.csv`) are not included, so this project is offered as a reviewed historical analysis. Its core lesson is the connection between the unit of analysis, the label, and the conclusion—not an unmeasured claim of business impact.
