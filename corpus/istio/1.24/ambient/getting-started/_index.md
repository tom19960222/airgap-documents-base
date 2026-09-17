---
collection: istio
version: "1.24"
title: "Getting Started"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/ambient/getting-started/_index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "How to deploy and install Istio in ambient mode."
---
This guide lets you quickly evaluate Istio's ambient mode. You'll need a Kubernetes cluster to proceed. If you don't have a cluster, you can use [kind](../../setup/platform-setup/kind/index.md) or any other [supported Kubernetes platform](../../setup/platform-setup/_index.md).

These steps require you to have a cluster running a
[supported version](../../releases/supported-releases/index.md#support-status-of-istio-releases) of Kubernetes ([supported_kubernetes_versions]).

## Download the Istio CLI

Istio is configured using a command line tool called `istioctl`.  Download it, and the Istio sample applications:

```bash
$ curl -L https://istio.io/downloadIstio | sh -
$ cd istio-[istio_full_version]
$ export PATH=$PWD/bin:$PATH
```

Check that you are able to run `istioctl` by printing the version of the command. At this point, Istio is not installed in your cluster, so you will see that there are no pods ready.

```bash
$ istioctl version
Istio is not present in the cluster: no running Istio pods in namespace "istio-system"
client version: [istio_full_version]
```

## Install Istio on to your cluster

`istioctl` supports a number of [configuration profiles](../../setup/additional-setup/config-profiles/index.md) that include different default options, and can be customized for your production needs. Support for ambient mode is included in the `ambient` profile. Install Istio with the following command:

```bash
$ istioctl install --set profile=ambient --skip-confirmation
```

Once the installation completes, you’ll get the following output that indicates all components have been installed successfully.

```plain
✔ Istio core installed
✔ Istiod installed
✔ CNI installed
✔ Ztunnel installed
✔ Installation complete
```

## Install the Kubernetes Gateway API CRDs

You will use the Kubernetes Gateway API to configure traffic routing.

---
---
Note that the Kubernetes Gateway API CRDs do not come installed by default on most Kubernetes clusters, so make sure they are
installed before using the Gateway API:

```bash
$ kubectl get crd gateways.gateway.networking.k8s.io &> /dev/null || \
  { kubectl apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/[k8s_gateway_api_version]/standard-install.yaml; }
```

## Next steps

Congratulations! You've successfully installed Istio with support for ambient mode. Continue to the next step to [install a sample application](deploy-sample-app/index.md).
