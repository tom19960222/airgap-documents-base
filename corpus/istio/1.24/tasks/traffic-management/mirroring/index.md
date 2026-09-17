---
collection: istio
version: "1.24"
title: "Mirroring"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/tasks/traffic-management/mirroring/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "This task demonstrates the traffic mirroring/shadowing capabilities of Istio."
---
This task demonstrates the traffic mirroring capabilities of Istio.

Traffic mirroring, also called shadowing, is a powerful concept that allows
feature teams to bring changes to production with as little risk as possible.
Mirroring sends a copy of live traffic to a mirrored service. The mirrored
traffic happens out of band of the critical request path for the primary service.

In this task, you will first force all traffic to `v1` of a test service. Then,
you will apply a rule to mirror a portion of traffic to `v2`.

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

1. Set up Istio by following the [Installation guide](../../../setup/_index.md).
1. Start by deploying two versions of the [httpbin](https://github.com/istio/istio/tree/8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99/samples/httpbin) service that have access logging enabled:

    1. Deploy `httpbin-v1`:

```bash
$ kubectl create -f - <<EOF
apiVersion: apps/v1
kind: Deployment
metadata:
  name: httpbin-v1
spec:
  replicas: 1
  selector:
    matchLabels:
      app: httpbin
      version: v1
  template:
    metadata:
      labels:
        app: httpbin
        version: v1
    spec:
      containers:
      - image: docker.io/kennethreitz/httpbin
        imagePullPolicy: IfNotPresent
        name: httpbin
        command: ["gunicorn", "--access-logfile", "-", "-b", "0.0.0.0:80", "httpbin:app"]
        ports:
        - containerPort: 80
EOF
```

    1. Deploy `httpbin-v2`:

```bash
$ kubectl create -f - <<EOF
apiVersion: apps/v1
kind: Deployment
metadata:
  name: httpbin-v2
spec:
  replicas: 1
  selector:
    matchLabels:
      app: httpbin
      version: v2
  template:
    metadata:
      labels:
        app: httpbin
        version: v2
    spec:
      containers:
      - image: docker.io/kennethreitz/httpbin
        imagePullPolicy: IfNotPresent
        name: httpbin
        command: ["gunicorn", "--access-logfile", "-", "-b", "0.0.0.0:80", "httpbin:app"]
        ports:
        - containerPort: 80
EOF
```

    1. Deploy the `httpbin` Kubernetes service:

```bash
$ kubectl create -f - <<EOF
apiVersion: v1
kind: Service
metadata:
  name: httpbin
  labels:
    app: httpbin
spec:
  ports:
  - name: http
    port: 8000
    targetPort: 80
  selector:
    app: httpbin
EOF
```

1. Deploy the `curl` workload you'll use to send requests to the `httpbin` service:

```bash
$ cat <<EOF | kubectl create -f -
apiVersion: apps/v1
kind: Deployment
metadata:
  name: curl
spec:
  replicas: 1
  selector:
    matchLabels:
      app: curl
  template:
    metadata:
      labels:
        app: curl
    spec:
      containers:
      - name: curl
        image: curlimages/curl
        command: ["/bin/sleep","3650d"]
        imagePullPolicy: IfNotPresent
EOF
```

## Creating a default routing policy

By default Kubernetes load balances across both versions of the `httpbin` service.
In this step, you will change that behavior so that all traffic goes to `v1`.

1. Create a default route rule to route all traffic to `v1` of the service:

**Tabset (config-api):**

**Tab: Istio APIs**

```bash
$ kubectl apply -f - <<EOF
apiVersion: networking.istio.io/v1
kind: VirtualService
metadata:
  name: httpbin
spec:
  hosts:
    - httpbin
  http:
  - route:
    - destination:
        host: httpbin
        subset: v1
      weight: 100
---
apiVersion: networking.istio.io/v1
kind: DestinationRule
metadata:
  name: httpbin
spec:
  host: httpbin
  subsets:
  - name: v1
    labels:
      version: v1
  - name: v2
    labels:
      version: v2
EOF
```

**Tab: Gateway API**

```bash
$ kubectl apply -f - <<EOF
apiVersion: v1
kind: Service
metadata:
  name: httpbin-v1
spec:
  ports:
  - port: 80
    name: http
  selector:
    app: httpbin
    version: v1
---
apiVersion: v1
kind: Service
metadata:
  name: httpbin-v2
spec:
  ports:
  - port: 80
    name: http
  selector:
    app: httpbin
    version: v2
---
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: httpbin
spec:
  parentRefs:
  - group: ""
    kind: Service
    name: httpbin
    port: 8000
  rules:
  - backendRefs:
    - name: httpbin-v1
      port: 80
EOF
```

1. Now, with all traffic directed to `httpbin:v1`, send a request to the service:

```bash
$ kubectl exec deploy/curl -c curl -- curl -sS http://httpbin:8000/headers
{
  "headers": {
    "Accept": "*/*",
    "Content-Length": "0",
    "Host": "httpbin:8000",
    "User-Agent": "curl/7.35.0",
    "X-B3-Parentspanid": "57784f8bff90ae0b",
    "X-B3-Sampled": "1",
    "X-B3-Spanid": "3289ae7257c3f159",
    "X-B3-Traceid": "b56eebd279a76f0b57784f8bff90ae0b",
    "X-Envoy-Attempt-Count": "1",
    "X-Forwarded-Client-Cert": "By=spiffe://cluster.local/ns/default/sa/default;Hash=20afebed6da091c850264cc751b8c9306abac02993f80bdb76282237422bd098;Subject=\"\";URI=spiffe://cluster.local/ns/default/sa/default"
  }
}
```

1. Check the logs from `httpbin-v1` and `httpbin-v2` pods. You should see access log entries for `v1` and none for `v2`:

```bash
$ kubectl logs deploy/httpbin-v1 -c httpbin
127.0.0.1 - - [07/Mar/2018:19:02:43 +0000] "GET /headers HTTP/1.1" 200 321 "-" "curl/7.35.0"
```

```bash
$ kubectl logs deploy/httpbin-v2 -c httpbin
<none>
```

## Mirroring traffic to `httpbin-v2`

1. Change the route rule to mirror traffic to `httpbin-v2`:

**Tabset (config-api):**

**Tab: Istio APIs**

```bash
$ kubectl apply -f - <<EOF
apiVersion: networking.istio.io/v1
kind: VirtualService
metadata:
  name: httpbin
spec:
  hosts:
    - httpbin
  http:
  - route:
    - destination:
        host: httpbin
        subset: v1
      weight: 100
    mirror:
      host: httpbin
      subset: v2
    mirrorPercentage:
      value: 100.0
EOF
```

    This route rule sends 100% of the traffic to `v1`. The last stanza specifies
    that you want to mirror (i.e., also send) 100% of the same traffic to the
    `httpbin:v2` service. When traffic gets mirrored,
    the requests are sent to the mirrored service with their Host/Authority headers
    appended with `-shadow`. For example, `cluster-1` becomes `cluster-1-shadow`.

    Also, it is important to note that these requests are mirrored as "fire and
    forget", which means that the responses are discarded.

    You can use the `value` field under the `mirrorPercentage` field to mirror a fraction of the traffic,
    instead of mirroring all requests. If this field is absent, all traffic will be mirrored.

**Tab: Gateway API**

```bash
$ kubectl apply -f - <<EOF
apiVersion: gateway.networking.k8s.io/v1
kind: HTTPRoute
metadata:
  name: httpbin
spec:
  parentRefs:
  - group: ""
    kind: Service
    name: httpbin
    port: 8000
  rules:
  - filters:
    - type: RequestMirror
      requestMirror:
        backendRef:
          name: httpbin-v2
          port: 80
    backendRefs:
    - name: httpbin-v1
      port: 80
EOF
```

    This route rule sends 100% of the traffic to `v1`. The `RequestMirror` filter
    specifies that you want to mirror (i.e., also send) 100% of the same traffic to the
    `httpbin:v2` service. When traffic gets mirrored,
    the requests are sent to the mirrored service with their Host/Authority headers
    appended with `-shadow`. For example, `cluster-1` becomes `cluster-1-shadow`.

    Also, it is important to note that these requests are mirrored as "fire and
    forget", which means that the responses are discarded.

1. Send the traffic:

```bash
$ kubectl exec deploy/curl -c curl -- curl -sS http://httpbin:8000/headers
```

    Now, you should see access logging for both `v1` and `v2`. The access logs
    created in `v2` are the mirrored requests that are actually going to `v1`.

```bash
$ kubectl logs deploy/httpbin-v1 -c httpbin
127.0.0.1 - - [07/Mar/2018:19:02:43 +0000] "GET /headers HTTP/1.1" 200 321 "-" "curl/7.35.0"
127.0.0.1 - - [07/Mar/2018:19:26:44 +0000] "GET /headers HTTP/1.1" 200 321 "-" "curl/7.35.0"
```

```bash
$ kubectl logs deploy/httpbin-v2 -c httpbin
127.0.0.1 - - [07/Mar/2018:19:26:44 +0000] "GET /headers HTTP/1.1" 200 361 "-" "curl/7.35.0"
```

## Cleaning up

1. Remove the rules:

**Tabset (config-api):**

**Tab: Istio APIs**

```bash
$ kubectl delete virtualservice httpbin
$ kubectl delete destinationrule httpbin
```

**Tab: Gateway API**

```bash
$ kubectl delete httproute httpbin
$ kubectl delete svc httpbin-v1 httpbin-v2
```

1. Delete `httpbin` and `curl` deployments and `httpbin` service:

```bash
$ kubectl delete deploy httpbin-v1 httpbin-v2 curl
$ kubectl delete svc httpbin
```
