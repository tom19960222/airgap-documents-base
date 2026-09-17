---
collection: istio
version: "1.24"
title: "Istio Workload Minimum TLS Version Configuration"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/tasks/security/tls-configuration/workload-min-tls-version/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Shows how to configure the minimum TLS version for Istio workloads."
---
This task shows how to configure the minimum TLS version for Istio workloads.
The maximum TLS version for Istio workloads is 1.3.

## Configuration of minimum TLS version for Istio workloads

* Install Istio through `istioctl` with the minimum TLS version configured.
  The `IstioOperator` custom resource used to configure Istio in the `istioctl install` command
  contains a field for the minimum TLS version for Istio workloads.
  The `minProtocolVersion` field specifies the minimum TLS version for the TLS connections
  among Istio workloads. In the following example,
  the minimum TLS version for Istio workloads is configured to be 1.3.

```bash
$ cat <<EOF > ./istio.yaml
apiVersion: install.istio.io/v1alpha1
kind: IstioOperator
spec:
  meshConfig:
    meshMTLS:
      minProtocolVersion: TLSV1_3
EOF
$ istioctl install -f ./istio.yaml
```

## Check the TLS configuration of Istio workloads

After configuring the minimum TLS version of Istio workloads,
you can verify that the minimum TLS version was configured and works as expected.

* Deploy two workloads: `httpbin` and `curl`. Deploy these into a single namespace,
  for example `foo`. Both workloads run with an Envoy proxy in front of each.

```bash
$ kubectl create ns foo
$ kubectl apply -f <(istioctl kube-inject -f @samples/httpbin/httpbin.yaml@) -n foo
$ kubectl apply -f <(istioctl kube-inject -f @samples/curl/curl.yaml@) -n foo
```

* Verify that `curl` successfully communicates with `httpbin` using this command:

```bash
$ kubectl exec "$(kubectl get pod -l app=curl -n foo -o jsonpath={.items..metadata.name})" -c curl -n foo -- curl http://httpbin.foo:8000/ip -sS -o /dev/null -w "%{http_code}\n"
200
```

> **Warning:**
>
> If you don’t see the expected output, retry after a few seconds.
> Caching and propagation can cause a delay.

In the example, the minimum TLS version was configured to be 1.3.
To check that TLS 1.3 is allowed, you can run the following command:

```bash
$ kubectl exec "$(kubectl get pod -l app=curl -n foo -o jsonpath={.items..metadata.name})" -c istio-proxy -n foo -- openssl s_client -alpn istio -tls1_3 -connect httpbin.foo:8000 | grep "TLSv1.3"
```

The text output should include:

```plain
TLSv1.3
```

To check that TLS 1.2 is not allowed, you can run the following command:

```bash
$ kubectl exec "$(kubectl get pod -l app=curl -n foo -o jsonpath={.items..metadata.name})" -c istio-proxy -n foo -- openssl s_client -alpn istio -tls1_2 -connect httpbin.foo:8000 | grep "Cipher is (NONE)"
```

The text output should include:

```plain
Cipher is (NONE)
```

## Cleanup

Delete sample applications `curl` and `httpbin` from the `foo` namespace:

```bash
$ kubectl delete -f samples/httpbin/httpbin.yaml -n foo
$ kubectl delete -f samples/curl/curl.yaml -n foo
```

Uninstall Istio from the cluster:

```bash
$ istioctl uninstall --purge -y
```

To remove the `foo` and `istio-system` namespaces:

```bash
$ kubectl delete ns foo istio-system
```
