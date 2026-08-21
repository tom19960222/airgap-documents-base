---
collection: k8s
version: "1.31.6"
title: "LabelSelector"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/kubernetes-api/common-definitions/label-selector.md
fetched_at: 2026-01-16T10:18:07+05:30
---
<!--
The file is auto-generated from the Go source code of the component using a generic
[generator](https://github.com/kubernetes-sigs/reference-docs/). To learn how
to generate the reference documentation, please read
[Contributing to the reference documentation](/docs/contribute/generate-ref-docs/).
To update the reference content, please follow the 
[Contributing upstream](/docs/contribute/generate-ref-docs/contribute-upstream/)
guide. You can file document formatting bugs against the
[reference-docs](https://github.com/kubernetes-sigs/reference-docs/) project.
-->

`import "k8s.io/apimachinery/pkg/apis/meta/v1"`

A label selector is a label query over a set of resources. The result of matchLabels and matchExpressions are ANDed. An empty label selector matches all objects. A null label selector matches no objects.

<hr>

- **matchExpressions** ([]LabelSelectorRequirement)

  *Atomic: will be replaced during a merge*
  
  matchExpressions is a list of label selector requirements. The requirements are ANDed.

  <a name="LabelSelectorRequirement"></a>
  *A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.*

  - **matchExpressions.key** (string), required

    key is the label key that the selector applies to.

  - **matchExpressions.operator** (string), required

    operator represents a key's relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.

  - **matchExpressions.values** ([]string)

    *Atomic: will be replaced during a merge*
    
    values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.

- **matchLabels** (map[string]string)

  matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.
