---
collection: cilium
version: "1.16.7"
title: "requirements-openshift"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/installation/requirements-openshift.rst
fetched_at: 2025-02-13T12:04:31Z
---
To install Cilium on [OpenShift](https://www.openshift.com/),
perform the following steps:

**Default Configuration:**

| Datapath | IPAM | Datastore |
| --- | --- | --- |
| Encapsulation | Cluster Pool | Kubernetes CRD |

**Requirements:**

* OpenShift 4.x
