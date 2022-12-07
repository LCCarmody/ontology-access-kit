# Slot: entailed_edge_count_by_predicate
_Number of entailed (includes indirect) edges grouped by predicate in the ontology or subset_


URI: [reporting:entailed_edge_count_by_predicate](https://w3id.org/linkml/reportentailed_edge_count_by_predicate)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description |
| --- | --- |
[UngroupedStatistics](UngroupedStatistics.md) | A summary statistics report object






## Properties

* Range: [FacetedCount](FacetedCount.md)
* Multivalued: True








## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| filter | EntailedEdge || facet | Predicate |



### Schema Source


* from schema: https://w3id.org/linkml/summary_statistics




## LinkML Source

<details>
```yaml
name: entailed_edge_count_by_predicate
annotations:
  filter:
    tag: filter
    value: EntailedEdge
  facet:
    tag: facet
    value: Predicate
description: Number of entailed (includes indirect) edges grouped by predicate in
  the ontology or subset
from_schema: https://w3id.org/linkml/summary_statistics
rank: 1000
multivalued: true
alias: entailed_edge_count_by_predicate
owner: UngroupedStatistics
domain_of:
- UngroupedStatistics
slot_group: metadata_statistic_group
range: FacetedCount
inlined: true

```
</details>