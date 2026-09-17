---
collection: istio
version: "1.24"
title: "Egress using Wildcard Hosts"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/tasks/traffic-management/egress/wildcard-egress-hosts/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Describes how to enable egress traffic for a set of hosts in a common domain, instead of configuring each and every host separately."
---
The [Accessing External Services](../egress-control/index.md) task and
the [Configure an Egress Gateway](../egress-gateway/index.md) example
describe how to configure egress traffic for specific hostnames, like `edition.cnn.com`.
This example shows how to enable egress traffic for a set of hosts in a common domain, for
example `*.wikipedia.org`, instead of configuring each and every host separately.

## Background

Suppose you want to enable egress traffic in Istio for the `wikipedia.org` sites in all languages.
Each version of `wikipedia.org` in a particular language has its own hostname, e.g., `en.wikipedia.org` and
`de.wikipedia.org` in the English and the German languages, respectively.
You want to enable egress traffic by common configuration items for all the Wikipedia sites,
without the need to specify every language's site separately.

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

*   Install Istio with access logging enabled and with the blocking-by-default outbound traffic policy:

**Tabset (config-api):**

**Tab: Istio APIs**

```bash
$ istioctl install --set profile=demo --set meshConfig.outboundTrafficPolicy.mode=REGISTRY_ONLY
```

