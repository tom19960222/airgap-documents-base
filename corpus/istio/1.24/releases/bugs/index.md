---
collection: istio
version: "1.24"
title: "Reporting Bugs"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/releases/bugs/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "What to do if you find a bug."
---
Oh no! You found a bug? We'd love to hear about it.

## Product bugs

Search our [issue database](https://github.com/istio/istio/issues/) to see if
we already know about your problem and learn about when we think we can fix
it. If you don't find your problem in the database, please open a [new
issue](https://github.com/istio/istio/issues/new/choose) and let us know
what's going on.

If you think a bug is in fact a security vulnerability, please visit [Reporting Security Vulnerabilities](../security-vulnerabilities/index.md)
to learn what to do.

### Kubernetes cluster state archives

If you're running on Kubernetes, consider including a cluster state
archive with your bug report.
For convenience, you can run the `istioctl bug-report` command to produce an archive containing
all of the relevant state from your Kubernetes cluster:

```bash
$ istioctl bug-report
```

Then attach the produced `bug-report.tgz` with your reported problem.

If your mesh spans multiple clusters, run `istioctl bug-report` against each cluster, specifying the `--context`
or `--kubeconfig` flags.

> **Tip:**
>
> The `istioctl bug-report` command is only available with `istioctl` version `1.8.0` and higher but it can be used to also collect the information from an older Istio version installed in your cluster.

> **Tip:**
>
> If you are running `bug-report` on a large cluster, it might fail to complete.
> Please use the `--include ns1,ns2` option to target the collection of proxy
> commands and logs only for the relevant namespaces. For more bug-report options,
> please visit [the istioctl bug-report
> reference](https://istio.io/v1.24/docs/reference/commands/istioctl/#istioctl-bug-report) <!-- unresolved-site-link: route=/docs/reference/commands/istioctl -->.

If you are unable to use the `bug-report` command, please attach your own archive
containing:

* Output of istioctl analyze:

```bash
$ istioctl analyze --all-namespaces
```

* Pods, services, deployments, and endpoints across all namespaces:

```bash
$ kubectl get pods,services,deployments,endpoints --all-namespaces -o yaml > k8s_resources.yaml
```

* Secret names in `istio-system`:

```bash
$ kubectl --namespace istio-system get secrets
```

* configmaps in the `istio-system` namespace:

```bash
$ kubectl --namespace istio-system get cm -o yaml
```

* Current and previous logs from all Istio components and sidecars. Here some examples on how to obtain those, please adapt for your environment:

    * Istiod logs:

```bash
$ kubectl logs -n istio-system -l app=istiod
```

    * Ingress Gateway logs:

```bash
$ kubectl logs -l istio=ingressgateway -n istio-system
```

    * Egress Gateway logs:

```bash
$ kubectl logs -l istio=egressgateway -n istio-system
```

    * Sidecar logs:

```bash
$ for ns in $(kubectl get ns -o jsonpath='{.items[*].metadata.name}') ; do kubectl logs -l service.istio.io/canonical-revision -c istio-proxy -n $ns ; done
```

* All Istio configuration artifacts:

```bash
$ kubectl get istio-io --all-namespaces -o yaml
```

## Documentation bugs

Search our [documentation issue database](https://github.com/istio/istio.io/issues/) to see if
we already know about your problem and learn about when we think we can fix it. If you don't
find your problem in the database, please [report the issue there](https://github.com/istio/istio.io/issues/new).
If you want to submit a proposed edit to a page, you will find an "Edit this Page on GitHub"
link at the bottom right of every page.
