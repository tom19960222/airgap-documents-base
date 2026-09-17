---
collection: cilium
version: "1.16.7"
title: "Create TLS Certificate and Private Key"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/network/servicemesh/tls-cert.rst
fetched_at: 2025-02-13T12:04:31Z
---
# Create TLS Certificate and Private Key

.. tabs::

   .. group-tab:: Self-signed Certificate

       For demonstration purposes we will use a TLS certificate signed by a made-up,
       [self-signed](https://cert-manager.io/docs/faq/terminology/#what-does-self-signed-mean-is-my-ca-self-signed)
       certificate authority (CA). One easy way to do this is with [mkcert](https://github.com/FiloSottile/mkcert).
       We want a certificate that will validate ``bookinfo.cilium.rocks`` and
       ``hipstershop.cilium.rocks``, as these are the host names used in this example.

       .. code-block:: shell-session

           $ mkcert bookinfo.cilium.rocks hispter.cilium.rocks
           Note: the local CA is not installed in the system trust store.
           Run "mkcert -install" for certificates to be trusted automatically ⚠️

           Created a new certificate valid for the following names 📜
            - "bookinfo.cilium.rocks"
            - "hispter.cilium.rocks"

           The certificate is at "./bookinfo.cilium.rocks+1.pem" and the key at "./bookinfo.cilium.rocks+1-key.pem" ✅

           It will expire on 29 November 2026 🗓

       Create a Kubernetes secret with this demo key and certificate:

       .. code-block:: shell-session

           $ kubectl create secret tls demo-cert --key=bookinfo.cilium.rocks+1-key.pem --cert=bookinfo.cilium.rocks+1.pem

   .. group-tab:: cert-manager

       Let us install cert-manager:

       .. code-block:: shell-session

           $ helm repo add jetstack https://charts.jetstack.io
           $ helm install cert-manager jetstack/cert-manager --version v1.10.0 \
               --namespace cert-manager \
               --set installCRDs=true \
               --create-namespace \
               --set "extraArgs={--feature-gates=ExperimentalGatewayAPISupport=true}"

       Now, create a CA Issuer:

       .. parsed-literal::

           $ kubectl apply -f \ |SCM_WEB|\/examples/kubernetes/servicemesh/ca-issuer.yaml
