# Class: TypeSeverityKeyValue
_key-value pair that maps a validation result type to a severity setting, for overriding default severity_




URI: [vm:TypeSeverityKeyValue](https://w3id.org/linkml/validation-model/TypeSeverityKeyValue)


```{mermaid}
 classDiagram
    class TypeSeverityKeyValue
      TypeSeverityKeyValue : severity
      TypeSeverityKeyValue : type
      
```



<!-- no inheritance hierarchy -->


## Slots

| Name | Cardinality and Range | Description | Inheritance |
| ---  | --- | --- | --- |
| [type](type.md) | 1..1 <br/> [ConstraintComponent](ConstraintComponent.md) | The type of validation result | direct |
| [severity](severity.md) | 0..1 <br/> [SeverityOptions](SeverityOptions.md) | the severity of the issue | direct |



## Usages

| used by | used in | type | used |
| ---  | --- | --- | --- |
| [ValidationConfiguration](ValidationConfiguration.md) | [type_severity_map](type_severity_map.md) | range | [TypeSeverityKeyValue](TypeSeverityKeyValue.md) |






## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/linkml/validation_results





## Mappings

| Mapping Type | Mapped Value |
| ---  | ---  |
| self | vm:TypeSeverityKeyValue |
| native | vm:TypeSeverityKeyValue |


## LinkML Source

<!-- TODO: investigate https://stackoverflow.com/questions/37606292/how-to-create-tabbed-code-blocks-in-mkdocs-or-sphinx -->

### Direct

<details>
```yaml
name: TypeSeverityKeyValue
conforms_to: wikidata:Q4818718
description: key-value pair that maps a validation result type to a severity setting,
  for overriding default severity
from_schema: https://w3id.org/linkml/validation_results
rank: 1000
attributes:
  type:
    name: type
    from_schema: https://w3id.org/linkml/validation_results
    key: true
    range: uriorcurie
  severity:
    name: severity
    from_schema: https://w3id.org/linkml/validation_results
    range: severity_options

```
</details>

### Induced

<details>
```yaml
name: TypeSeverityKeyValue
conforms_to: wikidata:Q4818718
description: key-value pair that maps a validation result type to a severity setting,
  for overriding default severity
from_schema: https://w3id.org/linkml/validation_results
rank: 1000
attributes:
  type:
    name: type
    from_schema: https://w3id.org/linkml/validation_results
    key: true
    alias: type
    owner: TypeSeverityKeyValue
    domain_of:
    - TypeSeverityKeyValue
    - ValidationResult
    range: ConstraintComponent
    required: true
  severity:
    name: severity
    from_schema: https://w3id.org/linkml/validation_results
    alias: severity
    owner: TypeSeverityKeyValue
    domain_of:
    - TypeSeverityKeyValue
    - ValidationResult
    range: severity_options

```
</details>