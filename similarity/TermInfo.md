# Class: TermInfo




URI: [sim:TermInfo](https://w3id.org/linkml/similarity/TermInfo)




```{mermaid}
 classDiagram
    class TermInfo
      TermInfo : id
      TermInfo : label
      
```




<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |
| [id](id.md) | 1..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string)  |   |
| [label](label.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string)  |   |


## Usages


| used by | used in | type | used |
| ---  | --- | --- | --- |
| [TermSetPairwiseSimilarity](TermSetPairwiseSimilarity.md) | [subject_termset](subject_termset.md) | range | TermInfo |
| [TermSetPairwiseSimilarity](TermSetPairwiseSimilarity.md) | [object_termset](object_termset.md) | range | TermInfo |



## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/linkml/similarity







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['sim:TermInfo'] |
| native | ['sim:TermInfo'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TermInfo
from_schema: https://w3id.org/linkml/similarity
rank: 1000
attributes:
  id:
    name: id
    from_schema: https://w3id.org/linkml/similarity
    rank: 1000
    identifier: true
  label:
    name: label
    from_schema: https://w3id.org/linkml/similarity
    rank: 1000
    slot_uri: rdfs:label

```
</details>

### Induced

<details>
```yaml
name: TermInfo
from_schema: https://w3id.org/linkml/similarity
rank: 1000
attributes:
  id:
    name: id
    from_schema: https://w3id.org/linkml/similarity
    rank: 1000
    identifier: true
    alias: id
    owner: TermInfo
    domain_of:
    - TermInfo
    range: string
  label:
    name: label
    from_schema: https://w3id.org/linkml/similarity
    rank: 1000
    slot_uri: rdfs:label
    alias: label
    owner: TermInfo
    domain_of:
    - TermInfo
    range: string

```
</details>