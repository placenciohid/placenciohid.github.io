---
project_id: knowledge-search
layout: post
title: "Finding information with AI"
description: "Finding information with AI — selected work by Darío Placencio."
---


## The problem

Technical information was spread across a large document collection. Finding the right source could involve searching and reading multiple documents manually.

## My contribution

At Rio Tinto’s Borates Digital team, I developed an AI search pipeline covering more than **300,000 documents**. It combined text extraction from document images with keyword and semantic search, followed by reranking to improve relevance.

## Adoption

The platform was adopted by **four teams**. It gave users a shared route into the document collection and reduced the need to locate material through separate manual searches.

The volume describes the collection covered by the system; it is not a count of unique users or a measured time saving. Employer documents, system access details, and source code are not included here.


## Technical companion: retrieval with inspectable evidence

The [public implementation](https://github.com/placenciohid/Resume/tree/main/projects/knowledge-search) demonstrates document chunking, hybrid retrieval, rank fusion, and source traceability. It uses six fictional documents and no employer systems. It starts with extracted text: OCR and a generative model are not included in this small companion.

### Data flow and design choices

`source documents → overlapping chunks + source IDs → two search indexes → rank fusion → reranking → evidence excerpts`

Each chunk retains its document identifier, title, and source reference. BM25 ranks exact vocabulary, while character-trigram TF-IDF supplies a second lexical similarity ranking. Reciprocal rank fusion combines the rankings without comparing incompatible raw scores. A simple token-coverage reranker promotes chunks that cover more of the question.

The vector index is lexical, not a semantic embedding model. A larger implementation could replace it with embeddings and use a learned reranker without changing the source metadata contract.

```python
def search(query, corpus=None, limit=3):
    corpus = chunks(DOCUMENTS) if corpus is None else corpus
    if not tokens(query) or not corpus: return []
    lexical, vector = bm25(query, corpus), vector_scores(query, corpus)
    fused = Counter()
    for values in (lexical, vector):
        for rank,index in enumerate(sorted(range(len(corpus)), key=lambda i:values[i], reverse=True),1):
            if values[index] > 0: fused[index] += 1/(60+rank)
    candidates = []
    for index,score in fused.items():
        coverage = len(set(tokens(query)) & set(tokens(corpus[index]['text'])))/len(set(tokens(query)))
        # Require lexical evidence; char overlap alone is not a reliable answer.
        if coverage == 0: continue
        candidates.append({**corpus[index], 'fusion_score':round(score,6),
                           'query_coverage':round(coverage,4), 'score':score+0.1*coverage})
    return sorted(candidates,key=lambda c:c['score'],reverse=True)[:limit]
```

### Example output

For `remittance fully cleared invoice`, the first result is the fictional remittance guide. It returns the exact passage, the document ID, and the source reference `synthetic/remittance.txt`. With no lexical evidence, retrieval returns no answer rather than inventing a response.

### Evaluation and limits

The executed fixture finds the expected top document for all five hand-written questions. These questions were designed alongside the tiny corpus, so the result is a regression check rather than an unbiased quality benchmark. Tests also check verbatim source evidence, empty questions, and abstention when no evidence exists. This example does not measure production latency, permission enforcement, or answer quality from an LLM.

```bash
python projects/knowledge-search/demo.py
python -m unittest discover -s tests -v
```

[Complete source and decisions](https://github.com/placenciohid/Resume/tree/main/projects/knowledge-search) · [Saved query results and evidence](https://github.com/placenciohid/Resume/blob/main/projects/knowledge-search/results.json). Python 3.10+; no packages or paid services. A production design would add OCR quality checks, document versioning, page citations, and access filtering before retrieval.
