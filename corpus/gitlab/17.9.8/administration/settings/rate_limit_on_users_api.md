---
collection: gitlab
version: "17.9.8"
title: "Rate limits on Users API"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/administration/settings/rate_limit_on_users_api.md
fetched_at: 2025-05-07T10:05:15Z
---
- Tier: Free, Premium, Ultimate
- Offering: GitLab Self-Managed

You can configure the per user rate limit for requests to [Users API](../../api/users.md).

To change the rate limit:

1. On the left sidebar, at the bottom, select **Admin**.
1. Select **Settings > Network**.
1. Expand **Users API rate limit**.
1. In the **Maximum requests per 10 minutes** text box, enter the new value.
1. Optional. In the **Users to exclude from the rate limit** box, list users allowed to exceed the limit.
1. Select **Save changes**.

This limit is:

- Applied independently per user.
- Not applied per IP address.

The default value is `300`.

Requests over the rate limit are logged into the `auth.log` file.

For example, if you set a limit of 300, requests to the `GET /users/:id` API endpoint
exceeding a rate of 300 per 10 minutes are blocked. Access to the endpoint is allowed after ten minutes have elapsed.
