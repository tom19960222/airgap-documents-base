---
collection: istio
version: "1.24"
title: "Clean up"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/ambient/getting-started/cleanup/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Delete Istio and associated resources."
---
If you no longer need Istio and associated resources, you can delete them by following the steps in this section.

## Remove waypoint proxies

To remove all waypoint proxies run the following commands:

```bash
$ kubectl label namespace default istio.io/use-waypoint-
$ istioctl waypoint delete --all
```

## Remove the namespace from the ambient data plane

The label that instructs Istio to automatically include applications in the `default` namespace to the ambient mesh is not removed when you remove Istio. Use the following command to remove it:

```bash
$ kubectl label namespace default istio.io/dataplane-mode-
```

You must remove workloads from the ambient data plane before uninstalling Istio.

## Remove the sample application

To delete the Bookinfo sample application and the `curl` deployment, run the following:

```bash
$ kubectl delete httproute reviews
$ kubectl delete authorizationpolicy productpage-viewer
$ kubectl delete -f samples/curl/curl.yaml
$ kubectl delete -f samples/bookinfo/platform/kube/bookinfo.yaml
$ kubectl delete -f samples/bookinfo/platform/kube/bookinfo-versions.yaml
$ kubectl delete -f samples/bookinfo/gateway-api/bookinfo-gateway.yaml
```

## Uninstall Istio

To uninstall Istio:

```bash
$ istioctl uninstall -y --purge
$ kubectl delete namespace istio-system
```

## Remove the Kubernetes Gateway API CRDs

---
---
Remove the Kubernetes Gateway API CRDs:

```bash
$ kubectl delete -f https://github.com/kubernetes-sigs/gateway-api/releases/download/[k8s_gateway_api_version]/standard-install.yaml
```
