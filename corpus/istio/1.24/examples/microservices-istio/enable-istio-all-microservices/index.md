---
collection: istio
version: "1.24"
title: "Enable Istio on all the microservices"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/examples/microservices-istio/enable-istio-all-microservices/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
Previously, you enabled Istio on a single microservice, `productpage`. You can
proceed to enable Istio on the microservices incrementally to get the Istio
functionality for more microservices. For the purpose of this tutorial, you will
enable Istio on all the remaining microservices in one step.

1.  For the purpose of this tutorial, scale the deployments of the microservices
    down to 1:

```bash
$ kubectl scale deployments --all --replicas 1
```

1.  Redeploy the Bookinfo application, Istio-enabled. The service `productpage` will not be
    redeployed since it already has Istio injected, and its pods will not be
    changed. This time you will use only a single replica of a microservice.

```bash
$ curl -s https://raw.githubusercontent.com/istio/istio/8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99/samples/bookinfo/platform/kube/bookinfo.yaml | istioctl kube-inject -f - | kubectl apply -l app!=reviews -f -
$ curl -s https://raw.githubusercontent.com/istio/istio/8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99/samples/bookinfo/platform/kube/bookinfo.yaml | istioctl kube-inject -f - | kubectl apply -l app=reviews,version=v2 -f -
service/details unchanged
serviceaccount/bookinfo-details unchanged
deployment.apps/details-v1 configured
service/ratings unchanged
serviceaccount/bookinfo-ratings unchanged
deployment.apps/ratings-v1 configured
serviceaccount/bookinfo-reviews unchanged
service/productpage unchanged
serviceaccount/bookinfo-productpage unchanged
deployment.apps/productpage-v1 configured
deployment.apps/reviews-v2 configured
```

1.  Access the application's webpage several times. Note that Istio was added
    **transparently**, the original application did not change. It was added on
    the fly, without the need to undeploy and redeploy the whole application.

1.  Check the application pods and verify that now each pod has two containers.
    One container is the microservice itself, the other is the sidecar proxy
    attached to it:

```bash
$ kubectl get pods
details-v1-58c68b9ff-kz9lf        2/2       Running   0          2m
productpage-v1-59b4f9f8d5-d4prx   2/2       Running   0          2m
ratings-v1-b7b7fbbc9-sggxf        2/2       Running   0          2m
reviews-v2-dfbcf859c-27dvk        2/2       Running   0          2m
curl-88ddbcfdd-cc85s              1/1       Running   0          7h
```

1.  Access the Istio dashboard using the custom URL you set in your `/etc/hosts` file
    [previously](../bookinfo-kubernetes/index.md#update-your-etc-hosts-configuration-file):

```plain
http://my-istio-dashboard.io/dashboard/db/istio-mesh-dashboard
```

1.  In the top left drop-down menu, select _Istio Mesh Dashboard_. Note that now all the services from your namespace
    appear in the list of services.

![Istio Mesh Dashboard](https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/examples/microservices-istio/enable-istio-all-microservices/dashboard-mesh-all.png)

1.  Check some other microservice in _Istio Service Dashboard_, e.g. `ratings` :

![Istio Service Dashboard](https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/examples/microservices-istio/enable-istio-all-microservices/dashboard-ratings.png)

1.  Visualize your application's topology by using the
    [Kiali](https://www.kiali.io) console, which is not a part of Istio, but is
    installed as part of the `demo` configuration.
    Access the dashboard using the custom URL you set in your `/etc/hosts` file
    [previously](../bookinfo-kubernetes/index.md#update-your-etc-hosts-configuration-file):

```plain
http://my-kiali.io/kiali/console
```

    If you installed Kiali as part of the [getting started](../../../setup/getting-started/index.md) instructions, your Kiali console user name is `admin` and the password is `admin`.

1.  Click on the Graph tab and select your namespace in the _Namespace_ drop-down menu in the top level corner.
    In the _Display_ drop-down menu mark the _Traffic Animation_ check box to see some cool traffic animation.

![Kiali Graph Tab, display drop-down menu](https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/examples/microservices-istio/enable-istio-all-microservices/kiali-display-menu.png)

1.  Try different options in the _Edge Labels_ drop-down menu. Hover with the mouse over the nodes and edges of the
    graph. Notice the traffic metrics on the right.

![Kiali Graph Tab, edge labels drop-down menu](https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/examples/microservices-istio/enable-istio-all-microservices/kiali-edge-labels-menu.png)

![Kiali Graph Tab](https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/examples/microservices-istio/enable-istio-all-microservices/kiali-initial.png)

You are ready to
[configure the Istio Ingress Gateway](../istio-ingress-gateway/index.md).
