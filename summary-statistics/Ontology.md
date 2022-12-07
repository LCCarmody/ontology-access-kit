# Class: Ontology
_An ontology_




URI: [owl:Ontology](http://www.w3.org/2002/07/owl#Ontology)


```{mermaid}
 classDiagram
    class Ontology
      Ontology : description
      Ontology : id
      Ontology : prefix
      Ontology : title
      Ontology : version
      Ontology : version_info
      
```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [id](id.md) | 0..1 <br/> NONE |  | direct |
| [description](description.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | a description of the resource | direct |
| [title](title.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | the title of the resource | direct |
| [prefix](prefix.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | the prefix for the ontology | direct |
| [version](version.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | the version of the resource | direct |
| [version_info](version_info.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string) | the version info of the resource | direct |



## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [SummaryStatisticsReport](SummaryStatisticsReport.md) | [ontologies](ontologies.md) | range | [Ontology](Ontology.md) |
| [SummaryStatisticsReport](SummaryStatisticsReport.md) | [compared_with](compared_with.md) | range | [Ontology](Ontology.md) |
| [GroupedStatistics](GroupedStatistics.md) | [ontologies](ontologies.md) | range | [Ontology](Ontology.md) |
| [GroupedStatistics](GroupedStatistics.md) | [compared_with](compared_with.md) | range | [Ontology](Ontology.md) |
| [UngroupedStatistics](UngroupedStatistics.md) | [ontologies](ontologies.md) | range | [Ontology](Ontology.md) |
| [UngroupedStatistics](UngroupedStatistics.md) | [compared_with](compared_with.md) | range | [Ontology](Ontology.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/linkml/summary_statistics





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | owl:Ontology |
| native | reporting:Ontology |


## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: Ontology
description: An ontology
from_schema: https://w3id.org/linkml/summary_statistics
rank: 1000
attributes:
  id:
    name: id
    description: the unique identifier for the resource
    from_schema: https://w3id.org/linkml/summary_statistics
    identifier: true
    range: string
  description:
    name: description
    description: a description of the resource
    from_schema: https://w3id.org/linkml/summary_statistics
    rank: 1000
    slot_uri: dcterms:description
    range: string
  title:
    name: title
    description: the title of the resource
    from_schema: https://w3id.org/linkml/summary_statistics
    rank: 1000
    slot_uri: dcterms:title
    range: string
  prefix:
    name: prefix
    description: the prefix for the ontology
    from_schema: https://w3id.org/linkml/summary_statistics
    rank: 1000
    slot_uri: sh:prefix
    range: string
  version:
    name: version
    description: the version of the resource
    from_schema: https://w3id.org/linkml/summary_statistics
    rank: 1000
    slot_uri: owl:versionIRI
    range: string
  version_info:
    name: version_info
    description: the version info of the resource
    from_schema: https://w3id.org/linkml/summary_statistics
    rank: 1000
    slot_uri: owl:versionInfo
    range: string
class_uri: owl:Ontology

```
</details>

### Induced

<details>
```yaml
name: Ontology
description: An ontology
from_schema: https://w3id.org/linkml/summary_statistics
rank: 1000
attributes:
  id:
    name: id
    description: the unique identifier for the resource
    from_schema: https://w3id.org/linkml/summary_statistics
    identifier: true
    alias: id
    owner: Ontology
    domain_of:
    - SummaryStatisticsReport
    - Ontology
    - Agent
    - ContributorRole
    range: string
  description:
    name: description
    description: a description of the resource
    from_schema: https://w3id.org/linkml/summary_statistics
    rank: 1000
    slot_uri: dcterms:description
    alias: description
    owner: Ontology
    domain_of:
    - Ontology
    range: string
  title:
    name: title
    description: the title of the resource
    from_schema: https://w3id.org/linkml/summary_statistics
    rank: 1000
    slot_uri: dcterms:title
    alias: title
    owner: Ontology
    domain_of:
    - Ontology
    range: string
  prefix:
    name: prefix
    description: the prefix for the ontology
    from_schema: https://w3id.org/linkml/summary_statistics
    rank: 1000
    slot_uri: sh:prefix
    alias: prefix
    owner: Ontology
    domain_of:
    - Ontology
    range: string
  version:
    name: version
    description: the version of the resource
    from_schema: https://w3id.org/linkml/summary_statistics
    rank: 1000
    slot_uri: owl:versionIRI
    alias: version
    owner: Ontology
    domain_of:
    - Ontology
    range: string
  version_info:
    name: version_info
    description: the version info of the resource
    from_schema: https://w3id.org/linkml/summary_statistics
    rank: 1000
    slot_uri: owl:versionInfo
    alias: version_info
    owner: Ontology
    domain_of:
    - Ontology
    range: string
class_uri: owl:Ontology

```
</details>