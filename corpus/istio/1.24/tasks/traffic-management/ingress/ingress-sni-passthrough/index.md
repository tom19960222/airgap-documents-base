---
collection: istio
version: "1.24"
title: "Ingress Gateway without TLS Termination"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/tasks/traffic-management/ingress/ingress-sni-passthrough/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Describes how to configure SNI passthrough for an ingress gateway."
---
The [Securing Gateways with HTTPS](../secure-ingress/index.md) task describes how to configure HTTPS
ingress access to an HTTP service. This example describes how to configure HTTPS ingress access to an HTTPS service,
i.e., configure an ingress gateway to perform SNI passthrough, instead of TLS termination on incoming requests.

The example HTTPS service used for this task is a simple [NGINX](https://www.nginx.com) server.
In the following steps you first deploy the NGINX service in your Kubernetes cluster.
Then you configure a gateway to provide ingress access to the service via host `nginx.example.com`.

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

> **Warning:**
>
> This document configures Istio using Gateway API features that are
> [experimental](https://gateway-api.sigs.k8s.io/geps/overview/#status)
> Before using the Gateway API instructions, make sure to:
>
> 1) Install the **experimental version** of the Gateway API CRDs:
>
>
>
> ```bash
> $ kubectl kustomize "github.com/kubernetes-sigs/gateway-api/config/crd/experimental?ref=[k8s_gateway_api_version]" | kubectl apply -f -
> ```
>
>
>
> 2) Configure Istio to read the alpha Gateway API resources by setting the `PILOT_ENABLE_ALPHA_GATEWAY_API` environment
>     variable to `true` when installing Istio:
>
>
>
> ```bash
> $ istioctl install --set values.pilot.env.PILOT_ENABLE_ALPHA_GATEWAY_API=true --set profile=minimal -y
> ```

## Before you begin

Setup Istio by following the instructions in the [Installation guide](../../../../setup/_index.md).

## Generate client and server certificates and keys

