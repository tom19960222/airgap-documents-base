---
collection: k8s
version: "1.31.6"
title: "Define Environment Variables for a Container"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/tasks/inject-data-application/define-environment-variable-container.md
fetched_at: 2026-01-16T10:18:07+05:30
---
<!-- overview -->

This page shows how to define environment variables for a container
in a Kubernetes Pod.

## Before you begin

You need to have a Kubernetes cluster, and the kubectl command-line tool must
be configured to communicate with your cluster. It is recommended to run this tutorial on a cluster with at least two nodes that are not acting as control plane hosts. If you do not already have a
cluster, you can create one by using
[minikube](https://minikube.sigs.k8s.io/docs/tutorials/multi_node/)
or you can use one of these Kubernetes playgrounds:

* [Killercoda](https://killercoda.com/playgrounds/scenario/kubernetes)
* [Play with Kubernetes](https://labs.play-with-k8s.com/)

<!-- steps -->

## Define an environment variable for a container

When you create a Pod, you can set environment variables for the containers
that run in the Pod. To set environment variables, include the `env` or
`envFrom` field in the configuration file.

The `env` and `envFrom` fields have different effects.

`env`
: allows you to set environment variables for a container, specifying a value directly for each variable that you name.

`envFrom`
: allows you to set environment variables for a container by referencing either a ConfigMap or a Secret.
 When you use `envFrom`, all the key-value pairs in the referenced ConfigMap or Secret
 are set as environment variables for the container.
 You can also specify a common prefix string.

You can read more about [ConfigMap](/docs/tasks/configure-pod-container/configure-pod-configmap/#configure-all-key-value-pairs-in-a-configmap-as-container-environment-variables)
and [Secret](/docs/tasks/inject-data-application/distribute-credentials-secure/#configure-all-key-value-pairs-in-a-secret-as-container-environment-variables).

This page explains how to use `env`.

In this exercise, you create a Pod that runs one container. The configuration
file for the Pod defines an environment variable with name `DEMO_GREETING` and
value `"Hello from the environment"`. Here is the configuration manifest for the
Pod:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: envar-demo
  labels:
    purpose: demonstrate-envars
spec:
  containers:
  - name: envar-demo-container
    image: gcr.io/google-samples/hello-app:2.0
    env:
    - name: DEMO_GREETING
      value: "Hello from the environment"
    - name: DEMO_FAREWELL
      value: "Such a sweet sorrow"
```

1. Create a Pod based on that manifest:

   ```shell
   kubectl apply -f https://k8s.io/examples/pods/inject/envars.yaml
   ```

1. List the running Pods:

   ```shell
   kubectl get pods -l purpose=demonstrate-envars
   ```

   The output is similar to:

   ```
   NAME            READY     STATUS    RESTARTS   AGE
   envar-demo      1/1       Running   0          9s
   ```

1. List the Pod's container environment variables:

   ```shell
   kubectl exec envar-demo -- printenv
   ```

   The output is similar to this:

   ```
   NODE_VERSION=4.4.2
   EXAMPLE_SERVICE_PORT_8080_TCP_ADDR=10.3.245.237
   HOSTNAME=envar-demo
   ...
   DEMO_GREETING=Hello from the environment
   DEMO_FAREWELL=Such a sweet sorrow
   ```

> **Note:**
>
> The environment variables set using the `env` or `envFrom` field
> override any environment variables specified in the container image.

> **Note:**
>
> Environment variables may reference each other, however ordering is important.
> Variables making use of others defined in the same context must come later in
> the list. Similarly, avoid circular references.

## Using environment variables inside of your config

Environment variables that you define in a Pod's configuration under 
`.spec.containers[*].env[*]` can be used elsewhere in the configuration, for 
example in commands and arguments that you set for the Pod's containers.
In the example configuration below, the `GREETING`, `HONORIFIC`, and
`NAME` environment variables are set to `Warm greetings to`, `The Most
Honorable`, and `Kubernetes`, respectively. The environment variable 
`MESSAGE` combines the set of all these environment variables and then uses it 
as a CLI argument passed to the `env-print-demo` container.

Environment variable names consist of letters, numbers, underscores,
dots, or hyphens, but the first character cannot be a digit.
If the `RelaxedEnvironmentVariableValidation` [feature gate](/docs/reference/command-line-tools-reference/feature-gates/) is enabled,
all [printable ASCII characters](https://www.ascii-code.com/characters/printable-characters) except "=" may be used for environment variable names.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: print-greeting
spec:
  containers:
  - name: env-print-demo
    image: bash
    env:
    - name: GREETING
      value: "Warm greetings to"
    - name: HONORIFIC
      value: "The Most Honorable"
    - name: NAME
      value: "Kubernetes"
    - name: MESSAGE
      value: "$(GREETING) $(HONORIFIC) $(NAME)"
    command: ["echo"]
    args: ["$(MESSAGE)"]
```

Upon creation, the command `echo Warm greetings to The Most Honorable Kubernetes` is run on the container.

## What's next

* Learn more about [environment variables](/docs/tasks/inject-data-application/environment-variable-expose-pod-information/).
* Learn about [using secrets as environment variables](/docs/concepts/configuration/secret/#using-secrets-as-environment-variables).
* See [EnvVarSource](/docs/reference/generated/kubernetes-api/version/#envvarsource-v1-core).
