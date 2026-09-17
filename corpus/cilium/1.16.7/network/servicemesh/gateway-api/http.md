---
collection: cilium
version: "1.16.7"
title: "HTTP Example"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/network/servicemesh/gateway-api/http.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

<a id="gs_gateway_http"></a>

# HTTP Example

In this example, we will deploy a simple HTTP service and expose it to the
Cilium Gateway API.

The demo application is from the ``bookinfo`` demo microservices app from
the Istio project.

Included file `Documentation/network/servicemesh/demo-app.rst`:

## Deploy the Demo App

```shell-session
$ kubectl apply -f https://raw.githubusercontent.com/istio/istio/release-1.11/samples/bookinfo/platform/kube/bookinfo.yaml
```

This is just deploying the demo app, it's not adding any Istio components. You
can confirm that with Cilium Service Mesh there is no Envoy sidecar created
alongside each of the demo app microservices.

```shell-session
$ kubectl get pods
NAME                              READY   STATUS    RESTARTS   AGE
details-v1-5498c86cf5-kjzkj       1/1     Running   0          2m39s
productpage-v1-65b75f6885-ff59g   1/1     Running   0          2m39s
ratings-v1-b477cf6cf-kv7bh        1/1     Running   0          2m39s
reviews-v1-79d546878f-r5bjz       1/1     Running   0          2m39s
reviews-v2-548c57f459-pld2f       1/1     Running   0          2m39s
reviews-v3-6dd79655b9-nhrnh       1/1     Running   0          2m39s
```

> **Note:**
> With the sidecar implementation the output would show 2/2 READY. One for
> the microservice and one for the Envoy sidecar.

## Deploy the Cilium Gateway

You'll find the example Gateway and HTTPRoute definition in ``basic-http.yaml``.

.. literalinclude:: ../../../../examples/kubernetes/gateway/basic-http.yaml

.. parsed-literal::

   $ kubectl apply -f \ |SCM_WEB|\/examples/kubernetes/gateway/basic-http.yaml

The above example creates a Gateway named ``my-gateway`` that listens on port 80.
Two routes are defined, one for ``/details`` to the ``details`` service, and
one for ``/`` to the ``productpage`` service.

Your cloud provider will automatically provision an external IP address for the
gateway, but it may take up to 20 minutes.

```shell-session
$ kubectl get gateway my-gateway
NAME         CLASS    ADDRESS        PROGRAMMED   AGE
my-gateway   cilium   10.100.26.37   True         2d7h
```

> **Note:**
> Some providers e.g. EKS use a fully-qualified domain name rather than an IP address.

## Make HTTP Requests

Now that the Gateway is ready, you can make HTTP requests to the services.

```shell-session
$ GATEWAY=$(kubectl get gateway my-gateway -o jsonpath='{.status.addresses[0].value}')
$ curl --fail -s http://"$GATEWAY"/details/1 | jq
{
  "id": 1,
  "author": "William Shakespeare",
  "year": 1595,
  "type": "paperback",
  "pages": 200,
  "publisher": "PublisherA",
  "language": "English",
  "ISBN-10": "1234567890",
  "ISBN-13": "123-1234567890"
}
$ curl -v -H 'magic: foo' http://"$GATEWAY"\?great\=example
...
<!DOCTYPE html>
<html>
  <head>
    <title>Simple Bookstore App</title>
<meta charset="utf-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">

<!-- Latest compiled and minified CSS -->
<link rel="stylesheet" href="static/bootstrap/css/bootstrap.min.css">

<!-- Optional theme -->
<link rel="stylesheet" href="static/bootstrap/css/bootstrap-theme.min.css">

  </head>
  <body>

<p>
    <h3>Hello! This is a simple bookstore application consisting of three services as shown below</h3>
</p>

<table class="table table-condensed table-bordered table-hover"><tr><th>name</th><td>http://details:9080</td></tr><tr><th>endpoint</th><td>details</td></tr><tr><th>children</th><td><table class="table table-condensed table-bordered table-hover"><tr><th>name</th><th>endpoint</th><th>children</th></tr><tr><td>http://details:9080</td><td>details</td><td></td></tr><tr><td>http://reviews:9080</td><td>reviews</td><td><table class="table table-condensed table-bordered table-hover"><tr><th>name</th><th>endpoint</th><th>children</th></tr><tr><td>http://ratings:9080</td><td>ratings</td><td></td></tr></table></td></tr></table></td></tr></table>

<p>
    <h4>Click on one of the links below to auto generate a request to the backend as a real user or a tester
    </h4>
</p>
<p><a href="/productpage?u=normal">Normal user</a></p>
<p><a href="/productpage?u=test">Test user</a></p>

<!-- Latest compiled and minified JavaScript -->
<script src="static/jquery.min.js"></script>

<!-- Latest compiled and minified JavaScript -->
<script src="static/bootstrap/js/bootstrap.min.js"></script>

  </body>
</html>
```
