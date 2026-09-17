---
collection: cilium
version: "1.16.7"
title: "Troubleshooting Cilium deployed with Argo CD"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/configuration/argocd-issues.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

<a id="argocd_issues"></a>

# Troubleshooting Cilium deployed with Argo CD

There have been reports from users hitting issues with Argo CD. This documentation
page outlines some of the known issues and their solutions.

## Argo CD deletes CustomResourceDefinitions

When deploying Cilium with Argo CD, some users have reported that Cilium-generated custom resources disappear,
causing one or more of the following issues:

- ``ciliumid`` not found (17614)
- Argo CD Out-of-sync issues for hubble-generate-certs (14550)
- Out-of-sync issues for Cilium using Argo CD (18298)

### Solution

To prevent these issues, declare resource exclusions in the Argo CD ``ConfigMap`` by following [these instructions](https://argo-cd.readthedocs.io/en/stable/operator-manual/declarative-setup/#resource-exclusioninclusion).

Here is an example snippet:

```yaml
resource.exclusions: |
 - apiGroups:
     - cilium.io
   kinds:
     - CiliumIdentity
   clusters:
     - "*"
```

Also, it has been reported that the problem may affect all workloads you deploy with Argo CD in a cluster running Cilium, not just Cilium itself.
If so, you will need the following exclusions in your Argo CD application definition to avoid getting “out of sync” when Hubble rotates its certificates.

```yaml
ignoreDifferences:
  - group: ""
    kind: ConfigMap
    name: hubble-ca-cert
    jsonPointers:
    - /data/ca.crt
  - group: ""
    kind: Secret
    name: hubble-relay-client-certs
    jsonPointers:
    - /data/ca.crt
    - /data/tls.crt
    - /data/tls.key
  - group: ""
    kind: Secret
    name: hubble-server-certs
    jsonPointers:
    - /data/ca.crt
    - /data/tls.crt
    - /data/tls.key
```

> **Note:**
> After applying the above configurations, for the settings to take effect, you will need to restart the Argo CD deployments.

## Helm template with serviceMonitor enabled fails

Some users have reported that when they install Cilium using Argo CD and run ``helm template`` with ``serviceMonitor`` enabled, it fails.
It fails because Argo CD CLI doesn't pass the ``--api-versions`` flag to Helm upon deployment.

### Solution

This [pull request](https://github.com/argoproj/argo-cd/pull/8371) fixed this issue in Argo CD's [v2.3.0 release](https://github.com/argoproj/argo-cd/releases/tag/v2.3.0).
Upgrade your Argo CD and check if ``helm template`` with ``serviceMonitor`` enabled still fails.

> **Note:**
> When using ``helm template``, it is highly recommended you set
> ``--kube-version`` and ``--api-versions`` with the values matching your
> target Kubernetes cluster. Helm charts such as Cilium's often conditionally
> enable certain Kubernetes features based on their availability (beta vs
> stable) on the target cluster.
>
> By specifying ``--api-versions=monitoring.coreos.com/v1`` you should be
> able to pass validation with ``helm template``.

If you have an issue with Argo CD that's not outlined above, check this [list
of Argo CD related issues on GitHub](https://github.com/cilium/cilium/issues?q=is%3Aissue+argocd).
If you can't find an issue that relates to yours, create one and/or seek help
on Cilium Slack <!-- unresolved-rst-link: kind=named target=Cilium Slack -->.
