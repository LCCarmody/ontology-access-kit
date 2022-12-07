# Slot: deprecated_object_property_count
_Number of deprecated (obsoleted) object properties in the ontology or subset_


URI: [reporting:deprecated_object_property_count](https://w3id.org/linkml/reportdeprecated_object_property_count)




## Inheritance

* [count_statistic](count_statistic.md)
    * **deprecated_object_property_count**





## Applicable Classes

| Name | Description |
| --- | --- |
[UngroupedStatistics](UngroupedStatistics.md) | A summary statistics report object






## Properties

* Range: [xsd:string](http://www.w3.org/2001/XMLSchema#string)







## Identifier and Mapping Information





### Annotations

| property | value |
| --- | --- |
| filter | ObjectProperty, Deprecated |



### Schema Source


* from schema: https://w3id.org/linkml/summary_statistics




## LinkML Source

<details>
```yaml
name: deprecated_object_property_count
annotations:
  filter:
    tag: filter
    value: ObjectProperty, Deprecated
description: Number of deprecated (obsoleted) object properties in the ontology or
  subset
from_schema: https://w3id.org/linkml/summary_statistics
rank: 1000
is_a: count_statistic
alias: deprecated_object_property_count
owner: UngroupedStatistics
domain_of:
- UngroupedStatistics
slot_group: property_statistic_group
range: string

```
</details>