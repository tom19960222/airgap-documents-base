---
collection: cilium
version: "1.16.7"
title: "L7 Path Translation"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/network/servicemesh/envoy-custom-listener.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

<a id="gs_envoy_custom_listener"></a>

# L7 Path Translation

This example replicates the Prometheus metrics listener which is
already available via the command line option ``--proxy-prometheus-port``.
So the point of this example is not to add new functionality, but to show
how a feature that previously required Cilium Agent code changes can be
implemented with the new Cilium Envoy Config CRD.

## Apply Example CRD

This example adds a new Envoy listener ``envoy-prometheus-metrics-listener``
on the standard Prometheus port (e.g. ``9090``) to each Cilium node, translating
the default Prometheus metrics path ``/metrics`` to Envoy's Prometheus metrics path
``/stats/prometheus``.

Apply this Cilium Envoy Config CRD:

.. parsed-literal::

   $ kubectl apply -f \ |SCM_WEB|\/examples/kubernetes/servicemesh/envoy/envoy-prometheus-metrics-listener.yaml

This version of the ``CiliumClusterwideEnvoyConfig`` CRD is Cluster-scoped,
(i.e., not namespaced), so the name needs to be unique in the cluster,
unless you want to replace a CRD with a new one.

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

```shell-session
$ kubectl logs -n kube-system ds/cilium | grep -E "level=(error|warning)"
```

## Test the Listener Port

Test that the new port is responding to the metrics requests:

```shell-session
$ curl http://<node-IP>:9090/metrics
```

Where ``<node-IP>`` is the IP address of one of your k8s cluster nodes.

## Clean-up

Remove the prometheus listener with:

.. parsed-literal::

   $ kubectl delete -f \ |SCM_WEB|\/examples/kubernetes/servicemesh/envoy/envoy-prometheus-metrics-listener.yaml
