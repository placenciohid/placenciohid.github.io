---
project_id: play-store
layout: post
title: "App reviews: topics and rating prediction"
description: "A reproducible text baseline, duplicate-aware validation, and a review of the original topic models."
summary: "A reproducible text baseline, duplicate-aware validation, and a review of the original topic models."
---

**Use text analysis to understand recurring concerns, then test whether the language predicts a clearly defined outcome.**

The original project explored app-review topics with LSI, LDA, and spaCy preprocessing, followed by a BERT classification experiment. The maintained analysis adds a reproducible classical baseline and makes the evaluation boundary explicit: similar or duplicated review text should not appear on both sides of a train/test split.

## Two questions require two kinds of evidence

Topic discovery asks what people discuss. Rating prediction asks whether review language predicts the selected label. A coherent topic model does not establish classification quality, and a good sentiment classifier does not automatically explain which product change to make.

The [original notebook](https://github.com/placenciohid/Resume/blob/main/projects/play-store-reviews/legacy/Google%20Play%20Store%20Review%20-%20%20Text%20Analytics.ipynb) compares several topic configurations. Its saved LSI search selects three topics with coherence 0.5502; its LDA search selects thirteen with coherence 0.5191. These are historical in-corpus selection statistics. They help compare configurations within that experiment, but they do not mean that 55% or 52% of topics are “correct.” Topic names still require interpretation and source review.

## A new reproducible classification baseline

[analyze.py](https://github.com/placenciohid/Resume/blob/main/projects/play-store-reviews/analyze.py) reads the existing review dataset and uses **1–2 star reviews as negative** and **4–5 star reviews as positive**. It excludes three-star reviews rather than silently assigning an ambiguous middle rating to a sentiment class.

The pipeline normalizes whitespace and case for grouping, then holds out 20% of distinct text groups. Every instance of identical normalized text remains in the same partition. TF-IDF vocabulary and inverse-document frequencies are fitted on training text only, followed by logistic regression. Usernames, IDs, replies, and star ratings are not model inputs.

```python
model = make_pipeline(
    TfidfVectorizer(ngram_range=(1, 2), min_df=3,
                    max_features=20000, sublinear_tf=True),
    LogisticRegression(max_iter=1500, random_state=42)
)
model.fit(training_text, training_labels)
```

## Held-out result

| Measure | Reproduced result |
| --- | --- |
| Raw reviews | 12,495 |
| Reviews retained after label/text filtering | 10,504 |
| Training / held-out rows | 8,428 / 2,076 |
| Identical text groups shared across partitions | 0 |
| Accuracy | 85.60% |
| F1 | 0.8614 |
| ROC AUC | 0.9336 |

The majority-class baseline would achieve 52.65% accuracy on this holdout. The model's 85.60% is useful evidence that the review language carries rating-related information under this protocol. The confusion matrix in [analysis-results.json](https://github.com/placenciohid/Resume/blob/main/projects/play-store-reviews/analysis-results.json) also shows the errors: 135 negative reviews predicted positive and 164 positive reviews predicted negative.

This is a retrospective text-group holdout, not a test on a future app release or an unseen application. Both could introduce vocabulary and rating shifts. The label is a rating-derived proxy, so it does not measure whether a product team would agree with every sentiment judgment.

## Why keep a classical baseline alongside BERT?

The baseline is inexpensive to run, has an inspectable vocabulary, and establishes a reference before a larger model is justified. The original BERT training output contains a non-finite training loss and does not preserve a usable held-out benchmark. Its architecture and training code remain available as an experiment; the completed TF-IDF result above supplies the reproducible evaluation.

A stronger next experiment would split by app or time, compare a transformer against this same baseline, and inspect errors around negation, sarcasm, mixed sentiment, and short reviews. For topic analysis, I would pair a topic with representative excerpts and its prevalence by version before recommending a change.

## Reproduce

```bash
python -m pip install -r requirements-analysis.txt
python projects/play-store-reviews/analyze.py
```

The existing [review dataset](https://github.com/placenciohid/Resume/blob/main/data/legacy/README.md) is read locally. `--write` updates the result snapshot; the output contains aggregate metrics rather than individual review text. Dataset hash, package versions, split sizes, and target definition are recorded with the result. The [original dataset source](https://www.kaggle.com/datasets/prakharrathi25/google-play-store-reviews) is credited separately from the analysis.
