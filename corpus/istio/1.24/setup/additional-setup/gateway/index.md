---
collection: istio
version: "1.24"
title: "Installing Gateways"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/setup/additional-setup/gateway/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "Install and customize Istio Gateways."
---
> **Tip:**
>
> ---
> ---
> Istio supports the Kubernetes [Gateway API](https://istio.io/v1.24/blog/2024/gateway-mesh-ga/) <!-- unresolved-site-link: route=/blog/2024/gateway-mesh-ga --> and intends to make it the default API for traffic management in the future.
>
>
> If you use the Gateway API, you will not need to install and manage a gateway `Deployment` as described in this document.
> By default, a gateway `Deployment` and `Service` will be automatically provisioned based on the `Gateway` configuration.
> Refer to the [Gateway API task](../../../tasks/traffic-management/ingress/gateway-api/index.md#automated-deployment) for details.

Along with creating a service mesh, Istio allows you to manage [gateways](../../../concepts/traffic-management/index.md#gateways),
which are Envoy proxies running at the edge of the mesh, providing fine-grained control over traffic entering and leaving the mesh.

Some of Istio's built in [configuration profiles](../config-profiles/index.md) deploy gateways during installation.
For example, a call to `istioctl install` with [default settings](../../install/istioctl/index.md#install-istio-using-the-default-profile)
will deploy an ingress gateway along with the control plane.
Although fine for evaluation and simple use cases, this couples the gateway to the control plane, making management and upgrade more complicated.
For production Istio deployments, it is highly recommended to decouple these to allow independent operation.

Follow this guide to separately deploy and manage one or more gateways in a production installation of Istio.

## Prerequisites

This guide requires the Istio control plane [to be installed](../../install/_index.md) before proceeding.

> **Tip:**
>
> You can use the `minimal` profile, for example `istioctl install --set profile=minimal`, to prevent any gateways from being deployed
> during installation.

## Deploying a gateway

Using the same mechanisms as [Istio sidecar injection](../sidecar-injection/index.md#automatic-sidecar-injection),
the Envoy proxy configuration for gateways can similarly be auto-injected.

Using auto-injection for gateway deployments is recommended as it gives developers full control over the gateway deployment,
while also simplifying operations.
When a new upgrade is available, or a configuration has changed, gateway pods can be updated by simply restarting them.
This makes the experience of operating a gateway deployment the same as operating sidecars.

To support users with existing deployment tools, Istio provides a few different ways to deploy a gateway.
Each method will produce the same result.
Choose the method you are most familiar with.

> **Tip:**
>
> As a security best practice, it is recommended to deploy the gateway in a different namespace from the control plane.

All methods listed below rely on [Injection](../sidecar-injection/index.md) to populate additional pod settings at runtime.
In order to support this, the namespace the gateway is deployed in must not have the `istio-injection=disabled` label.
If it does, you will see pods failing to startup attempting to pull the `auto` image, which is a placeholder that is intended to be replaced when a pod is created.

**Tabset (gateway-install-type):**

**Tab: IstioOperator**

First, setup an `IstioOperator` configuration file, called `ingress.yaml` here:

```yaml
apiVersion: install.istio.io/v1alpha1
kind: IstioOperator
metadata:
  name: ingress
spec:
  profile: empty # Do not install CRDs or the control plane
  components:
    ingressGateways:
    - name: istio-ingressgateway
      namespace: istio-ingress
      enabled: true
      label:
        # Set a unique label for the gateway. This is required to ensure Gateways
        # can select this workload
        istio: ingressgateway
  values:
    gateways:
      istio-ingressgateway:
        # Enable gateway injection
        injectionTemplate: gateway
```

Then install using standard `istioctl` commands:

```bash
$ kubectl create namespace istio-ingress
$ istioctl install -f ingress.yaml
```

**Tab: Helm**

Install using standard `helm` commands:

```bash
$ kubectl create namespace istio-ingress
$ helm install istio-ingressgateway istio/gateway -n istio-ingress
```

To see possible supported configuration values, run `helm show values istio/gateway`.
The Helm repository [README](https://artifacthub.io/packages/helm/istio-official/gateway) contains additional information
on usage.

> **Tip:**
>
> When deploying the gateway in an OpenShift cluster, use the `openshift` profile to override the default values, for example:
>
>
>
> ```bash
> $ helm install istio-ingressgateway istio/gateway -n istio-ingress --set global.platform=openshift
> ```

**Tab: Kubernetes YAML**

First, setup the Kubernetes configuration, called `ingress.yaml` here:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: istio-ingressgateway
  namespace: istio-ingress
spec:
  type: LoadBalancer
  selector:
    istio: ingressgateway
  ports:
  - port: 80
    name: http
  - port: 443
    name: https
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: istio-ingressgateway
  namespace: istio-ingress
spec:
  selector:
    matchLabels:
      istio: ingressgateway
  template:
    metadata:
      annotations:
        # Select the gateway injection template (rather than the default sidecar template)
        inject.istio.io/templates: gateway
      labels:
        # Set a unique label for the gateway. This is required to ensure Gateways can select this workload
        istio: ingressgateway
        # Enable gateway injection. If connecting to a revisioned control plane, replace with "istio.io/rev: revision-name"
        sidecar.istio.io/inject: "true"
    spec:
      # Allow binding to all ports (such as 80 and 443)
      securityContext:
        sysctls:
        - name: net.ipv4.ip_unprivileged_port_start
          value: "0"
      containers:
      - name: istio-proxy
        image: auto # The image will automatically update each time the pod starts.
        # Drop all privileges, allowing to run as non-root
        securityContext:
          capabilities:
            drop:
            - ALL
          runAsUser: 1337
          runAsGroup: 1337
---
# Set up roles to allow reading credentials for TLS
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: istio-ingressgateway-sds
  namespace: istio-ingress
rules:
- apiGroups: [""]
  resources: ["secrets"]
  verbs: ["get", "watch", "list"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: istio-ingressgateway-sds
  namespace: istio-ingress
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: istio-ingressgateway-sds
subjects:
- kind: ServiceAccount
  name: default
```

> **Warning:**
>
> This example shows the bare minimum needed to get a gateway running. For production usage, additional
> configuration such as `HorizontalPodAutoscaler`, `PodDisruptionBudget`, and resource requests/limits are recommended.
> These are automatically included when using the other gateway installation methods.

> **Tip:**
>
> The `sidecar.istio.io/inject` label on the pod is used in this example to enable injection. Just like application sidecar injection, this can instead be controlled at the namespace level.
> See [Controlling the injection policy](../sidecar-injection/index.md#controlling-the-injection-policy) for more information.

Next, apply it to the cluster:

```bash
$ kubectl create namespace istio-ingress
$ kubectl apply -f ingress.yaml
```

## Managing gateways

The following describes how to manage gateways after installation. For more information on their usage, follow
the [Ingress](../../../tasks/traffic-management/ingress/_index.md) and [Egress](../../../tasks/traffic-management/egress/_index.md) tasks.

### Gateway selectors

The labels on a gateway deployment's pods are used by `Gateway` configuration resources, so it's important that
your `Gateway` selector matches these labels.

For example, in the above deployments, the `istio=ingressgateway` label is set on the gateway pods.
To apply a `Gateway` to these deployments, you need to select the same label:

```yaml
apiVersion: networking.istio.io/v1
kind: Gateway
metadata:
  name: gateway
spec:
  selector:
    istio: ingressgateway
...
```

### Gateway deployment topologies

Depending on your mesh configuration and use cases, you may wish to deploy gateways in different ways.
A few different gateway deployment patterns are shown below.
Note that more than one of these patterns can be used within the same cluster.

#### Shared gateway

In this model, a single centralized gateway is used by many applications, possibly across many namespaces.
Gateway(s) in the `ingress` namespace delegate ownership of routes to application namespaces, but retain control over TLS configuration.

![Shared gateway](https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/setup/additional-setup/gateway/shared-gateway.svg)

This model works well when you have many applications you want to expose externally, as they are able to use shared infrastructure.
It also works well in use cases that have the same domain or TLS certificates shared by many applications.

#### Dedicated application gateway

In this model, an application namespace has its own dedicated gateway installation.
This allows giving full control and ownership to a single namespace.
This level of isolation can be helpful for critical applications that have strict performance or security requirements.

![Dedicated application gateway](https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/setup/additional-setup/gateway/user-gateway.svg)

Unless there is another load balancer in front of Istio, this typically means that each application will have its own IP address,
which may complicate DNS configurations.

## Upgrading gateways

### In place upgrade

Because gateways utilize pod injection, new gateway pods that are created will automatically be injected with the latest configuration, which includes the version.

To pick up changes to the gateway configuration, the pods can simply be restarted, using commands such as `kubectl rollout restart deployment`.

If you would like to change the [control plane revision](../../upgrade/canary/index.md) in use by the gateway, you can set the `istio.io/rev` label on the gateway Deployment, which will also trigger a rolling restart.

![In place upgrade in progress](https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/setup/additional-setup/gateway/inplace-upgrade.svg)

### Canary upgrade (advanced)

> **Warning:**
>
> This upgrade method depends on control plane revisions, and therefore can only be used in conjunction with
> [control plane canary upgrade](../../upgrade/canary/index.md).

If you would like to more slowly control the rollout of a new control plane revision, you can run multiple versions of a gateway deployment.
For example, if you want to roll out a new revision, `canary`, create a copy of your gateway deployment with the `istio.io/rev=canary` label set:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: istio-ingressgateway-canary
  namespace: istio-ingress
spec:
  selector:
    matchLabels:
      istio: ingressgateway
  template:
    metadata:
      annotations:
        inject.istio.io/templates: gateway
      labels:
        istio: ingressgateway
        istio.io/rev: canary # Set to the control plane revision you want to deploy
    spec:
      containers:
      - name: istio-proxy
        image: auto
```

When this deployment is created, you will then have two versions of the gateway, both selected by the same Service:

```bash
$ kubectl get endpoints -n istio-ingress -o "custom-columns=NAME:.metadata.name,PODS:.subsets[*].addresses[*].targetRef.name"
NAME                   PODS
istio-ingressgateway   istio-ingressgateway-...,istio-ingressgateway-canary-...
```

![Canary upgrade in progress](https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/setup/additional-setup/gateway/canary-upgrade.svg)

Unlike application services deployed inside the mesh, you cannot use [Istio traffic shifting](../../../tasks/traffic-management/traffic-shifting/index.md) to distribute the traffic between the gateway versions because their traffic is coming directly from external clients that Istio does not control.
Instead, you can control the distribution of traffic by the number of replicas of each deployment.
If you use another load balancer in front of Istio, you may also use that to control the traffic distribution.

> **Warning:**
>
> Because other installation methods bundle the gateway `Service`, which controls its external IP address, with the gateway `Deployment`,
> only the [Kubernetes YAML](index.md#tabset-docs-setup-additional-setup-gateway-1-2-tab) method is supported for this upgrade method.

### Canary upgrade with external traffic shifting (advanced)

A variant of the [canary upgrade](#canary-upgrade) approach is to shift the traffic between the versions using a high level construct outside Istio, such as an external load balancer or DNS.

![Canary upgrade in progress with external traffic shifting](https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/setup/additional-setup/gateway/high-level-canary.svg)

This offers fine-grained control, but may be unsuitable or overly complicated to set up in some environments.

## Cleanup

- Cleanup Istio ingress gateway

```bash
$ istioctl uninstall --istioNamespace istio-ingress -y --purge
$ kubectl delete ns istio-ingress
```
