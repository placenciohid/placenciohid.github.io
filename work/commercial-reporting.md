---
project_id: commercial-reporting
layout: post
title: "Collections & reporting"
description: "Collections & reporting — selected work by Darío Placencio."
---


## The problem

Collectors need a current view of customer balances, overdue invoices, unapplied payments, and follow-up priorities. Repeated manual extracts can make it difficult to keep that picture consistent.

## My contribution

In Commercial Services at Rio Tinto, I delivered Atlantic Aluminium collections reporting and an hourly accounts-receivable aging feed. I also worked on reconciliation tools that help users review invoice matches, payment differences, and exceptions.

## What changed

The reporting brings customer risk and collections information into a shared workflow. The hourly feed was designed to replace recurring manual SAP extracts, while reconciliation views make the items needing review easier to find.

These are reporting and workflow improvements. Amounts visible in a report are not presented as cash recovered, and modeled reporting capacity is not treated as measured time saved. Internal customer records, screenshots, and financial data are not published here.


## Technical companion: aging and whole-document matching

The [public companion](https://github.com/placenciohid/Resume/tree/main/projects/commercial-reporting) uses five fictional invoices and three remittance documents to demonstrate the logic behind an aging view and reconciliation queue. It is independent of the internal dashboard and does not contain customer data.

### Inputs and calculations

Invoices contain an identifier, customer, currency, amount, due date, and trade/sundry category. Remittances contain a document identifier, payment amount, currency, and referenced invoice IDs. Monetary arithmetic uses Python `Decimal`, and the reporting date is explicit.

The workflow resolves invoice references, rejects duplicate claims, flags currency mismatches, and checks each remittance total against its payment. Only fully matched documents contribute to matched-document throughput. Payment values are counted once per document, rather than repeated for every invoice row. Aging buckets are calculated separately by currency and category.

```python
def reconcile(invoices, remittances, tolerance=Decimal('0.01')):
    lookup = invoice_index(invoices)
    claimed = set()
    rows = []
    for remit in remittances:
        ids = remit['invoice_ids']
        if len(ids) != len(set(ids)) or any(i in claimed for i in ids):
            raise ValueError('An invoice cannot be claimed twice')
        claimed.update(ids)
        missing = [i for i in ids if i not in lookup]
        currencies = {lookup[i]['currency'] for i in ids if i in lookup}
        total = sum((Decimal(lookup[i]['amount']) for i in ids if i in lookup), Decimal('0'))
        difference = Decimal(remit['payment'])-total
        status = ('missing_invoice' if missing or not ids else
                  'currency_mismatch' if currencies != {remit['currency']} else
                  'cleared' if abs(difference) <= tolerance else 'payment_difference')
        rows.append({'remittance':remit['id'], 'currency':remit['currency'], 'invoice_count':len(ids),
                     'invoice_total':str(total), 'payment':remit['payment'], 'difference':str(difference),
                     'status':status, 'missing':missing})
    return rows
```

### Executed fixture results

| Remittance | Referenced lines | Payment | Outcome |
| --- | ---: | ---: | --- |
| R1 | 2 | USD 2,000.00 | Fully matched |
| R2 | 1 | CAD 850.00 | CAD 50.00 short; remains an exception |
| R3 | 1 | USD 100.00 | Unknown invoice; remains an exception |

The output reports **one fully matched document, two distinct invoice lines, and USD 2,000.00**. Those are synthetic test results, not actual cash recovery. The demonstration tolerance is one cent, not a representation of an internal business rule.

### Controls and limits

Tests cover repeated invoice references, duplicate invoice IDs, unknown references, currency errors, due-date boundaries, and document-level totals. The compact example does not allocate partial payments or handle installments; difference documents remain open for review. A matched record does not prove bank settlement. Sundry is shown separately without silently changing an official collections KPI.

```bash
python projects/commercial-reporting/demo.py
python -m unittest discover -s tests -v
```

[Full source and data contract](https://github.com/placenciohid/Resume/tree/main/projects/commercial-reporting) · [Complete aging and reconciliation output](https://github.com/placenciohid/Resume/blob/main/projects/commercial-reporting/results.json). Python 3.10+; no external packages.
