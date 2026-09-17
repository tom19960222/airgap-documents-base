---
collection: cilium
version: "1.16.7"
title: "Ingress and Network Policy Example"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/network/servicemesh/ingress-and-network-policy.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

<a id="gs_ingress_and_network_policy"></a>

# Ingress and Network Policy Example

This example uses the same configuration as the base HTTP Ingress example, using
the ``bookinfo`` demo microservices app from the Istio project, and then adds
CiliumNetworkPolicy on the top.

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

<a id="gs_basic_ingress_policy"></a>

Included file `Documentation/network/servicemesh/basic-ingress.rst`:

.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

## Deploy the First Ingress

You'll find the example Ingress definition in ``basic-ingress.yaml``.

.. literalinclude:: ../../../examples/kubernetes/servicemesh/basic-ingress.yaml

.. parsed-literal::

   $ kubectl apply -f \ |SCM_WEB|\/examples/kubernetes/servicemesh/basic-ingress.yaml

This example routes requests for the path ``/details`` to the ``details`` service,
and ``/`` to the ``productpage`` service.

Getting the list of services, you'll see a LoadBalancer service is automatically
created for this ingress. Your cloud provider will automatically provision an
external IP address, but it may take around 30 seconds.

```shell-session
# For dedicated load balancer mode
$ kubectl get svc
NAME                           TYPE           CLUSTER-IP       EXTERNAL-IP     PORT(S)        AGE
cilium-ingress-basic-ingress   LoadBalancer   10.98.169.125    10.98.169.125   80:32478/TCP   2m11s
details                        ClusterIP      10.102.131.226   <none>          9080/TCP       2m15s
kubernetes                     ClusterIP      10.96.0.1        <none>          443/TCP        10m
productpage                    ClusterIP      10.97.231.139    <none>          9080/TCP       2m15s
ratings                        ClusterIP      10.108.152.42    <none>          9080/TCP       2m15s
reviews                        ClusterIP      10.111.145.160   <none>          9080/TCP       2m15s

# For shared load balancer mode
$ kubectl get services -n kube-system cilium-ingress
NAME             TYPE           CLUSTER-IP      EXTERNAL-IP     PORT(S)                      AGE
cilium-ingress   LoadBalancer   10.98.169.125   10.98.169.125   80:32690/TCP,443:31566/TCP   18m
```

The external IP address should also be populated into the Ingress:

```shell-session
$ kubectl get ingress
NAME            CLASS    HOSTS   ADDRESS         PORTS   AGE
basic-ingress   cilium   *       10.98.169.125   80      97s
```

> **Note:**
> Some providers e.g. EKS use a fully-qualified domain name rather than an IP address.

Confirm that your Ingress is working:

```shell-session
$ HTTP_INGRESS=$(kubectl get ingress basic-ingress -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
$ curl --fail -s http://"$HTTP_INGRESS"/details/1 | jq
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
```

Included file `Documentation/network/servicemesh/external-ingress-policy.rst`:

.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

# External Lock-down Policy

By default, all the external traffic is allowed. Let's apply a `CiliumNetworkPolicy` to lock down external traffic.

.. literalinclude:: ../../../examples/kubernetes/servicemesh/policy/external-lockdown.yaml

.. parsed-literal::

   $ kubectl apply -f \ |SCM_WEB|\/examples/kubernetes/servicemesh/policy/external-lockdown.yaml

With this policy applied, any request originating from outside the cluster will be rejected with a ``403 Forbidden``

```shell-session
$ curl --fail -v http://"$HTTP_INGRESS"/details/1
*   Trying 172.18.255.194:80...
* Connected to 172.18.255.194 (172.18.255.194) port 80
> GET /details/1 HTTP/1.1
> Host: 172.18.255.194
> User-Agent: curl/8.6.0
> Accept: */*
>
< HTTP/1.1 403 Forbidden
< content-length: 15
< content-type: text/plain
< date: Thu, 29 Feb 2024 12:59:54 GMT
< server: envoy
* The requested URL returned error: 403
* Closing connection
curl: (22) The requested URL returned error: 403

# Capture hubble flows in another terminal
$ kubectl --namespace=kube-system exec -i -t cilium-xjl4x -- hubble observe -f --identity ingress
Defaulted container "cilium-agent" out of: cilium-agent, config (init), mount-cgroup (init), apply-sysctl-overwrites (init), mount-bpf-fs (init), wait-for-node-init (init), clean-cilium-state (init), install-cni-binaries (init)
Feb 29 13:00:29.389: 172.18.0.1:53866 (ingress) -> kube-system/cilium-ingress:80 (world) http-request DROPPED (HTTP/1.1 GET http://172.18.255.194/details/1)
Feb 29 13:00:29.389: 172.18.0.1:53866 (ingress) <- kube-system/cilium-ingress:80 (world) http-response FORWARDED (HTTP/1.1 403 0ms (GET http://172.18.255.194/details/1))
```

