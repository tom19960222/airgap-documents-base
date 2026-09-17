---
collection: istio
version: "1.24"
title: "JWT Token"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/tasks/security/authorization/authz-jwt/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Shows how to set up access control for JWT token."
---
This task shows you how to set up an Istio authorization policy to enforce access
based on a JSON Web Token (JWT). An Istio authorization policy supports both string typed
and list-of-string typed JWT claims.

## Before you begin

Before you begin this task, do the following:

* Complete the [Istio end user authentication task](../../authentication/authn-policy/index.md#end-user-authentication).

* Read the [Istio authorization concepts](../../../../concepts/security/index.md#authorization).

* Install Istio using [Istio installation guide](../../../../setup/install/istioctl/index.md).

* Deploy two workloads: `httpbin` and `curl`. Deploy these in one namespace,
  for example `foo`. Both workloads run with an Envoy proxy in front of each.
  Deploy the example namespace and workloads using these commands:

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

## Allow requests with valid JWT and list-typed claims

1. The following command creates the `jwt-example` request authentication policy
   for the `httpbin` workload in the `foo` namespace. This policy for `httpbin` workload
   accepts a JWT issued by `testing@secure.istio.io`:

```bash
$ kubectl apply -f - <<EOF
apiVersion: security.istio.io/v1
kind: RequestAuthentication
metadata:
  name: "jwt-example"
  namespace: foo
spec:
  selector:
    matchLabels:
      app: httpbin
  jwtRules:
  - issuer: "testing@secure.istio.io"
    jwksUri: "https://raw.githubusercontent.com/istio/istio/8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99/security/tools/jwt/samples/jwks.json"
EOF
```

1. Verify that a request with an invalid JWT is denied:

```bash
$ kubectl exec "$(kubectl get pod -l app=curl -n foo -o jsonpath={.items..metadata.name})" -c curl -n foo -- curl "http://httpbin.foo:8000/headers" -sS -o /dev/null -H "Authorization: Bearer invalidToken" -w "%{http_code}\n"
401
```

1. Verify that a request without a JWT is allowed because there is no authorization policy:

```bash
$ kubectl exec "$(kubectl get pod -l app=curl -n foo -o jsonpath={.items..metadata.name})" -c curl -n foo -- curl "http://httpbin.foo:8000/headers" -sS -o /dev/null -w "%{http_code}\n"
200
```

1. The following command creates the `require-jwt` authorization policy for the `httpbin` workload in the `foo` namespace.
   The policy requires all requests to the `httpbin` workload to have a valid JWT with
   `requestPrincipal` set to `testing@secure.istio.io/testing@secure.istio.io`.
   Istio constructs the `requestPrincipal` by combining the `iss` and `sub` of the JWT token
   with a `/` separator as shown:

```bash
$ kubectl apply -f - <<EOF
apiVersion: security.istio.io/v1
kind: AuthorizationPolicy
metadata:
  name: require-jwt
  namespace: foo
spec:
  selector:
    matchLabels:
      app: httpbin
  action: ALLOW
  rules:
  - from:
    - source:
       requestPrincipals: ["testing@secure.istio.io/testing@secure.istio.io"]
EOF
```

1. Get the JWT that sets the `iss` and `sub` keys to the same value, `testing@secure.istio.io`.
   This causes Istio to generate the attribute `requestPrincipal` with the value `testing@secure.istio.io/testing@secure.istio.io`:

```bash
$ TOKEN=$(curl https://raw.githubusercontent.com/istio/istio/8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99/security/tools/jwt/samples/demo.jwt -s) && echo "$TOKEN" | cut -d '.' -f2 - | base64 --decode
{"exp":4685989700,"foo":"bar","iat":1532389700,"iss":"testing@secure.istio.io","sub":"testing@secure.istio.io"}
```

1. Verify that a request with a valid JWT is allowed:

```bash
$ kubectl exec "$(kubectl get pod -l app=curl -n foo -o jsonpath={.items..metadata.name})" -c curl -n foo -- curl "http://httpbin.foo:8000/headers" -sS -o /dev/null -H "Authorization: Bearer $TOKEN" -w "%{http_code}\n"
200
```

1. Verify that a request without a JWT is denied:

```bash
$ kubectl exec "$(kubectl get pod -l app=curl -n foo -o jsonpath={.items..metadata.name})" -c curl -n foo -- curl "http://httpbin.foo:8000/headers" -sS -o /dev/null -w "%{http_code}\n"
403
```

1. The following command updates the `require-jwt` authorization policy to also require
   the JWT to have a claim named `groups` containing the value `group1`:

```bash
$ kubectl apply -f - <<EOF
apiVersion: security.istio.io/v1
kind: AuthorizationPolicy
metadata:
  name: require-jwt
  namespace: foo
spec:
  selector:
    matchLabels:
      app: httpbin
  action: ALLOW
  rules:
  - from:
    - source:
       requestPrincipals: ["testing@secure.istio.io/testing@secure.istio.io"]
    when:
    - key: request.auth.claims[groups]
      values: ["group1"]
EOF
```

> **Warning:**
>
> Don't include quotes in the `request.auth.claims` field unless the claim itself has quotes in it.

1. Get the JWT that sets the `groups` claim to a list of strings: `group1` and `group2`:

```bash
$ TOKEN_GROUP=$(curl https://raw.githubusercontent.com/istio/istio/8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99/security/tools/jwt/samples/groups-scope.jwt -s) && echo "$TOKEN_GROUP" | cut -d '.' -f2 - | base64 --decode
{"exp":3537391104,"groups":["group1","group2"],"iat":1537391104,"iss":"testing@secure.istio.io","scope":["scope1","scope2"],"sub":"testing@secure.istio.io"}
```

1. Verify that a request with the JWT that includes `group1` in the `groups` claim is allowed:

```bash
$ kubectl exec "$(kubectl get pod -l app=curl -n foo -o jsonpath={.items..metadata.name})" -c curl -n foo -- curl "http://httpbin.foo:8000/headers" -sS -o /dev/null -H "Authorization: Bearer $TOKEN_GROUP" -w "%{http_code}\n"
200
```

1. Verify that a request with a JWT, which doesn’t have the `groups` claim is rejected:

```bash
$ kubectl exec "$(kubectl get pod -l app=curl -n foo -o jsonpath={.items..metadata.name})" -c curl -n foo -- curl "http://httpbin.foo:8000/headers" -sS -o /dev/null -H "Authorization: Bearer $TOKEN" -w "%{http_code}\n"
403
```

## Clean up

Remove the namespace `foo`:

```bash
$ kubectl delete namespace foo
```
