# Class: HasProvenance



* __NOTE__: this is a mixin class intended to be used in combination with other classes, and not used directly


URI: [omoschema:HasProvenance](http://purl.obolibrary.org/obo/schema/HasProvenance)




```{mermaid}
 classDiagram
      AnnotationPropertyMixin <|-- HasProvenance
      
      HasProvenance : contributor
      HasProvenance : created
      HasProvenance : created_by
      HasProvenance : creation_date
      HasProvenance : creator
      HasProvenance : date
      HasProvenance : definition_source
      HasProvenance : editor_note
      HasProvenance : imported_from
      HasProvenance : isDefinedBy
      HasProvenance : ontology_term_requester
      HasProvenance : term_editor
      HasProvenance : term_tracker_item
      

```





## Inheritance
* [AnnotationPropertyMixin](AnnotationPropertyMixin.md)
    * **HasProvenance**



## Slots

| Name | Cardinality and Range  | Description  |
| ---  | ---  | --- |
| [created_by](created_by.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string)  |   |
| [creation_date](creation_date.md) | 0..* <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string)  |   |
| [contributor](contributor.md) | 0..* <br/> [Thing](Thing.md)  |   |
| [creator](creator.md) | 0..* <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string)  |   |
| [created](created.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string)  | when the term came into being  |
| [date](date.md) | 0..* <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string)  | when the term was updated  |
| [isDefinedBy](isDefinedBy.md) | 0..1 <br/> [Ontology](Ontology.md)  |   |
| [editor_note](editor_note.md) | 0..* <br/> [NarrativeText](NarrativeText.md)  |   |
| [term_editor](term_editor.md) | 0..* <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string)  |   |
| [definition_source](definition_source.md) | 0..* <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string)  |   |
| [ontology_term_requester](ontology_term_requester.md) | 0..1 <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string)  |   |
| [imported_from](imported_from.md) | 0..* <br/> [NamedIndividual](NamedIndividual.md)  |   |
| [term_tracker_item](term_tracker_item.md) | 0..* <br/> [xsd:string](http://www.w3.org/2001/XMLSchema#string)  |   |


## Usages



## Identifier and Mapping Information







### Schema Source


* from schema: http://purl.obolibrary.org/obo/omo/schema







## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | ['omoschema:HasProvenance'] |
| native | ['omoschema:HasProvenance'] |


## LinkML Specification

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: HasProvenance
from_schema: http://purl.obolibrary.org/obo/omo/schema
rank: 1000
is_a: AnnotationPropertyMixin
mixin: true
slots:
- created_by
- creation_date
- contributor
- creator
- created
- date
- isDefinedBy
- editor_note
- term_editor
- definition_source
- ontology_term_requester
- imported_from
- term_tracker_item

```
</details>

### Induced

<details>
```yaml
name: HasProvenance
from_schema: http://purl.obolibrary.org/obo/omo/schema
rank: 1000
is_a: AnnotationPropertyMixin
mixin: true
attributes:
  created_by:
    name: created_by
    deprecated: proposed obsoleted by OMO group 2022-04-12
    from_schema: http://purl.obolibrary.org/obo/omo/schema
    deprecated_element_has_exact_replacement: creator
    rank: 1000
    is_a: provenance_property
    slot_uri: oio:created_by
    alias: created_by
    owner: HasProvenance
    domain_of:
    - HasProvenance
    - Axiom
    range: string
  creation_date:
    name: creation_date
    deprecated: proposed obsoleted by OMO group 2022-04-12
    todos:
    - restrict range
    from_schema: http://purl.obolibrary.org/obo/omo/schema
    deprecated_element_has_exact_replacement: created
    rank: 1000
    is_a: provenance_property
    slot_uri: oio:creation_date
    multivalued: true
    alias: creation_date
    owner: HasProvenance
    domain_of:
    - HasProvenance
    range: string
  contributor:
    name: contributor
    from_schema: http://purl.obolibrary.org/obo/omo/schema
    close_mappings:
    - prov:wasAttributedTo
    rank: 1000
    is_a: provenance_property
    slot_uri: dcterms:contributor
    multivalued: true
    alias: contributor
    owner: HasProvenance
    domain_of:
    - HasProvenance
    range: Thing
  creator:
    name: creator
    from_schema: http://purl.obolibrary.org/obo/omo/schema
    close_mappings:
    - prov:wasAttributedTo
    rank: 1000
    is_a: provenance_property
    slot_uri: dcterms:creator
    multivalued: true
    alias: creator
    owner: HasProvenance
    domain_of:
    - HasProvenance
    - Ontology
    range: string
  created:
    name: created
    description: when the term came into being
    from_schema: http://purl.obolibrary.org/obo/omo/schema
    close_mappings:
    - pav:createdOn
    rank: 1000
    is_a: provenance_property
    slot_uri: dcterms:created
    multivalued: false
    alias: created
    owner: HasProvenance
    domain_of:
    - HasProvenance
    - Ontology
    range: string
  date:
    name: date
    description: when the term was updated
    from_schema: http://purl.obolibrary.org/obo/omo/schema
    close_mappings:
    - pav:authoredOn
    rank: 1000
    is_a: provenance_property
    slot_uri: dcterms:date
    multivalued: true
    alias: date
    owner: HasProvenance
    domain_of:
    - HasProvenance
    range: string
  isDefinedBy:
    name: isDefinedBy
    from_schema: http://purl.obolibrary.org/obo/omo/schema
    close_mappings:
    - pav:importedFrom
    - dcterms:publisher
    rank: 1000
    slot_uri: rdfs:isDefinedBy
    alias: isDefinedBy
    owner: HasProvenance
    domain_of:
    - HasProvenance
    range: Ontology
  editor_note:
    name: editor_note
    from_schema: http://purl.obolibrary.org/obo/omo/schema
    rank: 1000
    is_a: provenance_property
    slot_uri: IAO:0000116
    multivalued: true
    alias: editor_note
    owner: HasProvenance
    domain_of:
    - HasProvenance
    range: narrative text
  term_editor:
    name: term_editor
    from_schema: http://purl.obolibrary.org/obo/omo/schema
    rank: 1000
    is_a: provenance_property
    slot_uri: IAO:0000117
    multivalued: true
    alias: term_editor
    owner: HasProvenance
    domain_of:
    - HasProvenance
    range: string
  definition_source:
    name: definition_source
    todos:
    - restrict range
    in_subset:
    - obi permitted profile
    from_schema: http://purl.obolibrary.org/obo/omo/schema
    rank: 1000
    is_a: provenance_property
    slot_uri: IAO:0000119
    multivalued: true
    alias: definition_source
    owner: HasProvenance
    domain_of:
    - HasProvenance
    range: string
  ontology_term_requester:
    name: ontology_term_requester
    from_schema: http://purl.obolibrary.org/obo/omo/schema
    rank: 1000
    is_a: provenance_property
    slot_uri: IAO:0000234
    alias: ontology_term_requester
    owner: HasProvenance
    domain_of:
    - HasProvenance
    range: string
  imported_from:
    name: imported_from
    from_schema: http://purl.obolibrary.org/obo/omo/schema
    rank: 1000
    is_a: provenance_property
    slot_uri: IAO:0000412
    multivalued: true
    alias: imported_from
    owner: HasProvenance
    domain_of:
    - HasProvenance
    range: NamedIndividual
  term_tracker_item:
    name: term_tracker_item
    todos:
    - restrict range
    from_schema: http://purl.obolibrary.org/obo/omo/schema
    rank: 1000
    is_a: provenance_property
    slot_uri: IAO:0000233
    multivalued: true
    alias: term_tracker_item
    owner: HasProvenance
    domain_of:
    - HasProvenance
    range: string

```
</details>