Let's check if in-cluster traffic to the Ingress endpoint is still allowed:

.. parsed-literal::

   # The test-application.yaml contains a client pod with curl available
   $ kubectl apply -f \ |SCM_WEB|\/examples/kubernetes/servicemesh/envoy/test-application.yaml
   $ kubectl exec -it deployment/client -- curl -s http://$HTTP_INGRESS/details/1
   {"id":1,"author":"William Shakespeare","year":1595,"type":"paperback","pages":200,"publisher":"PublisherA","language":"English","ISBN-10":"1234567890","ISBN-13":"123-1234567890"}%

Another common use case is to allow only a specific set of IP addresses to access the Ingress. This can be achieved via
the below policy

.. literalinclude:: ../../../examples/kubernetes/servicemesh/policy/allow-ingress-cidr.yaml

.. parsed-literal::

   $ kubectl apply -f \ |SCM_WEB|\/examples/kubernetes/servicemesh/policy/allow-ingress-cidr.yaml

```shell-session
$ curl -s --fail http://"$HTTP_INGRESS"/details/1
{"id":1,"author":"William Shakespeare","year":1595,"type":"paperback","pages":200,"publisher":"PublisherA","language":"English","ISBN-10":"1234567890","ISBN-13":"123-1234567890"}
```

Included file `Documentation/network/servicemesh/default-deny-ingress-policy.rst`:

.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

# Default Deny Ingress Policy

Let's apply a `CiliumClusterwideNetworkPolicy` to deny all traffic by default:

.. literalinclude:: ../../../examples/kubernetes/servicemesh/policy/default-deny.yaml

.. parsed-literal::

   $ kubectl apply -f \ |SCM_WEB|\/examples/kubernetes/servicemesh/policy/default-deny.yaml

With this policy applied, the request to the ``/details`` endpoint will be denied for external and in-cluster traffic.

```shell-session
$ curl --fail -v http://"$HTTP_INGRESS"/details/1
*   Trying 172.19.255.194:80...
* Connected to 172.19.255.194 (172.19.255.194) port 80
> GET /details/1 HTTP/1.1
> Host: 172.19.255.194
> User-Agent: curl/8.6.0
> Accept: */*
>
< HTTP/1.1 403 Forbidden
< content-length: 15
< content-type: text/plain
< date: Sun, 17 Mar 2024 13:52:38 GMT
< server: envoy
* The requested URL returned error: 403
* Closing connection
curl: (22) The requested URL returned error: 403

# Capture hubble flows in another terminal
$ kubectl --namespace=kube-system exec -i -t cilium-xjl4x -- hubble observe -f --identity ingress
Defaulted container "cilium-agent" out of: cilium-agent, config (init), mount-cgroup (init), apply-sysctl-overwrites (init), mount-bpf-fs (init), wait-for-node-init (init), clean-cilium-state (init), install-cni-binaries (init)
Mar 17 13:56:00.709: 172.19.0.1:34104 (ingress) -> default/cilium-ingress-basic-ingress:80 (world) http-request DROPPED (HTTP/1.1 GET http://172.19.255.194/details/1)
Mar 17 13:56:00.709: 172.19.0.1:34104 (ingress) <- default/cilium-ingress-basic-ingress:80 (world) http-response FORWARDED (HTTP/1.1 403 0ms (GET http://172.19.255.194/details/1))
```

Now let's check if in-cluster traffic to the same endpoint is denied:

.. parsed-literal::

   # The test-application.yaml contains a client pod with curl available
   $ kubectl apply -f \ |SCM_WEB|\/examples/kubernetes/servicemesh/envoy/test-application.yaml
   $ kubectl exec -it deployment/client -- curl -s http://$HTTP_INGRESS/details/1
   Access denied

The next step is to allow ingress traffic to the ``/details`` endpoint:

.. literalinclude:: ../../../examples/kubernetes/servicemesh/policy/allow-ingress-cluster.yaml

.. parsed-literal::

   $ kubectl apply -f \ |SCM_WEB|\/examples/kubernetes/servicemesh/policy/allow-ingress-cluster.yaml

```shell-session
$ curl -s --fail http://"$HTTP_INGRESS"/details/1
{"id":1,"author":"William Shakespeare","year":1595,"type":"paperback","pages":200,"publisher":"PublisherA","language":"English","ISBN-10":"1234567890","ISBN-13":"123-1234567890"}
$ kubectl exec -it deployment/client -- curl -s http://$HTTP_INGRESS/details/1
{"id":1,"author":"William Shakespeare","year":1595,"type":"paperback","pages":200,"publisher":"PublisherA","language":"English","ISBN-10":"1234567890","ISBN-13":"123-1234567890"}
```

NetworkPolicy that selects ``reserved:ingress`` and allows egress
to specific identities could also be used. But in general, it's probably more
reliable to allow all traffic from the ``reserved:ingress`` identity to all
``cluster`` identities, given that Cilium Ingress is part of the networking
infrastructure.
