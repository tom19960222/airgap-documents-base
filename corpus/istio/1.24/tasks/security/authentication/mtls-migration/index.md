---
collection: istio
version: "1.24"
title: "Mutual TLS Migration"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/tasks/security/authentication/mtls-migration/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Shows you how to incrementally migrate your Istio services to mutual TLS."
---
This task shows how to ensure your workloads only communicate using mutual TLS as they are migrated to
Istio.

Istio automatically configures workload sidecars to use [mutual TLS](../authn-policy/index.md#auto-mutual-tls) when calling other workloads. By default, Istio configures the destination workloads using `PERMISSIVE` mode.
When `PERMISSIVE` mode is enabled, a service can accept both plaintext and mutual TLS traffic. In order to only allow
mutual TLS traffic, the configuration needs to be changed to `STRICT` mode.

You can use the [Grafana dashboard](../../../observability/metrics/using-istio-dashboard/index.md) to
check which workloads are still sending plaintext traffic to the workloads in `PERMISSIVE` mode and choose to lock
them down once the migration is done.

## Before you begin

<!-- TODO: update the link after other PRs are merged -->

* Understand Istio [authentication policy](../../../../concepts/security/index.md#authentication-policies) and related [mutual TLS authentication](../../../../concepts/security/index.md#mutual-tls-authentication) concepts.

* Read the [authentication policy task](../authn-policy/index.md) to
  learn how to configure authentication policy.

* Have a Kubernetes cluster with Istio installed, without global mutual TLS enabled (for example, use the `default` configuration profile as described in [installation steps](../../../../setup/getting-started/index.md)).

In this task, you can try out the migration process by creating sample workloads and modifying
the policies to enforce STRICT mutual TLS between the workloads.

## Set up the cluster

* Create two namespaces, `foo` and `bar`, and deploy [httpbin](https://github.com/istio/istio/tree/8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99/samples/httpbin) and [curl](https://github.com/istio/istio/tree/8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99/samples/curl) with sidecars on both of them:

```bash
$ kubectl create ns foo
$ kubectl apply -f <(istioctl kube-inject -f @samples/httpbin/httpbin.yaml@) -n foo
$ kubectl apply -f <(istioctl kube-inject -f @samples/curl/curl.yaml@) -n foo
$ kubectl create ns bar
$ kubectl apply -f <(istioctl kube-inject -f @samples/httpbin/httpbin.yaml@) -n bar
$ kubectl apply -f <(istioctl kube-inject -f @samples/curl/curl.yaml@) -n bar
```

* Create another namespace, `legacy`, and deploy [curl](https://github.com/istio/istio/tree/8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99/samples/curl) without a sidecar:

```bash
$ kubectl create ns legacy
$ kubectl apply -f @samples/curl/curl.yaml@ -n legacy
```

* Verify the setup by sending http requests (using curl) from the curl pods, in namespaces `foo`, `bar` and `legacy`, to `httpbin.foo` and `httpbin.bar`.
    All requests should succeed with return code 200.

```bash
$ for from in "foo" "bar" "legacy"; do for to in "foo" "bar"; do kubectl exec "$(kubectl get pod -l app=curl -n ${from} -o jsonpath={.items..metadata.name})" -c curl -n ${from} -- curl http://httpbin.${to}:8000/ip -s -o /dev/null -w "curl.${from} to httpbin.${to}: %{http_code}\n"; done; done
curl.foo to httpbin.foo: 200
curl.foo to httpbin.bar: 200
curl.bar to httpbin.foo: 200
curl.bar to httpbin.bar: 200
curl.legacy to httpbin.foo: 200
curl.legacy to httpbin.bar: 200
```

> **Tip:**
>
> If any of the curl commands fail, ensure that there are no existing authentication policies or destination rules
>     that might interfere with requests to the httpbin service.
>
>
>
> ```bash
> $ kubectl get peerauthentication --all-namespaces
> No resources found
> ```
>
>
>
>
>
> ```bash
> $ kubectl get destinationrule --all-namespaces
> No resources found
> ```

## Lock down to mutual TLS by namespace

After migrating all clients to Istio and injecting the Envoy sidecar, you can lock down workloads in the `foo` namespace
to only accept mutual TLS traffic.

```bash
$ kubectl apply -n foo -f - <<EOF
apiVersion: security.istio.io/v1
kind: PeerAuthentication
metadata:
  name: default
spec:
  mtls:
    mode: STRICT
EOF
```

Now, you should see the request from `curl.legacy` to `httpbin.foo` failing.

```bash
$ for from in "foo" "bar" "legacy"; do for to in "foo" "bar"; do kubectl exec "$(kubectl get pod -l app=curl -n ${from} -o jsonpath={.items..metadata.name})" -c curl -n ${from} -- curl http://httpbin.${to}:8000/ip -s -o /dev/null -w "curl.${from} to httpbin.${to}: %{http_code}\n"; done; done
curl.foo to httpbin.foo: 200
curl.foo to httpbin.bar: 200
curl.bar to httpbin.foo: 200
curl.bar to httpbin.bar: 200
curl.legacy to httpbin.foo: 000
command terminated with exit code 56
curl.legacy to httpbin.bar: 200
```

If you installed Istio with `values.global.proxy.privileged=true`, you can use `tcpdump` to verify
traffic is encrypted or not.

```bash
$ kubectl exec -nfoo "$(kubectl get pod -nfoo -lapp=httpbin -ojsonpath={.items..metadata.name})" -c istio-proxy -- sudo tcpdump dst port 80  -A
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes
```

You will see plain text and encrypted text in the output when requests are sent from `curl.legacy` and `curl.foo`
respectively.

If you can't migrate all your services to Istio (i.e., inject Envoy sidecar in all of them), you will need to continue to use `PERMISSIVE` mode.
However, when configured with `PERMISSIVE` mode, no authentication or authorization checks will be performed for plaintext traffic by default.
We recommend you use [Istio Authorization](../../authorization/authz-http/index.md) to configure different paths with different authorization policies.

## Lock down mutual TLS for the entire mesh

You can lock down workloads in all namespaces to only accept mutual TLS traffic by putting the policy in the system namespace of your Istio installation.

```bash
$ kubectl apply -n istio-system -f - <<EOF
apiVersion: security.istio.io/v1
kind: PeerAuthentication
metadata:
  name: default
spec:
  mtls:
    mode: STRICT
EOF
```

Now, both the `foo` and `bar` namespaces enforce mutual TLS only traffic, so you should see requests from `curl.legacy`
failing for both.

```bash
$ for from in "foo" "bar" "legacy"; do for to in "foo" "bar"; do kubectl exec "$(kubectl get pod -l app=curl -n ${from} -o jsonpath={.items..metadata.name})" -c curl -n ${from} -- curl http://httpbin.${to}:8000/ip -s -o /dev/null -w "curl.${from} to httpbin.${to}: %{http_code}\n"; done; done
```

## Clean up the example

1. Remove the mesh-wide authentication policy.

```bash
$ kubectl delete peerauthentication -n foo default
$ kubectl delete peerauthentication -n istio-system default
```

1. Remove the test namespaces.

```bash
$ kubectl delete ns foo bar legacy
Namespaces foo bar legacy deleted.
```
