# Slot: anonymous_individual_count
_Number of anonymous individuals in the ontology or subset_


URI: [reporting:anonymous_individual_count](https://w3id.org/linkml/reportanonymous_individual_count)




## Inheritance

* [count_statistic](count_statistic.md)
    * **anonymous_individual_count**





## Applicable Classes

| Name | Description |
| --- | --- |
[UngroupedStatistics](UngroupedStatistics.md) | A summary statistics report object






## Properties

* Range: [xsd:integer](http://www.w3.org/2001/XMLSchema#integer)







## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| filter | AnonymousIndividual |



### Schema Source


* from schema: https://w3id.org/linkml/summary_statistics




## LinkML Source

<details>
```yaml
name: anonymous_individual_count
annotations:
  filter:
    tag: filter
    value: AnonymousIndividual
description: Number of anonymous individuals in the ontology or subset
from_schema: https://w3id.org/linkml/summary_statistics
rank: 1000
is_a: count_statistic
alias: anonymous_individual_count
owner: UngroupedStatistics
domain_of:
- UngroupedStatistics
slot_group: individual_statistic_group
range: integer
equals_expression: '{named_individual_count} - {individual_count}'

```
</details>