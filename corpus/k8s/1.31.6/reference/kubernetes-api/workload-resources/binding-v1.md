---
collection: k8s
version: "1.31.6"
title: "Binding"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/kubernetes-api/workload-resources/binding-v1.md
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

`apiVersion: v1`

`import "k8s.io/api/core/v1"`

## Binding {#Binding}

Binding ties one object to another; for example, a pod is bound to a node by a scheduler. Deprecated in 1.7, please use the bindings subresource of pods instead.

<hr>

- **apiVersion**: v1

- **kind**: Binding

- **metadata** (<a href="../common-definitions/object-meta#ObjectMeta">ObjectMeta</a>)

  Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata

- **target** (<a href="../common-definitions/object-reference#ObjectReference">ObjectReference</a>), required

  The target object that you want to bind to the standard object.

## Operations {#Operations}

<hr>

### `create` create a Binding

#### HTTP Request

POST /api/v1/namespaces/{namespace}/bindings

#### Parameters

- **namespace** (*in path*): string, required

  <a href="../common-parameters/common-parameters#namespace">namespace</a>

- **body**: <a href="../workload-resources/binding-v1#Binding">Binding</a>, required

  

- **dryRun** (*in query*): string

  <a href="../common-parameters/common-parameters#dryRun">dryRun</a>

- **fieldManager** (*in query*): string

  <a href="../common-parameters/common-parameters#fieldManager">fieldManager</a>

- **fieldValidation** (*in query*): string

  <a href="../common-parameters/common-parameters#fieldValidation">fieldValidation</a>

- **pretty** (*in query*): string

  <a href="../common-parameters/common-parameters#pretty">pretty</a>

#### Response

200 (<a href="../workload-resources/binding-v1#Binding">Binding</a>): OK

201 (<a href="../workload-resources/binding-v1#Binding">Binding</a>): Created

202 (<a href="../workload-resources/binding-v1#Binding">Binding</a>): Accepted

401: Unauthorized

### `create` create binding of a Pod

#### HTTP Request

POST /api/v1/namespaces/{namespace}/pods/{name}/binding

#### Parameters

- **name** (*in path*): string, required

  name of the Binding

- **namespace** (*in path*): string, required

  <a href="../common-parameters/common-parameters#namespace">namespace</a>

- **body**: <a href="../workload-resources/binding-v1#Binding">Binding</a>, required

  

- **dryRun** (*in query*): string

  <a href="../common-parameters/common-parameters#dryRun">dryRun</a>

- **fieldManager** (*in query*): string

  <a href="../common-parameters/common-parameters#fieldManager">fieldManager</a>

- **fieldValidation** (*in query*): string

  <a href="../common-parameters/common-parameters#fieldValidation">fieldValidation</a>

- **pretty** (*in query*): string

  <a href="../common-parameters/common-parameters#pretty">pretty</a>

#### Response

200 (<a href="../workload-resources/binding-v1#Binding">Binding</a>): OK

201 (<a href="../workload-resources/binding-v1#Binding">Binding</a>): Created

202 (<a href="../workload-resources/binding-v1#Binding">Binding</a>): Accepted

401: Unauthorized
