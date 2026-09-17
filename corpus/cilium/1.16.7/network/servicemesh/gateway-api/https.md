---
collection: cilium
version: "1.16.7"
title: "HTTPS Example"
source_url: https://github.com/cilium/cilium/blob/2ab5f8da5915992a1e548c290105dbc08f4be52d/Documentation/network/servicemesh/gateway-api/https.rst
fetched_at: 2025-02-13T12:04:31Z
---
.. only:: not (epub or latex or html)

   WARNING: You are looking at unreleased Cilium documentation.
   Please use the official rendered version released here:
   https://docs.cilium.io

<a id="gs_gateway_https"></a>

# HTTPS Example

This example builds on the previous [gs_gateway_http](http.md#gs_gateway_http) and add TLS
termination for two HTTP routes. For simplicity, the second route to ``productpage``
is omitted.

.. literalinclude:: ../../../../examples/kubernetes/gateway/basic-https.yaml

Included file `Documentation/network/servicemesh/tls-cert.rst`:

## Create TLS Certificate and Private Key

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

## Deploy the Gateway and HTTPRoute

The Gateway configuration for this demo provides the similar routing to the
``details`` and ``productpage`` services.

.. tabs::

   .. group-tab:: Self-signed Certificate

       .. parsed-literal::

           $ kubectl apply -f \ |SCM_WEB|\/examples/kubernetes/gateway/basic-https.yaml

   .. group-tab:: cert-manager

       .. parsed-literal::

           $ kubectl apply -f \ |SCM_WEB|\/examples/kubernetes/gateway/basic-https.yaml

       To tell cert-manager that this Ingress needs a certificate, annotate the
       Gateway with the name of the CA issuer we previously created:

       .. code-block:: shell-session

           $ kubectl annotate gateway tls-gateway cert-manager.io/issuer=ca-issuer

       This creates a Certificate object along with a Secret containing the TLS
       certificate.

       .. code-block:: shell-session

           $ kubectl get certificate,secret demo-cert
           NAME                                    READY   SECRET      AGE
           certificate.cert-manager.io/demo-cert   True    demo-cert   29s
           NAME               TYPE                DATA   AGE
           secret/demo-cert   kubernetes.io/tls   3      29s

External IP address will be shown up in Gateway. Also, the host names should be shown up in
related HTTPRoutes.

```shell-session
$ kubectl get gateway tls-gateway
NAME          CLASS    ADDRESS         PROGRAMMED   AGE
tls-gateway   cilium   10.104.247.23   True         29s

$ kubectl get httproutes https-app-route-1 https-app-route-2
NAME                HOSTNAMES                      AGE
https-app-route-1   ["bookinfo.cilium.rocks"]      29s
https-app-route-2   ["hipstershop.cilium.rocks"]   29s
```

Update ``/etc/hosts`` with the host names and IP address of the Gateway:

```shell-session
$ sudo perl -ni -e 'print if !/\.cilium\.rocks$/d' /etc/hosts; sudo tee -a /etc/hosts \
  <<<"$(kubectl get gateway tls-gateway -o jsonpath='{.status.addresses[0].value}') bookinfo.cilium.rocks hipstershop.cilium.rocks"
```

## Make HTTPS Requests

.. tabs::

   .. group-tab:: Self-signed Certificate

       By specifying the CA's certificate on a curl request, you can say that you trust certificates
       signed by that CA.

       .. code-block:: shell-session

           $ curl --cacert minica.pem -v https://bookinfo.cilium.rocks/details/1
           $ curl --cacert minica.pem -v https://hipstershop.cilium.rocks/

       If you prefer, instead of supplying the CA you can specify ``-k`` to tell the
       curl client not to validate the server's certificate. Without either, you
       will get an error that the certificate was signed by an unknown authority.

       Specifying -v on the curl request, you can see that the TLS handshake took
       place successfully.

   .. group-tab:: cert-manager

       .. code-block:: shell-session

           $ curl https://bookinfo.cilium.rocks/details/1
           $ curl https://hipstershop.cilium.rocks/
