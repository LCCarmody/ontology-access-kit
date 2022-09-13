# Slot: label

URI: [http://www.w3.org/2000/01/rdf-schema#label](http://www.w3.org/2000/01/rdf-schema#label)



<!-- no inheritance hierarchy -->



## Mixin Usage

| mixed into | description | range | domain |
| --- | --- | --- | --- |
| [left_subject_label](left_subject_label.md) | The name of the subject (child) of the source/left edge | Label |  |
| [left_object_label](left_object_label.md) | The name of the object (parent) of the source/left edge | Label |  |
| [left_predicate_label](left_predicate_label.md) | The name of the predicate of the source/left edge | Label |  |
| [right_subject_label](right_subject_label.md) | The name of the subject (child) of the matched/right edge, if matchable | Label |  |
| [right_object_label](right_object_label.md) | The name of the object (parent) of the matched/right edge, if matchable | Label |  |
| [right_predicate_labels](right_predicate_labels.md) | The names corresponding to the right_predicate_ids | Label |  |



## Properties

* Range: [xsd:string](http://www.w3.org/2001/XMLSchema#string)
* Multivalued: None




* Mixin: True




## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/linkml/cross_ontology_diff




## LinkML Specification

<details>
```yaml
name: label
from_schema: https://w3id.org/linkml/cross_ontology_diff
rank: 1000
mixin: true
slot_uri: rdfs:label
alias: label
range: string

```
</details>