> **Tip:**
>
> You can run this task on an Istio configuration other than the `demo` profile as long as you make sure to
> [deploy the Istio egress gateway](../egress-gateway/index.md#deploy-istio-egress-gateway),
> [enable Envoy’s access logging](../../../observability/logs/access-log/index.md#enable-envoy-s-access-logging), and
> [apply the blocking-by-default outbound traffic policy](../egress-control/index.md#change-to-the-blocking-by-default-policy)
> in your installation.

**Tab: Gateway API**

```bash
$ istioctl install --set profile=minimal -y \
    --set values.pilot.env.PILOT_ENABLE_ALPHA_GATEWAY_API=true \
    --set meshConfig.accessLogFile=/dev/stdout \
    --set meshConfig.outboundTrafficPolicy.mode=REGISTRY_ONLY
```

*   Deploy the [curl](https://github.com/istio/istio/tree/8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99/samples/curl) sample app to use as a test source for sending requests.
    If you have
    [automatic sidecar injection](../../../../setup/additional-setup/sidecar-injection/index.md#automatic-sidecar-injection)
    enabled, run the following command to deploy the sample app:

```bash
$ kubectl apply -f @samples/curl/curl.yaml@
```

    Otherwise, manually inject the sidecar before deploying the `curl` application with the following command:

```bash
$ kubectl apply -f <(istioctl kube-inject -f @samples/curl/curl.yaml@)
```

> **Tip:**
>
> You can use any pod with `curl` installed as a test source.

*   Set the `SOURCE_POD` environment variable to the name of your source pod:

```bash
$ export SOURCE_POD=$(kubectl get pod -l app=curl -o jsonpath={.items..metadata.name})
```

## Configure direct traffic to a wildcard host

The first, and simplest, way to access a set of hosts within a common domain is by configuring
a simple `ServiceEntry` with a wildcard host and calling the services directly from the sidecar.
When calling services directly (i.e., not via an egress gateway), the configuration for
a wildcard host is no different than that of any other (e.g., fully qualified) host,
only much more convenient when there are many hosts within the common domain.

> **Warning:**
>
> Note that the configuration below can be easily bypassed by a malicious application. For a secure egress traffic control,
> direct the traffic through an egress gateway.

> **Warning:**
>
> Note that the `DNS` resolution cannot be used for wildcard hosts. This is why the `NONE` resolution (omitted since it is
> the default) is used in the service entry below.

1.  Define a `ServiceEntry` for `*.wikipedia.org`:

```bash
$ kubectl apply -f - <<EOF
apiVersion: networking.istio.io/v1
kind: ServiceEntry
metadata:
  name: wikipedia
spec:
  hosts:
  - "*.wikipedia.org"
  ports:
  - number: 443
    name: https
    protocol: HTTPS
EOF
```

1.  Send HTTPS requests to
    [https://en.wikipedia.org](https://en.wikipedia.org) and [https://de.wikipedia.org](https://de.wikipedia.org):

```bash
$ kubectl exec "$SOURCE_POD" -c curl -- sh -c 'curl -s https://en.wikipedia.org/wiki/Main_Page | grep -o "<title>.*</title>"; curl -s https://de.wikipedia.org/wiki/Wikipedia:Hauptseite | grep -o "<title>.*</title>"'
<title>Wikipedia, the free encyclopedia</title>
<title>Wikipedia – Die freie Enzyklopädie</title>
```

### Cleanup direct traffic to a wildcard host

```bash
$ kubectl delete serviceentry wikipedia
```

## Configure egress gateway traffic to a wildcard host

When all wildcard hosts are served by a single server, the configuration for
egress gateway-based access to a wildcard host is very similar to that of any host, with one exception:
the configured route destination will not be the same as the configured host,
i.e., the wildcard. It will instead be configured with the host of the single server for
the set of domains.

1.  Create an egress `Gateway` for _*.wikipedia.org_ and route rules
    to direct the traffic through the egress gateway and from the egress gateway to the external service:

**Tabset (config-api):**

**Tab: Istio APIs**

```bash
$ kubectl apply -f - <<EOF
apiVersion: networking.istio.io/v1
kind: Gateway
metadata:
  name: istio-egressgateway
spec:
  selector:
    istio: egressgateway
  servers:
  - port:
      number: 443
      name: https
      protocol: HTTPS
    hosts:
    - "*.wikipedia.org"
    tls:
      mode: PASSTHROUGH
---
apiVersion: networking.istio.io/v1
kind: DestinationRule
metadata:
  name: egressgateway-for-wikipedia
spec:
  host: istio-egressgateway.istio-system.svc.cluster.local
  subsets:
    - name: wikipedia
---
apiVersion: networking.istio.io/v1
kind: VirtualService
metadata:
  name: direct-wikipedia-through-egress-gateway
spec:
  hosts:
  - "*.wikipedia.org"
  gateways:
  - mesh
  - istio-egressgateway
  tls:
  - match:
    - gateways:
      - mesh
      port: 443
      sniHosts:
      - "*.wikipedia.org"
    route:
    - destination:
        host: istio-egressgateway.istio-system.svc.cluster.local
        subset: wikipedia
        port:
          number: 443
      weight: 100
  - match:
    - gateways:
      - istio-egressgateway
      port: 443
      sniHosts:
      - "*.wikipedia.org"
    route:
    - destination:
        host: www.wikipedia.org
        port:
          number: 443
      weight: 100
EOF
```

**Tab: Gateway API**

```bash
$ kubectl apply -f - <<EOF
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: wikipedia-egress-gateway
  annotations:
    networking.istio.io/service-type: ClusterIP
spec:
  gatewayClassName: istio
  listeners:
  - name: tls
    hostname: "*.wikipedia.org"
    port: 443
    protocol: TLS
    tls:
      mode: Passthrough
    allowedRoutes:
      namespaces:
        from: Same
---
apiVersion: gateway.networking.k8s.io/v1alpha2
kind: TLSRoute
metadata:
  name: direct-wikipedia-to-egress-gateway
spec:
  parentRefs:
  - kind: ServiceEntry
    group: networking.istio.io
    name: wikipedia
  rules:
  - backendRefs:
    - name: wikipedia-egress-gateway-istio
      port: 443
---
apiVersion: gateway.networking.k8s.io/v1alpha2
kind: TLSRoute
metadata:
  name: forward-wikipedia-from-egress-gateway
spec:
  parentRefs:
  - name: wikipedia-egress-gateway
  hostnames:
  - "*.wikipedia.org"
  rules:
  - backendRefs:
    - kind: Hostname
      group: networking.istio.io
      name: www.wikipedia.org
      port: 443
---
apiVersion: networking.istio.io/v1
kind: ServiceEntry
metadata:
  name: wikipedia
spec:
  hosts:
  - "*.wikipedia.org"
  ports:
  - number: 443
    name: https
    protocol: HTTPS
EOF
```

2)  Create a `ServiceEntry` for the destination server, _www.wikipedia.org_:

```bash
$ kubectl apply -f - <<EOF
apiVersion: networking.istio.io/v1
kind: ServiceEntry
metadata:
  name: www-wikipedia
spec:
  hosts:
  - www.wikipedia.org
  ports:
  - number: 443
    name: https
    protocol: HTTPS
  resolution: DNS
EOF
```

3)  Send HTTPS requests to
    [https://en.wikipedia.org](https://en.wikipedia.org) and [https://de.wikipedia.org](https://de.wikipedia.org):

```bash
$ kubectl exec "$SOURCE_POD" -c curl -- sh -c 'curl -s https://en.wikipedia.org/wiki/Main_Page | grep -o "<title>.*</title>"; curl -s https://de.wikipedia.org/wiki/Wikipedia:Hauptseite | grep -o "<title>.*</title>"'
<title>Wikipedia, the free encyclopedia</title>
<title>Wikipedia – Die freie Enzyklopädie</title>
```

4)  Check the statistics of the egress gateway's proxy for the counter that corresponds to your
    requests to _*.wikipedia.org_:

**Tabset (config-api):**

**Tab: Istio APIs**

```bash
$ kubectl exec "$(kubectl get pod -l istio=egressgateway -n istio-system -o jsonpath='{.items[0].metadata.name}')" -c istio-proxy -n istio-system -- pilot-agent request GET clusters | grep '^outbound|443||www.wikipedia.org.*cx_total:'
outbound|443||www.wikipedia.org::208.80.154.224:443::cx_total::2
```

**Tab: Gateway API**

```bash
$ kubectl exec "$(kubectl get pod -l gateway.networking.k8s.io/gateway-name=wikipedia-egress-gateway -o jsonpath='{.items[0].metadata.name}')" -c istio-proxy -- pilot-agent request GET clusters | grep '^outbound|443||www.wikipedia.org.*cx_total:'
outbound|443||www.wikipedia.org::208.80.154.224:443::cx_total::2
```

### Cleanup egress gateway traffic to a wildcard host

**Tabset (config-api):**

**Tab: Istio APIs**

```bash
$ kubectl delete serviceentry www-wikipedia
$ kubectl delete gateway istio-egressgateway
$ kubectl delete virtualservice direct-wikipedia-through-egress-gateway
$ kubectl delete destinationrule egressgateway-for-wikipedia
```

**Tab: Gateway API**

```bash
$ kubectl delete se wikipedia
$ kubectl delete se www-wikipedia
$ kubectl delete gtw wikipedia-egress-gateway
$ kubectl delete tlsroute direct-wikipedia-to-egress-gateway
$ kubectl delete tlsroute forward-wikipedia-from-egress-gateway
```

## Wildcard configuration for arbitrary domains

The configuration in the previous section worked because all the `*.wikipedia.org` sites can be served by any one
of the `wikipedia.org` servers. However, this is not always the case. For example, you may want to configure egress
control for access to more general wildcard domains like `*.com` or `*.org`. Configuring traffic to arbitrary
wildcard domains introduces a challenge for Istio gateways; an Istio gateway can only be configured to route traffic
to predefined hosts, predefined IP addresses, or to the original destination IP address of the request.

In the previous section you configured the virtual service to direct traffic to the predefined host `www.wikipedia.org`.
In the general case, however, you don't know the host or IP address that can serve an arbitrary host received in a
request, which leaves the original destination address of the request as the only value with which to route the request.
Unfortunately, when using an egress gateway, the original destination address of the request is lost since the original
request is redirected to the gateway, causing the destination IP address to become the IP address of the gateway.

Although not as easy and somewhat fragile as it relies on Istio implementation details, you can use
[Envoy filters](https://istio.io/v1.24/docs/reference/config/networking/envoy-filter/) <!-- unresolved-site-link: route=/docs/reference/config/networking/envoy-filter --> to configure a gateway to support arbitrary domains
by using the [SNI](https://en.wikipedia.org/wiki/Server_Name_Indication) value in an HTTPS, or any TLS, request to
identify the original destination to which to route the request. One example of this configuration approach can be
found in [routing egress traffic to wildcard destinations](https://istio.io/v1.24/blog/2023/egress-sni/) <!-- unresolved-site-link: route=/blog/2023/egress-sni -->.

## Cleanup

* Shutdown the [curl](https://github.com/istio/istio/tree/8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99/samples/curl) service:

```bash
$ kubectl delete -f @samples/curl/curl.yaml@
```

* Uninstall Istio from your cluster:

```bash
$ istioctl uninstall --purge -y
```
