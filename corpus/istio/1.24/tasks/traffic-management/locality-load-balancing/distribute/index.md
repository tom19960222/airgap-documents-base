---
collection: istio
version: "1.24"
title: "Locality weighted distribution"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/tasks/traffic-management/locality-load-balancing/distribute/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
description: "This guide demonstrates how to configure locality distribution."
---
Follow this guide to configure the distribution of traffic across localities.

Before proceeding, be sure to complete the steps under
[before you begin](../before-you-begin/index.md).

In this task, you will use the `curl` pod in `region1` `zone1` as the source of
requests to the `HelloWorld` service. You will configure Istio with the following
distribution across localities:

Region | Zone | % of traffic
------ | ---- | ------------
`region1` | `zone1` | 70
`region1` | `zone2` | 20
`region2` | `zone3` | 0
`region3` | `zone4` | 10

## Configure Weighted Distribution

Apply a `DestinationRule` that configures the following:

- [Outlier detection](https://istio.io/v1.24/docs/reference/config/networking/destination-rule/#OutlierDetection) <!-- unresolved-site-link: route=/docs/reference/config/networking/destination-rule -->
  for the `HelloWorld` service. This is required in order for distribution to
  function properly. In particular, it configures the sidecar proxies to know
  when endpoints for a service are unhealthy.

- [Weighted Distribution](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/upstream/load_balancing/locality_weight.html?highlight=weight)
  for the `HelloWorld` service as described in the table above.

```bash
$ kubectl --context="${CTX_PRIMARY}" apply -n sample -f - <<EOF
apiVersion: networking.istio.io/v1
kind: DestinationRule
metadata:
  name: helloworld
spec:
  host: helloworld.sample.svc.cluster.local
  trafficPolicy:
    loadBalancer:
      localityLbSetting:
        enabled: true
        distribute:
        - from: region1/zone1/*
          to:
            "region1/zone1/*": 70
            "region1/zone2/*": 20
            "region3/zone4/*": 10
    outlierDetection:
      consecutive5xxErrors: 100
      interval: 1s
      baseEjectionTime: 1m
EOF
```

## Verify the distribution

Call the `HelloWorld` service from the `curl` pod:

```bash
$ kubectl exec --context="${CTX_R1_Z1}" -n sample -c curl \
  "$(kubectl get pod --context="${CTX_R1_Z1}" -n sample -l \
  app=curl -o jsonpath='{.items[0].metadata.name}')" \
  -- curl -sSL helloworld.sample:5000/hello
```

Repeat this a number of times and verify that the number of replies
for each pod match the expected percentage in the table at the top of
this guide.

**Congratulations!** You successfully configured locality distribution!

## Next steps

[Cleanup](../cleanup/index.md)
resources and files from this task.
