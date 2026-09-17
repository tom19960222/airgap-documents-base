---
collection: gatekeeper
version: "3.18.2"
title: "Emergency Recovery"
source_url: https://github.com/open-policy-agent/gatekeeper/blob/35f8bb97ec9badb12266e2e3f74465ef718c6237/website/docs/emergency.md
fetched_at: 2025-01-09T10:04:08-08:00
---
If a situation arises where Gatekeeper is preventing the cluster from operating correctly,
the webhook can be disabled. This will remove all Gatekeeper admission checks. Assuming
the default webhook name has been used this can be achieved by running:

`kubectl delete validatingwebhookconfigurations.admissionregistration.k8s.io gatekeeper-validating-webhook-configuration`

Redeploying the webhook configuration will re-enable Gatekeeper.
