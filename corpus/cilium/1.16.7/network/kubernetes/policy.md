---
collection: cilium
version: "1.16.7"
title: "Network Policy"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/network/kubernetes/policy.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

<a id="k8s_policy"></a>

# Network Policy

If you are running Cilium on Kubernetes, you can benefit from Kubernetes
distributing policies for you. In this mode, Kubernetes is responsible for
distributing the policies across all nodes and Cilium will automatically apply
the policies. Three formats are available to configure network policies natively
with Kubernetes:

- The standard `NetworkPolicy` resource which supports L3 and L4 policies
  at ingress or egress of the Pod.

- The extended `CiliumNetworkPolicy` format which is available as a
  CustomResourceDefinition which supports specification of policies
  at Layers 3-7 for both ingress and egress.

- The `CiliumClusterwideNetworkPolicy` format which is a cluster-scoped
  CustomResourceDefinition for specifying cluster-wide policies to be enforced
  by Cilium. The specification is same as that of `CiliumNetworkPolicy` with
  no specified namespace.

Cilium supports running multiple of these policy types at the same time.
However caution should be applied when using multiple policy types at the same
time, as it can be confusing to understand the complete set of allowed traffic
across multiple policy types.  If close attention is not applied this may lead
to unintended policy allow behavior.

<a id="networkpolicy"></a>
<a id="networkpolicy_state"></a>

## NetworkPolicy

For more information, see the official [NetworkPolicy documentation](https://kubernetes.io/docs/concepts/services-networking/network-policies/).

Known missing features for Kubernetes Network Policy:

| Feature | Tracking Issue |
| --- | --- |
| ``ipBlock`` set with a pod IP | 9209 |
| SCTP | 5719 |

As of v1.15, ``ipBlock`` can now optionally select [node IPs](../../security/policy/language.md#cidr_select_nodes). Previously,
nodes were excluded from ``ipBlock``; see 20550.

<a id="ciliumnetworkpolicy"></a>

## CiliumNetworkPolicy

The `CiliumNetworkPolicy` is very similar to the standard `NetworkPolicy`. The
purpose is to provide the functionality which is not yet supported in
`NetworkPolicy`. Ideally all of the functionality will be merged into the
standard resource format and this CRD will no longer be required.

The raw specification of the resource in Go looks like this:

```go
type CiliumNetworkPolicy struct {
        // +deepequal-gen=false
        metav1.TypeMeta `json:",inline"`
        // +deepequal-gen=false
        metav1.ObjectMeta `json:"metadata"`

        // Spec is the desired Cilium specific rule specification.
        Spec *api.Rule `json:"spec,omitempty"`

        // Specs is a list of desired Cilium specific rule specification.
        Specs api.Rules `json:"specs,omitempty"`

        // Status is the status of the Cilium policy rule
        //
        // +deepequal-gen=false
        // +kubebuilder:validation:Optional
        Status CiliumNetworkPolicyStatus `json:"status"`
}
```

Metadata
  Describes the policy. This includes:

    * Name of the policy, unique within a namespace
    * Namespace of where the policy has been injected into
    * Set of labels to identify a resource in Kubernetes

Spec
  Field which contains a [policy_rule](../../security/policy/intro.md#policy_rule).
Specs
  Field which contains a list of [policy_rule](../../security/policy/intro.md#policy_rule). This field is useful if
  multiple rules must be removed or added automatically.

Status
  Provides visibility into whether the policy has been successfully applied.

## Examples

See [policy_examples](../../security/policy/language.md#policy_examples), [l4_policy](../../security/policy/language.md#l4_policy) and [l7_policy](../../security/policy/language.md#l7_policy) for
detailed lists of example policies.

<a id="ciliumclusterwidenetworkpolicy"></a>

## CiliumClusterwideNetworkPolicy

`CiliumClusterwideNetworkPolicy` is similar to `CiliumNetworkPolicy`, except
(1) policies defined by `CiliumClusterwideNetworkPolicy` are non-namespaced and are
cluster-scoped, and (2) it enables the use of [NodeSelector](https://kubernetes.io/docs/concepts/scheduling-eviction/assign-pod-node/#nodeselector). Internally
the policy is identical to `CiliumNetworkPolicy` and thus the effects of this
policy specification are also same.

The raw specification of the resource in Go looks like this:

```go
type CiliumClusterwideNetworkPolicy struct {
        // Spec is the desired Cilium specific rule specification.
        Spec *api.Rule

        // Specs is a list of desired Cilium specific rule specification.
        Specs api.Rules

        // Status is the status of the Cilium policy rule.
        //
        // The reason this field exists in this structure is due a bug in the k8s
        // code-generator that doesn't create a `UpdateStatus` method because the
        // field does not exist in the structure.
        //
        // +kubebuilder:validation:Optional
        Status CiliumNetworkPolicyStatus
}
```
