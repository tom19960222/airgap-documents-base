---
collection: gitlab
version: "17.9.8"
title: "Web Commits API"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/api/web_commits.md
fetched_at: 2025-05-07T10:05:15Z
---
- Tier: Free
- Offering: GitLab.com, GitLab Self-Managed, GitLab Dedicated

**History:**

- [Introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/442533) in GitLab 17.4.

Use this API to retrieve information about commits created with the Web UI.

## Get public signing key

Get the GitLab public key for signing web commits.

```plaintext
GET /web_commits/public_key
```

If successful, returns [`200`](rest/troubleshooting.md#status-codes) and the following
response attribute:

| Attribute    | Type   | Description                                 |
|--------------|--------|---------------------------------------------|
| `public_key` | string | GitLab public key for signing web commits.  |

Example request:

```shell
curl --url "https://gitlab.example.com/api/v4/web_commits/public_key"
```

Example response:

```json
[
  {
    public_key: "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAIEAiPWx6WM4lhHNedGfBpPJNPpZ7yKu+dnn1SJejgt4596k6YjzGGphH2TUxwKzxcKDKKezwkpfnxPkSMkuEspGRt/aZZ9wa++Oi7Qkr8prgHc4soW6NUlfDzpvZK2H5E7eQaSeP3SAwGmQKUFHCddNaP0L+hM7zhFNzjFvpaMgJw0=\""
  }
]
```
