---
collection: istio
version: "1.24"
title: "Getting Started"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/setup/getting-started/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Try Istio’s features quickly and easily."
---
> **Tip:**
>
> Want to explore Istio's ambient mode? Visit the [Getting Started with Ambient Mode](../../ambient/getting-started/_index.md) guide!

This guide lets you quickly evaluate Istio. If you are already familiar with
Istio or interested in installing other configuration profiles or
advanced [deployment models](../../ops/deployment/deployment-models/index.md), refer to our
[which Istio installation method should I use?](https://istio.io/v1.24/about/faq/#install-method-selection) <!-- unresolved-site-link: route=/about/faq -->
FAQ page.

You will need a Kubernetes cluster to proceed. If you don't have a cluster, you can use [kind](../platform-setup/kind/index.md) or any other [supported Kubernetes platform](../platform-setup/_index.md).

Follow these steps to get started with Istio:

1. [Download and install Istio](#download)
1. [Install the Kubernetes Gateway API CRDs](#gateway-api)
1. [Deploy the sample application](#bookinfo)
1. [Open the application to outside traffic](#ip)
1. [View the dashboard](#dashboard)

## Download Istio {#download}

1.  Go to the [Istio release](https://github.com/istio/istio/releases/tag/1.24.0) page to
    download the installation file for your OS, or [download and
    extract the latest release automatically](../additional-setup/download-istio-release/index.md)
    (Linux or macOS):

```bash
$ curl -L https://istio.io/downloadIstio | sh -
```

1.  Move to the Istio package directory. For example, if the package is
    `istio-{{< istio_full_version >}}`:

```bash
$ cd istio-[istio_full_version]
```

    The installation directory contains:

    - Sample applications in `samples/`
    - The [`istioctl`](https://istio.io/v1.24/docs/reference/commands/istioctl) <!-- unresolved-site-link: route=/docs/reference/commands/istioctl --> client binary in the
      `bin/` directory.

1.  Add the `istioctl` client to your path (Linux or macOS):

```bash
$ export PATH=$PWD/bin:$PATH
```

## Install Istio {#install}

For this guide, we use the `demo`
[configuration profile](../additional-setup/config-profiles/index.md). It is
selected to have a good set of defaults for testing, but there are other
profiles for production, performance testing or [OpenShift](../platform-setup/openshift/index.md).

Unlike [Istio Gateways](../../concepts/traffic-management/index.md#gateways), creating
[Kubernetes Gateways](https://gateway-api.sigs.k8s.io/api-types/gateway/) will, by default, also
[deploy gateway proxy servers](../../tasks/traffic-management/ingress/gateway-api/index.md#automated-deployment).
Because they won't be used, we disable the deployment of the default Istio gateway services that
are normally installed as part of the `demo` profile.

1. Install Istio using the `demo` profile, without any gateways:

```bash
$ istioctl install -f @samples/bookinfo/demo-profile-no-gateways.yaml@ -y
✔ Istio core installed
✔ Istiod installed
✔ Installation complete
Made this installation the default for injection and validation.
```

1.  Add a namespace label to instruct Istio to automatically inject Envoy
    sidecar proxies when you deploy your application later:

```bash
$ kubectl label namespace default istio-injection=enabled
namespace/default labeled
```

## Install the Kubernetes Gateway API CRDs {#gateway-api}

The Kubernetes Gateway API CRDs do not come installed by default on most Kubernetes clusters, so make sure they are
installed before using the Gateway API.

1. Install the Gateway API CRDs, if they are not already present:

```bash
$ kubectl get crd gateways.gateway.networking.k8s.io &> /dev/null || \
{ kubectl kustomize "github.com/kubernetes-sigs/gateway-api/config/crd?ref=[k8s_gateway_api_version]" | kubectl apply -f -; }
```

## Deploy the sample application {#bookinfo}

You have configured Istio to inject sidecar containers into any application you deploy in your `default` namespace.

1.  Deploy the [`Bookinfo` sample application](../../examples/bookinfo/index.md):

```bash
$ kubectl apply -f https://raw.githubusercontent.com/istio/istio/8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99/samples/bookinfo/platform/kube/bookinfo.yaml
service/details created
serviceaccount/bookinfo-details created
deployment.apps/details-v1 created
service/ratings created
serviceaccount/bookinfo-ratings created
deployment.apps/ratings-v1 created
service/reviews created
serviceaccount/bookinfo-reviews created
deployment.apps/reviews-v1 created
deployment.apps/reviews-v2 created
deployment.apps/reviews-v3 created
service/productpage created
serviceaccount/bookinfo-productpage created
deployment.apps/productpage-v1 created
```

    The application will start. As each pod becomes ready, the Istio sidecar will be
    deployed along with it.

```bash
$ kubectl get services
NAME          TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
details       ClusterIP   10.0.0.212      <none>        9080/TCP   29s
kubernetes    ClusterIP   10.0.0.1        <none>        443/TCP    25m
productpage   ClusterIP   10.0.0.57       <none>        9080/TCP   28s
ratings       ClusterIP   10.0.0.33       <none>        9080/TCP   29s
reviews       ClusterIP   10.0.0.28       <none>        9080/TCP   29s
```

    and

```bash
$ kubectl get pods
NAME                              READY   STATUS    RESTARTS   AGE
details-v1-558b8b4b76-2llld       2/2     Running   0          2m41s
productpage-v1-6987489c74-lpkgl   2/2     Running   0          2m40s
ratings-v1-7dc98c7588-vzftc       2/2     Running   0          2m41s
reviews-v1-7f99cc4496-gdxfn       2/2     Running   0          2m41s
reviews-v2-7d79d5bd5d-8zzqd       2/2     Running   0          2m41s
reviews-v3-7dbcdcbc56-m8dph       2/2     Running   0          2m41s
```

    Note that the pods show `READY 2/2`, confirming they have their application container and the Istio sidecar container.

1.  Validate that the app is running inside the cluster by
    checking for the page title in the response:

```bash
$ kubectl exec "$(kubectl get pod -l app=ratings -o jsonpath='{.items[0].metadata.name}')" -c ratings -- curl -sS productpage:9080/productpage | grep -o "<title>.*</title>"
<title>Simple Bookstore App</title>
```

## Open the application to outside traffic {#ip}

The Bookinfo application is deployed, but not accessible from the outside. To make it accessible,
you need to create an ingress gateway, which maps a path to a
route at the edge of your mesh.

1.  Create a [Kubernetes Gateway](https://gateway-api.sigs.k8s.io/api-types/gateway/) for the Bookinfo application:

```bash
$ kubectl apply -f @samples/bookinfo/gateway-api/bookinfo-gateway.yaml@
gateway.gateway.networking.k8s.io/bookinfo-gateway created
httproute.gateway.networking.k8s.io/bookinfo created
```

    By default, Istio creates a `LoadBalancer` service for a gateway. As we will access this gateway by a tunnel, we don't need a load balancer. If you want to learn about how load balancers are configured for external IP addresses, read the [ingress gateways](../../tasks/traffic-management/ingress/ingress-control/index.md) documentation.

1. Change the service type to `ClusterIP` by annotating the gateway:

```bash
$ kubectl annotate gateway bookinfo-gateway networking.istio.io/service-type=ClusterIP --namespace=default
```

1. To check the status of the gateway, run:

```bash
$ kubectl get gateway
NAME               CLASS   ADDRESS                                            PROGRAMMED   AGE
bookinfo-gateway   istio   bookinfo-gateway-istio.default.svc.cluster.local   True         42s
```

## Access the application

You will connect to the Bookinfo `productpage` service through the gateway you just provisioned. To access the gateway, you need to use the `kubectl port-forward` command:

```bash
$ kubectl port-forward svc/bookinfo-gateway-istio 8080:80
```

Open your browser and navigate to `http://localhost:8080/productpage` to view the Bookinfo application.

![Bookinfo Application](https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/setup/getting-started/bookinfo-browser.png)

If you refresh the page, you should see the book reviews and ratings changing as the requests are distributed across the different versions of the `reviews` service.

## View the dashboard {#dashboard}

Istio integrates with [several different telemetry applications](../../ops/integrations/_index.md). These can help you gain
an understanding of the structure of your service mesh, display the topology of the mesh, and analyze the health of your mesh.

Use the following instructions to deploy the [Kiali](../../ops/integrations/kiali/index.md) dashboard, along with [Prometheus](../../ops/integrations/prometheus/index.md), [Grafana](../../ops/integrations/grafana/index.md), and [Jaeger](../../ops/integrations/jaeger/index.md).

1.  Install [Kiali and the other addons](https://github.com/istio/istio/tree/8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99/samples/addons) and wait for them to be deployed.

```bash
$ kubectl apply -f samples/addons
$ kubectl rollout status deployment/kiali -n istio-system
Waiting for deployment "kiali" rollout to finish: 0 of 1 updated replicas are available...
deployment "kiali" successfully rolled out
```

1.  Access the Kiali dashboard.

```bash
$ istioctl dashboard kiali
```

1.  In the left navigation menu, select _Graph_ and in the _Namespace_ drop down, select _default_.

> **Tip:**
>
> ---
> ---
> To see trace data, you must send requests to your service. The number of requests depends on Istio's sampling rate and can be configured using the [Telemetry API](../../tasks/observability/telemetry/index.md). With the default sampling rate of 1%, you need to send at least 100 requests before the first trace is visible.
> To send 100 requests to the `productpage` service, use the following command:
>
>
>
> ```bash
> $ for i in $(seq 1 100); do curl -s -o /dev/null "http://$GATEWAY_URL/productpage"; done
> ```

    The Kiali dashboard shows an overview of your mesh with the relationships
    between the services in the `Bookinfo` sample application. It also provides
    filters to visualize the traffic flow.

![Kiali Dashboard](https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/setup/getting-started/kiali-example2.png)

## Next steps

Congratulations on completing the evaluation installation!

These tasks are a great place for beginners to further evaluate Istio's
features using this `demo` installation:

- [Request routing](../../tasks/traffic-management/request-routing/index.md)
- [Fault injection](../../tasks/traffic-management/fault-injection/index.md)
- [Traffic shifting](../../tasks/traffic-management/traffic-shifting/index.md)
- [Querying metrics](../../tasks/observability/metrics/querying-metrics/index.md)
- [Visualizing metrics](../../tasks/observability/metrics/using-istio-dashboard/index.md)
- [Accessing external services](../../tasks/traffic-management/egress/egress-control/index.md)
- [Visualizing your mesh](../../tasks/observability/kiali/index.md)

Before you customize Istio for production use, see these resources:

- [Deployment models](../../ops/deployment/deployment-models/index.md)
- [Deployment best practices](../../ops/best-practices/deployment/index.md)
- [Pod requirements](../../ops/deployment/application-requirements/index.md)
- [General installation instructions](../_index.md)

## Join the Istio community

We welcome you to ask questions and give us feedback by joining the
[Istio community](https://istio.io/v1.24/get-involved/) <!-- unresolved-site-link: route=/get-involved -->.

## Uninstall

To delete the `Bookinfo` sample application and its configuration, see
[`Bookinfo` cleanup](../../examples/bookinfo/index.md#cleanup).

The Istio uninstall deletes the RBAC permissions and all resources hierarchically
under the `istio-system` namespace. It is safe to ignore errors for non-existent
resources because they may have been deleted hierarchically.

```bash
$ kubectl delete -f @samples/addons@
$ istioctl uninstall -y --purge
```

The `istio-system` namespace is not removed by default.
If no longer needed, use the following command to remove it:

```bash
$ kubectl delete namespace istio-system
```

The label to instruct Istio to automatically inject Envoy sidecar proxies is not removed by default.
If no longer needed, use the following command to remove it:

```bash
$ kubectl label namespace default istio-injection-
```

If you installed the Kubernetes Gateway API CRDs and would now like to remove them, run one of the following commands:

- If you ran any tasks that required the **experimental version** of the CRDs:

```bash
$ kubectl kustomize "github.com/kubernetes-sigs/gateway-api/config/crd/experimental?ref=[k8s_gateway_api_version]" | kubectl delete -f -
```

- Otherwise:

```bash
$ kubectl kustomize "github.com/kubernetes-sigs/gateway-api/config/crd?ref=[k8s_gateway_api_version]" | kubectl delete -f -
```
