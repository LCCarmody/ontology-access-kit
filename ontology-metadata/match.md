# Slot: match

URI: [http://purl.obolibrary.org/obo/schema/match](http://purl.obolibrary.org/obo/schema/match)




## Inheritance

* **match** [ match_aspect]
    * [broadMatch](broadMatch.md)
    * [closeMatch](closeMatch.md)
    * [exactMatch](exactMatch.md)
    * [narrowMatch](narrowMatch.md)
    * [database_cross_reference](database_cross_reference.md)





## Properties

* Range: [xsd:string](http://www.w3.org/2001/XMLSchema#string)
* Multivalued: None







## Identifier and Mapping Information







### Schema Source


* from schema: http://purl.obolibrary.org/obo/omo/schema




## LinkML Specification

<details>
```yaml
name: match
from_schema: http://purl.obolibrary.org/obo/omo/schema
rank: 1000
abstract: true
mixins:
- match_aspect
alias: match
range: string

```
</details>