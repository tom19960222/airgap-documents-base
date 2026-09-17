---
collection: istio
version: "1.24"
title: "Configure Istio Ingress Gateway"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/examples/microservices-istio/istio-ingress-gateway/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
Until now, you used a Kubernetes Ingress to access your application from the
outside. In this module, you configure the traffic to enter through an Istio
ingress gateway, in order to apply Istio control on traffic to your microservices.

1.  Store the name of your namespace in the `NAMESPACE` environment variable.
    You will need it to recognize your microservices in the logs:

```bash
$ export NAMESPACE=$(kubectl config view -o jsonpath="{.contexts[?(@.name == \"$(kubectl config current-context)\")].context.namespace}")
$ echo $NAMESPACE
tutorial
```

1.  Create an environment variable for the hostname of the Istio ingress gateway:

```bash
$ export MY_INGRESS_GATEWAY_HOST=istio.$NAMESPACE.bookinfo.com
$ echo $MY_INGRESS_GATEWAY_HOST
istio.tutorial.bookinfo.com
```

1.  Configure an Istio ingress gateway:

```bash
$ kubectl apply -f - <<EOF
apiVersion: networking.istio.io/v1
kind: Gateway
metadata:
  name: bookinfo-gateway
spec:
  selector:
    istio: ingressgateway # use Istio default gateway implementation
  servers:
  - port:
      number: 80
      name: http
      protocol: HTTP
    hosts:
    - $MY_INGRESS_GATEWAY_HOST
---
apiVersion: networking.istio.io/v1
kind: VirtualService
metadata:
  name: bookinfo
spec:
  hosts:
  - $MY_INGRESS_GATEWAY_HOST
  gateways:
  - bookinfo-gateway.$NAMESPACE.svc.cluster.local
  http:
  - match:
    - uri:
        exact: /productpage
    - uri:
        exact: /login
    - uri:
        exact: /logout
    - uri:
        prefix: /static
    route:
    - destination:
        host: productpage
        port:
          number: 9080
EOF
```

1.  Set `INGRESS_HOST` and `INGRESS_PORT` using the instructions in the
    [Determining the Ingress IP and ports](../../../tasks/traffic-management/ingress/ingress-control/index.md#determining-the-ingress-ip-and-ports) section.

1.  Add the output of this command to your `/etc/hosts` file:

```bash
$ echo $INGRESS_HOST $MY_INGRESS_GATEWAY_HOST
```

1.  Access the application's home page from the command line:

```bash
$ curl -s $MY_INGRESS_GATEWAY_HOST:$INGRESS_PORT/productpage | grep -o "<title>.*</title>"
<title>Simple Bookstore App</title>
```

1.  Paste the output of the following command in your browser address bar:

```bash
$ echo http://$MY_INGRESS_GATEWAY_HOST:$INGRESS_PORT/productpage
```

1.  Simulate real-world user traffic to your application by setting an infinite
    loop in a new terminal window:

```bash
$ while :; do curl -s <output of the previous command> | grep -o "<title>.*</title>"; sleep 1; done
<title>Simple Bookstore App</title>
<title>Simple Bookstore App</title>
<title>Simple Bookstore App</title>
<title>Simple Bookstore App</title>
...
```

1.  Check the graph of your namespace in the Kiali console
    `my-kiali.io/kiali/console`.
    (The `my-kiali.io` URL should be in your `/etc/hosts` file that you set
    [previously](../bookinfo-kubernetes/index.md#update-your-etc-hosts-configuration-file)).

    This time, you can see that traffic arrives from two sources, `unknown` (the
    Kubernetes Ingress) and from `istio-ingressgateway istio-system` (the Istio
    Ingress Gateway).

![Kiali Graph Tab with Istio Ingress Gateway](https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/examples/microservices-istio/istio-ingress-gateway/kiali-ingress-gateway.png)

1.  At this point you can stop sending requests through the Kubernetes Ingress
    and use Istio Ingress Gateway only. Stop the infinite loop (`Ctrl-C` in the
    terminal window) you set in the previous steps.
    In a real production environment, you would update the DNS entry of your
    application to contain the IP of Istio ingress gateway or configure your
    external Load Balancer.

1.  Delete the Kubernetes Ingress resource:

```bash
$ kubectl delete ingress bookinfo
ingress.extensions "bookinfo" deleted
```

1.  In a new terminal window, restart the real-world user traffic simulation as described in the previous steps.

1.  Check your graph in the Kiali console. After about a minute, you will see
    the Istio Ingress Gateway as a single source of traffic for your
    application.

![Kiali Graph Tab with Istio Ingress Gateway as a single source of traffic](https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/examples/microservices-istio/istio-ingress-gateway/kiali-ingress-gateway-only.png)

You are ready to configure [logging with Istio](../logs-istio/index.md).
