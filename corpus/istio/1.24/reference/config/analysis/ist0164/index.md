---
collection: istio
version: "1.24"
title: "ExternalControlPlaneAddressIsNotAHostname"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/config/analysis/ist0164/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
This message occurs when the address provided for the ingress gateway on the external control plane is an IP address and not a hostname.

## Example

You will receive this message:

```plain
Info [IST0164] (MutatingWebhookConfiguration istio-sidecar-injector-external-istiod testing.yml:28) The address (https://999.999.999.999:5100/inject/cluster/your-cluster-name/net/network1) that was provided for the webhook (rev.namespace.sidecar-injector.istio.io) to reach the ingress gateway on the external control plane cluster is an IP address. This is not recommended for a production environment.
```

when your cluster has the following `ValidatingWebhookConfiguration` and `MutatingWebhookConfiguration` (shortened for clarity):

```yaml
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingWebhookConfiguration
metadata:
  name: istio-validator-external-istiod
webhooks:
- admissionReviewVersions:
  - v1beta1
  - v1
  clientConfig:
    url: https://test.com:15017/validate
  name: rev.validation.istio.io

---
apiVersion: admissionregistration.k8s.io/v1
kind: ValidatingWebhookConfiguration
metadata:
  name: istiod-default-validator
webhooks:
- admissionReviewVersions:
  - v1beta1
  - v1
  clientConfig:
    url: https://test.com:15017/validate
  failurePolicy: Ignore
  name: validation.istio.io

---
apiVersion: admissionregistration.k8s.io/v1
kind: MutatingWebhookConfiguration
metadata:
  name: istio-sidecar-injector-external-istiod
webhooks:
- admissionReviewVersions:
  - v1beta1
  - v1
  clientConfig:
    url: https://999.999.999.999:5100/inject/cluster/your-cluster-name/net/network1
  failurePolicy: Fail
  name: rev.namespace.sidecar-injector.istio.io
- admissionReviewVersions:
  - v1beta1
  - v1
  clientConfig:
    url: https://test.com/inject/cluster/your-cluster-name/net/network1
  failurePolicy: Fail
  name: rev.object.sidecar-injector.istio.io
- admissionReviewVersions:
  - v1beta1
  - v1
  clientConfig:
    url: https://test.com/inject/cluster/your-cluster-name/net/network1
  failurePolicy: Fail
  name: namespace.sidecar-injector.istio.io
- admissionReviewVersions:
  - v1beta1
  - v1
  clientConfig:
    url: https://test.com/inject/cluster/your-cluster-name/net/network1
  failurePolicy: Fail
  name: object.sidecar-injector.istio.io
```

## How to resolve

Using an IP address instead of a hostname for your ingress gateway running in the external control plane is not recommended in a production environment.

If you are running in a production environment, you can fix this info message by changing the address to a valid hostname that resolves to the IP address of your ingress gateway.

Instructions for exposing the ingress gateway service using a public hostname with TLS can be found [here](../../../../setup/install/external-controlplane/index.md#set-up-a-gateway-in-the-external-cluster).
