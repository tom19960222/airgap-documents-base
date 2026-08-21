---
collection: k8s
version: "1.31.6"
title: "AllowInsecureKubeletCertificateSigningRequests"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/allow-insecure-kubelet-certificate-signing-requests.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Disable node admission validation of
[CertificateSigningRequests](/docs/reference/access-authn-authz/certificate-signing-requests/#certificate-signing-requests)
for kubelet signers. Unless you disable this feature gate, Kubernetes enforces that new
kubelet certificates have a `commonName` matching `system:node:$nodeName`.
