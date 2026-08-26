---
collection: gitlab
version: "17.9.8"
title: "Database migrations API"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/api/database_migrations.md
fetched_at: 2025-05-07T10:05:15Z
---
- Tier: Free, Premium, Ultimate
- Offering: GitLab Self-Managed

**History:**

- [Introduced](https://gitlab.com/gitlab-org/gitlab/-/merge_requests/123408) in GitLab 16.2.

This API is for managing database migrations used in the development of GitLab.

All methods require administrator authorization.

## Mark a migration as successful

Mark pending migrations as successfully executed to prevent them from being
executed by the `db:migrate` tasks. Use this API to skip failing
migrations after they are determined to be safe to skip.

```plaintext
POST /api/v4/admin/migrations/:version/mark
```

| Attribute       | Type           | Required | Description                                                                                                                                                                                      |
|-----------------|----------------|----------|----------------------------------------------------------------------------------|
| `version`       | integer        | yes      | Version timestamp of the migration to be skipped                                 |
| `database`      | string         | no       | The database name for which the migration is skipped. Defaults to `main`.        |

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" \
   --url "https://gitlab.example.com/api/v4/admin/migrations/:version/mark"
```
