---
collection: istio
version: "1.24"
title: "Add a new version of reviews"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/examples/microservices-istio/add-new-microservice-version/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
In this module, you deploy a new version of the `reviews` service, `_v2_`,
which will return the number and star color of ratings provided by reviewers. In
a real-world scenario, before you deploy, you would perform static analysis tests, unit tests, integration
tests, end-to-end tests and tests in a staging environment.

1.  Deploy the new version of the `reviews` microservice without the
    `app=reviews` label. Without that label, the new version will not be
    selected to provide the `reviews` service. As such, it will not be called by
    the production code. Run the following command to deploy the `reviews`
    microservice version 2, while replacing the label `app=reviews` by
    `app=reviews_test`:

```bash
$ curl -s https://raw.githubusercontent.com/istio/istio/8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99/samples/bookinfo/platform/kube/bookinfo.yaml | sed 's/app: reviews/app: reviews_test/' | kubectl apply -l app=reviews_test,version=v2 -f -
deployment.apps/reviews-v2 created
```

1.  Access your application to ensure the deployed microservice did not disrupt
    it.

1.  Test the new version of your microservice from inside the cluster using the
    testing container you deployed earlier. Note that your new version accesses
    the production pods of the `ratings` microservice during the test. Also note
    that you have to use the pod IP to access your new version of the
    microservice, because it is not selected for the `reviews` service.

    1.  Get the IP of the pod:

```bash
$ REVIEWS_V2_POD_IP=$(kubectl get pod -l app=reviews_test,version=v2 -o jsonpath='{.items[0].status.podIP}')
$ echo $REVIEWS_V2_POD_IP
```

    1.  Send a request to the pod and see that it returns the correct result:

```bash
$ kubectl exec $(kubectl get pod -l app=curl -o jsonpath='{.items[0].metadata.name}') -- curl -sS "$REVIEWS_V2_POD_IP:9080/reviews/7"
{"id": "7","reviews": [{  "reviewer": "Reviewer1",  "text": "An extremely entertaining play by Shakespeare. The slapstick humour is refreshing!", "rating": {"stars": 5, "color": "black"}},{  "reviewer": "Reviewer2",  "text": "Absolutely fun and entertaining. The play lacks thematic depth when compared to other plays by Shakespeare.", "rating": {"stars": 4, "color": "black"}}]}
```

    1.  Perform primitive load testing by sending a request 10 times in a row:

```bash
$ kubectl exec $(kubectl get pod -l app=curl -o jsonpath='{.items[0].metadata.name}') -- sh -c "for i in 1 2 3 4 5 6 7 8 9 10; do curl -o /dev/null -s -w '%{http_code}\n' $REVIEWS_V2_POD_IP:9080/reviews/7; done"
200
200
...
```

1.  The previous steps ensure that your new version of `reviews` will work
    and you can deploy it. You will deploy a single replica of the service into
    production so the real production traffic will start to arrive to your new
    service version. With the current setting, 75% of the traffic will arrive to the old
    version (three pods of the old version) and 25% will arrive to the new
    version (a single pod).

    To deploy _reviews v2_, redeploy the new version with the `app=reviews`
    label, so it will become addressable by the `reviews` service.

```bash
$ kubectl label pods -l version=v2 app=reviews --overwrite
pod "reviews-v2-79c8c8c7c5-4p4mn" labeled
```

1.  Now, you access the application web page and observe that the black stars
    appear for ratings. You can access the page several times and see that
    sometimes the page is returned with stars (approximately 25% of the time)
    and sometimes without stars (approximately 75% of the time).

![Bookinfo Web Application with black stars as ratings](https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/examples/microservices-istio/add-new-microservice-version/bookinfo-reviews-v2.png)

1.  If you encounter any problems with the new version in a real-world scenario,
    you could quickly undeploy the new version, so only the old version will be
    used:

```bash
$ kubectl delete deployment reviews-v2
$ kubectl delete pod -l app=reviews,version=v2
deployment.apps "reviews-v2" deleted
pod "reviews-v2-79c8c8c7c5-4p4mn" deleted
```

    Allow time for the configuration change to propagate through the system. Then,
    access your application's webpage several times and see that now black stars
    do not appear.

    To restore the new version:

```bash
$ kubectl apply -l app=reviews,version=v2 -f https://raw.githubusercontent.com/istio/istio/8825a6b7f8c9a2d66005a5f8b64e98aaee0dda99/samples/bookinfo/platform/kube/bookinfo.yaml
deployment.apps/reviews-v2 created
```

    Access your application's webpage several times and see that now the black
    stars are present approximately 25% of the time.

1.  Next, increase the replicas of your new version. You can do it gradually,
    carefully checking that the number of errors does not increase:

```bash
$ kubectl scale deployment reviews-v2 --replicas=3
deployment.apps/reviews-v2 scaled
```

    Now, access your application's webpage several times and see that the black
    stars appear approximately half the time.

1.  Now, you can decommission the old version:

```bash
$ kubectl delete deployment reviews-v1
deployment.apps "reviews-v1" deleted
```

    Accessing the web page of the application will return reviews with black
    stars only.

In the previous steps, you performed the update of `reviews`. First,
you deployed the new version without sending it simulated production traffic. You
tested it in the production environment using test traffic. You checked that the
new version provides correct results. You released the new version, gradually
increasing the production traffic to it. Finally, you decommissioned the old
version.

From here, you can improve your deployment strategy using the following example
tasks. First, test the new version end-to-end in production. This requires the
ability to drive traffic to your new version using request parameters, for
example using the user name stored in a cookie. In addition, perform shadowing
of the production traffic to your new version and check if your new version
provides incorrect results or produces errors. Finally, gain more detailed
control of the rollout. As an example, you can deploy at 1%, then increase by 1%
an hour as long as there does not appear to be degradation in the service. Istio
enhances the value of Kubernetes by helping you perform these tasks in a
straightforward way. For more detailed information and best practices about
deployment, see
[Deployment models](../../../ops/deployment/deployment-models/index.md).

From here, you have two choices:

1. Use a _service mesh_. In a service mesh, you put all the reporting, routing,
   policies, security logic in _sidecar_ proxies, injected *transparently* into
   your application pods. The business logic remains in the code of the
   application, no changes are required to the application code.

1. Implement the required functionality in the application code. Most of the
   functionality is already available in various libraries, for example in the
   Netflix's [Hystrix](https://github.com/Netflix/Hystrix) library  for the Java
   programming language. However, now you have to change your code to use the
   libraries. You have to put additional effort, your code will bloat, business
   logic will be mixed with reporting, routing, policies, networking logic.
   Since your microservices use different programming languages, you have to
   learn, use, update multiple libraries.

See [The Istio service mesh](https://istio.io/v1.24/about/service-mesh/) <!-- unresolved-site-link: route=/about/service-mesh --> to learn how Istio can per
can perform the tasks mentioned here and more. In the
next modules, you explore various Istio features.

You are ready to
[enable Istio on `productpage`](../add-istio/index.md).
