---
collection: istio
version: "1.24"
title: "JWT claim based routing"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/tasks/security/authentication/jwt-route/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Shows you how to use Istio authentication policy to route requests based on JWT claims."
---
---
---

> **Warning:**
>
> This feature is targeted at developers / expert users and is considered
> [Alpha](https://github.com/istio/community/blob/master/FEATURE-LIFECYCLE.md).

This task shows you how to route requests based on JWT claims on an Istio ingress gateway using the request authentication
and virtual service.

Note: this feature only supports Istio ingress gateway and requires the use of both request authentication and virtual
service to properly validate and route based on JWT claims.

## Before you begin

* Understand Istio [authentication policy](../../../../concepts/security/index.md#authentication-policies) and [virtual service](../../../../concepts/traffic-management/index.md#virtual-services) concepts.

* Install Istio using the [Istio installation guide](../../../../setup/install/istioctl/index.md).

* Deploy a workload, `httpbin` in a namespace, for example `foo`, and expose it through the Istio ingress gateway with this command:

```bash
$ kubectl create ns foo
$ kubectl apply -f <(istioctl kube-inject -f @samples/httpbin/httpbin.yaml@) -n foo
$ kubectl apply -f @samples/httpbin/httpbin-gateway.yaml@ -n foo
```

*  Follow the instructions in
   [Determining the ingress IP and ports](../../../traffic-management/ingress/ingress-control/index.md#determining-the-ingress-ip-and-ports)
   to define the `INGRESS_HOST` and `INGRESS_PORT` environment variables.

* Verify that the `httpbin` workload and ingress gateway are working as expected using this command:

```bash
$ curl "$INGRESS_HOST:$INGRESS_PORT"/headers -s -o /dev/null -w "%{http_code}\n"
200
```

> **Warning:**
>
> If you don’t see the expected output, retry after a few seconds. Caching and propagation overhead can cause a delay.

## Configuring ingress routing based on JWT claims

The Istio ingress gateway supports routing based on authenticated JWT, which is useful for routing based on end user
identity and more secure compared using the unauthenticated HTTP attributes (e.g. path or header).

1. In order to route based on JWT claims, first create the request authentication to enable JWT validation:

```bash
$ kubectl apply -f - <<EOF
apiVersion: security.istio.io/v1
kind: RequestAuthentication
metadata:
  name: ingress-jwt
  namespace: istio-system
spec:
  selector:
    matchLabels:
      istio: ingressgateway
  jwtRules:
  - issuer: "testing@secure.istio.io"
    jwksUri: "https://raw.githubusercontent.com/istio/istio/8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99/security/tools/jwt/samples/jwks.json"
EOF
```

    The request authentication enables JWT validation on the Istio ingress gateway so that the validated JWT claims
    can later be used in the virtual service for routing purposes.

    The request authentication is applied on the ingress gateway because the JWT claim based routing is only supported
    on ingress gateways.

    Note: the request authentication will only check the JWT if it exists in the request. To make the JWT required and
    reject the request if it does not include JWT, apply the authorization policy as specified in the [task](../authn-policy/index.md#require-a-valid-token).

1. Update the virtual service to route based on validated JWT claims:

```bash
$ kubectl apply -f - <<EOF
apiVersion: networking.istio.io/v1
kind: VirtualService
metadata:
  name: httpbin
  namespace: foo
spec:
  hosts:
  - "*"
  gateways:
  - httpbin-gateway
  http:
  - match:
    - uri:
        prefix: /headers
      headers:
        "@request.auth.claims.groups":
          exact: group1
    route:
    - destination:
        port:
          number: 8000
        host: httpbin
EOF
```

    The virtual service uses the reserved header `"@request.auth.claims.groups"` to match with the JWT claim `groups`.
    The prefix `@` denotes it is matching with the metadata derived from the JWT validation and not with HTTP headers.

    Claim of type string, list of string and nested claims are supported. Use the `.` or `[]` as a separator for nested claim
    names. For example, `"@request.auth.claims.name.givenName"` or `"@request.auth.claims[name][givenName]"` matches
    the nested claim `name` and `givenName`, they are equivalent here. When the claim name contains `.`, only `[]` can be used as a separator.

## Validating ingress routing based on JWT claims

1. Validate the ingress gateway returns the HTTP code 404 without JWT:

```bash
$ curl -s -I "http://$INGRESS_HOST:$INGRESS_PORT/headers"
HTTP/1.1 404 Not Found
...
```

    You can also create the authorization policy to explicitly reject the request with HTTP code 403 when JWT is missing.

1. Validate the ingress gateway returns the HTTP code 401 with invalid JWT:

```bash
$ curl -s -I "http://$INGRESS_HOST:$INGRESS_PORT/headers" -H "Authorization: Bearer some.invalid.token"
HTTP/1.1 401 Unauthorized
...
```

    The 401 is returned by the request authentication because the JWT failed the validation.

1. Validate the ingress gateway routes the request with a valid JWT token that includes the claim `groups: group1`:

```bash
$ TOKEN_GROUP=$(curl https://raw.githubusercontent.com/istio/istio/8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99/security/tools/jwt/samples/groups-scope.jwt -s) && echo "$TOKEN_GROUP" | cut -d '.' -f2 - | base64 --decode
{"exp":3537391104,"groups":["group1","group2"],"iat":1537391104,"iss":"testing@secure.istio.io","scope":["scope1","scope2"],"sub":"testing@secure.istio.io"}
```

```bash
$ curl -s -I "http://$INGRESS_HOST:$INGRESS_PORT/headers" -H "Authorization: Bearer $TOKEN_GROUP"
HTTP/1.1 200 OK
...
```

1. Validate the ingress gateway returns the HTTP code 404 with a valid JWT but does not include the claim `groups: group1`:

```bash
$ TOKEN_NO_GROUP=$(curl https://raw.githubusercontent.com/istio/istio/8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99/security/tools/jwt/samples/demo.jwt -s) && echo "$TOKEN_NO_GROUP" | cut -d '.' -f2 - | base64 --decode
{"exp":4685989700,"foo":"bar","iat":1532389700,"iss":"testing@secure.istio.io","sub":"testing@secure.istio.io"}
```

```bash
$ curl -s -I "http://$INGRESS_HOST:$INGRESS_PORT/headers" -H "Authorization: Bearer $TOKEN_NO_GROUP"
HTTP/1.1 404 Not Found
...
```

## Cleanup

* Remove the namespace `foo`:

```bash
$ kubectl delete namespace foo
```

* Remove the request authentication:

```bash
$ kubectl delete requestauthentication ingress-jwt -n istio-system
```
