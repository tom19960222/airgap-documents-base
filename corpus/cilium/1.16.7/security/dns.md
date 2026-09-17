---
collection: cilium
version: "1.16.7"
title: "Locking Down External Access with DNS-Based Policies"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/security/dns.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

<a id="gs_dns"></a>

# Locking Down External Access with DNS-Based Policies

This document serves as an introduction for using Cilium to enforce DNS-based
security policies for Kubernetes pods.

Included file `Documentation/security/gsg_requirements.rst`:

If you haven't read the [intro](../overview/intro.md#intro) yet, we'd encourage you to do that first.

The best way to get help if you get stuck is to ask a question on Cilium Slack <!-- unresolved-rst-link: kind=named target=Cilium Slack -->. With Cilium contributors across the globe, there is almost always
someone available to help.

## Setup Cilium

If you have not set up Cilium yet, follow the guide [k8s_install_standard](../gettingstarted/k8s-install-default.md#k8s_install_standard)
for instructions on how to quickly bootstrap a Kubernetes cluster and install
Cilium. If in doubt, pick the minikube route, you will be good to go in less
than 5 minutes.

## Deploy the Demo Application

DNS-based policies are very useful for controlling access to services running outside the Kubernetes cluster. DNS acts as a persistent service identifier for both external services provided by AWS, Google, Twilio, Stripe, etc., and internal services such as database clusters running in private subnets outside Kubernetes. CIDR or IP-based policies are cumbersome and hard to maintain as the IPs associated with external services can change frequently. The Cilium DNS-based policies provide an easy mechanism to specify access control while Cilium manages the harder aspects of tracking DNS to IP mapping.

In this guide we will learn about:

- Controlling egress access to services outside the cluster using DNS-based policies
- Using patterns (or wildcards) to whitelist a subset of DNS domains
- Combining DNS, port and L7 rules for restricting access to external service

In line with our Star Wars theme examples, we will use a simple scenario where
the Empire's ``mediabot`` pods need access to GitHub for managing the Empire's
git repositories. The pods shouldn't have access to any other external service.

.. parsed-literal::

   $ kubectl create -f \ |SCM_WEB|\/examples/kubernetes-dns/dns-sw-app.yaml
   $ kubectl wait pod/mediabot --for=condition=Ready
   $ kubectl get pods
   NAME                             READY   STATUS    RESTARTS   AGE
   pod/mediabot                     1/1     Running   0          14s

## Apply DNS Egress Policy

The following Cilium network policy allows ``mediabot`` pods to only access ``api.github.com``.

.. tabs::

   .. group-tab:: Generic

      .. literalinclude:: ../../examples/kubernetes-dns/dns-matchname.yaml

   .. group-tab:: OpenShift

      .. literalinclude:: ../../examples/kubernetes-dns/dns-matchname-openshift.yaml

> **Note:**
> OpenShift users will need to modify the policies to match the namespace
> ``openshift-dns`` (instead of ``kube-system``), remove the match on the
> ``k8s:k8s-app=kube-dns`` label, and change the port to 5353.

Let's take a closer look at the policy:

* The first egress section uses ``toFQDNs: matchName`` specification to allow
  egress to ``api.github.com``. The destination DNS should match exactly the
  name specified in the rule. The ``endpointSelector`` allows only pods with
  labels ``class: mediabot, org:empire`` to have the egress access.
* The second egress section (``toEndpoints``) allows ``mediabot`` pods to access
  ``kube-dns`` service. Note that ``rules: dns`` instructs Cilium to inspect and
  allow DNS lookups matching specified patterns. In this case, inspect and allow
  all DNS queries.

Note that with this policy the ``mediabot`` doesn't have access to any internal
cluster service other than ``kube-dns``. Refer to [Network Policy](../network/clustermesh/policy.md#network-policy) to learn
more about policies for controlling access to internal cluster services.

Let's apply the policy:

.. parsed-literal::

   kubectl apply -f \ |SCM_WEB|\/examples/kubernetes-dns/dns-matchname.yaml

Testing the policy, we see that ``mediabot`` has access to ``api.github.com``
but doesn't have access to any other external service, e.g.,
``support.github.com``.

```shell-session
$ kubectl exec mediabot -- curl -I -s https://api.github.com | head -1
HTTP/2 200

$ kubectl exec mediabot -- curl -I -s --max-time 5 https://support.github.com | head -1
curl: (28) Connection timed out after 5000 milliseconds
command terminated with exit code 28
```

## DNS Policies Using Patterns

The above policy controlled DNS access based on exact match of the DNS domain
name. Often, it is required to allow access to a subset of domains. Let's say,
in the above example, ``mediabot`` pods need access to any GitHub sub-domain,
e.g., the pattern ``*.github.com``. We can achieve this easily by changing the
``toFQDN`` rule to use ``matchPattern`` instead of ``matchName``.

.. literalinclude:: ../../examples/kubernetes-dns/dns-pattern.yaml

.. parsed-literal::

   kubectl apply -f \ |SCM_WEB|\/examples/kubernetes-dns/dns-pattern.yaml

Test that ``mediabot`` has access to multiple GitHub services for which the DNS
matches the pattern ``*.github.com``. It is important to note and test that this
doesn't allow access to ``github.com`` because the ``*.`` in the pattern
requires one subdomain to be present in the DNS name. You can simply add more
``matchName`` and ``matchPattern`` clauses to extend the access. (See [DNS based](policy/language.md#dns-based)
policies to learn more about specifying DNS rules using patterns and names.)

```shell-session
$ kubectl exec mediabot -- curl -I -s https://support.github.com | head -1
HTTP/1.1 200 OK

$ kubectl exec mediabot -- curl -I -s https://gist.github.com | head -1
HTTP/1.1 302 Found

$ kubectl exec mediabot -- curl -I -s --max-time 5 https://github.com | head -1
curl: (28) Connection timed out after 5000 milliseconds
command terminated with exit code 28
```

## Combining DNS, Port and L7 Rules

The DNS-based policies can be combined with port (L4) and API (L7) rules to
further restrict the access. In our example, we will restrict ``mediabot`` pods
to access GitHub services only on ports ``443``. The ``toPorts`` section in the
policy below achieves the port-based restrictions along with the DNS-based
policies.

.. literalinclude:: ../../examples/kubernetes-dns/dns-port.yaml

.. parsed-literal::

   kubectl apply -f \ |SCM_WEB|\/examples/kubernetes-dns/dns-port.yaml

Testing, the access to ``https://support.github.com`` on port ``443`` will
succeed but the access to ``http://support.github.com`` on port ``80`` will be
denied.

```shell-session
$ kubectl exec mediabot -- curl -I -s https://support.github.com | head -1
HTTP/1.1 200 OK

$ kubectl exec mediabot -- curl -I -s --max-time 5 http://support.github.com | head -1
curl: (28) Connection timed out after 5001 milliseconds
command terminated with exit code 28
```

Refer to [l4_policy](policy/language.md#l4_policy) and [l7_policy](policy/language.md#l7_policy) to learn more about Cilium L4 and
L7 network policies.

## Clean-up

.. parsed-literal::

   kubectl delete -f \ |SCM_WEB|\/examples/kubernetes-dns/dns-sw-app.yaml
   kubectl delete cnp fqdn
