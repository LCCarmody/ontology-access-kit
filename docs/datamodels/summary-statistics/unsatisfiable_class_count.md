# Slot: unsatisfiable_class_count
_Number of unsatisfiable classes in the ontology or subset_


URI: [reporting:unsatisfiable_class_count](https://w3id.org/linkml/reportunsatisfiable_class_count)




## Inheritance

* [count_statistic](count_statistic.md)
    * **unsatisfiable_class_count**





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
| filter | Class, Unsatisfiable |



### Schema Source


* from schema: https://w3id.org/linkml/summary_statistics




## LinkML Source

<details>
```yaml
name: unsatisfiable_class_count
annotations:
  filter:
    tag: filter
    value: Class, Unsatisfiable
description: Number of unsatisfiable classes in the ontology or subset
from_schema: https://w3id.org/linkml/summary_statistics
rank: 1000
is_a: count_statistic
alias: unsatisfiable_class_count
owner: UngroupedStatistics
domain_of:
- UngroupedStatistics
slot_group: class_statistic_group
range: integer

```
</details>