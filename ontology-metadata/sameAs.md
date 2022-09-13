# Slot: sameAs

URI: [http://www.w3.org/2002/07/owl#sameAs](http://www.w3.org/2002/07/owl#sameAs)




## Inheritance

* [logical_predicate](logical_predicate.md)
    * **sameAs** [ match_aspect]





## Properties

* Range: [Thing](Thing.md)
* Multivalued: True







## TODOs

* restrict range

## Identifier and Mapping Information







### Schema Source


* from schema: http://purl.obolibrary.org/obo/omo/schema




## LinkML Specification

<details>
```yaml
name: sameAs
todos:
- restrict range
from_schema: http://purl.obolibrary.org/obo/omo/schema
rank: 1000
is_a: logical_predicate
mixins:
- match_aspect
slot_uri: owl:sameAs
multivalued: true
alias: sameAs
range: Thing

```
</details>