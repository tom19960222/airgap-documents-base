---
collection: cilium
version: "1.16.7"
title: "requirements-eks"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/installation/requirements-eks.rst
fetched_at: 2025-02-13T12:04:31Z
---
To install Cilium on [Amazon Elastic Kubernetes Service (EKS)](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html),
perform the following steps:

**Default Configuration:**

| Datapath | IPAM | Datastore |
| --- | --- | --- |
| Direct Routing (ENI) | AWS ENI | Kubernetes CRD |

For more information on AWS ENI mode, see [ipam_eni](../network/concepts/ipam/eni.md#ipam_eni).

> **Tip:**
> To chain Cilium on top of the AWS CNI, see [chaining_aws_cni](cni-chaining-aws-cni.md#chaining_aws_cni).
>
> You can also bring up Cilium in a Single-Region, Multi-Region, or Multi-AZ environment for EKS.

**Requirements:**

* The [EKS Managed Nodegroups](https://eksctl.io/usage/eks-managed-nodes) must
  be properly tainted to ensure applications pods are properly managed by
  Cilium:

  * ``managedNodeGroups`` should be tainted with
    ``node.cilium.io/agent-not-ready=true:NoExecute`` to ensure application
    pods will only be scheduled once Cilium is ready to manage them. However,
    there are other options. Please make sure to read and understand the
    documentation page on [taint effects and unmanaged pods](taints.md#taint_effects).

    Below is an example on how to use [ClusterConfig](https://eksctl.io/usage/creating-and-managing-clusters/#using-config-files)
    file to create the cluster:

```yaml
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig
...
managedNodeGroups:
- name: ng-1
  ...
  # taint nodes so that application pods are
  # not scheduled/executed until Cilium is deployed.
  # Alternatively, see the note above regarding taint effects.
  taints:
   - key: "node.cilium.io/agent-not-ready"
     value: "true"
     effect: "NoExecute"
```

**Limitations:**

* The AWS ENI integration of Cilium is currently only enabled for IPv4. If you
  want to use IPv6, use a datapath/IPAM mode other than ENI.
