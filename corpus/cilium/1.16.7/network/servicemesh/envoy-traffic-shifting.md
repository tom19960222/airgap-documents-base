---
collection: cilium
version: "1.16.7"
title: "L7 Traffic Shifting"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/network/servicemesh/envoy-traffic-shifting.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

<a id="gs_envoy_traffic_shifting"></a>

# L7 Traffic Shifting

Cilium Service Mesh defines a ``CiliumEnvoyConfig`` CRD which allows users
to set the configuration of the Envoy component built into Cilium agents.

This example sets up an Envoy listener which load balances requests
to the helloworld Service by sending 90% of incoming requests to the
backend ``helloworld-v1`` and 10% of incoming requests to the backend
``helloworld-v2``.

## Deploy Test Applications

.. parsed-literal::

   $ kubectl apply -f \ |SCM_WEB|\/examples/kubernetes/servicemesh/envoy/client-helloworld.yaml

The test workloads consist of:

- One client Deployment, ``client``
- Two server Deployments, ``helloworld-v1`` and ``helloworld-v2``

View information about these Pods and the helloworld Service:

```shell-session
$ kubectl get pods --show-labels -o wide
NAME                             READY   STATUS    RESTARTS   AGE     IP           NODE                   NOMINATED NODE   READINESS GATES   LABELS
client-64848f85dd-sjfmb          1/1     Running   0          2m23s   10.0.0.206   cilium-control-plane   <none>           <none>            kind=client,name=client,pod-template-hash=64848f85dd
helloworld-v1-5845f97d6b-gkdtk   1/1     Running   0          2m23s   10.0.0.241   cilium-control-plane   <none>           <none>            app=helloworld,pod-template-hash=5845f97d6b,version=v1
helloworld-v2-7d55d87964-ns9kh   1/1     Running   0          2m23s   10.0.0.251   cilium-control-plane   <none>           <none>            app=helloworld,pod-template-hash=7d55d87964,version=v2

$ kubectl get svc --show-labels
NAME         TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)    AGE   LABELS
helloworld   ClusterIP   10.96.194.77   <none>        5000/TCP   8m27s app=helloworld,service=helloworld
```

## Apply weight-based routing

Make an environment variable with the Pod name for client:

```shell-session
$ export CLIENT=$(kubectl get pods -l name=client -o jsonpath='{.items[0].metadata.name}')
```

Try making several requests to the helloworld Service.

```shell-session
$ for i in {1..10}; do  kubectl exec -it $CLIENT -- curl  helloworld:5000/hello; done
```

The test results are as follows:

```
Hello version: v2, instance: helloworld-v2-7d55d87964-ns9kh
Hello version: v2, instance: helloworld-v2-7d55d87964-ns9kh
Hello version: v2, instance: helloworld-v2-7d55d87964-ns9kh
Hello version: v1, instance: helloworld-v1-5845f97d6b-gkdtk
Hello version: v1, instance: helloworld-v1-5845f97d6b-gkdtk
Hello version: v1, instance: helloworld-v1-5845f97d6b-gkdtk
Hello version: v2, instance: helloworld-v2-7d55d87964-ns9kh
Hello version: v1, instance: helloworld-v1-5845f97d6b-gkdtk
Hello version: v2, instance: helloworld-v2-7d55d87964-ns9kh
Hello version: v1, instance: helloworld-v1-5845f97d6b-gkdtk
```

The test results were as expected. Of the requests sent to the helloworld service,
50% of them were sent to the backend ``helloworld-v1`` and 50% of them were sent to
the backend ``helloworld-v2``.

``CiliumEnvoyConfig`` can be used to load balance traffic destined to one Service to a
group of backend Services. To load balance traffic to the helloworld Service, first create
individual Services for each backend Deployment.

.. parsed-literal::
   $ kubectl apply -f \ |SCM_WEB|\/examples/kubernetes/servicemesh/envoy/helloworld-service-v1-v2.yaml

Apply the ``envoy-helloworld-v1-90-v2-10.yaml`` file, which defines a ``CiliumEnvoyConfig``
to send 90% of traffic to the helloworld-v1 Service backend and 10% of traffic to the helloworld-v2 Service backend:

