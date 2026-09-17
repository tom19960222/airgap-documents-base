---
collection: istio
version: "1.24"
title: "NamespaceNotInjected"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/config/analysis/ist0102/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
This message occurs when a namespace is missing either the `istio-injection` label,
which enables/disables sidecar injection, or the `istio.io/rev` label,
which specifies the Istio control plane revision for the sidecar, or when
`.values.sidecarInjectorWebhook.enableNamespacesByDefault` is not enabled.

For example, you receive this error:

```plain
Warn [IST0102] (Namespace default) The namespace is not enabled for Istio
injection. Run 'kubectl label namespace default istio-injection=enabled' to
enable it, or 'kubectl label namespace default istio-injection=disabled' to
explicitly mark it as not needing injection Error: Analyzer found issues.
```

To resolve this problem, use a label to explicitly declare whether
or not you want the namespace to be auto-injected. For example:

```bash
$ kubectl label namespace <namespace-name> istio-injection=enabled
```

It is strongly recommended to explicitly define the desired injection behavior.
Forgetting to add labels to a namespace is a common cause of errors.
