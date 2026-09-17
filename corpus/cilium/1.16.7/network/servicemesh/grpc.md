---
collection: cilium
version: "1.16.7"
title: "Ingress gRPC Example"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/network/servicemesh/grpc.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

<a id="gs_ingress_grpc"></a>

# Ingress gRPC Example

The example ingress configuration in ``grpc-ingress.yaml`` shows how to route
gRPC traffic to backend services.

## Deploy the Demo App

For this demo we will use [GCP's microservices demo app](https://github.com/GoogleCloudPlatform/microservices-demo).

```shell-session
$ kubectl apply -f https://raw.githubusercontent.com/GoogleCloudPlatform/microservices-demo/main/release/kubernetes-manifests.yaml
```

Since gRPC is binary-encoded, you also need the proto definitions for the gRPC
services in order to make gRPC requests. Download this for the demo app:

```shell-session
$ curl -o demo.proto https://raw.githubusercontent.com/GoogleCloudPlatform/microservices-demo/main/protos/demo.proto
```

## Deploy GRPC Ingress

You'll find the example Ingress definition in ``examples/kubernetes/servicemesh/grpc-ingress.yaml``.

.. literalinclude:: ../../../examples/kubernetes/servicemesh/grpc-ingress.yaml

.. parsed-literal::

   $ kubectl apply -f \ |SCM_WEB|\/examples/kubernetes/servicemesh/grpc-ingress.yaml

This defines paths for requests to be routed to the ``productcatalogservice`` and
``currencyservice`` microservices.

Just as in the previous HTTP Ingress Example, this creates a LoadBalancer service,
and it may take a little while for your cloud provider to provision an external
IP address.

```shell-session
$ kubectl get ingress
NAME           CLASS    HOSTS   ADDRESS         PORTS   AGE
grpc-ingress   cilium   *       10.111.109.99   80      3s
```

## Make gRPC Requests to Backend Services

To issue client gRPC requests you can use [grpcurl](https://github.com/fullstorydev/grpcurl#binaries).

```shell-session
$ GRPC_INGRESS=$(kubectl get ingress grpc-ingress -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
# To access the currency service:
$ grpcurl -plaintext -proto ./demo.proto $GRPC_INGRESS:80 hipstershop.CurrencyService/GetSupportedCurrencies
#To access the product catalog service:
$ grpcurl -plaintext -proto ./demo.proto $GRPC_INGRESS:80 hipstershop.ProductCatalogService/ListProducts
```
