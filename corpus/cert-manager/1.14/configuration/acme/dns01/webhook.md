---
collection: cert-manager
version: "1.14"
title: "Webhook"
source_url: https://github.com/cert-manager/website/blob/d2e1bdfbbe23fcf24dcb68ab54353a65a4131c20/content/v1.14-docs/configuration/acme/dns01/webhook.md
fetched_at: 2026-09-15T21:21:15Z
app_version: "1.14.7"
---
The webhook `Issuer` is a generic ACME solver. The actual work is done by an
external service. Look at the respective documentation of
[`dns-providers`](../../../contributing/dns-providers.md) <!-- unresolved-source-link: target=../../../contributing/dns-providers.md -->.

View more webhook solvers at https://github.com/topics/cert-manager-webhook.

Here is an example of how webhook providers are to be configured. All `DNS01`
providers will contain their own specific configuration however all require a
`groupName` and `solverName` field.

```yaml
apiVersion: cert-manager.io/v1
kind: Issuer
metadata:
  name: example-issuer
spec:
  acme:
   ...
    solvers:
    - dns01:
        webhook:
          groupName: $WEBHOOK_GROUP_NAME
          solverName: $WEBHOOK_SOLVER_NAME
          config:
            ...
            <webhook-specific-configuration>
```
