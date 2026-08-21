---
collection: k8s
version: "1.31.6"
title: "ReloadKubeletServerCertificateFile"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/reload-kubelet-server-certificate-file.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Enable the kubelet TLS server to update its certificate if the specified certificate file are changed.

This feature is useful when specifying `tlsCertFile` and `tlsPrivateKeyFile` in kubelet configuration.
The feature gate has no effect for other cases such as using TLS boostrap.
