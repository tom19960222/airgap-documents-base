---
collection: k8s
version: "1.31.6"
title: "Handling retriable and non-retriable pod failures with Pod failure policy"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/tasks/job/pod-failure-policy.md
fetched_at: 2026-01-16T10:18:07+05:30
---
(Feature gate: JobPodFailurePolicy)

<!-- overview -->

This document shows you how to use the
[Pod failure policy](/docs/concepts/workloads/controllers/job#pod-failure-policy),
in combination with the default
[Pod backoff failure policy](/docs/concepts/workloads/controllers/job#pod-backoff-failure-policy),
to improve the control over the handling of container- or Pod-level failure
within a Job.

The definition of Pod failure policy may help you to:
* better utilize the computational resources by avoiding unnecessary Pod retries.
* avoid Job failures due to Pod disruptions (such preemption,
API-initiated eviction
or taint-based eviction).

## Before you begin

You should already be familiar with the basic use of [Job](/docs/concepts/workloads/controllers/job/).

You need to have a Kubernetes cluster, and the kubectl command-line tool must
be configured to communicate with your cluster. It is recommended to run this tutorial on a cluster with at least two nodes that are not acting as control plane hosts. If you do not already have a
cluster, you can create one by using
[minikube](https://minikube.sigs.k8s.io/docs/tutorials/multi_node/)
or you can use one of these Kubernetes playgrounds:

* [Killercoda](https://killercoda.com/playgrounds/scenario/kubernetes)
* [Play with Kubernetes](https://labs.play-with-k8s.com/)
 

## Using Pod failure policy to avoid unnecessary Pod retries

With the following example, you can learn how to use Pod failure policy to
avoid unnecessary Pod restarts when a Pod failure indicates a non-retriable
software bug.

First, create a Job based on the config:

```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: job-pod-failure-policy-failjob
spec:
  completions: 8
  parallelism: 2
  template:
    spec:
      restartPolicy: Never
      containers:
      - name: main
        image: docker.io/library/bash:5
        command: ["bash"]
        args:
        - -c
        - echo "Hello world! I'm going to exit with 42 to simulate a software bug." && sleep 30 && exit 42
  backoffLimit: 6
  podFailurePolicy:
    rules:
    - action: FailJob
      onExitCodes:
        containerName: main
        operator: In
        values: [42]
```

by running:

```sh
kubectl create -f job-pod-failure-policy-failjob.yaml
```

After around 30s the entire Job should be terminated. Inspect the status of the Job by running:

```sh
kubectl get jobs -l job-name=job-pod-failure-policy-failjob -o yaml
```

In the Job status, the following conditions display:
- `FailureTarget` condition: has a `reason` field set to `PodFailurePolicy` and
  a `message` field with more information about the termination, like
  `Container main for pod default/job-pod-failure-policy-failjob-8ckj8 failed with exit code 42 matching FailJob rule at index 0`.
  The Job controller adds this condition as soon as the Job is considered a failure.
  For details, see [Termination of Job Pods](/docs/concepts/workloads/controllers/job/#termination-of-job-pods).
- `Failed` condition: same `reason` and `message` as the `FailureTarget`
  condition. The Job controller adds this condition after all of the Job's Pods
  are terminated.

For comparison, if the Pod failure policy was disabled it would take 6 retries
of the Pod, taking at least 2 minutes.

### Clean up

Delete the Job you created:

```sh
kubectl delete jobs/job-pod-failure-policy-failjob
```

The cluster automatically cleans up the Pods.

## Using Pod failure policy to ignore Pod disruptions

With the following example, you can learn how to use Pod failure policy to
ignore Pod disruptions from incrementing the Pod retry counter towards the
`.spec.backoffLimit` limit.

> **Caution:**
>
> Timing is important for this example, so you may want to read the steps before
> execution. In order to trigger a Pod disruption it is important to drain the
> node while the Pod is running on it (within 90s since the Pod is scheduled).

1. Create a Job based on the config:

   
```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: job-pod-failure-policy-ignore
spec:
  completions: 4
  parallelism: 2
  template:
    spec:
      restartPolicy: Never
      containers:
      - name: main
        image: docker.io/library/bash:5
        command: ["bash"]
        args:
        - -c
        - echo "Hello world! I'm going to exit with 0 (success)." && sleep 90 && exit 0
  backoffLimit: 0
  podFailurePolicy:
    rules:
    - action: Ignore
      onPodConditions:
      - type: DisruptionTarget
```

   by running:

   ```sh
   kubectl create -f job-pod-failure-policy-ignore.yaml
   ```

2. Run this command to check the `nodeName` the Pod is scheduled to:

   ```sh
   nodeName=$(kubectl get pods -l job-name=job-pod-failure-policy-ignore -o jsonpath='{.items[0].spec.nodeName}')
   ```

3. Drain the node to evict the Pod before it completes (within 90s):
   
   ```sh
   kubectl drain nodes/$nodeName --ignore-daemonsets --grace-period=0
   ```

4. Inspect the `.status.failed` to check the counter for the Job is not incremented:

   ```sh
   kubectl get jobs -l job-name=job-pod-failure-policy-ignore -o yaml
   ```

5. Uncordon the node:

   ```sh
   kubectl uncordon nodes/$nodeName
   ```

The Job resumes and succeeds.

For comparison, if the Pod failure policy was disabled the Pod disruption would
result in terminating the entire Job (as the `.spec.backoffLimit` is set to 0).

### Cleaning up

Delete the Job you created:

```sh
kubectl delete jobs/job-pod-failure-policy-ignore
```

The cluster automatically cleans up the Pods.

## Using Pod failure policy to avoid unnecessary Pod retries based on custom Pod Conditions

With the following example, you can learn how to use Pod failure policy to
avoid unnecessary Pod restarts based on custom Pod Conditions.

> **Note:**
>
> The example below works since version 1.27 as it relies on transitioning of
> deleted pods, in the `Pending` phase, to a terminal phase
> (see: [Pod Phase](/docs/concepts/workloads/pods/pod-lifecycle/#pod-phase)).

1. First, create a Job based on the config:

   
```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: job-pod-failure-policy-config-issue
spec:
  completions: 8
  parallelism: 2
  template:
    spec:
      restartPolicy: Never
      containers:
      - name: main
        image: "non-existing-repo/non-existing-image:example"
  backoffLimit: 6
  podFailurePolicy:
    rules:
    - action: FailJob
      onPodConditions:
      - type: ConfigIssue
```

   by running:

   ```sh
   kubectl create -f job-pod-failure-policy-config-issue.yaml
   ```

   Note that, the image is misconfigured, as it does not exist.

2. Inspect the status of the job's Pods by running:

   ```sh
   kubectl get pods -l job-name=job-pod-failure-policy-config-issue -o yaml
   ```

   You will see output similar to this:
   ```yaml
   containerStatuses:
   - image: non-existing-repo/non-existing-image:example
      ...
      state:
      waiting:
         message: Back-off pulling image "non-existing-repo/non-existing-image:example"
         reason: ImagePullBackOff
         ...
   phase: Pending
   ```

   Note that the pod remains in the `Pending` phase as it fails to pull the
   misconfigured image. This, in principle, could be a transient issue and the
   image could get pulled. However, in this case, the image does not exist so
   we indicate this fact by a custom condition.

3. Add the custom condition. First prepare the patch by running:

   ```sh
   cat <<EOF > patch.yaml
   status:
     conditions:
     - type: ConfigIssue
       status: "True"
       reason: "NonExistingImage"
       lastTransitionTime: "$(date -u +"%Y-%m-%dT%H:%M:%SZ")"
   EOF
   ```
   Second, select one of the pods created by the job by running:
   ```
   podName=$(kubectl get pods -l job-name=job-pod-failure-policy-config-issue -o jsonpath='{.items[0].metadata.name}')
   ```

   Then, apply the patch on one of the pods by running the following command:

   ```sh
   kubectl patch pod $podName --subresource=status --patch-file=patch.yaml
   ```

   If applied successfully, you will get a notification like this:

   ```sh
   pod/job-pod-failure-policy-config-issue-k6pvp patched
   ```

4. Delete the pod to transition it to `Failed` phase, by running the command:

   ```sh
   kubectl delete pods/$podName
   ```

5. Inspect the status of the Job by running:

   ```sh
   kubectl get jobs -l job-name=job-pod-failure-policy-config-issue -o yaml
   ```

   In the Job status, see a job `Failed` condition with the field `reason`
   equal `PodFailurePolicy`. Additionally, the `message` field contains a
   more detailed information about the Job termination, such as:
   `Pod default/job-pod-failure-policy-config-issue-k6pvp has condition ConfigIssue matching FailJob rule at index 0`.

> **Note:**
>
> In a production environment, the steps 3 and 4 should be automated by a
> user-provided controller.

### Cleaning up

Delete the Job you created:

```sh
kubectl delete jobs/job-pod-failure-policy-config-issue
```

The cluster automatically cleans up the Pods.

## Alternatives

You could rely solely on the
[Pod backoff failure policy](/docs/concepts/workloads/controllers/job#pod-backoff-failure-policy),
by specifying the Job's `.spec.backoffLimit` field. However, in many situations
it is problematic to find a balance between setting a low value for `.spec.backoffLimit`
 to avoid unnecessary Pod retries, yet high enough to make sure the Job would
not be terminated by Pod disruptions.
