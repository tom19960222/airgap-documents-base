---
collection: istio
version: "1.24"
title: "Deploy a sample application"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/ambient/getting-started/deploy-sample-app/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Deploy the Bookinfo sample application."
---
To explore Istio, you will install the sample [Bookinfo application](../../../examples/bookinfo/index.md), composed of four separate microservices used to demonstrate various Istio features.

![Istio's Bookinfo sample application is written in many different languages](https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/ambient/getting-started/deploy-sample-app/bookinfo.svg)

As part of this guide, you'll deploy the Bookinfo application and expose the `productpage` service using an ingress gateway.

## Deploy the Bookinfo application

Start by deploying the application:

```bash
$ kubectl apply -f https://raw.githubusercontent.com/istio/istio/8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99/samples/bookinfo/platform/kube/bookinfo.yaml
$ kubectl apply -f https://raw.githubusercontent.com/istio/istio/8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99/samples/bookinfo/platform/kube/bookinfo-versions.yaml
```

To verify that the application is running, check the status of the pods:

```bash
$ kubectl get pods
NAME                             READY   STATUS    RESTARTS   AGE
details-v1-cf74bb974-nw94k       1/1     Running   0          42s
productpage-v1-87d54dd59-wl7qf   1/1     Running   0          42s
ratings-v1-7c4bbf97db-rwkw5      1/1     Running   0          42s
reviews-v1-5fd6d4f8f8-66j45      1/1     Running   0          42s
reviews-v2-6f9b55c5db-6ts96      1/1     Running   0          42s
reviews-v3-7d99fd7978-dm6mx      1/1     Running   0          42s
```

To access the `productpage` service from outside the cluster, you need to configure an ingress gateway.

## Deploy and configure the ingress gateway

You will use the Kubernetes Gateway API to deploy a gateway called `bookinfo-gateway`:

```bash
$ kubectl apply -f https://raw.githubusercontent.com/istio/istio/8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99/samples/bookinfo/gateway-api/bookinfo-gateway.yaml
```

By default, Istio creates a `LoadBalancer` service for a gateway. As you will access this gateway by a tunnel, you don't need a load balancer. Change the service type to `ClusterIP` by annotating the gateway:

```bash
$ kubectl annotate gateway bookinfo-gateway networking.istio.io/service-type=ClusterIP --namespace=default
```

To check the status of the gateway, run:

```bash
$ kubectl get gateway
NAME               CLASS   ADDRESS                                            PROGRAMMED   AGE
bookinfo-gateway   istio   bookinfo-gateway-istio.default.svc.cluster.local   True         42s
```

Wait for the gateway to show as programmed before continuing.

## Access the application

You will connect to the Bookinfo `productpage` service through the gateway you just provisioned. To access the gateway, you need to use the `kubectl port-forward` command:

```bash
$ kubectl port-forward svc/bookinfo-gateway-istio 8080:80
```

Open your browser and navigate to `http://localhost:8080/productpage` to view the Bookinfo application.

![Bookinfo Application](https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/ambient/getting-started/deploy-sample-app/bookinfo-browser.png)

If you refresh the page, you should see the display of the book ratings changing as the requests are distributed across the different versions of the `reviews` service.

## Next steps

[Continue to the next section](../secure-and-visualize/index.md) to add the application to the mesh, and learn how to secure and visualize the communication between the applications.
