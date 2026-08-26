---
collection: gitlab
version: "17.9.8"
title: "Version API"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/api/version.md
fetched_at: 2025-05-07T10:05:15Z
---
- Tier: Free, Premium, Ultimate
- Offering: GitLab.com, GitLab Self-Managed, GitLab Dedicated

> **Note:**
>
> We recommend you use the [Metadata API](metadata.md) instead of the Version API.
> It contains additional information and is aligned with the GraphQL metadata endpoint.
> As of GitLab 15.5, the Version API is a mirror of the Metadata API.

Retrieves version information for the GitLab instance. Responds with `200 OK` for
authenticated users.

```plaintext
GET /version
```

```shell
curl --header "PRIVATE-TOKEN: <your_access_token>" \
  "https://gitlab.example.com/api/v4/version"
```

## Example responses

### GitLab 15.5 and later

See [Metadata API](metadata.md) for the response.

### GitLab 15.4 and earlier

```json
{
  "version": "8.13.0-pre",
  "revision": "4e963fe"
}
```
