---
collection: istio
version: "1.24"
title: "Run Bookinfo with Kubernetes"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/examples/microservices-istio/bookinfo-kubernetes/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
---
---

> **Warning:**
>
> This is work in progress. We will add its sections in pieces. Your feedback is welcome at [discuss.istio.io](https://discuss.istio.io).

This module shows you an application composed of four microservices written in different programming languages: `productpage`, `details`, `ratings` and `reviews`. We call the composed application `Bookinfo`, and you can learn more about it on the
[Bookinfo example](../../bookinfo/index.md) page.

The [Bookinfo example](../../bookinfo/index.md) shows the final state of the application, in which the `reviews` microservice has three versions: `v1`, `v2`, `v3`. In this module, the application only uses the `v1` version of the
`reviews` microservice. The next modules enhance the application by deploying newer versions of the `reviews`
microservice.

## Deploy the application and a testing pod

1.  Set the `MYHOST` environment variable to hold the URL of the application:

```bash
$ export MYHOST=$(kubectl config view -o jsonpath={.contexts..namespace}).bookinfo.com
```

1.  Skim [`bookinfo.yaml`](https://github.com/istio/istio/blob/8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99/samples/bookinfo/platform/kube/bookinfo.yaml).
    This is the Kubernetes deployment spec of the app. Notice the services and the deployments.

1.  Deploy the application to your Kubernetes cluster:

```bash
$ kubectl apply -l version!=v2,version!=v3 -f https://raw.githubusercontent.com/istio/istio/8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99/samples/bookinfo/platform/kube/bookinfo.yaml
service/details created
serviceaccount/bookinfo-details created
deployment.apps/details-v1 created
service/ratings created
serviceaccount/bookinfo-ratings created
deployment.apps/ratings-v1 created
service/reviews created
serviceaccount/bookinfo-reviews created
deployment.apps/reviews-v1 created
service/productpage created
serviceaccount/bookinfo-productpage created
deployment.apps/productpage-v1 created
```

1.  Check the status of the pods:

```bash
$ kubectl get pods
NAME                            READY   STATUS    RESTARTS   AGE
details-v1-6d86fd9949-q8rrf     1/1     Running   0          10s
productpage-v1-c9965499-tjdjx   1/1     Running   0          8s
ratings-v1-7bf577cb77-pq9kg     1/1     Running   0          9s
reviews-v1-77c65dc5c6-kjvxs     1/1     Running   0          9s
```

1.  After the four pods achieve the `Running` status, you can scale the deployment. To let each version of each microservice run in three pods, execute the following command:

```bash
$ kubectl scale deployments --all --replicas 3
deployment.apps/details-v1 scaled
deployment.apps/productpage-v1 scaled
deployment.apps/ratings-v1 scaled
deployment.apps/reviews-v1 scaled
```

1.  Check the pods status. Notice that each microservice has three pods:

```bash
$ kubectl get pods
NAME                            READY   STATUS    RESTARTS   AGE
details-v1-6d86fd9949-fr59p     1/1     Running   0          50s
details-v1-6d86fd9949-mksv7     1/1     Running   0          50s
details-v1-6d86fd9949-q8rrf     1/1     Running   0          1m
productpage-v1-c9965499-hwhcn   1/1     Running   0          50s
productpage-v1-c9965499-nccwq   1/1     Running   0          50s
productpage-v1-c9965499-tjdjx   1/1     Running   0          1m
ratings-v1-7bf577cb77-cbdsg     1/1     Running   0          50s
ratings-v1-7bf577cb77-cz6jm     1/1     Running   0          50s
ratings-v1-7bf577cb77-pq9kg     1/1     Running   0          1m
reviews-v1-77c65dc5c6-5wt8g     1/1     Running   0          49s
reviews-v1-77c65dc5c6-kjvxs     1/1     Running   0          1m
reviews-v1-77c65dc5c6-r55tl     1/1     Running   0          49s
```

1.  After the services achieve the `Running` status, deploy a testing pod,
    [curl](https://github.com/istio/istio/tree/8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99/samples/curl), to use for sending requests
    to your microservices:

```bash
$ kubectl apply -f https://raw.githubusercontent.com/istio/istio/8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99/samples/curl/curl.yaml
```

1.  To confirm that the Bookinfo application is running, send a request to it
    with a curl command from your testing pod:

```bash
$ kubectl exec $(kubectl get pod -l app=curl -o jsonpath='{.items[0].metadata.name}') -c curl -- curl -sS productpage:9080/productpage | grep -o "<title>.*</title>"
<title>Simple Bookstore App</title>
```

## Enable external access to the application

Once your application is running, enable clients from outside the cluster to access it. Once you configure the steps
below successfully, you can access the application from your laptop's browser.

> **Warning:**
>
> If your cluster runs on GKE, change the `productpage` service type to `LoadBalancer`:
>
>
>
> ```bash
> $ kubectl patch svc productpage -p '{"spec": {"type": "LoadBalancer"}}'
> service/productpage patched
> ```

### Configure the Kubernetes Ingress resource and access your application's webpage

1.  Create a Kubernetes Ingress resource:

```bash
$ kubectl apply -f - <<EOF
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: bookinfo
  annotations:
    kubernetes.io/ingress.class: istio
spec:
  rules:
  - host: $MYHOST
    http:
      paths:
      - path: /productpage
        pathType: Prefix
        backend:
          service:
            name: productpage
            port:
              number: 9080
      - path: /login
        pathType: Prefix
        backend:
          service:
            name: productpage
            port:
              number: 9080
      - path: /logout
        pathType: Prefix
        backend:
          service:
            name: productpage
            port:
              number: 9080
      - path: /static
        pathType: Prefix
        backend:
          service:
            name: productpage
            port:
              number: 9080
EOF
```

### Update your `/etc/hosts` configuration file

1.  Get the IP address for the Kubernetes ingress named `bookinfo`:

```bash
$ kubectl get ingress bookinfo
```

1.  In your `/etc/hosts` file, add the previous IP address to the host entries
    provided by the following command. You should have a
    [Superuser](https://en.wikipedia.org/wiki/Superuser) privilege and probably
    use [`sudo`](https://en.wikipedia.org/wiki/Sudo) to edit `/etc/hosts`.

```bash
$ echo $(kubectl get ingress istio-system -n istio-system -o jsonpath='{..ip} {..host}') $(kubectl get ingress bookinfo -o jsonpath='{..host}')
```

### Access your application

1.  Access the application's home page from the command line:

```bash
$ curl -s $MYHOST/productpage | grep -o "<title>.*</title>"
<title>Simple Bookstore App</title>
```

1.  Paste the output of the following command in your browser address bar:

```bash
$ echo http://$MYHOST/productpage
```

    You should see the following webpage:

![Bookinfo Web Application](https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/examples/microservices-istio/bookinfo-kubernetes/bookinfo.png)

1.  Observe how microservices call each other. For example, `reviews` calls the `ratings` microservice using the
    `http://ratings:9080/ratings` URL.
    See the [code of `reviews`](https://github.com/istio/istio/blob/8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99/samples/bookinfo/src/reviews/reviews-application/src/main/java/application/rest/LibertyRestEndpoint.java):

```java
private final static String ratings_service = "http://ratings:9080/ratings";
```

1.  Set an infinite loop in a separate terminal window to send traffic to your application to simulate the
    constant user traffic in the real world:

```bash
$ while :; do curl -s $MYHOST/productpage | grep -o "<title>.*</title>"; sleep 1; done
<title>Simple Bookstore App</title>
<title>Simple Bookstore App</title>
<title>Simple Bookstore App</title>
<title>Simple Bookstore App</title>
...
```

You are ready to [test the application](../production-testing/index.md).
