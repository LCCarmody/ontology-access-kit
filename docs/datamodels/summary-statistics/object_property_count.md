# Slot: object_property_count
_Number of object properties (relations) in the ontology or subset_


URI: [reporting:object_property_count](https://w3id.org/linkml/reportobject_property_count)




## Inheritance

* [count_statistic](count_statistic.md)
    * **object_property_count**





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
| filter | ObjectProperty |



### Schema Source


* from schema: https://w3id.org/linkml/summary_statistics




## LinkML Source

<details>
```yaml
name: object_property_count
annotations:
  filter:
    tag: filter
    value: ObjectProperty
description: Number of object properties (relations) in the ontology or subset
from_schema: https://w3id.org/linkml/summary_statistics
rank: 1000
is_a: count_statistic
alias: object_property_count
owner: UngroupedStatistics
domain_of:
- UngroupedStatistics
slot_group: property_statistic_group
range: integer

```
</details>