---
collection: cilium
version: "1.16.7"
title: "Restricting privileged Cilium pod access"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/security/restrict-pod-access.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

<a id="security_restrict_pod_access"></a>

# Restricting privileged Cilium pod access

This page shows you how to restrict privileged access to Cilium pods by limiting access from the Kubernetes API, specifically from [kubernetes exec pod](https://kubernetes.io/docs/tasks/debug/debug-application/get-shell-running-container/).

Included file `Documentation/security/gsg_requirements.rst`:

If you haven't read the [intro](../overview/intro.md#intro) yet, we'd encourage you to do that first.

The best way to get help if you get stuck is to ask a question on Cilium Slack <!-- unresolved-rst-link: kind=named target=Cilium Slack -->. With Cilium contributors across the globe, there is almost always
someone available to help.

### Setup Cilium

If you have not set up Cilium yet, follow the guide [k8s_install_standard](../gettingstarted/k8s-install-default.md#k8s_install_standard)
for instructions on how to quickly bootstrap a Kubernetes cluster and install
Cilium. If in doubt, pick the minikube route, you will be good to go in less
than 5 minutes.

## Background

The Cilium agent needs some specific Linux capabilities to perform essential system and network operations.

Cilium relies on Kubernetes and containers to set up the environment and mount the corresponding volumes. Cilium doesn't perform any extra operations that could result in an unsafe volume mount.

Cilium needs kernel interfaces to properly configure the environment. Some kernel interfaces are part of the ``/proc`` filesystem, which includes host and machine configurations that can't be virtualized or namespaced.

If ``pod exec`` operations aren't restricted, then remote [exec into pods](https://kubernetes.io/docs/tasks/debug/debug-application/get-shell-running-container/) and containers defeats Linux namespace restrictions.

The Linux kernel restricts joining other namespaces by default. To enter the Cilium container, the ``CAP_SYS_ADMIN`` capability is required in both the current user namespace and in the Cilium user namespace (the initial namespace). If both namespaces have the ``CAP_SYS_ADMIN`` capability, then this is already a privileged access.

To prevent privileged access to Cilium pods, restrict access to the Kubernetes API and arbitrary ``pod exec`` operations.

## Restrict authorization for ``kubernetes exec pod``

To restrict access to Cilium pods through ``kubernetes exec pod``:

1. Configure [RBAC authorization](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) in Kubernetes.

2. Limit [access to the proxy subresource of Nodes](https://kubernetes.io/docs/concepts/security/rbac-good-practices/#access-to-proxy-subresource-of-nodes).

## References

For more information about namespace security, visit:

- https://man7.org/linux/man-pages/man7/user_namespaces.7.html
- https://man7.org/linux/man-pages/man1/nsenter.1.html
- https://man7.org/linux/man-pages/man2/setns.2.html
