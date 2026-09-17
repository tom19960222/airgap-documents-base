---
collection: istio
version: "1.24"
title: "PortNameIsNotUnderNamingConvention"
source_url: https://github.com/istio/istio.io/blob/34199a22213d0bbfe10ab1759d89242ee752ac12/content/en/docs/reference/config/analysis/ist0118/index.md
fetched_at: 2025-08-28T08:00:11-04:00
app_version: "1.24.0"
---
This message occurs when the port doesn't follow the [Istio service port naming convention](../../../../ops/configuration/traffic-management/protocol-selection/index.md)
or the port is unnamed.

## Example

You will receive this message:

```plain
Info [IST0118] (Service httpbin.default) Port name foo-http (port: 80, targetPort: 80) doesn't follow the naming convention of Istio port.
```

when your cluster has following service:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: httpbin
  labels:
    app: httpbin
spec:
  ports:
  - name: foo-http
    port: 8000
    targetPort: 80
  selector:
    app: httpbin
```

In this example, the port name `foo-http` does not follow the syntax: `name: <protocol>[-<suffix>]`.

## How to resolve

- If you know the protocol the service port is serving, rename the port with `<protocol>[-<suffix>]` format;
- If you don't know the protocol the service port is serving, you need to [query metrics from Prometheus](../../../../tasks/observability/metrics/querying-metrics/index.md)
    - Run query `istio_requests_total{reporter="destination",destination_service_name="SERVICE_NAME",response_code="200"}[TIME_RANGE]`. If you are using Telemetry metric overrides,
      you can also run query `istio_requests_total{reporter="destination",destination_service_name="SERVICE_NAME",response_code="200",destination_port="TARGET_PORT"}[TIME_RANGE]`.
    - If there are outputs, you can find the `request_protocol` from the record. E.g., if the `request_protocol` is "http", rename port to "http-foo";
    - If there is no output, you can leave the port as it is.
