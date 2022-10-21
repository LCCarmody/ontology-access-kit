# Slot: subject_label
_The portion of the subject text that is matched, ranging from subject_start to subject_end_


URI: [ann:subject_label](https://w3id.org/linkml/text_annotator/subject_label)



<!-- no inheritance hierarchy -->




## Applicable Classes

| Name | Description |
| --- | --- |
[HasSpan](HasSpan.md) | None
[TextAnnotation](TextAnnotation.md) | An individual text annotation






## Properties

* Range: [xsd:string](http://www.w3.org/2001/XMLSchema#string)
* Multivalued: None







## Identifier and Mapping Information







### Schema Source


* from schema: https://w3id.org/linkml/text_annotator




## LinkML Source

<details>
```yaml
name: subject_label
description: The portion of the subject text that is matched, ranging from subject_start
  to subject_end
from_schema: https://w3id.org/linkml/text_annotator
exact_mappings:
- bpa:text
rank: 1000
alias: subject_label
owner: HasSpan
domain_of:
- HasSpan
range: string

```
</details>