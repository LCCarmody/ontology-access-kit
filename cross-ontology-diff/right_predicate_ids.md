# Slot: right_predicate_ids
_* If the match type is consistent, then all consistent predicates.
* If the match type is identical, then the identical predicate.
* If the match type is OtherRelationship, then all predicates that form a path between right subject and object_


URI: [https://w3id.org/linkml/text_annotator/right_predicate_ids](https://w3id.org/linkml/text_annotator/right_predicate_ids)




## Inheritance

* **right_predicate_ids** [ right_side predicate]





## Properties

* Range: [EntityReference](EntityReference.md)
* Multivalued: True







## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/linkml/cross_ontology_diff




## LinkML Specification

<details>
```yaml
name: right_predicate_ids
description: '* If the match type is consistent, then all consistent predicates.

  * If the match type is identical, then the identical predicate.

  * If the match type is OtherRelationship, then all predicates that form a path between
  right subject and object'
from_schema: https://w3id.org/linkml/cross_ontology_diff
rank: 1000
mixins:
- right_side
- predicate
multivalued: true
alias: right_predicate_ids
domain_of:
- RelationalDiff
range: EntityReference

```
</details>