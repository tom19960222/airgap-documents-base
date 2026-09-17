---
collection: istio
version: "1.24"
title: "Ingress Gateways"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/tasks/traffic-management/ingress/ingress-control/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Describes how to configure an Istio gateway to expose a service outside of the service mesh."
---
Along with support for Kubernetes [Ingress](../kubernetes-ingress/index.md) resources, Istio also allows you to configure ingress traffic
using either an [Istio Gateway](../../../../concepts/traffic-management/index.md#gateways) or [Kubernetes Gateway](https://gateway-api.sigs.k8s.io/api-types/gateway/) resource.
A `Gateway` provides more extensive customization and flexibility than `Ingress`, and allows Istio features such as monitoring and route rules to be applied to traffic entering the cluster.

This task describes how to configure Istio to expose a service outside of the service mesh using a `Gateway`.

---
---

> **Tip:**
>
> ---
> ---
> Istio supports the Kubernetes [Gateway API](https://istio.io/v1.24/blog/2024/gateway-mesh-ga/) <!-- unresolved-site-link: route=/blog/2024/gateway-mesh-ga --> and intends to make it the default API for traffic management in the future.
>
>
>
>
> ---
> ---
> The following instructions allow you to choose to use either the Gateway API or the Istio configuration API when configuring
> traffic management in the mesh. Follow instructions under either the `Gateway API` or `Istio APIs` tab,
> according to your preference.
>
>
>
>
>
> ---
> ---
> Note that the Kubernetes Gateway API CRDs do not come installed by default on most Kubernetes clusters, so make sure they are
> installed before using the Gateway API:
>
>
>
> ```bash
> $ kubectl get crd gateways.gateway.networking.k8s.io &> /dev/null || \
>   { kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/[k8s_gateway_api_version]/standard-install.yaml; }
> ```

## Before you begin

*   Setup Istio by following the instructions in the [Installation guide](../../../../setup/_index.md).

> **Tip:**
>
> If you are going to use the `Gateway API` instructions, you can install Istio using the `minimal`
>     profile because you will not need the `istio-ingressgateway` which is otherwise installed
>     by default:
>
>
>
> ```bash
> $ istioctl install --set profile=minimal
> ```

*   Start the [httpbin](https://github.com/istio/istio/tree/8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99/samples/httpbin) sample, which will serve as the target service
    for ingress traffic:

```bash
$ kubectl apply -f @samples/httpbin/httpbin.yaml@
```

    Note that for the purpose of this document, which shows how to use a gateway to control ingress traffic
    into your "Kubernetes cluster", you can start the `httpbin` service with or without
    sidecar injection enabled (i.e., the target service can be either inside or outside of the Istio mesh).

## Configuring ingress using a gateway

An ingress `Gateway` describes a load balancer operating at the edge of the mesh that receives incoming HTTP/TCP connections.
It configures exposed ports, protocols, etc.
but, unlike [Kubernetes Ingress Resources](https://kubernetes.io/docs/concepts/services-networking/ingress/),
does not include any traffic routing configuration. Traffic routing for ingress traffic is instead configured
using routing rules, exactly in the same way as for internal service requests.

Let's see how you can configure a `Gateway` on port 80 for HTTP traffic.

**Tabset (config-api):**

**Tab: Istio APIs**

Create an [Istio Gateway](https://istio.io/v1.24/docs/reference/config/networking/gateway/) <!-- unresolved-site-link: route=/docs/reference/config/networking/gateway -->:

```bash
$ kubectl apply -f - <<EOF
apiVersion: networking.istio.io/v1
kind: Gateway
metadata:
  name: httpbin-gateway
spec:
  # The selector matches the ingress gateway pod labels.
  # If you installed Istio using Helm following the standard documentation, this would be "istio=ingress"
  selector:
    istio: ingressgateway
  servers:
  - port:
      number: 80
      name: http
      protocol: HTTP
    hosts:
    - "httpbin.example.com"
EOF
```

Configure routes for traffic entering via the `Gateway`:

```bash
$ kubectl apply -f - <<EOF
apiVersion: networking.istio.io/v1
kind: VirtualService
metadata:
  name: httpbin
spec:
  hosts:
  - "httpbin.example.com"
  gateways:
  - httpbin-gateway
  http:
  - match:
    - uri:
        prefix: /status
    - uri:
        prefix: /delay
    route:
    - destination:
        port:
          number: 8000
        host: httpbin
EOF
```

You have now created a [virtual service](https://istio.io/v1.24/docs/reference/config/networking/virtual-service/) <!-- unresolved-site-link: route=/docs/reference/config/networking/virtual-service -->
configuration for the `httpbin` service containing two route rules that allow traffic for paths `/status` and
`/delay`.

The [gateways](https://istio.io/v1.24/docs/reference/config/networking/virtual-service/#VirtualService-gateways) <!-- unresolved-site-link: route=/docs/reference/config/networking/virtual-service --> list
specifies that only requests through your `httpbin-gateway` are allowed.
All other external requests will be rejected with a 404 response.

> **Warning:**
>
> Internal requests from other services in the mesh are not subject to these rules
> but instead will default to round-robin routing. To apply these rules to internal calls as well,
> you can add the special value `mesh` to the list of `gateways`. Since the internal hostname for the
> service is probably different (e.g., `httpbin.default.svc.cluster.local`) from the external one,
> you will also need to add it to the `hosts` list. Refer to the
> [operations guide](../../../../ops/common-problems/network-issues/index.md#route-rules-have-no-effect-on-ingress-gateway-requests)
> for more details.

**Tab: Gateway API**

Create a [Kubernetes Gateway](https://gateway-api.sigs.k8s.io/references/spec/#gateway.networking.k8s.io/v1.Gateway):

```bash
$ kubectl apply -f - <<EOF
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: httpbin-gateway
spec:
  gatewayClassName: istio
  listeners:
  - name: http
    hostname: "httpbin.example.com"
    port: 80
    protocol: HTTP
    allowedRoutes:
      namespaces:
        from: Same
EOF
```

> **Tip:**
>
> In a production environment, a `Gateway` and its corresponding routes are often created in separate namespaces by users
> performing different roles. In that case, the `allowedRoutes` field in the `Gateway` would be configured to specify the
> namespaces where routes should be created, instead of, as in this example, expecting them to be in the same namespace
> as the `Gateway`.

Because creating a Kubernetes `Gateway` resource will also
[deploy an associated proxy service](../gateway-api/index.md#automated-deployment),
run the following command to wait for the gateway to be ready:

```bash
$ kubectl wait --for=condition=programmed gtw httpbin-gateway
```

Configure routes for traffic entering via the `Gateway`:

```bash
$ kubectl apply -f - <<EOF
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: httpbin
spec:
  parentRefs:
  - name: httpbin-gateway
  hostnames: ["httpbin.example.com"]
  rules:
  - matches:
    - path:
        type: PathPrefix
        value: /status
    - path:
        type: PathPrefix
        value: /delay
    backendRefs:
    - name: httpbin
      port: 8000
EOF
```

You have now created an [HTTP Route](https://gateway-api.sigs.k8s.io/references/spec/#gateway.networking.k8s.io/v1.HTTPRoute)
configuration for the `httpbin` service containing two route rules that allow traffic for paths `/status` and
`/delay`.

## Determining the ingress IP and ports

Every `Gateway` is backed by a [service of type LoadBalancer](https://kubernetes.io/docs/tasks/access-application-cluster/create-external-load-balancer/).
The external load balancer IP and ports for this service are used to access the gateway.
Kubernetes services of type `LoadBalancer` are supported by default in clusters running on most cloud platforms but
in some environments (e.g., test) you may need to do the following:

* `minikube` - start an external load balancer by running the following command in a different terminal:

```bash
$ minikube tunnel
```

* `kind` - follow the [guide](https://kind.sigs.k8s.io/docs/user/loadbalancer/) to get `LoadBalancer` type services to work.

* other platforms - you may be able to use [MetalLB](https://metallb.universe.tf/installation/) to get an `EXTERNAL-IP` for `LoadBalancer` services.

For convenience, we will store the ingress IP and ports in environment variables which will be used in later instructions.
Set the `INGRESS_HOST` and `INGRESS_PORT` environment variables according to the following instructions:

**Tabset (config-api):**

**Tab: Istio APIs**

Set the following environment variables to the name and namespace where the Istio ingress gateway is located in your cluster:

```bash
$ export INGRESS_NAME=istio-ingressgateway
$ export INGRESS_NS=istio-system
```

> **Tip:**
>
> If you installed Istio using Helm, the ingress gateway name and namespace are both `istio-ingress`:
>
>
>
> ```bash
> $ export INGRESS_NAME=istio-ingress
> $ export INGRESS_NS=istio-ingress
> ```

Run the following command to determine if your Kubernetes cluster is in an environment that supports external load balancers:

```bash
$ kubectl get svc "$INGRESS_NAME" -n "$INGRESS_NS"
NAME                   TYPE           CLUSTER-IP       EXTERNAL-IP      PORT(S)   AGE
istio-ingressgateway   LoadBalancer   172.21.109.129   130.211.10.121   ...       17h
```

If the `EXTERNAL-IP` value is set, your environment has an external load balancer that you can use for the ingress gateway.
If the `EXTERNAL-IP` value is `<none>` (or perpetually `<pending>`), your environment does not provide an external load balancer for the ingress gateway.

If your environment does not support external load balancers, you can try
[accessing the ingress gateway using node ports](#using-node-ports-of-the-ingress-gateway-service).
Otherwise, set the ingress IP and ports using the following commands:

```bash
$ export INGRESS_HOST=$(kubectl -n "$INGRESS_NS" get service "$INGRESS_NAME" -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
$ export INGRESS_PORT=$(kubectl -n "$INGRESS_NS" get service "$INGRESS_NAME" -o jsonpath='{.spec.ports[?(@.name=="http2")].port}')
$ export SECURE_INGRESS_PORT=$(kubectl -n "$INGRESS_NS" get service "$INGRESS_NAME" -o jsonpath='{.spec.ports[?(@.name=="https")].port}')
$ export TCP_INGRESS_PORT=$(kubectl -n "$INGRESS_NS" get service "$INGRESS_NAME" -o jsonpath='{.spec.ports[?(@.name=="tcp")].port}')
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
> $ export INGRESS_HOST=$(kubectl -n "$INGRESS_NS" get service "$INGRESS_NAME" -o jsonpath='{.status.loadBalancer.ingress[0].hostname}')
> ```

**Tab: Gateway API**

Get the gateway address and port from the httpbin gateway resource:

```bash
$ export INGRESS_HOST=$(kubectl get gtw httpbin-gateway -o jsonpath='{.status.addresses[0].value}')
$ export INGRESS_PORT=$(kubectl get gtw httpbin-gateway -o jsonpath='{.spec.listeners[?(@.name=="http")].port}')
```

> **Tip:**
>
> You can use similar commands to find other ports on any gateway. For example to access a secure HTTP
> port named `https` on a gateway named `my-gateway`:
>
>
>
> ```bash
> $ export INGRESS_HOST=$(kubectl get gtw my-gateway -o jsonpath='{.status.addresses[0].value}')
> $ export SECURE_INGRESS_PORT=$(kubectl get gtw my-gateway -o jsonpath='{.spec.listeners[?(@.name=="https")].port}')
> ```

## Accessing ingress services

1.  Access the _httpbin_ service using _curl_:

```bash
$ curl -s -I -HHost:httpbin.example.com "http://$INGRESS_HOST:$INGRESS_PORT/status/200"
...
HTTP/1.1 200 OK
...
server: istio-envoy
...
```

    Note that you use the `-H` flag to set the _Host_ HTTP header to
    "httpbin.example.com". This is needed because your ingress `Gateway` is configured to handle "httpbin.example.com",
    but in your test environment you have no DNS binding for that host and are simply sending your request to the ingress IP.

1.  Access any other URL that has not been explicitly exposed. You should see an HTTP 404 error:

```bash
$ curl -s -I -HHost:httpbin.example.com "http://$INGRESS_HOST:$INGRESS_PORT/headers"
HTTP/1.1 404 Not Found
...
```

### Accessing ingress services using a browser

Entering the `httpbin` service URL in a browser won't work because you can't pass the _Host_ header
to a browser like you did with `curl`. In a real world situation, this is not a problem
because you configure the requested host properly and DNS resolvable. Thus, you use the host's domain name
in the URL, for example, `https://httpbin.example.com/status/200`.

You can work around this problem for simple tests and demos as follows:

**Tabset (config-api):**

**Tab: Istio APIs**

Use a wildcard `*` value for the host in the `Gateway`
and `VirtualService` configurations. For example, change your ingress configuration to the following:

```bash
$ kubectl apply -f - <<EOF
apiVersion: networking.istio.io/v1
kind: Gateway
metadata:
  name: httpbin-gateway
spec:
  # The selector matches the ingress gateway pod labels.
  # If you installed Istio using Helm following the standard documentation, this would be "istio=ingress"
  selector:
    istio: ingressgateway
  servers:
  - port:
      number: 80
      name: http
      protocol: HTTP
    hosts:
    - "*"
---
apiVersion: networking.istio.io/v1
kind: VirtualService
metadata:
  name: httpbin
spec:
  hosts:
  - "*"
  gateways:
  - httpbin-gateway
  http:
  - match:
    - uri:
        prefix: /headers
    route:
    - destination:
        port:
          number: 8000
        host: httpbin
EOF
```

**Tab: Gateway API**

If you remove the host names from the `Gateway` and `HTTPRoute` configurations, they will apply to any request.
For example, change your ingress configuration to the following:

```bash
$ kubectl apply -f - <<EOF
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: httpbin-gateway
spec:
  gatewayClassName: istio
  listeners:
  - name: http
    port: 80
    protocol: HTTP
    allowedRoutes:
      namespaces:
        from: Same
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: httpbin
spec:
  parentRefs:
  - name: httpbin-gateway
  rules:
  - matches:
    - path:
        type: PathPrefix
        value: /headers
    backendRefs:
    - name: httpbin
      port: 8000
EOF
```

You can then use `$INGRESS_HOST:$INGRESS_PORT` in the browser URL. For example,
`http://$INGRESS_HOST:$INGRESS_PORT/headers` will display all the headers that your browser sends.

## Understanding what happened

The `Gateway` configuration resources allow external traffic to enter the
Istio service mesh and make the traffic management and policy features of Istio
available for edge services.

In the preceding steps, you created a service inside the service mesh
and exposed an HTTP endpoint of the service to external traffic.

## Using node ports of the ingress gateway service

> **Warning:**
>
> You should not use these instructions if your Kubernetes environment has an external load balancer supporting
> [services of type LoadBalancer](https://kubernetes.io/docs/tasks/access-application-cluster/create-external-load-balancer/).

If your environment does not support external load balancers, you can still experiment with some of the Istio features by
using the `istio-ingressgateway` service's [node ports](https://kubernetes.io/docs/concepts/services-networking/service/#type-nodeport).

Set the ingress ports:

```bash
$ export INGRESS_PORT=$(kubectl -n "${INGRESS_NS}" get service "${INGRESS_NAME}" -o jsonpath='{.spec.ports[?(@.name=="http2")].nodePort}')
$ export SECURE_INGRESS_PORT=$(kubectl -n "${INGRESS_NS}" get service "${INGRESS_NAME}" -o jsonpath='{.spec.ports[?(@.name=="https")].nodePort}')
$ export TCP_INGRESS_PORT=$(kubectl -n "${INGRESS_NS}" get service "${INGRESS_NAME}" -o jsonpath='{.spec.ports[?(@.name=="tcp")].nodePort}')
```

Setting the ingress IP depends on the cluster provider:

1.  _GKE:_

```bash
$ export INGRESS_HOST=worker-node-address
```

    You need to create firewall rules to allow the TCP traffic to the _ingressgateway_ service's ports.
    Run the following commands to allow the traffic for the HTTP port, the secure port (HTTPS) or both:

```bash
$ gcloud compute firewall-rules create allow-gateway-http --allow "tcp:$INGRESS_PORT"
$ gcloud compute firewall-rules create allow-gateway-https --allow "tcp:$SECURE_INGRESS_PORT"
```

1.  _IBM Cloud Kubernetes Service:_

```bash
$ ibmcloud ks workers --cluster cluster-name-or-id
$ export INGRESS_HOST=public-IP-of-one-of-the-worker-nodes
```

1.  _Docker For Desktop:_

```bash
$ export INGRESS_HOST=127.0.0.1
```

1.  _Other environments:_

```bash
$ export INGRESS_HOST=$(kubectl get po -l istio=ingressgateway -n "${INGRESS_NS}" -o jsonpath='{.items[0].status.hostIP}')
```

## Troubleshooting

1.  Inspect the values of the `INGRESS_HOST` and `INGRESS_PORT` environment variables. Make sure
they have valid values, according to the output of the following commands:

```bash
$ kubectl get svc -n istio-system
$ echo "INGRESS_HOST=$INGRESS_HOST, INGRESS_PORT=$INGRESS_PORT"
```

1.  Check that you have no other Istio ingress gateways defined on the same port:

```bash
$ kubectl get gateway --all-namespaces
```

1.  Check that you have no Kubernetes Ingress resources defined on the same IP and port:

```bash
$ kubectl get ingress --all-namespaces
```

1.  If you have an external load balancer and it does not work for you, try to
    [access the gateway using its node port](#using-node-ports-of-the-ingress-gateway-service).

## Cleanup

**Tabset (config-api):**

**Tab: Istio APIs**

Delete the `Gateway` and `VirtualService` configuration, and shutdown the [httpbin](https://github.com/istio/istio/tree/8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99/samples/httpbin) service:

```bash
$ kubectl delete gateway httpbin-gateway
$ kubectl delete virtualservice httpbin
$ kubectl delete --ignore-not-found=true -f @samples/httpbin/httpbin.yaml@
```

**Tab: Gateway API**

Delete the `Gateway` and `HTTPRoute` configuration, and shutdown the [httpbin](https://github.com/istio/istio/tree/8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99/samples/httpbin) service:

```bash
$ kubectl delete httproute httpbin
$ kubectl delete gtw httpbin-gateway
$ kubectl delete --ignore-not-found=true -f @samples/httpbin/httpbin.yaml@
```
