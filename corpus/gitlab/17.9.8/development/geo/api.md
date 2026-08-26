---
collection: gitlab
version: "17.9.8"
title: "Geo API"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/development/geo/api.md
fetched_at: 2025-05-07T10:05:15Z
---
- Tier: Premium, Ultimate
- Offering: GitLab Self-Managed
- Status: Beta

The Geo API is used internally by GitLab components to assist in coordinating Geo actions. It is inaccessible to admins or users.

## Fetch pipeline refs

**History:**

- [Introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/415179) in GitLab 16.7.

This method returns a list of branches matching `pipeline/refs/X` that exist on the repository for `gl_repository` on the current Geo node. This endpoint is used by runners registered with a secondary Geo instance to check if a repository is up to date.

```plaintext
GET /geo/repositories/:gl_repository/pipeline_refs
```

Supported attributes:

| Attribute                | Type     | Required | Description           |
|--------------------------|----------|----------|-----------------------|
| `gl_repository`          | string   | Yes      | The `gl_repository` ID of the repository to query |

If successful, returns [`200`](../../api/rest/troubleshooting.md#status-codes) and the following
response attributes:

| Attribute                | Type     | Description           |
|--------------------------|----------|-----------------------|
| `attribute`              | 'array' | An array of ids matching `refs/pipeline/X` created for running pipelines. |
