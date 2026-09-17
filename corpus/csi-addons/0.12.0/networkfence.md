---
collection: csi-addons
version: "0.12.0"
title: "NetworkFence"
source_url: https://github.com/csi-addons/kubernetes-csi-addons/blob/57383f123ba4500174f945b919e81f41b61541d9/docs/networkfence.md
fetched_at: 2025-03-03T16:21:53+01:00
---
# NetworkFence

NetworkFence is a cluster-scoped custom resource that allows Kubernetes to invoke "Network fence" operation on a storage provider.

The user needs to specify the list of CIDR blocks on which network fencing operation will be performed; alongside the csi driver name.
The creation of NetworkFence CR will add a network fence, and its deletion will undo the operation.

## Fence Operation

```yaml
apiVersion: csiaddons.openshift.io/v1alpha1
kind: NetworkFence
metadata:
  name: network-fence-sample
spec:
  driver: example.driver
  cidrs:
    - 10.90.89.66/32
    - 11.67.12.42/24
  secret:
    name: fence-secret
    namespace: default
  parameters:
    key: value
```

> **Note**: Creation of a NetworkFence CR blocks access to the corresponding CIDR block; which is then unblocked the CR deletion.

- `provisioner`: specifies the name of storage provisioner.
- `cidrs`: refers to the CIDR blocks on which the mentioned fence/unfence operation is to be performed.
- `secret`: refers to the kubernetes secret required for network fencing operation.
  - `name`: specifies the name of the secret
  - `namespace`: specifies the namespace in which the secret is located.
- `parameters`: specifies storage provider specific parameters.
