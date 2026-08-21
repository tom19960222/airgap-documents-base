---
collection: k8s
version: "1.31.6"
title: "API Access Control"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/access-authn-authz/_index.md
fetched_at: 2026-01-16T10:18:07+05:30
---
For an introduction to how Kubernetes implements and controls API access,
read [Controlling Access to the Kubernetes API](/docs/concepts/security/controlling-access/).

Reference documentation:

- [Authenticating](/docs/reference/access-authn-authz/authentication/)
   - [Authenticating with Bootstrap Tokens](/docs/reference/access-authn-authz/bootstrap-tokens/)
- [Admission Controllers](/docs/reference/access-authn-authz/admission-controllers/)
   - [Dynamic Admission Control](/docs/reference/access-authn-authz/extensible-admission-controllers/)
- [Authorization](/docs/reference/access-authn-authz/authorization/)
   - [Role Based Access Control](/docs/reference/access-authn-authz/rbac/)
   - [Attribute Based Access Control](/docs/reference/access-authn-authz/abac/)
   - [Node Authorization](/docs/reference/access-authn-authz/node/)
   - [Webhook Authorization](/docs/reference/access-authn-authz/webhook/)
- [Certificate Signing Requests](/docs/reference/access-authn-authz/certificate-signing-requests/)
   - including [CSR approval](/docs/reference/access-authn-authz/certificate-signing-requests/#approval-rejection)
     and [certificate signing](/docs/reference/access-authn-authz/certificate-signing-requests/#signing)
- Service accounts
  - [Developer guide](/docs/tasks/configure-pod-container/configure-service-account/)
  - [Administration](/docs/reference/access-authn-authz/service-accounts-admin/)
- [Kubelet Authentication & Authorization](/docs/reference/access-authn-authz/kubelet-authn-authz/)
  - including kubelet [TLS bootstrapping](/docs/reference/access-authn-authz/kubelet-tls-bootstrapping/)
