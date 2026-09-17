---
collection: istio
version: "1.24"
title: "Health Checking of Istio Services"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/ops/configuration/mesh/app-health-check/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Shows how to do health checking for Istio services."
---
[Kubernetes liveness and readiness probes](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-probes/)
describes several ways to configure liveness and readiness probes:

1. [Command](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#define-a-liveness-command)
1. [HTTP request](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#define-a-liveness-http-request)
1. [TCP probe](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#define-a-tcp-liveness-probe)
1. [gRPC probe](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/#define-a-grpc-liveness-probe)

The command approach works with no changes required, but HTTP requests, TCP probes, and gRPC probes require Istio to make changes to the pod configuration.

The health check requests to the `liveness-http` service are sent by Kubelet.
This becomes a problem when mutual TLS is enabled, because the Kubelet does not have an Istio issued certificate.
Therefore the health check requests will fail.

TCP probe checks need special handling, because Istio redirects all incoming traffic into the sidecar, and so all TCP ports appear open. The Kubelet simply checks if some process is listening on the specified port, and so the probe will always succeed as long as the sidecar is running.

Istio solves both these problems by rewriting the application `PodSpec` readiness/liveness probe,
so that the probe request is sent to the [sidecar agent](https://istio.io/v1.24/docs/reference/commands/pilot-agent/) <!-- unresolved-site-link: route=/docs/reference/commands/pilot-agent -->.

## Liveness probe rewrite example

To demonstrate how the readiness/liveness probe is rewritten at the application `PodSpec` level, let us use the [liveness-http-same-port sample](https://raw.githubusercontent.com/istio/istio/8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99/samples/health-check/liveness-http-same-port.yaml).

First create and label a namespace for the example:

```bash
$ kubectl create namespace istio-io-health-rewrite
$ kubectl label namespace istio-io-health-rewrite istio-injection=enabled
```

And deploy the sample application:

```bash
$ kubectl apply -f - <<EOF
apiVersion: apps/v1
kind: Deployment
metadata:
  name: liveness-http
  namespace: istio-io-health-rewrite
spec:
  selector:
    matchLabels:
      app: liveness-http
      version: v1
  template:
    metadata:
      labels:
        app: liveness-http
        version: v1
    spec:
      containers:
      - name: liveness-http
        image: docker.io/istio/health:example
        ports:
        - containerPort: 8001
        livenessProbe:
          httpGet:
            path: /foo
            port: 8001
          initialDelaySeconds: 5
          periodSeconds: 5
EOF
```

Once deployed, you can inspect the pod's application container to see the changed path:

```bash
$ kubectl get pod "$LIVENESS_POD" -n istio-io-health-rewrite -o json | jq '.spec.containers[0].livenessProbe.httpGet'
{
  "path": "/app-health/liveness-http/livez",
  "port": 15020,
  "scheme": "HTTP"
}
```

The original `livenessProbe` path is now mapped against the new path in the sidecar container environment variable `ISTIO_KUBE_APP_PROBERS`:

```bash
$ kubectl get pod "$LIVENESS_POD" -n istio-io-health-rewrite -o=jsonpath="{.spec.containers[1].env[?(@.name=='ISTIO_KUBE_APP_PROBERS')]}"
{
  "name":"ISTIO_KUBE_APP_PROBERS",
  "value":"{\"/app-health/liveness-http/livez\":{\"httpGet\":{\"path\":\"/foo\",\"port\":8001,\"scheme\":\"HTTP\"},\"timeoutSeconds\":1}}"
}
```

For HTTP and gRPC requests, the sidecar agent redirects the request to the application and strips the response body, only returning the response code. For TCP probes, the sidecar agent will then do the port check while avoiding the traffic redirection.

The rewriting of problematic probes is enabled by default in all built-in Istio
[configuration profiles](../../../../setup/additional-setup/config-profiles/index.md) but can be disabled as described below.

## Liveness and readiness probes using the command approach

Istio provides a [liveness sample](https://raw.githubusercontent.com/istio/istio/8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99/samples/health-check/liveness-command.yaml) that
implements this approach. To demonstrate it working with mutual TLS enabled,
first create a namespace for the example:

```bash
$ kubectl create ns istio-io-health
```

To configure strict mutual TLS, run:

```bash
$ kubectl apply -f - <<EOF
apiVersion: security.istio.io/v1
kind: PeerAuthentication
metadata:
  name: "default"
  namespace: "istio-io-health"
spec:
  mtls:
    mode: STRICT
EOF
```

Next, change directory to the root of the Istio installation and run the following command to deploy the sample service:

```bash
$ kubectl -n istio-io-health apply -f <(istioctl kube-inject -f @samples/health-check/liveness-command.yaml@)
```

To confirm that the liveness probes are working, check the status of the sample pod to verify that it is running.

```bash
$ kubectl -n istio-io-health get pod
NAME                             READY     STATUS    RESTARTS   AGE
liveness-6857c8775f-zdv9r        2/2       Running   0           4m
```

## Liveness and readiness probes using the HTTP, TCP, and gRPC approach {#liveness-and-readiness-probes-using-the-http-request-approach}

As stated previously, Istio uses probe rewrite to implement HTTP, TCP, and gRPC probes by default. You can disable this
feature either for specific pods, or globally.

### Disable the probe rewrite for a pod {#disable-the-http-probe-rewrite-for-a-pod}

You can [annotate the pod](https://istio.io/v1.24/docs/reference/config/annotations/) <!-- unresolved-site-link: route=/docs/reference/config/annotations --> with `sidecar.istio.io/rewriteAppHTTPProbers: "false"`
to disable the probe rewrite option. Make sure you add the annotation to the
[pod resource](https://kubernetes.io/docs/concepts/workloads/pods/pod-overview/) because it will be ignored
anywhere else (for example, on an enclosing deployment resource).

**Tabset (disable-probe-rewrite):**

**Tab: HTTP Probe**

```yaml
kubectl apply -f - <<EOF
apiVersion: apps/v1
kind: Deployment
metadata:
  name: liveness-http
spec:
  selector:
    matchLabels:
      app: liveness-http
      version: v1
  template:
    metadata:
      labels:
        app: liveness-http
        version: v1
      annotations:
        sidecar.istio.io/rewriteAppHTTPProbers: "false"
    spec:
      containers:
      - name: liveness-http
        image: docker.io/istio/health:example
        ports:
        - containerPort: 8001
        livenessProbe:
          httpGet:
            path: /foo
            port: 8001
          initialDelaySeconds: 5
          periodSeconds: 5
EOF
```

**Tab: gRPC Probe**

```yaml
kubectl apply -f - <<EOF
apiVersion: apps/v1
kind: Deployment
metadata:
  name: liveness-grpc
spec:
  selector:
    matchLabels:
      app: liveness-grpc
      version: v1
  template:
    metadata:
      labels:
        app: liveness-grpc
        version: v1
      annotations:
        sidecar.istio.io/rewriteAppHTTPProbers: "false"
    spec:
      containers:
      - name: etcd
        image: registry.k8s.io/etcd:3.5.1-0
        command: ["--listen-client-urls", "http://0.0.0.0:2379", "--advertise-client-urls", "http://127.0.0.1:2379", "--log-level", "debug"]
        ports:
        - containerPort: 2379
        livenessProbe:
          grpc:
            port: 2379
          initialDelaySeconds: 10
          periodSeconds: 5
EOF
```

This approach allows you to disable the health check probe rewrite gradually on individual deployments,
without reinstalling Istio.

### Disable the probe rewrite globally

[Install Istio](../../../../setup/install/istioctl/index.md) using `--set values.sidecarInjectorWebhook.rewriteAppHTTPProbe=false`
to disable the probe rewrite globally. **Alternatively**, update the configuration map for the Istio sidecar injector:

```bash
$ kubectl get cm istio-sidecar-injector -n istio-system -o yaml | sed -e 's/"rewriteAppHTTPProbe": true/"rewriteAppHTTPProbe": false/' | kubectl apply -f -
```

## Cleanup

Remove the namespaces used for the examples:

```bash
$ kubectl delete ns istio-io-health istio-io-health-rewrite
```
