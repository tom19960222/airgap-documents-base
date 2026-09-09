---
collection: rook
version: "1.20.7"
title: "OpenShift Common Issues"
source_url: https://github.com/rook/rook/blob/95a8e2a8b61cf7f8152213939f995c88a2e72ab6/Documentation/Troubleshooting/openshift-common-issues.md
fetched_at: 2026-09-02T11:15:12-06:00
---
## Enable Monitoring in the Storage Dashboard

OpenShift Console uses OpenShift Prometheus for monitoring and populating data in Storage Dashboard. Additional configuration is required to monitor the Ceph Cluster from the storage dashboard.

1. Change the monitoring namespace to `openshift-monitoring`

    Change the namespace of the RoleBinding `rook-ceph-metrics` from `rook-ceph` to `openshift-monitoring` for the `prometheus-k8s` ServiceAccount in [rbac.yaml](https://github.com/rook/rook/blob/95a8e2a8b61cf7f8152213939f995c88a2e72ab6/deploy/examples/monitoring/rbac.yaml#L70).

    ```yaml
    subjects:
    - kind: ServiceAccount
    name: prometheus-k8s
    namespace: openshift-monitoring
    ```

2. Enable Ceph Cluster monitoring

    Follow [ceph-monitoring/prometheus-alerts](../Storage-Configuration/Monitoring/ceph-monitoring.md#prometheus-alerts).

3. Set the required label on the namespace

    ```console
    oc label namespace rook-ceph "openshift.io/cluster-monitoring=true"
    ```

## Troubleshoot Monitoring Issues

!!! attention
    Switch to `rook-ceph` namespace using `oc project rook-ceph`.

1. Ensure ceph-mgr pod is Running

    ```console
    $ oc get pods -l app=rook-ceph-mgr
    NAME            READY   STATUS    RESTARTS   AGE
    rook-ceph-mgr   1/1     Running   0          14h
    ```

2. Ensure service monitor is present

    ```console
    $ oc get servicemonitor rook-ceph-mgr
    NAME                          AGE
    rook-ceph-mgr                 14h
    ```

3. Ensure the prometheus rules object has been created

    ```console
    $ oc get prometheusrules -l prometheus=rook-prometheus
    NAME                    AGE
    prometheus-ceph-rules   14h
    ```
