---
collection: istio
version: "1.24"
title: "Trust Domain Migration"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/tasks/security/authorization/authz-td-migration/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Shows how to migrate from one trust domain to another without changing authorization policy."
---
This task shows you how to migrate from one trust domain to another without changing authorization policy.

In Istio 1.4, we introduce an alpha feature to support trust domain migration for authorization policy. This means if an
Istio mesh needs to change its trust domain, the authorization policy doesn't need to be changed manually.
In Istio, if a workload is running in namespace `foo` with the service account `bar`, and the trust domain of the system is `my-td`,
the identity of said workload is `spiffe://my-td/ns/foo/sa/bar`. By default, the Istio mesh trust domain is `cluster.local`,
unless you specify it during the installation.

## Before you begin

Before you begin this task, do the following:

1. Read the [Istio authorization concepts](../../../../concepts/security/index.md#authorization).

1. Install Istio with a custom trust domain and mutual TLS enabled.

```bash
$ istioctl install --set profile=demo --set meshConfig.trustDomain=old-td
```

1. Deploy the [httpbin](https://github.com/istio/istio/tree/8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99/samples/httpbin) sample in the `default` namespace
 and the [curl](https://github.com/istio/istio/tree/8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99/samples/curl) sample in the `default` and `curl-allow` namespaces:

```bash
$ kubectl label namespace default istio-injection=enabled
$ kubectl apply -f @samples/httpbin/httpbin.yaml@
$ kubectl apply -f @samples/curl/curl.yaml@
$ kubectl create namespace curl-allow
$ kubectl label namespace curl-allow istio-injection=enabled
$ kubectl apply -f @samples/curl/curl.yaml@ -n curl-allow
```

1. Apply the authorization policy below to deny all requests to `httpbin` except from `curl` in the `curl-allow` namespace.

```bash
$ kubectl apply -f - <<EOF
apiVersion: security.istio.io/v1
kind: AuthorizationPolicy
metadata:
  name: service-httpbin.default.svc.cluster.local
  namespace: default
spec:
  rules:
  - from:
    - source:
        principals:
        - old-td/ns/curl-allow/sa/curl
    to:
    - operation:
        methods:
        - GET
  selector:
    matchLabels:
      app: httpbin
---
EOF
```

    Notice that it may take tens of seconds for the authorization policy to be propagated to the sidecars.

1. Verify that requests to `httpbin` from:

    * `curl` in the `default` namespace are denied.

```bash
$ kubectl exec "$(kubectl get pod -l app=curl -o jsonpath={.items..metadata.name})" -c curl -- curl http://httpbin.default:8000/ip -sS -o /dev/null -w "%{http_code}\n"
403
```

    * `curl` in the `curl-allow` namespace are allowed.

```bash
$ kubectl exec "$(kubectl -n curl-allow get pod -l app=curl -o jsonpath={.items..metadata.name})" -c curl -n curl-allow -- curl http://httpbin.default:8000/ip -sS -o /dev/null -w "%{http_code}\n"
200
```

## Migrate trust domain without trust domain aliases

1. Install Istio with a new trust domain.

```bash
$ istioctl install --set profile=demo --set meshConfig.trustDomain=new-td
```

1. Redeploy istiod to pick up the trust domain changes.

```bash
$ kubectl rollout restart deployment -n istio-system istiod
```

    Istio mesh is now running with a new trust domain, `new-td`.

1. Redeploy the `httpbin` and `curl` applications to pick up changes from the new Istio control plane.

```bash
$ kubectl delete pod --all
```

```bash
$ kubectl delete pod --all -n curl-allow
```

1. Verify that requests to `httpbin` from both `curl` in `default` namespace and `curl-allow` namespace are denied.

```bash
$ kubectl exec "$(kubectl get pod -l app=curl -o jsonpath={.items..metadata.name})" -c curl -- curl http://httpbin.default:8000/ip -sS -o /dev/null -w "%{http_code}\n"
403
```

```bash
$ kubectl exec "$(kubectl -n curl-allow get pod -l app=curl -o jsonpath={.items..metadata.name})" -c curl -n curl-allow -- curl http://httpbin.default:8000/ip -sS -o /dev/null -w "%{http_code}\n"
403
```

    This is because we specified an authorization policy that deny all requests to `httpbin`, except the ones
    the `old-td/ns/curl-allow/sa/curl` identity, which is the old identity of the `curl` application in `curl-allow` namespace.
    When we migrated to a new trust domain above, i.e. `new-td`, the identity of this `curl` application is now `new-td/ns/curl-allow/sa/curl`,
    which is not the same as `old-td/ns/curl-allow/sa/curl`. Therefore, requests from the `curl` application in `curl-allow` namespace
    to `httpbin` were allowed before are now being denied. Prior to Istio 1.4, the only way to make this work is to change the authorization
    policy manually. In Istio 1.4, we introduce an easy way, as shown below.

## Migrate trust domain with trust domain aliases

1. Install Istio with a new trust domain and trust domain aliases.

```bash
$ cat <<EOF > ./td-installation.yaml
apiVersion: install.istio.io/v1alpha1
kind: IstioOperator
spec:
  meshConfig:
    trustDomain: new-td
    trustDomainAliases:
      - old-td
EOF
$ istioctl install --set profile=demo -f td-installation.yaml -y
```

1. Without changing the authorization policy, verify that requests to `httpbin` from:

    * `curl` in the `default` namespace are denied.

```bash
$ kubectl exec "$(kubectl get pod -l app=curl -o jsonpath={.items..metadata.name})" -c curl -- curl http://httpbin.default:8000/ip -sS -o /dev/null -w "%{http_code}\n"
403
```

    * `curl` in the `curl-allow` namespace are allowed.

```bash
$ kubectl exec "$(kubectl -n curl-allow get pod -l app=curl -o jsonpath={.items..metadata.name})" -c curl -n curl-allow -- curl http://httpbin.default:8000/ip -sS -o /dev/null -w "%{http_code}\n"
200
```

## Best practices

Starting from Istio 1.4, when writing authorization policy, you should consider using the value `cluster.local` as the
trust domain part in the policy. For example, instead of `old-td/ns/curl-allow/sa/curl`, it should be `cluster.local/ns/curl-allow/sa/curl`.
Notice that in this case, `cluster.local` is not the Istio mesh trust domain (the trust domain is still `old-td`). However,
in authorization policy, `cluster.local` is a pointer that points to the current trust domain, i.e. `old-td` (and later `new-td`), as well as its aliases.
By using `cluster.local` in the authorization policy, when you migrate to a new trust domain, Istio will detect this and treat the new trust domain
as the old trust domain without you having to include the aliases.

## Clean up

```bash
$ kubectl delete authorizationpolicy service-httpbin.default.svc.cluster.local
$ kubectl delete deploy httpbin; kubectl delete service httpbin; kubectl delete serviceaccount httpbin
$ kubectl delete deploy curl; kubectl delete service curl; kubectl delete serviceaccount curl
$ istioctl uninstall --purge -y
$ kubectl delete namespace curl-allow istio-system
$ rm ./td-installation.yaml
```