For this task you can use your favorite tool to generate certificates and keys. The commands below use
[openssl](https://man.openbsd.org/openssl.1):

1.  Create a root certificate and private key to sign the certificate for your services:

```bash
$ mkdir example_certs
$ openssl req -x509 -sha256 -nodes -days 365 -newkey rsa:2048 -subj '/O=example Inc./CN=example.com' -keyout example_certs/example.com.key -out example_certs/example.com.crt
```

1.  Create a certificate and a private key for `nginx.example.com`:

```bash
$ openssl req -out example_certs/nginx.example.com.csr -newkey rsa:2048 -nodes -keyout example_certs/nginx.example.com.key -subj "/CN=nginx.example.com/O=some organization"
$ openssl x509 -req -sha256 -days 365 -CA example_certs/example.com.crt -CAkey example_certs/example.com.key -set_serial 0 -in example_certs/nginx.example.com.csr -out example_certs/nginx.example.com.crt
```

## Deploy an NGINX server

1. Create a Kubernetes [Secret](https://kubernetes.io/docs/concepts/configuration/secret/) to hold the server's
   certificate.

```bash
$ kubectl create secret tls nginx-server-certs \
  --key example_certs/nginx.example.com.key \
  --cert example_certs/nginx.example.com.crt
```

1.  Create a configuration file for the NGINX server:

```bash
$ cat <<\EOF > ./nginx.conf
events {
}

http {
  log_format main '$remote_addr - $remote_user [$time_local]  $status '
  '"$request" $body_bytes_sent "$http_referer" '
  '"$http_user_agent" "$http_x_forwarded_for"';
  access_log /var/log/nginx/access.log main;
  error_log  /var/log/nginx/error.log;

  server {
    listen 443 ssl;

    root /usr/share/nginx/html;
    index index.html;

    server_name nginx.example.com;
    ssl_certificate /etc/nginx-server-certs/tls.crt;
    ssl_certificate_key /etc/nginx-server-certs/tls.key;
  }
}
EOF
```

1.  Create a Kubernetes [ConfigMap](https://kubernetes.io/docs/tasks/configure-pod-container/configure-pod-configmap/)
to hold the configuration of the NGINX server:

```bash
$ kubectl create configmap nginx-configmap --from-file=nginx.conf=./nginx.conf
```

1.  Deploy the NGINX server:

```bash
$ cat <<EOF | kubectl apply -f -
apiVersion: v1
kind: Service
metadata:
  name: my-nginx
  labels:
    run: my-nginx
spec:
  ports:
  - port: 443
    protocol: TCP
  selector:
    run: my-nginx
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-nginx
spec:
  selector:
    matchLabels:
      run: my-nginx
  replicas: 1
  template:
    metadata:
      labels:
        run: my-nginx
        sidecar.istio.io/inject: "true"
    spec:
      containers:
      - name: my-nginx
        image: nginx
        ports:
        - containerPort: 443
        volumeMounts:
        - name: nginx-config
          mountPath: /etc/nginx
          readOnly: true
        - name: nginx-server-certs
          mountPath: /etc/nginx-server-certs
          readOnly: true
      volumes:
      - name: nginx-config
        configMap:
          name: nginx-configmap
      - name: nginx-server-certs
        secret:
          secretName: nginx-server-certs
EOF
```

1.  To test that the NGINX server was deployed successfully, send a request to the server from its sidecar proxy
    without checking the server's certificate (use the `-k` option of `curl`). Ensure that the server's certificate is
    printed correctly, i.e., `common name (CN)` is equal to `nginx.example.com`.

```bash
$ kubectl exec "$(kubectl get pod  -l run=my-nginx -o jsonpath={.items..metadata.name})" -c istio-proxy -- curl -sS -v -k --resolve nginx.example.com:443:127.0.0.1 https://nginx.example.com
...
SSL connection using TLSv1.2 / ECDHE-RSA-AES256-GCM-SHA384
ALPN, server accepted to use http/1.1
Server certificate:
  subject: CN=nginx.example.com; O=some organization
  start date: May 27 14:18:47 2020 GMT
  expire date: May 27 14:18:47 2021 GMT
  issuer: O=example Inc.; CN=example.com
  SSL certificate verify result: unable to get local issuer certificate (20), continuing anyway.

> GET / HTTP/1.1
> User-Agent: curl/7.58.0
> Host: nginx.example.com
...
< HTTP/1.1 200 OK

< Server: nginx/1.17.10
...
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
...
```

## Configure an ingress gateway

1.  Define a `Gateway` exposing port 443 with passthrough TLS mode. This instructs
    the gateway to pass the ingress traffic "as is", without terminating TLS:

**Tabset (config-api):**

**Tab: Istio APIs**

```bash
$ kubectl apply -f - <<EOF
apiVersion: networking.istio.io/v1
kind: Gateway
metadata:
  name: mygateway
spec:
  selector:
    istio: ingressgateway # use istio default ingress gateway
  servers:
  - port:
      number: 443
      name: https
      protocol: HTTPS
    tls:
      mode: PASSTHROUGH
    hosts:
    - nginx.example.com
EOF
```

**Tab: Gateway API**

```bash
$ kubectl apply -f - <<EOF
apiVersion: gateway.networking.k8s.io/v1
kind: Gateway
metadata:
  name: mygateway
spec:
  gatewayClassName: istio
  listeners:
  - name: https
    hostname: "nginx.example.com"
    port: 443
    protocol: TLS
    tls:
      mode: Passthrough
    allowedRoutes:
      namespaces:
        from: All
EOF
```

2)  Configure routes for traffic entering via the `Gateway`:

**Tabset (config-api):**

**Tab: Istio APIs**

```bash
$ kubectl apply -f - <<EOF
apiVersion: networking.istio.io/v1
kind: VirtualService
metadata:
  name: nginx
spec:
  hosts:
  - nginx.example.com
  gateways:
  - mygateway
  tls:
  - match:
    - port: 443
      sniHosts:
      - nginx.example.com
    route:
    - destination:
        host: my-nginx
        port:
          number: 443
EOF
```

**Tab: Gateway API**

```bash
$ kubectl apply -f - <<EOF
apiVersion: gateway.networking.k8s.io/v1alpha2
kind: TLSRoute
metadata:
  name: nginx
spec:
  parentRefs:
  - name: mygateway
  hostnames:
  - "nginx.example.com"
  rules:
  - backendRefs:
    - name: my-nginx
      port: 443
EOF
```

3)  Determine the ingress IP and port:

**Tabset (config-api):**

**Tab: Istio APIs**

Follow the instructions in
[Determining the ingress IP and ports](../ingress-control/index.md#determining-the-ingress-ip-and-ports)
to set the `SECURE_INGRESS_PORT` and `INGRESS_HOST` environment variables.

**Tab: Gateway API**

Use the following commands to set the `SECURE_INGRESS_PORT` and `INGRESS_HOST` environment variables:

```bash
$ kubectl wait --for=condition=programmed gtw mygateway
$ export INGRESS_HOST=$(kubectl get gtw mygateway -o jsonpath='{.status.addresses[0].value}')
$ export SECURE_INGRESS_PORT=$(kubectl get gtw mygateway -o jsonpath='{.spec.listeners[?(@.name=="https")].port}')
```

4)  Access the NGINX service from outside the cluster. Note that the correct certificate is returned by the server and
    it is successfully verified (_SSL certificate verify ok_ is printed).

```bash
$ curl -v --resolve "nginx.example.com:$SECURE_INGRESS_PORT:$INGRESS_HOST" --cacert example_certs/example.com.crt "https://nginx.example.com:$SECURE_INGRESS_PORT"
Server certificate:
  subject: CN=nginx.example.com; O=some organization
  start date: Wed, 15 Aug 2018 07:29:07 GMT
  expire date: Sun, 25 Aug 2019 07:29:07 GMT
  issuer: O=example Inc.; CN=example.com
  SSL certificate verify ok.

  < HTTP/1.1 200 OK
  < Server: nginx/1.15.2
  ...
  <html>
  <head>
  <title>Welcome to nginx!</title>
```

## Cleanup

1.  Delete the gateway configuration and route:

**Tabset (config-api):**

**Tab: Istio APIs**

```bash
$ kubectl delete gateway mygateway
$ kubectl delete virtualservice nginx
```

**Tab: Gateway API**

```bash
$ kubectl delete gtw mygateway
$ kubectl delete tlsroute nginx
```

2)  Remove the NGINX resources and configuration file:

```bash
$ kubectl delete secret nginx-server-certs
$ kubectl delete configmap nginx-configmap
$ kubectl delete service my-nginx
$ kubectl delete deployment my-nginx
$ rm ./nginx.conf
```

1)  Delete the certificates and keys:

```bash
$ rm -rf ./example_certs
```
