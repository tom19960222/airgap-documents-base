---
collection: istio
version: "1.24"
title: "Ingress Access Control"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/tasks/security/authorization/authz-ingress/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Shows how to set up access control on an ingress gateway."
---
This task shows you how to enforce IP-based access control on an Istio ingress gateway using an authorization policy.

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

Before you begin this task, do the following:

* Read the [Istio authorization concepts](../../../../concepts/security/index.md#authorization).

* Install Istio using the [Istio installation guide](../../../../setup/install/istioctl/index.md).

* Deploy a workload, `httpbin`, in namespace `foo` with sidecar injection enabled:

```bash
$ kubectl create ns foo
$ kubectl label namespace foo istio-injection=enabled
$ kubectl apply -f @samples/httpbin/httpbin.yaml@ -n foo
```

* Expose `httpbin` through an ingress gateway:

**Tabset (config-api):**

**Tab: Istio APIs**

Configure the gateway:

```bash
$ kubectl apply -f @samples/httpbin/httpbin-gateway.yaml@ -n foo
```

Turn on RBAC debugging in Envoy for the ingress gateway:

```bash
$ kubectl get pods -n istio-system -o name -l istio=ingressgateway | sed 's|pod/||' | while read -r pod; do istioctl proxy-config log "$pod" -n istio-system --level rbac:debug; done
```

Follow the instructions in
[Determining the ingress IP and ports](../../../traffic-management/ingress/ingress-control/index.md#determining-the-ingress-ip-and-ports)
to define the `INGRESS_PORT` and `INGRESS_HOST` environment variables.

**Tab: Gateway API**

Create the gateway:

```bash
$ kubectl apply -f @samples/httpbin/gateway-api/httpbin-gateway.yaml@ -n foo
```

Wait for the gateway to be ready:

```bash
$ kubectl wait --for=condition=programmed gtw -n foo httpbin-gateway
```

Turn on RBAC debugging in Envoy for the ingress gateway:

```bash
$ kubectl get pods -n foo -o name -l gateway.networking.k8s.io/gateway-name=httpbin-gateway | sed 's|pod/||' | while read -r pod; do istioctl proxy-config log "$pod" -n foo --level rbac:debug; done
```

Set the `INGRESS_PORT` and `INGRESS_HOST` environment variables:

```bash
$ export INGRESS_HOST=$(kubectl get gtw httpbin-gateway -n foo -o jsonpath='{.status.addresses[0].value}')
$ export INGRESS_PORT=$(kubectl get gtw httpbin-gateway -n foo -o jsonpath='{.spec.listeners[?(@.name=="http")].port}')
```

* Verify that the `httpbin` workload and ingress gateway are working as expected using this command:

```bash
$ curl "$INGRESS_HOST:$INGRESS_PORT"/headers -s -o /dev/null -w "%{http_code}\n"
200
```

> **Warning:**
>
> If you don’t see the expected output, retry after a few seconds.
>     Caching and propagation overhead can cause a delay.

## Getting traffic into Kubernetes and Istio

All methods of getting traffic into Kubernetes involve opening a port on all worker nodes.
The main features that accomplish this are the `NodePort` service and the `LoadBalancer` service.
Even the Kubernetes `Ingress` resource must be backed by an Ingress controller that will create
either a `NodePort` or a `LoadBalancer` service.

* A `NodePort` just opens up a port in the range 30000-32767 on each worker node and uses a label
  selector to identify which Pods to send the traffic to. You have to manually create some kind
  of load balancer in front of your worker nodes or use Round-Robin DNS.

* A `LoadBalancer` is just like a `NodePort`, except it also creates an environment specific external
  load balancer to handle distributing traffic to the worker nodes.  For example, in AWS EKS, the `LoadBalancer`
  service will create a Classic ELB with your worker nodes as targets. If your Kubernetes environment
  does not have a `LoadBalancer` implementation, then it will just behave like a `NodePort`.  An Istio
  ingress gateway creates a `LoadBalancer` service.

What if the Pod that is handling traffic from the `NodePort` or `LoadBalancer` isn't running on
the worker node that received the traffic?  Kubernetes has its own internal proxy called kube-proxy
that receives the packets and forwards them to the correct node.

## Source IP address of the original client

If a packet goes through an external proxy load balancer and/or kube-proxy, then the original source IP address of the client is lost.
The following subsections describe some strategies for preserving the original client IP for logging or security purpose
for different load balancer types:

1. [TCP/UDP Proxy Load Balancer](#tcp-proxy)
1. [Network Load Balancer](#network)
1. [HTTP/HTTPS Load Balancer](#http-https)

For reference, here are the types of load balancers created by Istio with a `LoadBalancer` service on popular managed Kubernetes environments:

|Cloud Provider | Load Balancer Name            | Load Balancer Type
----------------|-------------------------------|-------------------
|AWS EKS        | Classic Elastic Load Balancer | TCP Proxy
|GCP GKE        | TCP/UDP Network Load Balancer | Network
|Azure AKS      | Azure Load Balancer           | Network
|IBM IKS/ROKS   | Network Load Balancer         | Network
|DO DOKS        | Load Balancer                 | Network

> **Tip:**
>
> You can instruct AWS EKS to create a Network Load Balancer with an annotation on the gateway service:
>
>
>
> **Tabset (config-api):**
>
> **Tab: Istio APIs**
>
> ```yaml
> apiVersion: install.istio.io/v1alpha1
> kind: IstioOperator
> spec:
>   meshConfig:
>     accessLogEncoding: JSON
>     accessLogFile: /dev/stdout
>   components:
>     ingressGateways:
>     - enabled: true
>       k8s:
>         hpaSpec:
>           maxReplicas: 10
>           minReplicas: 5
>         serviceAnnotations:
>           service.beta.kubernetes.io/aws-load-balancer-type: "nlb"
> ```
>
>
>
>
>
> **Tab: Gateway API**
>
> ```yaml
> apiVersion: gateway.networking.k8s.io/v1
> kind: Gateway
> metadata:
>   name: httpbin-gateway
>   annotations:
>     service.beta.kubernetes.io/aws-load-balancer-type: "nlb"
> spec:
>   gatewayClassName: istio
>   ...
> ```

### TCP/UDP Proxy Load Balancer {#tcp-proxy}

If you are using a TCP/UDP Proxy external load balancer (AWS Classic ELB), it can use the [PROXY Protocol](https://www.haproxy.com/blog/haproxy/proxy-protocol/) to embed the original client IP address in the packet data.  Both the external load balancer and the Istio ingress gateway must support the PROXY protocol for it to work.

Here is a sample configuration that shows how to make an ingress gateway on AWS EKS support the PROXY Protocol:

**Tabset (config-api):**

**Tab: Istio APIs**

```yaml
apiVersion: install.istio.io/v1alpha1
kind: IstioOperator
spec:
  meshConfig:
    accessLogEncoding: JSON
    accessLogFile: /dev/stdout
    defaultConfig:
      gatewayTopology:
        proxyProtocol: {}
  components:
    ingressGateways:
    - enabled: true
      name: istio-ingressgateway
      k8s:
        hpaSpec:
          maxReplicas: 10
          minReplicas: 5
        serviceAnnotations:
          service.beta.kubernetes.io/aws-load-balancer-proxy-protocol: "*"
        ...
```

**Tab: Gateway API**

```yaml
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: httpbin-gateway
  annotations:
    service.beta.kubernetes.io/aws-load-balancer-proxy-protocol: "*"
    proxy.istio.io/config: '{"gatewayTopology" : { "proxyProtocol": {} }}'
spec:
  gatewayClassName: istio
  ...
---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: httpbin-gateway
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: httpbin-gateway-istio
  minReplicas: 5
  maxReplicas: 10
```

### Network Load Balancer {#network}

If you are using a TCP/UDP network load balancer that preserves the client IP address (AWS Network Load Balancer, GCP External Network Load Balancer, Azure Load Balancer) or you are using Round-Robin DNS, then you can use the `externalTrafficPolicy: Local` setting to also preserve the client IP inside Kubernetes by bypassing kube-proxy and preventing it from sending traffic to other nodes.

> **Warning:**
>
> For production deployments it is strongly recommended to **deploy an ingress gateway pod to multiple nodes** if you enable `externalTrafficPolicy: Local`. Otherwise, this creates a situation where **only** nodes with an active ingress gateway pod will be able to accept and distribute incoming NLB traffic to the rest of the cluster, creating potential ingress traffic bottlenecks and reduced internal load balancing capability, or even complete loss of ingress traffic to the cluster if the subset of nodes with ingress gateway pods go down. See [Source IP for Services with `Type=NodePort`](https://kubernetes.io/docs/tutorials/services/source-ip/#source-ip-for-services-with-type-nodeport) for more information.

Update the ingress gateway to set `externalTrafficPolicy: Local` to preserve the
original client source IP on the ingress gateway using the following command:

**Tabset (config-api):**

**Tab: Istio APIs**

```bash
$ kubectl patch svc istio-ingressgateway -n istio-system -p '{"spec":{"externalTrafficPolicy":"Local"}}'
```

**Tab: Gateway API**

```bash
$ kubectl patch svc httpbin-gateway-istio -n foo -p '{"spec":{"externalTrafficPolicy":"Local"}}'
```

### HTTP/HTTPS Load Balancer {#http-https}

If you are using an HTTP/HTTPS external load balancer (AWS ALB, GCP ), it can put the original client IP address in the X-Forwarded-For header.  Istio can extract the client IP address from this header with some configuration.  See [Configuring Gateway Network Topology](../../../../ops/configuration/traffic-management/network-topologies/index.md). Quick example if using a single load balancer in front of Kubernetes:

```yaml
apiVersion: install.istio.io/v1alpha1
kind: IstioOperator
spec:
  meshConfig:
    accessLogEncoding: JSON
    accessLogFile: /dev/stdout
    defaultConfig:
      gatewayTopology:
        numTrustedProxies: 1
```

## IP-based allow list and deny list

**When to use `ipBlocks` vs. `remoteIpBlocks`:** If you are using the X-Forwarded-For HTTP header or the PROXY Protocol to determine the original client IP address, then you should use `remoteIpBlocks` in your `AuthorizationPolicy`. If you are using `externalTrafficPolicy: Local`, then you should use `ipBlocks` in your `AuthorizationPolicy`.

|Load Balancer Type |Source of Client IP   | `ipBlocks` vs. `remoteIpBlocks`
--------------------|----------------------|---------------------------
| TCP Proxy         | PROXY Protocol       | `remoteIpBlocks`
| Network           | packet source address| `ipBlocks`
| HTTP/HTTPS        | X-Forwarded-For      | `remoteIpBlocks`

* The following command creates the authorization policy, `ingress-policy`, for
the Istio ingress gateway. The following policy sets the `action` field to `ALLOW` to
allow the IP addresses specified in the `ipBlocks` to access the ingress gateway.
IP addresses not in the list will be denied. The `ipBlocks` supports both single IP address and CIDR notation.

**Tabset (config-api):**

**Tab: Istio APIs**

***ipBlocks:***

```bash
$ kubectl apply -f - <<EOF
apiVersion: security.istio.io/v1
kind: AuthorizationPolicy
metadata:
  name: ingress-policy
  namespace: istio-system
spec:
  selector:
    matchLabels:
      app: istio-ingressgateway
  action: ALLOW
  rules:
  - from:
    - source:
        ipBlocks: ["1.2.3.4", "5.6.7.0/24"]
EOF
```

***remoteIpBlocks:***

```bash
$ kubectl apply -f - <<EOF
apiVersion: security.istio.io/v1
kind: AuthorizationPolicy
metadata:
  name: ingress-policy
  namespace: istio-system
spec:
  selector:
    matchLabels:
      app: istio-ingressgateway
  action: ALLOW
  rules:
  - from:
    - source:
        remoteIpBlocks: ["1.2.3.4", "5.6.7.0/24"]
EOF
```

**Tab: Gateway API**

***ipBlocks:***

```bash
$ kubectl apply -f - <<EOF
apiVersion: security.istio.io/v1
kind: AuthorizationPolicy
metadata:
  name: ingress-policy
  namespace: foo
spec:
  targetRef:
    kind: Gateway
    group: gateway.networking.k8s.io
    name: httpbin-gateway
  action: ALLOW
  rules:
  - from:
    - source:
        ipBlocks: ["1.2.3.4", "5.6.7.0/24"]
EOF
```

***remoteIpBlocks:***

```bash
$ kubectl apply -f - <<EOF
apiVersion: security.istio.io/v1
kind: AuthorizationPolicy
metadata:
  name: ingress-policy
  namespace: foo
spec:
  targetRef:
    kind: Gateway
    group: gateway.networking.k8s.io
    name: httpbin-gateway
  action: ALLOW
  rules:
  - from:
    - source:
        remoteIpBlocks: ["1.2.3.4", "5.6.7.0/24"]
EOF
```

* Verify that a request to the ingress gateway is denied:

```bash
$ curl "$INGRESS_HOST:$INGRESS_PORT"/headers -s -o /dev/null -w "%{http_code}\n"
403
```

* Assign your original client IP address to an env variable. If you don't know it, you can an find it
    in the Envoy logs using the following command:

**Tabset (config-api):**

**Tab: Istio APIs**

***ipBlocks:***

```bash
$ CLIENT_IP=$(kubectl get pods -n istio-system -o name -l istio=ingressgateway | sed 's|pod/||' | while read -r pod; do kubectl logs "$pod" -n istio-system | grep remoteIP; done | tail -1 | awk -F, '{print $3}' | awk -F: '{print $2}' | sed 's/ //') && echo "$CLIENT_IP"
192.168.10.15
```

***remoteIpBlocks:***

```bash
$ CLIENT_IP=$(kubectl get pods -n istio-system -o name -l istio=ingressgateway | sed 's|pod/||' | while read -r pod; do kubectl logs "$pod" -n istio-system | grep remoteIP; done | tail -1 | awk -F, '{print $4}' | awk -F: '{print $2}' | sed 's/ //') && echo "$CLIENT_IP"
192.168.10.15
```

**Tab: Gateway API**

***ipBlocks:***

```bash
$ CLIENT_IP=$(kubectl get pods -n foo -o name -l gateway.networking.k8s.io/gateway-name=httpbin-gateway | sed 's|pod/||' | while read -r pod; do kubectl logs "$pod" -n foo | grep remoteIP; done | tail -1 | awk -F, '{print $3}' | awk -F: '{print $2}' | sed 's/ //') && echo "$CLIENT_IP"
192.168.10.15
```

***remoteIpBlocks:***

```bash
$ CLIENT_IP=$(kubectl get pods -n foo -o name -l gateway.networking.k8s.io/gateway-name=httpbin-gateway | sed 's|pod/||' | while read -r pod; do kubectl logs "$pod" -n foo | grep remoteIP; done | tail -1 | awk -F, '{print $4}' | awk -F: '{print $2}' | sed 's/ //') && echo "$CLIENT_IP"
192.168.10.15
```

* Update the `ingress-policy` to include your client IP address:

**Tabset (config-api):**

**Tab: Istio APIs**

***ipBlocks:***

```bash
$ kubectl apply -f - <<EOF
apiVersion: security.istio.io/v1
kind: AuthorizationPolicy
metadata:
  name: ingress-policy
  namespace: istio-system
spec:
  selector:
    matchLabels:
      app: istio-ingressgateway
  action: ALLOW
  rules:
  - from:
    - source:
        ipBlocks: ["1.2.3.4", "5.6.7.0/24", "$CLIENT_IP"]
EOF
```

***remoteIpBlocks:***

```bash
$ kubectl apply -f - <<EOF
apiVersion: security.istio.io/v1
kind: AuthorizationPolicy
metadata:
  name: ingress-policy
  namespace: istio-system
spec:
  selector:
    matchLabels:
      app: istio-ingressgateway
  action: ALLOW
  rules:
  - from:
    - source:
        remoteIpBlocks: ["1.2.3.4", "5.6.7.0/24", "$CLIENT_IP"]
EOF
```

**Tab: Gateway API**

***ipBlocks:***

```bash
$ kubectl apply -f - <<EOF
apiVersion: security.istio.io/v1
kind: AuthorizationPolicy
metadata:
  name: ingress-policy
  namespace: foo
spec:
  targetRef:
    kind: Gateway
    group: gateway.networking.k8s.io
    name: httpbin-gateway
  action: ALLOW
  rules:
  - from:
    - source:
        ipBlocks: ["1.2.3.4", "5.6.7.0/24", "$CLIENT_IP"]
EOF
```

***remoteIpBlocks:***

```bash
$ kubectl apply -f - <<EOF
apiVersion: security.istio.io/v1
kind: AuthorizationPolicy
metadata:
  name: ingress-policy
  namespace: foo
spec:
  targetRef:
    kind: Gateway
    group: gateway.networking.k8s.io
    name: httpbin-gateway
  action: ALLOW
  rules:
  - from:
    - source:
        remoteIpBlocks: ["1.2.3.4", "5.6.7.0/24", "$CLIENT_IP"]
EOF
```

* Verify that a request to the ingress gateway is allowed:

```bash
$ curl "$INGRESS_HOST:$INGRESS_PORT"/headers -s -o /dev/null -w "%{http_code}\n"
200
```

* Update the `ingress-policy` authorization policy to set
the `action` key to `DENY` so that the IP addresses specified in the `ipBlocks` are
not allowed to access the ingress gateway:

**Tabset (config-api):**

**Tab: Istio APIs**

***ipBlocks:***

```bash
$ kubectl apply -f - <<EOF
apiVersion: security.istio.io/v1
kind: AuthorizationPolicy
metadata:
  name: ingress-policy
  namespace: istio-system
spec:
  selector:
    matchLabels:
      app: istio-ingressgateway
  action: DENY
  rules:
  - from:
    - source:
        ipBlocks: ["$CLIENT_IP"]
EOF
```

***remoteIpBlocks:***

```bash
$ kubectl apply -f - <<EOF
apiVersion: security.istio.io/v1
kind: AuthorizationPolicy
metadata:
  name: ingress-policy
  namespace: istio-system
spec:
  selector:
    matchLabels:
      app: istio-ingressgateway
  action: DENY
  rules:
  - from:
    - source:
        remoteIpBlocks: ["$CLIENT_IP"]
EOF
```

**Tab: Gateway API**

***ipBlocks:***

```bash
$ kubectl apply -f - <<EOF
apiVersion: security.istio.io/v1
kind: AuthorizationPolicy
metadata:
  name: ingress-policy
  namespace: foo
spec:
  targetRef:
    kind: Gateway
    group: gateway.networking.k8s.io
    name: httpbin-gateway
  action: DENY
  rules:
  - from:
    - source:
        ipBlocks: ["$CLIENT_IP"]
EOF
```

***remoteIpBlocks:***

```bash
$ kubectl apply -f - <<EOF
apiVersion: security.istio.io/v1
kind: AuthorizationPolicy
metadata:
  name: ingress-policy
  namespace: foo
spec:
  targetRef:
    kind: Gateway
    group: gateway.networking.k8s.io
    name: httpbin-gateway
  action: DENY
  rules:
  - from:
    - source:
        remoteIpBlocks: ["$CLIENT_IP"]
EOF
```

* Verify that a request to the ingress gateway is denied:

```bash
$ curl "$INGRESS_HOST:$INGRESS_PORT"/headers -s -o /dev/null -w "%{http_code}\n"
403
```

* You could use an online proxy service to access the ingress gateway using a
different client IP to verify the request is allowed.

* If you are not getting the responses you expect, view the ingress gateway logs which should show RBAC debugging information:

**Tabset (config-api):**

**Tab: Istio APIs**

```bash
$ kubectl get pods -n istio-system -o name -l istio=ingressgateway | sed 's|pod/||' | while read -r pod; do kubectl logs "$pod" -n istio-system; done
```

**Tab: Gateway API**

```bash
$ kubectl get pods -n foo -o name -l gateway.networking.k8s.io/gateway-name=httpbin-gateway | sed 's|pod/||' | while read -r pod; do kubectl logs "$pod" -n foo; done
```

## Clean up

* Remove the authorization policy:

**Tabset (config-api):**

**Tab: Istio APIs**

```bash
$ kubectl delete authorizationpolicy ingress-policy -n istio-system
```

**Tab: Gateway API**

```bash
$ kubectl delete authorizationpolicy ingress-policy -n foo
```

* Remove the namespace `foo`:

```bash
$ kubectl delete namespace foo
```