.. parsed-literal::
   $ kubectl apply -f \ |SCM_WEB|\/examples/kubernetes/servicemesh/envoy/envoy-helloworld-v1-90-v2-10.yaml

View information about these Pods and Services:

```shell-session
$ kubectl get pods --show-labels -o wide
NAME                             READY   STATUS    RESTARTS   AGE     IP           NODE                   NOMINATED NODE   READINESS GATES   LABELS
client-64848f85dd-sjfmb          1/1     Running   0          2m23s   10.0.0.206   cilium-control-plane   <none>           <none>            kind=client,name=client,pod-template-hash=64848f85dd
helloworld-v1-5845f97d6b-gkdtk   1/1     Running   0          2m23s   10.0.0.241   cilium-control-plane   <none>           <none>            app=helloworld,pod-template-hash=5845f97d6b,version=v1
helloworld-v2-7d55d87964-ns9kh   1/1     Running   0          2m23s   10.0.0.251   cilium-control-plane   <none>           <none>            app=helloworld,pod-template-hash=7d55d87964,version=v2

$ kubectl get svc --show-labels
NAME            TYPE        CLUSTER-IP     EXTERNAL-IP   PORT(S)    AGE   LABELS
helloworld      ClusterIP   10.96.194.77   <none>        5000/TCP   16m   app=helloworld,service=helloworld
helloworld-v1   ClusterIP   10.96.0.240    <none>        5000/TCP   4s    app=helloworld,service=helloworld,version=v1
helloworld-v2   ClusterIP   10.96.41.142   <none>        5000/TCP   4s    app=helloworld,service=helloworld,version=v2
```

Included file `Documentation/network/servicemesh/warning.rst`:

> **Note:**
> Note that these Envoy resources are not validated by K8s at all, so
> any errors in the Envoy resources will only be seen by the Cilium
> Agent observing these CRDs. This means that ``kubectl apply`` will
> report success, while parsing and/or installing the resources for the
> node-local Envoy instance may have failed. Currently the only way of
> verifying this is by observing Cilium Agent logs for errors and
> warnings. Additionally, Cilium Agent will print warning logs for any
> conflicting Envoy resources in the cluster.

> **Note:**
> Note that Cilium Ingress Controller will configure required Envoy
> resource under the hood. Please check Cilium Agent logs if you are
> creating Envoy resources explicitly to make sure there is no conflict.

Try making several requests to the helloworld Service again.

```shell-session
$ for i in {1..10}; do  kubectl exec -it $CLIENT -- curl  helloworld:5000/hello; done
```

The test results are as follows:

```
Hello version: v1, instance: helloworld-v1-5845f97d6b-gkdtk
Hello version: v1, instance: helloworld-v1-5845f97d6b-gkdtk
Hello version: v1, instance: helloworld-v1-5845f97d6b-gkdtk
Hello version: v2, instance: helloworld-v2-7d55d87964-ns9kh
Hello version: v1, instance: helloworld-v1-5845f97d6b-gkdtk
Hello version: v1, instance: helloworld-v1-5845f97d6b-gkdtk
Hello version: v1, instance: helloworld-v1-5845f97d6b-gkdtk
Hello version: v1, instance: helloworld-v1-5845f97d6b-gkdtk
Hello version: v1, instance: helloworld-v1-5845f97d6b-gkdtk
Hello version: v1, instance: helloworld-v1-5845f97d6b-gkdtk
```

The test results were as expected. Of the requests sent to the helloworld service,
90% of them were sent to the backend ``helloworld-v1`` and 10% of them were sent to
the backend ``helloworld-v2``.

## Cleaning up

Remove the rules.

.. parsed-literal::

   $ kubectl delete -f \ |SCM_WEB|\/examples/kubernetes/servicemesh/envoy/envoy-helloworld-v1-90-v2-10.yaml

Remove the test application.

.. parsed-literal::

   $ kubectl delete -f \ |SCM_WEB|\/examples/kubernetes/servicemesh/envoy/client-helloworld.yaml
   $ kubectl delete -f \ |SCM_WEB|\/examples/kubernetes/servicemesh/envoy/helloworld-service-v1-v2.yaml
