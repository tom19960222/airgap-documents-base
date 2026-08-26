---
collection: gitlab
version: "17.9.8"
title: "Avatar API"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/api/avatar.md
fetched_at: 2025-05-07T10:05:15Z
---
- Tier: Free, Premium, Ultimate
- Offering: GitLab.com, GitLab Self-Managed, GitLab Dedicated

Use this API to interact with user avatars.

## Get details on an account avatar

Gets the URL of an account [avatar](../user/profile/_index.md#access-your-user-settings) associated with a given public email address. This endpoint does not require authentication.

- If successful, returns the URL of the avatar.
- If no account is associated with the given email address, returns results from external avatar services.
- If the public visibility is restricted and the request isn't authenticated, returns `403 Forbidden`.

```plaintext
GET /avatar?email=admin@example.com
```

Parameters:

| Attribute | Type    | Required | Description |
| --------- | ------- | -------- | ----------- |
| `email`   | string  | yes      | Public email address of the account. |
| `size`    | integer | no       | Single pixel dimension. Only used for avatar lookups at `Gravatar` or a configured `Libravatar` server. |

Example request:

```shell
curl --request GET \
  --url "https://gitlab.example.com/api/v4/avatar?email=admin@example.com&size=32"
```

Example response:

```json
{
  "avatar_url": "https://www.gravatar.com/avatar/e64c7d89f26bd1972efa854d13d7dd61?s=64&d=identicon"
}
```
