---
project_id: knowledge-search
layout: post
case_study: true
title: "Making technical knowledge searchable"
description: "The decisions behind a search platform spanning 300,000+ documents."
summary: "The decisions behind a search platform spanning 300,000+ documents."
---

{% include case-facts-knowledge-search.html %}

**Find the relevant passage, preserve its source, and give the user a way to check it.**

At Rio Tinto’s Borates Digital team, I engineered an AI knowledge-search platform covering more than **300,000 documents**, adopted by **four teams**. My work combined document extraction using vision-language models with hybrid retrieval. The operational problem was straightforward: useful information existed, but locating it across a large technical collection could take longer than the question itself warranted.

## From files to usable evidence

Searching a document collection involves more than placing text in a vector index. Scanned pages need extraction; technical identifiers need exact matching; users may describe a concept differently from the wording in a manual. A result also has to retain its document identity so the person using it can check the original context.

The professional implementation brought extraction, indexing, and retrieval together. Its 300,000-document scale and four-team adoption describe the delivered platform. The independent implementation here opens up a smaller part of that design: how passages are represented, ranked, combined, and returned with evidence.

## An implementation small enough to inspect end to end

[demo.py](https://github.com/placenciohid/Resume/blob/main/projects/knowledge-search/demo.py) searches six fictional technical and commercial documents. Each chunk carries a stable document ID, chunk ID, title, excerpt, and source path. Those fields survive every ranking step.

| Stage | Implementation | Reason for the choice |
| --- | --- | --- |
| Chunking | Word windows with overlap | Keep excerpts manageable while retaining context near a boundary |
| Exact retrieval | BM25 | Reward distinctive query terms without letting long documents dominate |
| Second retrieval view | Character-trigram TF-IDF and cosine similarity | Add a view of surface-form similarity without a model download |
| Combination | Reciprocal rank fusion | Combine ranks rather than incomparable raw scores |
| Reranking | Query-token coverage | Make the final preference inspectable |
| Response | Source excerpt and reference | Let a reader verify what was retrieved |

The character-vector index is lexical; it is not a semantic embedding model. It makes the fusion mechanics portable while keeping the professional platform's semantic-retrieval work distinct.

### Why rank fusion helps

A BM25 score and a cosine similarity do not share a scale. Simply adding them lets their numerical ranges determine the result. Reciprocal rank fusion instead adds `1 / (60 + rank)` from each ranking. [Cormack, Clarke, and Büttcher's original paper](https://cormack.uwaterloo.ca/cormack/cormacksigir09-rrf.pdf) describes the method.

```python
for values in (lexical, vector):
    for rank, index in enumerate(
        sorted(range(len(corpus)), key=lambda i: values[i], reverse=True), 1
    ):
        if values[index] > 0:
            fused[index] += 1 / (60 + rank)
```

The reranker then adds a simple coverage signal. This is deliberately easy to inspect; a learned reranker would require its own evaluation data, latency budget, and failure analysis.

## What the example returns

For `remittance fully cleared invoice`, the top source explains that all invoice references must match and the payment difference must fall within tolerance. The response includes `synthetic/remittance.txt`, rather than an unsupported generated answer. A query with no token evidence returns an empty result.

Five hand-written regression queries retrieve their expected top-ranked documents in the saved run. These queries were written alongside this six-document corpus, so **5/5 is a regression result**, not an independent retrieval-quality benchmark. [results.json](https://github.com/placenciohid/Resume/blob/main/projects/knowledge-search/results.json) contains the queries, expected sources, actual top sources, and an example ranked evidence list.

## The engineering tradeoffs

Chunk size trades context against retrieval precision. Overlap can recover a passage cut at a boundary but also produces near-duplicate results. Exact identifiers often favor keyword search; paraphrases favor semantic representations. Fusing both approaches is useful only if the final result is evaluated against questions representative of actual users.

For a larger deployment, I would evaluate source recall and ranking quality on held-out questions, inspect failures by document type, and measure extraction failures separately from retrieval failures. Access filters must apply before restricted passages enter the retrieval context. Versioned document identities also matter: a highly relevant superseded procedure can still be the wrong answer.

<details class="technical-detail" markdown="1">
<summary>Run and inspect the implementation <span>Source, results & reproduction</span></summary>

## Reproduce

```bash
python projects/knowledge-search/demo.py
python -m unittest discover -s tests -v
```

Python 3.10+, standard library only. The [fictional source documents](https://github.com/placenciohid/Resume/tree/main/projects/knowledge-search/synthetic) are included. Tests verify source-text fidelity, expected-source retrieval, and empty/no-evidence behavior. The professional case demonstrates delivery and adoption; this companion demonstrates the retrieval decisions a reviewer can inspect and run.

</details>
