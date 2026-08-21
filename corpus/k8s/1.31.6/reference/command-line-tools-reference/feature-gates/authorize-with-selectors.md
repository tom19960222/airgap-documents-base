---
collection: k8s
version: "1.31.6"
title: "AuthorizeWithSelectors"
source_url: https://github.com/kubernetes/website/blob/release-1.31/content/en/docs/reference/command-line-tools-reference/feature-gates/authorize-with-selectors.md
fetched_at: 2026-01-16T10:18:07+05:30
---
Allows authorization to use field and label selectors.
Enables `fieldSelector` and `labelSelector` fields in the [SubjectAccessReview API](/docs/reference/kubernetes-api/authorization-resources/subject-access-review-v1/),
passes field and label selector information to [authorization webhooks](/docs/reference/access-authn-authz/webhook/),
enables `fieldSelector` and `labelSelector` functions in the [authorizer CEL library](https://pkg.go.dev/k8s.io/apiserver/pkg/cel/library#AuthzSelectors),
and enables checking `fieldSelector` and `labelSelector` fields in [authorization webhook `matchConditions`](/docs/reference/access-authn-authz/authorization/#using-configuration-file-for-authorization).
