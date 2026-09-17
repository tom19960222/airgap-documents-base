---
collection: cilium
version: "1.16.7"
title: "Creating Policies from Verdicts"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/security/policy-creation.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

<a id="policy_verdicts"></a>

# Creating Policies from Verdicts

Policy Audit Mode configures Cilium to allow all traffic while logging all
connections that would otherwise be dropped by network policies. Policy Audit
Mode may be configured for the entire daemon using ``--policy-audit-mode=true``
or for individual Cilium Endpoints. When Policy Audit Mode is enabled, no
network policy is enforced so this setting is **not recommended for production
deployment**. Policy Audit Mode supports auditing network policies implemented
at networks layers 3 and 4. This guide walks through the process of creating
policies using Policy Audit Mode.

Included file `Documentation/security/gsg_requirements.rst`:

If you haven't read the [intro](../overview/intro.md#intro) yet, we'd encourage you to do that first.

The best way to get help if you get stuck is to ask a question on Cilium Slack <!-- unresolved-rst-link: kind=named target=Cilium Slack -->. With Cilium contributors across the globe, there is almost always
someone available to help.

## Setup Cilium

If you have not set up Cilium yet, follow the guide [k8s_install_standard](../gettingstarted/k8s-install-default.md#k8s_install_standard)
for instructions on how to quickly bootstrap a Kubernetes cluster and install
Cilium. If in doubt, pick the minikube route, you will be good to go in less
than 5 minutes.

Included file `Documentation/security/gsg_sw_demo.rst`:

## Deploy the Demo Application

When we have Cilium deployed and ``kube-dns`` operating correctly we can deploy our demo application.

In our Star Wars-inspired example, there are three microservices applications: *deathstar*, *tiefighter*, and *xwing*. The *deathstar* runs an HTTP webservice on port 80, which is exposed as a [Kubernetes Service](https://kubernetes.io/docs/concepts/services-networking/service/) to load-balance requests to *deathstar* across two pod replicas. The *deathstar* service provides landing services to the empire's spaceships so that they can request a landing port. The *tiefighter* pod represents a landing-request client service on a typical empire ship and *xwing* represents a similar service on an alliance ship. They exist so that we can test different security policies for access control to *deathstar* landing services.

**Application Topology for Cilium and Kubernetes**

![](/gettingstarted/images/cilium_http_gsg.png)

The file ``http-sw-app.yaml`` contains a [Kubernetes Deployment](https://kubernetes.io/docs/concepts/workloads/controllers/deployment/) for each of the three services.
Each deployment is identified using the Kubernetes labels (``org=empire, class=deathstar``), (``org=empire, class=tiefighter``),
and (``org=alliance, class=xwing``).
It also includes a deathstar-service, which load-balances traffic to all pods with label (``org=empire, class=deathstar``).

.. parsed-literal::

   $ kubectl create -f \ |SCM_WEB|\/examples/minikube/http-sw-app.yaml
   service/deathstar created
   deployment.apps/deathstar created
   pod/tiefighter created
   pod/xwing created

Kubernetes will deploy the pods and service in the background.  Running
``kubectl get pods,svc`` will inform you about the progress of the operation.
Each pod will go through several states until it reaches ``Running`` at which
point the pod is ready.

```shell-session
$ kubectl get pods,svc
NAME                             READY   STATUS    RESTARTS   AGE
pod/deathstar-6fb5694d48-5hmds   1/1     Running   0          107s
pod/deathstar-6fb5694d48-fhf65   1/1     Running   0          107s
pod/tiefighter                   1/1     Running   0          107s
pod/xwing                        1/1     Running   0          107s

NAME                 TYPE        CLUSTER-IP    EXTERNAL-IP   PORT(S)   AGE
service/deathstar    ClusterIP   10.96.110.8   <none>        80/TCP    107s
service/kubernetes   ClusterIP   10.96.0.1     <none>        443/TCP   3m53s
```

Each pod will be represented in Cilium as an [endpoint](../gettingstarted/terminology.md#endpoint) in the local cilium agent.
We can invoke the ``cilium`` tool inside the Cilium pod to list them (in a single-node installation
``kubectl -n kube-system exec ds/cilium -- cilium-dbg endpoint list`` lists them all, but in a
multi-node installation, only the ones running on the same node will be listed):

```shell-session
$ kubectl -n kube-system get pods -l k8s-app=cilium
NAME           READY   STATUS    RESTARTS   AGE
cilium-5ngzd   1/1     Running   0          3m19s

$ kubectl -n kube-system exec cilium-5ngzd -- cilium-dbg endpoint list
ENDPOINT   POLICY (ingress)   POLICY (egress)   IDENTITY   LABELS (source:key[=value])                       IPv6   IPv4         STATUS
           ENFORCEMENT        ENFORCEMENT
232        Disabled           Disabled          16530      k8s:class=deathstar                                      10.0.0.147   ready
                                                           k8s:io.cilium.k8s.policy.cluster=default
                                                           k8s:io.cilium.k8s.policy.serviceaccount=default
                                                           k8s:io.kubernetes.pod.namespace=default
                                                           k8s:org=empire
726        Disabled           Disabled          1          reserved:host                                                         ready
883        Disabled           Disabled          4          reserved:health                                          10.0.0.244   ready
1634       Disabled           Disabled          51373      k8s:io.cilium.k8s.policy.cluster=default                 10.0.0.118   ready
                                                           k8s:io.cilium.k8s.policy.serviceaccount=coredns
                                                           k8s:io.kubernetes.pod.namespace=kube-system
                                                           k8s:k8s-app=kube-dns
1673       Disabled           Disabled          31028      k8s:class=tiefighter                                     10.0.0.112   ready
                                                           k8s:io.cilium.k8s.policy.cluster=default
                                                           k8s:io.cilium.k8s.policy.serviceaccount=default
                                                           k8s:io.kubernetes.pod.namespace=default
                                                           k8s:org=empire
2811       Disabled           Disabled          51373      k8s:io.cilium.k8s.policy.cluster=default                 10.0.0.47    ready
                                                           k8s:io.cilium.k8s.policy.serviceaccount=coredns
                                                           k8s:io.kubernetes.pod.namespace=kube-system
                                                           k8s:k8s-app=kube-dns
2843       Disabled           Disabled          16530      k8s:class=deathstar                                      10.0.0.89    ready
                                                           k8s:io.cilium.k8s.policy.cluster=default
                                                           k8s:io.cilium.k8s.policy.serviceaccount=default
                                                           k8s:io.kubernetes.pod.namespace=default
                                                           k8s:org=empire
3184       Disabled           Disabled          22654      k8s:class=xwing                                          10.0.0.30    ready
                                                           k8s:io.cilium.k8s.policy.cluster=default
                                                           k8s:io.cilium.k8s.policy.serviceaccount=default
                                                           k8s:io.kubernetes.pod.namespace=default
                                                           k8s:org=alliance
```

Both ingress and egress policy enforcement is still disabled on all of these pods because no network
policy has been imported yet which select any of the pods.

## Scale down the deathstar Deployment

In this guide we're going to scale down the deathstar Deployment in order to
simplify the next steps:

```shell-session
$ kubectl scale --replicas=1 deployment deathstar
deployment.apps/deathstar scaled
```

## Enable Policy Audit Mode (Entire Daemon)

To observe policy audit messages for all endpoints managed by this Daemonset,
modify the Cilium ConfigMap and restart all daemons:

.. tabs::

   .. group-tab:: Configure via kubectl

      .. code-block:: shell-session

         $ kubectl patch -n $CILIUM_NAMESPACE configmap cilium-config --type merge --patch '{"data":{"policy-audit-mode":"true"}}'
         configmap/cilium-config patched
         $ kubectl -n $CILIUM_NAMESPACE rollout restart ds/cilium
         daemonset.apps/cilium restarted
         $ kubectl -n $CILIUM_NAMESPACE rollout status ds/cilium
         Waiting for daemon set "cilium" rollout to finish: 0 of 1 updated pods are available...
         daemon set "cilium" successfully rolled out

   .. group-tab:: Helm Upgrade

      If you installed Cilium via ``helm install``, then you can use ``helm
      upgrade`` to enable Policy Audit Mode:

      .. parsed-literal::

         $ helm upgrade cilium |CHART_RELEASE| \\
             --namespace $CILIUM_NAMESPACE \\
             --reuse-values \\
             --set policyAuditMode=true

## Enable Policy Audit Mode (Specific Endpoint)

Cilium can enable Policy Audit Mode for a specific endpoint. This may be helpful when enabling
Policy Audit Mode for the entire daemon is too broad. Enabling per endpoint will ensure other
endpoints managed by the same daemon are not impacted.

This approach is meant to be temporary.  **Restarting Cilium pod will reset the Policy Audit
Mode to match the daemon's configuration.**

Policy Audit Mode is enabled for a given endpoint by modifying the endpoint configuration via
the ``cilium`` tool on the endpoint's Kubernetes node. The steps include:

1. Determine the endpoint id on which Policy Audit Mode will be enabled.
1. Identify the Cilium pod running on the same Kubernetes node corresponding to the endpoint.
1. Using the Cilium pod above, modify the endpoint configuration by setting ``PolicyAuditMode=Enabled``.

The following shell commands perform these steps:

```shell-session
$ PODNAME=$(kubectl get pods -l app.kubernetes.io/name=deathstar -o jsonpath='{.items[*].metadata.name}')
$ NODENAME=$(kubectl get pod -o jsonpath="{.items[?(@.metadata.name=='$PODNAME')].spec.nodeName}")
$ ENDPOINT=$(kubectl get cep -o jsonpath="{.items[?(@.metadata.name=='$PODNAME')].status.id}")
$ CILIUM_POD=$(kubectl -n "$CILIUM_NAMESPACE" get pod --all-namespaces --field-selector spec.nodeName="$NODENAME" -lk8s-app=cilium -o jsonpath='{.items[*].metadata.name}')
$ kubectl -n "$CILIUM_NAMESPACE" exec "$CILIUM_POD" -c cilium-agent -- \
    cilium-dbg endpoint config "$ENDPOINT" PolicyAuditMode=Enabled
 Endpoint 232 configuration updated successfully
```

We can check that Policy Audit Mode is enabled for this endpoint with

```shell-session
$ kubectl -n "$CILIUM_NAMESPACE" exec "$CILIUM_POD" -c cilium-agent -- \
    cilium-dbg endpoint get "$ENDPOINT" -o jsonpath='{[*].spec.options.PolicyAuditMode}'
Enabled
```

<a id="observe_policy_verdicts"></a>

## Observe policy verdicts

In this example, we are tasked with applying security policy for the deathstar.
First, from the Cilium pod we need to monitor the notifications for policy
verdicts using the Hubble CLI. We'll be monitoring for inbound traffic towards
the deathstar to identify it and determine whether to extend the network policy
to allow that traffic.

Apply a default-deny policy:

.. literalinclude:: ../../examples/minikube/sw_deny_policy.yaml

CiliumNetworkPolicies match on pod labels using an ``endpointSelector`` to identify
the sources and destinations to which the policy applies. The above policy denies
traffic sent to any pods with label (``org=empire``). Due to the Policy Audit Mode
enabled above (either for the entire daemon, or for just the ``deathstar`` endpoint),
the traffic will not actually be denied but will instead trigger policy verdict
notifications.

To apply this policy, run:

.. parsed-literal::

   $ kubectl create -f \ |SCM_WEB|\/examples/minikube/sw_deny_policy.yaml
   ciliumnetworkpolicy.cilium.io/empire-default-deny created

With the above policy, we will enable a default-deny posture on ingress to pods
with the label ``org=empire`` and enable the policy verdict notifications for
those pods. The same principle applies on egress as well.

Now let's send some traffic from the tiefighter to the deathstar:

```shell-session
$ kubectl exec tiefighter -- curl -s -XPOST deathstar.default.svc.cluster.local/v1/request-landing
Ship landed
```

We can check the policy verdict from the Cilium Pod:

```shell-session
$ kubectl -n "$CILIUM_NAMESPACE" exec "$CILIUM_POD" -c cilium-agent -- \
    hubble observe flows -t policy-verdict --last 1
Feb  7 12:53:39.168: default/tiefighter:54134 (ID:31028) -> default/deathstar-6fb5694d48-5hmds:80 (ID:16530) policy-verdict:none AUDITED (TCP Flags: SYN)
```

In the above example, we can see that the Pod ``deathstar-6fb5694d48-5hmds`` has
received traffic from the ``tiefighter`` Pod which doesn't match the policy
(``policy-verdict:none AUDITED``).

<a id="create_network_policy"></a>

## Create the Network Policy

We can get more information about the flow with

```shell-session
$ kubectl -n "$CILIUM_NAMESPACE" exec "$CILIUM_POD" -c cilium-agent -- \
    hubble observe flows -t policy-verdict -o json --last 1
```

Given the above information, we now know the labels of the source and
destination Pods, the traffic direction, and the destination port. In this case,
we can see clearly that the source (i.e. the tiefighter Pod) is an empire
aircraft (as it has the ``org=empire`` label) so once we've determined that we
expect this traffic to arrive at the deathstar, we can form a policy to match
the traffic:

.. literalinclude:: ../../examples/minikube/sw_l3_l4_policy.yaml

To apply this L3/L4 policy, run:

.. parsed-literal::

   $ kubectl create -f \ |SCM_WEB|\/examples/minikube/sw_l3_l4_policy.yaml
   ciliumnetworkpolicy.cilium.io/rule1 created

Now if we run the landing requests again,

```shell-session
$ kubectl exec tiefighter -- curl -s -XPOST deathstar.default.svc.cluster.local/v1/request-landing
Ship landed
```

we can then observe that the traffic which was previously audited to be dropped
by the policy is reported as allowed:

```shell-session
$ kubectl -n "$CILIUM_NAMESPACE" exec "$CILIUM_POD" -c cilium-agent -- \
    hubble observe flows -t policy-verdict --last 1
...
Feb  7 13:06:45.130: default/tiefighter:59824 (ID:31028) -> default/deathstar-6fb5694d48-5hmds:80 (ID:16530) policy-verdict:L3-L4 ALLOWED (TCP Flags: SYN)
```

Now the policy verdict states that the traffic would be allowed:
``policy-verdict:L3-L4 ALLOWED``. Success!

## Disable Policy Audit Mode (Entire Daemon)

These steps should be repeated for each connection in the cluster to ensure
that the network policy allows all of the expected traffic. The final step
after deploying the policy is to disable Policy Audit Mode again:

.. tabs::

   .. group-tab:: Configure via kubectl

      .. code-block:: shell-session

         $ kubectl patch -n $CILIUM_NAMESPACE configmap cilium-config --type merge --patch '{"data":{"policy-audit-mode":"false"}}'
         configmap/cilium-config patched
         $ kubectl -n $CILIUM_NAMESPACE rollout restart ds/cilium
         daemonset.apps/cilium restarted
         $ kubectl -n kube-system rollout status ds/cilium
         Waiting for daemon set "cilium" rollout to finish: 0 of 1 updated pods are available...
         daemon set "cilium" successfully rolled out

   .. group-tab:: Helm Upgrade

      .. parsed-literal::

         $ helm upgrade cilium |CHART_RELEASE| \\
             --namespace $CILIUM_NAMESPACE \\
             --reuse-values \\
             --set policyAuditMode=false

## Disable Policy Audit Mode (Specific Endpoint)

These steps are nearly identical to enabling Policy Audit Mode.

```shell-session
$ PODNAME=$(kubectl get pods -l app.kubernetes.io/name=deathstar -o jsonpath='{.items[*].metadata.name}')
$ NODENAME=$(kubectl get pod -o jsonpath="{.items[?(@.metadata.name=='$PODNAME')].spec.nodeName}")
$ ENDPOINT=$(kubectl get cep -o jsonpath="{.items[?(@.metadata.name=='$PODNAME')].status.id}")
$ CILIUM_POD=$(kubectl -n "$CILIUM_NAMESPACE" get pod --all-namespaces --field-selector spec.nodeName="$NODENAME" -lk8s-app=cilium -o jsonpath='{.items[*].metadata.name}')
$ kubectl -n "$CILIUM_NAMESPACE" exec "$CILIUM_POD" -c cilium-agent -- \
    cilium-dbg endpoint config "$ENDPOINT" PolicyAuditMode=Disabled
 Endpoint 232 configuration updated successfully
```

Alternatively, **restarting the Cilium pod** will set the endpoint Policy Audit Mode to the daemon set configuration.

## Verify Policy Audit Mode is Disabled

```shell-session
$ kubectl -n "$CILIUM_NAMESPACE" exec "$CILIUM_POD" -c cilium-agent -- \
    cilium-dbg endpoint get "$ENDPOINT" -o jsonpath='{[*].spec.options.PolicyAuditMode}'
Disabled
```

Now if we run the landing requests again, only the *tiefighter* pods with the
label ``org=empire`` should succeed:

```shell-session
$ kubectl exec tiefighter -- curl -s -XPOST deathstar.default.svc.cluster.local/v1/request-landing
Ship landed
```

And we can observe that the traffic was allowed by the policy:

```shell-session
$ kubectl -n "$CILIUM_NAMESPACE" exec "$CILIUM_POD" -c cilium-agent -- \
    hubble observe flows -t policy-verdict --from-pod tiefighter --last 1
Feb  7 13:34:26.112: default/tiefighter:37314 (ID:31028) -> default/deathstar-6fb5694d48-5hmds:80 (ID:16530) policy-verdict:L3-L4 ALLOWED (TCP Flags: SYN)
```

This works as expected. Now the same request from an *xwing* Pod should fail:

```shell-session
$ kubectl exec xwing -- curl --connect-timeout 3 -s -XPOST deathstar.default.svc.cluster.local/v1/request-landing
command terminated with exit code 28
```

This curl request should timeout after three seconds, we can observe the policy
verdict with:

```shell-session
$ kubectl -n "$CILIUM_NAMESPACE" exec "$CILIUM_POD" -c cilium-agent -- \
    hubble observe flows -t policy-verdict --from-pod xwing --last 1
Feb  7 13:43:46.791: default/xwing:54842 (ID:22654) <> default/deathstar-6fb5694d48-5hmds:80 (ID:16530) policy-verdict:none DENIED (TCP Flags: SYN)
```

We hope you enjoyed the tutorial.  Feel free to play more with the setup,
follow the `gs_http` guide, and reach out to us on Cilium Slack <!-- unresolved-rst-link: kind=named target=Cilium Slack --> with any
questions!

## Clean-up

.. parsed-literal::

   $ kubectl delete -f \ |SCM_WEB|\/examples/minikube/http-sw-app.yaml
   $ kubectl delete cnp empire-default-deny rule1
