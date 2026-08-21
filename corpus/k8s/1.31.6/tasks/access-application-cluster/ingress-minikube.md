---
collection: k8s
version: "1.31.6"
title: "Set up Ingress on Minikube with the NGINX Ingress Controller"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/tasks/access-application-cluster/ingress-minikube.md
fetched_at: 2026-01-16T10:18:07+05:30
---
<!-- overview -->

An [Ingress](/docs/concepts/services-networking/ingress/) is an API object that defines rules
which allow external access to services in a cluster. An
[Ingress controller](/docs/concepts/services-networking/ingress-controllers/)
fulfills the rules set in the Ingress.

This page shows you how to set up a simple Ingress which routes requests to Service 'web' or
'web2' depending on the HTTP URI.

## Before you begin

This tutorial assumes that you are using `minikube` to run a local Kubernetes cluster.
Visit [Install tools](/docs/tasks/tools/#minikube) to learn how to install `minikube`.

> **Note:**
>
> This tutorial uses a container that requires the AMD64 architecture. 
> If you are using minikube on a computer with a different CPU architecture,
> you could try using minikube with a driver that can emulate AMD64.
> For example, the Docker Desktop driver can do this.

You need to have a Kubernetes cluster, and the kubectl command-line tool must
be configured to communicate with your cluster. It is recommended to run this tutorial on a cluster with at least two nodes that are not acting as control plane hosts. If you do not already have a
cluster, you can create one by using
[minikube](https://minikube.sigs.k8s.io/docs/tutorials/multi_node/)
or you can use one of these Kubernetes playgrounds:

* [Killercoda](https://killercoda.com/playgrounds/scenario/kubernetes)
* [Play with Kubernetes](https://labs.play-with-k8s.com/)
 
If you are using an older Kubernetes version, switch to the documentation for that version.

### Create a minikube cluster

If you haven't already set up a cluster locally, run `minikube start` to create a cluster.

<!-- steps -->

## Enable the Ingress controller

1. To enable the NGINX Ingress controller, run the following command:

   ```shell
   minikube addons enable ingress
   ```

1. Verify that the NGINX Ingress controller is running

   ```shell
   kubectl get pods -n ingress-nginx
   ```

   

> **Note:**
>
> It can take up to a minute before you see these pods running OK.

   The output is similar to:

   ```none
   NAME                                        READY   STATUS      RESTARTS    AGE
   ingress-nginx-admission-create-g9g49        0/1     Completed   0          11m
   ingress-nginx-admission-patch-rqp78         0/1     Completed   1          11m
   ingress-nginx-controller-59b45fb494-26npt   1/1     Running     0          11m
   ```

## Deploy a hello, world app

1. Create a Deployment using the following command:

   ```shell
   kubectl create deployment web --image=gcr.io/google-samples/hello-app:1.0
   ```

   The output should be:

   ```none
   deployment.apps/web created
   ```
   
   Verify that the Deployment is in a Ready state:
   
   ```shell
   kubectl get deployment web 
   ```  

   The output should be similar to:

   ```none
   NAME   READY   UP-TO-DATE   AVAILABLE   AGE
   web    1/1     1            1           53s
   ``` 
    
    

1. Expose the Deployment:

   ```shell
   kubectl expose deployment web --type=NodePort --port=8080
   ```

   The output should be:

   ```none
   service/web exposed
   ```

1. Verify the Service is created and is available on a node port:

   ```shell
   kubectl get service web
   ```

   The output is similar to:

   ```none
   NAME      TYPE       CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
   web       NodePort   10.104.133.249   <none>        8080:31637/TCP   12m
   ```

1. Visit the Service via NodePort, using the [`minikube service`](https://minikube.sigs.k8s.io/docs/handbook/accessing/#using-minikube-service-with-tunnel) command. Follow the instructions for your platform:

   
   

**Tab: Linux**

   
   ```shell
   minikube service web --url
   ```
   The output is similar to:
   ```none
   http://172.17.0.15:31637
   ```
   Invoke the URL obtained in the output of the previous step:
   ```shell
   curl http://172.17.0.15:31637 
   ```
   
   

**Tab: MacOS**

   ```shell
   # The command must be run in a separate terminal.
   minikube service web --url 
   ```
   The output is similar to:
   ```none
   http://127.0.0.1:62445
   ! Because you are using a Docker driver on darwin, the terminal needs to be open to run it.
   ```
   From a different terminal, invoke the URL obtained in the output of the previous step:
   ```shell
   curl http://127.0.0.1:62445 
   ```
   
   
   <br>
   The output is similar to:

   ```none
   Hello, world!
   Version: 1.0.0
   Hostname: web-55b8c6998d-8k564
   ```

   You can now access the sample application via the Minikube IP address and NodePort.
   The next step lets you access the application using the Ingress resource.

## Create an Ingress

The following manifest defines an Ingress that sends traffic to your Service via
`hello-world.example`.

1. Create `example-ingress.yaml` from the following file:

   
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: example-ingress
spec:
  ingressClassName: nginx
  rules:
    - host: hello-world.example
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: web
                port:
                  number: 8080
```

1. Create the Ingress object by running the following command:

   ```shell
   kubectl apply -f https://k8s.io/examples/service/networking/example-ingress.yaml
   ```

   The output should be:

   ```none
   ingress.networking.k8s.io/example-ingress created
   ```

1. Verify the IP address is set:

   ```shell
   kubectl get ingress
   ```

   

> **Note:**
>
> This can take a couple of minutes.

   You should see an IPv4 address in the `ADDRESS` column; for example:

   ```none
   NAME              CLASS   HOSTS                 ADDRESS        PORTS   AGE
   example-ingress   nginx   hello-world.example   172.17.0.15    80      38s
   ```

1. Verify that the Ingress controller is directing traffic, by following the instructions for your platform:

   

> **Note:**
>
> The network is limited if using the Docker driver on MacOS (Darwin) and the Node IP is not reachable directly. To get ingress to work you’ll need to open a new terminal and run `minikube tunnel`.  
>    `sudo` permission is required for it, so provide the password when prompted.

    

   
   

**Tab: Linux**

   ```shell
   curl --resolve "hello-world.example:80:$( minikube ip )" -i http://hello-world.example
   ```
   
   

**Tab: MacOS**

   ```shell
   minikube tunnel
   ```
   The output is similar to:

   ```none
   Tunnel successfully started

   NOTE: Please do not close this terminal as this process must stay alive for the tunnel to be accessible ...

   The service/ingress example-ingress requires privileged ports to be exposed: [80 443]
   sudo permission will be asked for it.
   Starting tunnel for service example-ingress.
   ```

   From within a new terminal, invoke the following command:
   ```shell
   curl --resolve "hello-world.example:80:127.0.0.1" -i http://hello-world.example
   ```

   
  
   <br>
   You should see:

   ```none
   Hello, world!
   Version: 1.0.0
   Hostname: web-55b8c6998d-8k564
   ```

1. Optionally, you can also visit `hello-world.example` from your browser.

   Add a line to the bottom of the `/etc/hosts` file on
     your computer (you will need administrator access):

     
     

**Tab: Linux**

   Look up the external IP address as reported by minikube
   ```none
     minikube ip 
   ``` 
   <br>

   ```none
     172.17.0.15 hello-world.example
   ```
   
   

> **Note:**
>
> Change the IP address to match the output from `minikube ip`.

   
     

**Tab: MacOS**

 
   ```none
   127.0.0.1 hello-world.example
   ```
     
     
   
     <br>
   
     After you make this change, your web browser sends requests for
     `hello-world.example` URLs to Minikube.

## Create a second Deployment

1. Create another Deployment using the following command:

   ```shell
   kubectl create deployment web2 --image=gcr.io/google-samples/hello-app:2.0
   ```

   The output should be:

   ```none
   deployment.apps/web2 created
   ```
   Verify that the Deployment is in a Ready state:

   ```shell
   kubectl get deployment web2 
   ```  

   The output should be similar to:

   ```none
   NAME   READY   UP-TO-DATE   AVAILABLE   AGE
   web2   1/1     1            1           16s
   ``` 

1. Expose the second Deployment:

   ```shell
   kubectl expose deployment web2 --port=8080 --type=NodePort
   ```

   The output should be:

   ```none
   service/web2 exposed
   ```

## Edit the existing Ingress {#edit-ingress}

1. Edit the existing `example-ingress.yaml` manifest, and add the
   following lines at the end:

    ```yaml
    - path: /v2
      pathType: Prefix
      backend:
        service:
          name: web2
          port:
            number: 8080
    ```

1. Apply the changes:

   ```shell
   kubectl apply -f example-ingress.yaml
   ```

   You should see:

   ```none
   ingress.networking/example-ingress configured
   ```

## Test your Ingress

1. Access the 1st version of the Hello World app.

   
   

**Tab: Linux**

   ```shell
   curl --resolve "hello-world.example:80:$( minikube ip )" -i http://hello-world.example
   ```
   
   

**Tab: MacOS**

   ```shell
   minikube tunnel
   ```
   The output is similar to:

   ```none
   Tunnel successfully started

   NOTE: Please do not close this terminal as this process must stay alive for the tunnel to be accessible ...

   The service/ingress example-ingress requires privileged ports to be exposed: [80 443]
   sudo permission will be asked for it.
   Starting tunnel for service example-ingress.
   ```

   From within a new terminal, invoke the following command:
   ```shell
   curl --resolve "hello-world.example:80:127.0.0.1" -i http://hello-world.example
   ```

   
   
   <br>

   The output is similar to:

   ```none
   Hello, world!
   Version: 1.0.0
   Hostname: web-55b8c6998d-8k564
   ```

1. Access the 2nd version of the Hello World app.

   
   

**Tab: Linux**

   ```shell
   curl --resolve "hello-world.example:80:$( minikube ip )" -i http://hello-world.example/v2
   ```
   
   

**Tab: MacOS**

   ```shell
   minikube tunnel
   ```
   The output is similar to:

   ```none
   Tunnel successfully started

   NOTE: Please do not close this terminal as this process must stay alive for the tunnel to be accessible ...

   The service/ingress example-ingress requires privileged ports to be exposed: [80 443]
   sudo permission will be asked for it.
   Starting tunnel for service example-ingress.
   ```

   From within a new terminal, invoke the following command:
   ```shell
   curl --resolve "hello-world.example:80:127.0.0.1" -i http://hello-world.example/v2
   ```

   
   

   The output is similar to:

   ```none
   Hello, world!
   Version: 2.0.0
   Hostname: web2-75cd47646f-t8cjk
   ```

   

> **Note:**
>
> If you did the optional step to update `/etc/hosts`, you can also visit `hello-world.example` and
>    `hello-world.example/v2` from your browser.

## What's next

* Read more about [Ingress](/docs/concepts/services-networking/ingress/)
* Read more about [Ingress Controllers](/docs/concepts/services-networking/ingress-controllers/)
* Read more about [Services](/docs/concepts/services-networking/service/)
