---
collection: gitlab
version: "17.9.8"
title: "Client-side secret detection"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/user/application_security/secret_detection/client/_index.md
fetched_at: 2025-05-07T10:05:15Z
---
- Tier: Free, Premium, Ultimate
- Offering: GitLab.com, GitLab Self-Managed, GitLab Dedicated

**History:**

- [Introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/368434) in GitLab 15.11.
- Detection of personal access tokens with a custom prefix was [introduced](https://gitlab.com/gitlab-org/gitlab/-/issues/411146) in GitLab 16.1. GitLab Self-Managed only.

When you create an issue, propose a merge request, or write a comment, you might accidentally post a
secret. For example, you might paste in the details of an API request or an environment variable
that contains an authentication token. If a secret is leaked it could be used to do harm.

Client-side secret detection helps to minimize the risk of that happening. When you edit the
description or comment in an issue or merge request, GitLab checks if it contains a secret. If a
secret is found, a warning message is displayed. You can then edit the description or comment to
remove the secret before posting your message, or add the description or comment as it is. This
check occurs in your browser, so the secret is not revealed to anyone else unless you add it to
GitLab. The check is always on; you don't have to set it up.

Client-side secret detection checks only the following for secrets:

- Comments in issues or merge requests.
- Descriptions of issues or merge requests.

For details of which types of secrets are covered by client-side secret detection, see
[Detected secrets](../detected_secrets.md).
