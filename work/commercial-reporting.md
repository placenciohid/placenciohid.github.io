---
project_id: commercial-reporting
layout: post
case_study: true
title: "Collections reporting & reconciliation"
description: "Current receivables information backed by clear matching and counting rules."
summary: "Current receivables information backed by clear matching and counting rules."
---

{% include case-facts-commercial-reporting.html %}

**Make the next action visible without losing control of the numbers underneath it.**

In Rio Tinto Commercial Services, I delivered collections reporting for Atlantic Aluminium, an hourly accounts-receivable aging feed, and reconciliation views. The work brings overdue balances, unapplied cash, customer risk, and follow-up priorities into a shared reporting workflow. It connects process improvement with the calculation details that make a report reliable.

## The operational problem

A collector's work is organized around customers, invoices, payments, and exceptions. Those do not all share the same unit of analysis. One customer can have many invoices; one remittance document can reference several invoice lines. A report can look reasonable while overstating throughput if it repeats a document's payment value on each line.

The reporting work reduces the need to assemble that picture from recurring SAP extracts. The hourly aging feed keeps the source view current, while the dashboard and reconciliation views support review and follow-up. The published outcome is the delivered reporting workflow; refreshed data and easier review support clearance, but a reporting refresh is not itself evidence of recovered cash.

## The central design decision: define what “cleared” means

The public companion evaluates **whole remittance documents**. A document is fully matched only when its references exist, its currency agrees, and the payment equals the referenced invoice total within an explicit tolerance. The term `cleared` in this example means this matching condition; actual bank settlement would require a separate confirmed source.

| Record | Grain | Example fields |
| --- | --- | --- |
| Invoice | One open account item | ID, customer, currency, amount, due date, trade/sundry category |
| Remittance | One payment advice document | ID, currency, payment amount, invoice references |
| Reconciliation result | One remittance evaluation | Resolved line count, difference, status, missing references |
| Aging output | Currency × category × age bucket | Open line count and amount at a stated reporting date |

The implementation uses `Decimal` for monetary arithmetic. It groups currencies separately and requires a caller-supplied reporting date, making a past aging calculation reproducible.

## A small example with an important distinction

| Fictional remittance | Referenced lines | Result | Amount |
| --- | ---: | --- | ---: |
| R1 | 2 | Fully matched | USD 2,000.00 |
| R2 | 1 | Payment difference | CAD 850.00 payment against CAD 900.00 invoiced |
| R3 | 1 unresolved reference | Missing invoice | USD 100.00 remains an exception |

The correct throughput summary is **one matched document, two invoice lines, and USD 2,000.00**. Counting two documents or USD 4,000.00 would confuse the document and line grains. [results.json](https://github.com/placenciohid/Resume/blob/main/projects/commercial-reporting/results.json) preserves the complete reconciliation and open-aging output for this fictional fixture.

### Inspect the rule, not just the total

```python
status = ('missing_invoice' if missing or not ids else
          'currency_mismatch' if currencies != {remit['currency']} else
          'cleared' if abs(difference) <= tolerance else 'payment_difference')
```

In [demo.py](https://github.com/placenciohid/Resume/blob/main/projects/commercial-reporting/demo.py), duplicate invoice IDs, duplicate remittance IDs, and repeated invoice claims raise errors. The one-cent tolerance is an explicit example parameter. A real implementation needs business-approved matching rules, including treatment of short payments and partial allocations.

## Separate scope before reporting performance

Trade and sundry balances remain separate in the aging output. That makes the effect of scope visible before someone changes a collection KPI. Removing an out-of-scope item from a collections measure changes the denominator; it should be explainable and reproducible rather than achieved by hiding rows.

The same principle applies to adoption and throughput: report the reporting period, exclude development/test usage, distinguish report views from operational activity, and count a remittance amount once. Usage can show that a tool is being used. Document-level processing can show what passed through it. Neither alone proves incremental cash recovery.

<details class="technical-detail" markdown="1">
<summary>Run and inspect the implementation <span>Source, results & reproduction</span></summary>

## Reproduce and extend

```bash
python projects/commercial-reporting/demo.py
python -m unittest discover -s tests -v
```

Python 3.10+, standard library only. Tests cover aging boundaries, currency separation, duplicate identities, missing references, and whole-document throughput. The next extension would be an allocation ledger that supports partial settlements and repeated installments while preserving the document-to-line audit trail. That extension belongs in the calculation model before a dashboard presents a larger clearance number.

</details>
