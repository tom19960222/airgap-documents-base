---
collection: cilium
version: "1.16.7"
title: "Threat Model"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/security/threat-model.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

# Threat Model

This section presents a threat model for Cilium. This threat model
allows interested parties to understand:

-  security-specific implications of Cilium's architecture
-  controls that are in place to secure data flowing through Cilium's various components
-  recommended controls for running Cilium in a production environment

## Scope and Prerequisites

This threat model considers the possible attacks that could affect an
up-to-date version of Cilium running in a production environment; it
will be refreshed when there are significant changes to Cilium's
architecture or security posture.

This model does not consider supply-chain attacks, such as attacks where
a malicious contributor is able to intentionally inject vulnerable code
into Cilium. For users who are concerned about supply-chain attacks,
Cilium's [security audit](https://github.com/cilium/cilium.io/blob/main/Security-Reports/CiliumSecurityAudit2022.pdf) assessed Cilium's supply chain controls
against [the SLSA framework](https://slsa.dev/).

In order to understand the following threat model, readers will need
familiarity with basic Kubernetes concepts, as well as a high-level
understanding of Cilium's [architecture and components](../overview/component-overview.md#component_overview).

## Methodology

This threat model considers eight different types of threat
actors, placed at different parts of a typical deployment stack. We will
primarily use Kubernetes as an example but the threat model remains
accurate if deployed with other orchestration systems, or when running
Cilium outside of Kubernetes. The attackers will have different levels
of initial privileges, giving us a broad overview of the security
guarantees that Cilium can provide depending on the nature of the threat
and the extent of a previous compromise.

For each threat actor, this guide uses the [the STRIDE methodology](https://en.wikipedia.org/wiki/STRIDE_(security)) to
assess likely attacks. Where one attack type in the STRIDE set can lead to others
(for example, tampering leading to denial of service), we have described the
attack path under the most impactful attack type. For the potential attacks
that we identify, we recommend controls that can be used to reduce the
risk of the identified attacks compromising a cluster. Applying the
recommended controls is strongly advised in order to run Cilium securely
in production.

## Reference Architecture

For ease of understanding, consider a single Kubernetes
cluster running Cilium, as illustrated below:

![](https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/security/images/cilium_threat_model_reference_architecture.png)

### The Threat Surface

In the above scenario, the aim of Cilium's security controls is to
ensure that all the components of the Cilium platform are operating
correctly, to the extent possible given the abilities of the threat
actor that Cilium is faced with. The key components that need to be
protected are:

-  the Cilium agent running on a node, either as a Kubernetes pod, a host process, or as an entire virtual machine
-  Cilium state (either stored via CRDs or via an external key-value store like etcd)
-  eBPF programs loaded by Cilium into the kernel
-  network packets managed by Cilium
-  observability data collected by Cilium and stored by Hubble

## The Threat Model

For each type of attacker, we consider the plausible types of attacks
available to them, how Cilium can be used to protect against these
attacks, as well as the security controls that Cilium provides. For
attacks which might arise as a consequence of the high level of
privileges required by Cilium, we also suggest mitigations that users
should apply to secure their environments.

<a id="kubernetes-workload-attacker"></a>

### Kubernetes Workload Attacker

For the first scenario, consider an attacker who has been able to
gain access to a Kubernetes pod, and is now able to run arbitrary code
inside a container. This could occur, for example, if a vulnerable
service is exposed externally to a network. In this case, let us also
assume that the compromised pod does not have any elevated privileges
(in Kubernetes or on the host) or direct access to host files.

![](https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/security/images/cilium_threat_model_workload.png)

In this scenario, there is no potential for compromise of the Cilium
stack; in fact, Cilium provides several features that would allow users
to limit the scope of such an attack:

.. rst-class:: wrapped-table

| Threat surface <br> | Identified STRIDE <br> threats | Cilium security benefits <br> |
| --- | --- | --- |
| Cilium agent <br> <br> <br> <br> <br> <br> <br> | Potential denial of <br> service if the <br> compromised <br> <br> Kubernetes workload <br> does not have <br> defined resource <br> limits. | Cilium can enforce <br> [bandwidth limitations](https://docs.cilium.io/en/stable/network/kubernetes/bandwidth-manager/) <br> on pods to limit the network <br> resource utilization. <br> <br> <br> <br> |
| Cilium <br> configuration | None <br> | <br> |
| Cilium eBPF <br> programs | None <br> | <br> |
| Network data <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> | None <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> | - Cilium's network policy can <br> be used to provide <br> least-privilege isolation <br> between Kubernetes <br> workloads, and between <br> Kubernetes workloads and <br> "external" endpoints running <br> outside the Kubernetes <br> cluster, or running on the <br> Kubernetes worker nodes. <br> Users should ideally define <br> specific allow rules that <br> only permit expected <br> communication between <br> services. <br> - Cilium's network <br> connectivity will prevent an <br> attacker from observing the <br> traffic intended for other <br> workloads, or sending <br> traffic that "spoofs" the <br> identity of another pod, <br> even if transparent <br> encryption is not in use. <br> Pods cannot send traffic <br> that "spoofs" other pods due <br> to limits on the use of <br> source IPs and limits on <br> sending tunneled traffic. |
| Observability <br> data <br> <br> <br> | None <br> <br> <br> <br> | Cilium's Hubble flow-event <br> observability can be used to <br> provide reliable audit of <br> the attacker's L3/L4 and L7 <br> network connectivity. |

#### Recommended Controls

-  Kubernetes workloads should have [defined resource limits](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/).
   This will help in ensuring that Cilium is not starved of resources due to a misbehaving deployment in a cluster.
-  Cilium can be given prioritized access to system resources either via
   Kubernetes, cgroups, or other controls.
-  Runtime security solutions such as [Tetragon](https://github.com/cilium/tetragon) should be deployed to
   ensure that container compromises can be detected as they occur.

<a id="limited-privilege-host-attacker"></a>

### Limited-privilege Host Attacker

In this scenario, the attacker is someone with the ability to run
arbitrary code with direct access to the host PID or network namespace
(or both), but without "root" privileges that would allow them to
disable Cilium components or undermine the eBPF and other kernel state
Cilium relies on.

This level of access could exist for a variety of reasons, including:

-  Pods or other containers running in the host PID or network
   namespace, but not with "root" privileges. This includes
   ``hostNetwork: true`` and ``hostPID: true`` containers.
-  Non-"root" SSH or other console access to a node.
-  A containerized workload that has "escaped" the container namespace
   but as a non-privileged user.

![](https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/security/images/cilium_threat_model_non_privileged.png)

In this case, an attacker would be able to bypass some of Cilium's
network controls, as described below:

.. rst-class:: wrapped-table

| **Threat <br> surface** | **Identified STRIDE <br> threats** | **Cilium security <br> benefits** |
| --- | --- | --- |
| Cilium agent <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> | - If the non-privileged <br> attacker is able to <br> access the container <br> runtime and Cilium is <br> running as a <br> container, the <br> attacker will be able <br> to tamper with the <br> Cilium agent running <br> on the node. <br> - Denial of service is <br> also possible via <br> spawning workloads <br> directly on the host. | <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> |
| Cilium <br> configuration <br> <br> <br> <br> <br> <br> <br> | Same as for the Cilium <br> agent. <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> <br> |
| Cilium eBPF <br> programs <br> <br> <br> <br> <br> <br> <br> | Same as for the Cilium <br> agent. <br> <br> <br> <br> <br> <br> <br> | <br> <br> <br> <br> <br> <br> <br> <br> |
| Network data <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> | Elevation of <br> privilege: traffic <br> sent by the attacker <br> will no longer be <br> subject to Kubernetes <br> or <br> container-networked <br> Cilium network <br> policies. <br> [Host-networked <br> Cilium <br> policies <br>](host-firewall.md#host_firewall) <br> will continue to <br> apply. Other traffic <br> within the cluster <br> remains unaffected. | Cilium's network <br> connectivity will prevent <br> an attacker from observing <br> the traffic intended for <br> other workloads, or <br> sending traffic that <br> spoofs the identity of <br> another pod, even if <br> transparent encryption is <br> not in use. <br> <br> <br> <br> <br> <br> <br> |
| Observability <br> data <br> <br> <br> <br> <br> <br> <br> <br> <br> | None <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> | Cilium's Hubble flow-event <br> observability can be used <br> to provide reliable audit <br> of the attacker's L3/L4 <br> and L7 network <br> connectivity. Traffic sent <br> by the attacker will be <br> attributed to the worker <br> node, and not to a <br> specific Kubernetes <br> workload. |

#### Recommended Controls

In addition to the recommended controls against the [kubernetes-workload-attacker](threat-model.md#kubernetes-workload-attacker):

-  Container images should be regularly patched to reduce the chance of
   compromise.
-  Minimal container images should be used where possible.
-  Host-level privileges should be avoided where possible.
-  Ensure that the container users do not have access to the underlying
   container runtime.

<a id="root-equivalent-host-attacker"></a>

### Root-equivalent Host Attacker

A "root" privilege host attacker has full privileges to do everything on
the local host. This access could exist for several reasons, including:

-  Root SSH or other console access to the Kubernetes worker node.
-  A containerized workload that has escaped the container namespace as
   a privileged user.
-  Pods running with ``privileged: true`` or other significant
   capabilities like ``CAP_SYS_ADMIN`` or ``CAP_BPF``.

![](https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/security/images/cilium_threat_model_root.png)

.. rst-class:: wrapped-table

+-------------------+--------------------------------------------------+
| **Threat          | **Identified STRIDE threats**                    |
| surface**         |                                                  |
+===================+==================================================+
| Cilium agent      | In this situation, all potential attacks covered |
|                   | by STRIDE are possible. Of note:                 |
|                   |                                                  |
|                   | -  The attacker would be able to disable eBPF on |
|                   |    the node, disabling Cilium's network and      |
|                   |    runtime visibility and enforcement. All       |
|                   |    further operations by the attacker will be    |
|                   |    unlimited and unaudited.                      |
|                   | -  The attacker would be able to observe network |
|                   |    connectivity across all workloads on the      |
|                   |    host.                                         |
|                   | -  The attacker can spoof traffic from the node  |
|                   |    such that it appears to come from pods        |
|                   |    with any identity.                            |
|                   | -  If the physical network allows ARP poisoning, |
|                   |    or if any other attack allows a               |
|                   |    compromised node to "attract" traffic         |
|                   |    destined to other nodes, the attacker can     |
|                   |    potentially intercept all traffic in the      |
|                   |    cluster, even if this traffic is encrypted    |
|                   |    using IPsec, since we use a cluster-wide      |
|                   |    pre-shared key.                               |
|                   | -  The attacker can also use Cilium's            |
|                   |    credentials to [attack the Kubernetes | | | API server](threat-model.md#kubernetes-api-server-attacker), |
|                   |    as well as Cilium's [etcd key-value | | | store](threat-model.md#kv-store-attacker) (if in use).       |
|                   | -  If the compromised node is running the        |
|                   |    ``cilium-operator`` pod, the attacker         |
|                   |    would be able to carry out denial of          |
|                   |    service attacks against other nodes using     |
|                   |    the ``cilium-operator`` service account       |
|                   |    credentials found on the node.                |
+-------------------+                                                  |
| Cilium            |                                                  |
| configuration     |                                                  |
+-------------------+                                                  |
| Cilium eBPF       |                                                  |
| programs          |                                                  |
+-------------------+                                                  |
| Network data      |                                                  |
+-------------------+                                                  |
| Observability     |                                                  |
| data              |                                                  |
+-------------------+--------------------------------------------------+

This attack scenario emphasizes the importance of securing Kubernetes
nodes, minimizing the permissions available to container workloads, and
monitoring for suspicious activity on the node, container, and API
server levels.

#### Recommended Controls

In addition to the controls against a [limited-privilege-host-attacker](threat-model.md#limited-privilege-host-attacker):

-  Workloads with privileged access should be reviewed; privileged access should
   only be provided to deployments if essential.
-  Network policies should be configured to limit connectivity to workloads with
   privileged access.
-  Kubernetes audit logging should be enabled, with audit logs being sent to a
   centralized external location for automated review.
-  Detections should be configured to alert on suspicious activity.
-  ``cilium-operator`` pods should not be scheduled on nodes that run regular
   workloads, and should instead be configured to run on control plane nodes.

<a id="mitm-attacker"></a>

### Man-in-the-middle Attacker

In this scenario, our attacker has access to the underlying network
between Kubernetes worker nodes, but not the Kubernetes worker nodes
themselves. This attacker may inspect, modify, or inject malicious
network traffic.

![](https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/security/images/cilium_threat_model_mitm.png)

The threat matrix for such an attacker is as follows:

.. rst-class:: wrapped-table

| **Threat <br> surface** | **Identified STRIDE threats** <br> |
| --- | --- |
| Cilium agent | None |
| Cilium <br> configuration | None <br> |
| Cilium eBPF <br> programs | None <br> |
| Network data <br> <br> <br> <br> <br> <br> <br> <br> | - Without transparent encryption, an attacker <br> could inspect traffic between workloads in both <br> overlay and native routing modes. <br> - An attacker with knowledge of pod network <br> configuration (including pod IP addresses and <br> ports) could inject traffic into a cluster by <br> forging packets. <br> - Denial of service could occur depending on the <br> behavior of the attacker. |
| Observability <br> data <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> | - TLS is required for all connectivity between <br> Cilium components, as well as for exporting <br> data to other destinations, removing the <br> scope for spoofing or tampering. <br> - Without transparent encryption, the attacker <br> could re-create the observability data as <br> available on the network level. <br> - Information leakage could occur via an attacker <br> scraping Hubble Prometheus metrics. These <br> metrics are disabled by default, and <br> can contain sensitive information on network <br> flows. <br> - Denial of service could occur depending on the <br> behavior of the attacker. |

#### Recommended Controls

- [gsg_encryption](network/encryption.md#gsg_encryption) should be configured to ensure the confidentiality of
  communication between workloads.
- TLS should be configured for communication between the Prometheus
  metrics endpoints and the Prometheus server.
- Network policies should be configured such that only the Prometheus
  server is allowed to scrape [Hubble metrics](../configuration/api-rate-limiting.md#metrics) in particular.

<a id="network-attacker"></a>

### Network Attacker

In our threat model, a generic network attacker has access to the same
underlying IP network as Kubernetes worker nodes, but is not inline
between the nodes. The assumption is that this attacker is still able to
send IP layer traffic that reaches a Kubernetes worker node. This is a
weaker variant of the man-in-the-middle attack described above, as the
attacker can only inject traffic to worker nodes, but not see the
replies.

![](https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/security/images/cilium_threat_model_network_attacker.png)

For such an attacker, the threat matrix is as follows:

.. rst-class:: wrapped-table

| **Threat <br> surface** | **Identified STRIDE threats** <br> |
| --- | --- |
| Cilium agent | None |
| Cilium <br> configuration | None <br> |
| Cilium eBPF <br> programs | None <br> |
| Network data <br> <br> <br> <br> <br> | - An attacker with knowledge of pod network <br> configuration (including pod IP addresses and <br> ports) could inject traffic into a cluster by <br> forging packets. <br> - Denial of service could occur depending on the <br> behavior of the attacker. |
| Observability <br> data <br> <br> <br> | - Denial of service could occur depending on the <br> behavior of the attacker. <br> - Information leakage could occur via an attacker <br> scraping Cilium or Hubble Prometheus metrics, <br> depending on the specific metrics enabled. |

#### Recommended Controls

- [gsg_encryption](network/encryption.md#gsg_encryption) should be configured to ensure the confidentiality of
  communication between workloads.

<a id="kubernetes-api-server-attacker"></a>

### Kubernetes API Server Attacker

This type of attack could be carried out by any user or code with
network access to the Kubernetes API server and credentials that allow
Kubernetes API requests. Such permissions would allow the user to read
or manipulate the API server state (for example by changing CRDs).

This section is intended to cover any attack that might be exposed via
Kubernetes API server access, regardless of whether the access is full or
limited.

![](https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/security/images/cilium_threat_model_api_server_attacker.png)

For such an attacker, our threat matrix is as follows:

.. rst-class:: wrapped-table

| **Threat <br> surface** | **Identified STRIDE threats** <br> |
| --- | --- |
| Cilium agent <br> <br> <br> <br> <br> <br> <br> | - A Kubernetes API user with ``kubectl exec`` <br> access to the pod running Cilium effectively <br> becomes a [root-equivalent host <br> attacker](threat-model.md#root-equivalent-host-attacker), <br> since Cilium runs as a privileged pod. <br> - An attacker with permissions to configure <br> workload settings effectively becomes a <br> [kubernetes-workload-attacker](threat-model.md#kubernetes-workload-attacker). |
| Cilium <br> configuration <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> | The ability to modify the ``Cilium*`` <br> CustomResourceDefinitions, as well as any <br> CustomResource from Cilium, in the cluster could <br> have the following effects: <br> <br> - The ability to create or modify CiliumIdentity <br> and CiliumEndpoint or CiliumEndpointSlice <br> resources would allow an attacker to tamper <br> with the identities of pods. <br> - The ability to delete Kubernetes or Cilium <br> NetworkPolicies would remove policy <br> enforcement. <br> - Creating a large number of CiliumIdentity <br> resources could result in denial of service. <br> - Workloads external to the cluster could be <br> added to the network. <br> - Traffic routing settings between workloads <br> could be modified <br> <br> The cumulative effect of such actions could <br> result in the escalation of a single-node <br> compromise into a multi-node compromise. |
| Cilium eBPF <br> programs <br> | An attacker with ``kubectl exec`` access to the <br> Cilium agent pod will be able to modify eBPF <br> programs. |
| Network data <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> <br> | Privileged Kubernetes API server access (``exec`` <br> access to Cilium pods or access to view <br> Kubernetes secrets) could allow an attacker to <br> access the pre-shared key used for IPsec. When <br> used by a [man-in-the-middle <br> attacker](threat-model.md#mitm-attacker), this <br> could undermine the confidentiality and integrity <br> of workload communication. <br> \|br\| \|br\| <br> Depending on the attacker's level of access, the <br> ability to spoof identities or tamper with policy <br> enforcement could also allow them to view network <br> data. |
| Observability <br> data | Users with permissions to configure workload <br> settings could cause denial of service. |

#### Recommended Controls

- [Kubernetes RBAC](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) should be configured to only grant necessary permissions
  to users and service accounts. Access to resources in the ``kube-system``
  and ``cilium`` namespaces in particular should be highly limited.
- Kubernetes audit logs should be used to automatically review requests
  made to the API server, and detections should be configured to
  alert on suspicious activity.

<a id="kv-store-attacker"></a>

### Cilium Key-value Store Attacker

Cilium can use [an external key-value store](../installation/k8s-install-external-etcd.md#k8s_install_etcd)
such as etcd to store state. In this scenario, we consider a user with
network access to the Cilium etcd endpoints and credentials to access
those etcd endpoints. The credentials to the etcd endpoints are stored
as Kubernetes secrets; any attacker would first have to compromise these
secrets before gaining access to the key-value store.

![](https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/security/images/cilium_threat_model_etcd_attacker.png)

.. rst-class:: wrapped-table

| **Threat <br> surface** | **Identified STRIDE threats** <br> |
| --- | --- |
| Cilium agent | None |
| Cilium <br> configuration <br> <br> <br> <br> <br> <br> | The ability to create or modify Identities or <br> Endpoints in etcd would allow an attacker to <br> "give" any pod any identity. The ability to spoof <br> identities in this manner might be used to <br> escalate a single node compromise to a multi-node <br> compromise, for example by spoofing identities to <br> undermine ingress segmentation rules that would <br> be applied on remote nodes. |
| Cilium eBPF <br> programs | None <br> |
| Network data <br> <br> <br> | An attacker would be able to modify the routing <br> of traffic within a cluster, and as a consequence <br> gain the privileges of a [mitm-attacker](threat-model.md#mitm-attacker). <br> |
| Observability <br> data | None <br> |

#### Recommended Controls

-  The ``etcd`` instance deployed to store Cilium configuration should be independent
   of the instance that is typically deployed as part of configuring a Kubernetes
   cluster. This separation reduces the risk of a Cilium ``etcd`` compromise
   leading to further cluster-wide impact.
-  Kubernetes RBAC controls should be applied to restrict access to Kubernetes
   secrets.
-  Kubernetes audit logs should be used to detect access to secret data and
   alert if such access is suspicious.

### Hubble Data Attacker

This is an attacker with network reachability to Kubernetes worker
nodes, or other systems that store or expose Hubble data, with the goal
of gaining access to potentially sensitive Hubble flow or process data.

![](https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/security/images/cilium_threat_model_hubble_attacker.png)

.. rst-class:: wrapped-table

| **Threat <br> surface** | **Identified STRIDE threats** <br> |
| --- | --- |
| Cilium pods | None |
| Cilium <br> configuration | None <br> |
| Cilium eBPF <br> programs | None <br> |
| Network data | None |
| Observability <br> data <br> <br> <br> <br> <br> <br> <br> <br> | None, assuming correct configuration of the <br> following: <br> <br> - Network policy to limit access to <br> ``hubble-relay`` or ``hubble-ui`` services <br> - Limited access to ``cilium``, <br> ``hubble-relay``, or ``hubble-ui`` pods <br> - TLS for external data export <br> - Security controls at the destination of any <br> exported data |

#### Recommended Controls

-  Network policies should limit access to the ``hubble-relay`` and
   ``hubble-ui`` services
-  Kubernetes RBAC should be used to limit access to any ``cilium-*``
   or ``hubble-`*`` pods
-  TLS should be configured for access to the Hubble Relay API and Hubble UI
-  TLS should be correctly configured for any data export
-  The destination data stores for exported data should be secured (such
   as by applying encryption at rest and cloud provider specific RBAC
   controls, for example)

## Overall Recommendations

To summarize the recommended controls to be used when configuring a
production Kubernetes cluster with Cilium:

1. Ensure that Kubernetes roles are scoped correctly to the requirements of your
   users, and that service account permissions for pods are tightly scoped to
   the needs of the workloads. In particular, access to sensitive namespaces,
   ``exec`` actions, and Kubernetes secrets should all be highly controlled.
1. Use resource limits for workloads where possible to reduce the chance of
   denial of service attacks.
1. Ensure that workload privileges and capabilities are only granted when
   essential to the functionality of the workload, and ensure that specific
   controls to limit and monitor the behavior of the workload are in place.
1. Use [network policies](policy/index.md#network_policy) to ensure that network traffic in Kubernetes is segregated.
1. Use [gsg_encryption](network/encryption.md#gsg_encryption) in Cilium to ensure that communication between
   workloads is secured.
1. Enable Kubernetes audit logging, forward the audit logs to a centralized
   monitoring platform, and define alerting for suspicious activity.
1. Enable TLS for access to any externally-facing services, such as Hubble Relay
   and Hubble UI.
1. Use [Tetragon](https://github.com/cilium/tetragon) as a runtime security solution to rapidly detect unexpected
   behavior within your Kubernetes cluster.

If you have questions, suggestions, or would like to help improve Cilium's security
posture, reach out to security@cilium.io.

.. |br| raw:: html

      <br>
