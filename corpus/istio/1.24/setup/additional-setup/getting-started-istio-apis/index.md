---
collection: istio
version: "1.24"
title: "Getting Started without the Gateway API"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/setup/additional-setup/getting-started-istio-apis/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Try Istio’s features with the legacy Istio APIs."
---
This guide lets you quickly evaluate Istio, using only its legacy APIs. If you want to use the Kubernetes Gateway API, [please see that example](../../getting-started/index.md).
If you are already familiar with
Istio or interested in installing other configuration profiles or
advanced [deployment models](../../../ops/deployment/deployment-models/index.md), refer to our
[which Istio installation method should I use?](https://istio.io/v1.24/about/faq/#install-method-selection) <!-- unresolved-site-link: route=/about/faq -->
FAQ page.

These steps require you to have a cluster running a
[supported version](../../../releases/supported-releases/index.md#support-status-of-istio-releases) of Kubernetes ([supported_kubernetes_versions]). You can use any supported platform, for
example [Minikube](https://kubernetes.io/docs/tasks/tools/install-minikube/) or
others specified by the
[platform-specific setup instructions](../../platform-setup/_index.md).

Follow these steps to get started with Istio:

1. [Download and install Istio](#download)
1. [Deploy the sample application](#bookinfo)
1. [Open the application to outside traffic](#ip)
1. [View the dashboard](#dashboard)

## Download Istio {#download}

1.  Go to the [Istio release](https://github.com/istio/istio/releases/tag/1.24.0) page to
    download the installation file for your OS, or download and
    extract the latest release automatically (Linux or macOS):

```bash
$ curl -L https://istio.io/downloadIstio | sh -
```

> **Tip:**
>
> The command above downloads the latest release (numerically) of Istio.
>     You can pass variables on the command line to download a specific version
>     or to override the processor architecture.
>     For example, to download Istio [istio_full_version] for the x86_64 architecture,
>     run:
>
>
>
> ```bash
> $ curl -L https://istio.io/downloadIstio | ISTIO_VERSION=[istio_full_version] TARGET_ARCH=x86_64 sh -
> ```

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

1.  For this installation, we use the `demo`
    [configuration profile](../config-profiles/index.md). It's
    selected to have a good set of defaults for testing, but there are other
    profiles for production or performance testing.

> **Warning:**
>
> If your platform has a vendor-specific configuration profile, e.g., Openshift, use
>     it in the following command, instead of the `demo` profile. Refer to your
>     [platform instructions](../../platform-setup/_index.md) for details.

```bash
$ istioctl install --set profile=demo -y
✔ Istio core installed
✔ Istiod installed
✔ Egress gateways installed
✔ Ingress gateways installed
✔ Installation complete
```

1.  Add a namespace label to instruct Istio to automatically inject Envoy
    sidecar proxies when you deploy your application later:

```bash
$ kubectl label namespace default istio-injection=enabled
namespace/default labeled
```

## Deploy the sample application {#bookinfo}

1.  Deploy the [`Bookinfo` sample application](../../../examples/bookinfo/index.md):

```bash
$ kubectl apply -f @samples/bookinfo/platform/kube/bookinfo.yaml@
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

1.  The application will start. As each pod becomes ready, the Istio sidecar will be
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

> **Tip:**
>
> Re-run the previous command and wait until all pods report READY `2/2` and
>     STATUS `Running` before you go to the next step. This might take a few minutes
>     depending on your platform.

1.  Verify everything is working correctly up to this point. Run this command to
    see if the app is running inside the cluster and serving HTML pages by
    checking for the page title in the response:

```bash
$ kubectl exec "$(kubectl get pod -l app=ratings -o jsonpath='{.items[0].metadata.name}')" -c ratings -- curl -sS productpage:9080/productpage | grep -o "<title>.*</title>"
<title>Simple Bookstore App</title>
```

## Open the application to outside traffic {#ip}

The Bookinfo application is deployed but not accessible from the outside. To make it accessible,
you need to create an
[Istio Ingress Gateway](../../../concepts/traffic-management/index.md#gateways), which maps a path to a
route at the edge of your mesh.

1.  Associate this application with the Istio gateway:

```bash
$ kubectl apply -f @samples/bookinfo/networking/bookinfo-gateway.yaml@
gateway.networking.istio.io/bookinfo-gateway created
virtualservice.networking.istio.io/bookinfo created
```

1.  Ensure that there are no issues with the configuration:

```bash
$ istioctl analyze
✔ No validation issues found when analyzing namespace: default.
```

### Determining the ingress IP and ports

Follow these instructions to set the `INGRESS_HOST` and `INGRESS_PORT` variables
for accessing the gateway. Use the tabs to choose the instructions for your
chosen platform:

**Tabset (gateway-ip):**

**Tab: Minikube**

Run this command in a new terminal window to start a Minikube tunnel that
sends traffic to your Istio Ingress Gateway. This will provide an external
load balancer, `EXTERNAL-IP`, for `service/istio-ingressgateway`.

```bash
$ minikube tunnel
```

Set the ingress host and ports:

```bash
$ export INGRESS_HOST=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
$ export INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="http2")].port}')
$ export SECURE_INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="https")].port}')
```

Ensure an IP address and ports were successfully assigned to each environment variable:

```bash
$ echo "$INGRESS_HOST"
127.0.0.1
```

```bash
$ echo "$INGRESS_PORT"
80
```

```bash
$ echo "$SECURE_INGRESS_PORT"
443
```

**Tab: Other platforms**

Execute the following command to determine if your Kubernetes cluster is running in an environment that supports external load balancers:

```bash
$ kubectl get svc istio-ingressgateway -n istio-system
NAME                   TYPE           CLUSTER-IP       EXTERNAL-IP     PORT(S)                                      AGE
istio-ingressgateway   LoadBalancer   172.21.109.129   130.211.10.121  80:31380/TCP,443:31390/TCP,31400:31400/TCP   17h
```

If the `EXTERNAL-IP` value is set, your environment has an external load balancer that you can use for the ingress gateway.
If the `EXTERNAL-IP` value is `<none>` (or perpetually `<pending>`), your environment does not provide an external load balancer for the ingress gateway.
In this case, you can access the gateway using the service's [node port](https://kubernetes.io/docs/concepts/services-networking/service/#type-nodeport).

Choose the instructions corresponding to your environment:

**Follow these instructions if you have determined that your environment has an external load balancer.**

Set the ingress IP and ports:

```bash
$ export INGRESS_HOST=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
$ export INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="http2")].port}')
$ export SECURE_INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="https")].port}')
```

> **Warning:**
>
> In certain environments, the load balancer may be exposed using a host name, instead of an IP address.
> In this case, the ingress gateway's `EXTERNAL-IP` value will not be an IP address,
> but rather a host name, and the above command will have failed to set the `INGRESS_HOST` environment variable.
> Use the following command to correct the `INGRESS_HOST` value:
>
>
>
> ```bash
> $ export INGRESS_HOST=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.status.loadBalancer.ingress[0].hostname}')
> ```

**Follow these instructions if your environment does not have an external load balancer and choose a node port instead.**

Set the ingress ports:

```bash
$ export INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="http2")].nodePort}')
$ export SECURE_INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="https")].nodePort}')
```

_GKE:_

```bash
$ export INGRESS_HOST=worker-node-address
```

You need to create firewall rules to allow the TCP traffic to the `ingressgateway` service's ports.
Run the following commands to allow the traffic for the HTTP port, the secure port (HTTPS) or both:

```bash
$ gcloud compute firewall-rules create allow-gateway-http --allow "tcp:$INGRESS_PORT"
$ gcloud compute firewall-rules create allow-gateway-https --allow "tcp:$SECURE_INGRESS_PORT"
```

_IBM Cloud Kubernetes Service:_

```bash
$ ibmcloud ks workers --cluster cluster-name-or-id
$ export INGRESS_HOST=public-IP-of-one-of-the-worker-nodes
```

_Docker For Desktop:_

```bash
$ export INGRESS_HOST=127.0.0.1
```

_Other environments:_

```bash
$ export INGRESS_HOST=$(kubectl get po -l istio=ingressgateway -n istio-system -o jsonpath='{.items[0].status.hostIP}')
```

1.  Set `GATEWAY_URL`:

```bash
$ export GATEWAY_URL=$INGRESS_HOST:$INGRESS_PORT
```

1.  Ensure an IP address and port were successfully assigned to the environment variable:

```bash
$ echo "$GATEWAY_URL"
127.0.0.1:80
```

### Verify external access {#confirm}

Confirm that the Bookinfo application is accessible from outside
by viewing the Bookinfo product page using a browser.

1.  Run the following command to retrieve the external address of the Bookinfo application.

```bash
$ echo "http://$GATEWAY_URL/productpage"
```

1.  Paste the output from the previous command into your web browser and confirm that the Bookinfo product page is displayed.

## View the dashboard {#dashboard}

Istio integrates with [several](../../../ops/integrations/_index.md) different telemetry applications. These can help you gain
an understanding of the structure of your service mesh, display the topology of the mesh, and analyze the health of your mesh.

Use the following instructions to deploy the [Kiali](../../../ops/integrations/kiali/index.md) dashboard, along with [Prometheus](../../../ops/integrations/prometheus/index.md), [Grafana](../../../ops/integrations/grafana/index.md), and [Jaeger](../../../ops/integrations/jaeger/index.md).

1.  Install [Kiali and the other addons](https://github.com/istio/istio/tree/8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99/samples/addons) and wait for them to be deployed.

```bash
$ kubectl apply -f samples/addons
$ kubectl rollout status deployment/kiali -n istio-system
Waiting for deployment "kiali" rollout to finish: 0 of 1 updated replicas are available...
deployment "kiali" successfully rolled out
```

> **Tip:**
>
> If there are errors trying to install the addons, try running the command again. There may
>     be some timing issues which will be resolved when the command is run again.

1.  Access the Kiali dashboard.

```bash
$ istioctl dashboard kiali
```

1.  In the left navigation menu, select _Graph_ and in the _Namespace_ drop down, select _default_.

> **Tip:**
>
> ---
> ---
> To see trace data, you must send requests to your service. The number of requests depends on Istio's sampling rate and can be configured using the [Telemetry API](../../../tasks/observability/telemetry/index.md). With the default sampling rate of 1%, you need to send at least 100 requests before the first trace is visible.
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

![Kiali Dashboard](https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/setup/additional-setup/getting-started-istio-apis/kiali-example2.png)

## Next steps

Congratulations on completing the evaluation installation!

These tasks are a great place for beginners to further evaluate Istio's
features using this `demo` installation:

- [Request routing](../../../tasks/traffic-management/request-routing/index.md)
- [Fault injection](../../../tasks/traffic-management/fault-injection/index.md)
- [Traffic shifting](../../../tasks/traffic-management/traffic-shifting/index.md)
- [Querying metrics](../../../tasks/observability/metrics/querying-metrics/index.md)
- [Visualizing metrics](../../../tasks/observability/metrics/using-istio-dashboard/index.md)
- [Accessing external services](../../../tasks/traffic-management/egress/egress-control/index.md)
- [Visualizing your mesh](../../../tasks/observability/kiali/index.md)

Before you customize Istio for production use, see these resources:

- [Deployment models](../../../ops/deployment/deployment-models/index.md)
- [Deployment best practices](../../../ops/best-practices/deployment/index.md)
- [Pod requirements](../../../ops/deployment/application-requirements/index.md)
- [General installation instructions](../../_index.md)

## Join the Istio community

We welcome you to ask questions and give us feedback by joining the
[Istio community](https://istio.io/v1.24/get-involved/) <!-- unresolved-site-link: route=/get-involved -->.

## Uninstall

To delete the `Bookinfo` sample application and its configuration, see
[`Bookinfo` cleanup](../../../examples/bookinfo/index.md#cleanup).

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
