---
collection: gitlab
version: "17.9.8"
title: "Mock CI"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/user/project/integrations/mock_ci.md
fetched_at: 2025-05-07T10:05:15Z
---
- Tier: Free, Premium, Ultimate
- Offering: GitLab.com, GitLab Self-Managed, GitLab Dedicated

> **Note:**
>
> This integration is only available in a development environment.

To set up the mock CI service server, respond to the following endpoints:

- `commit_status`: `#{project.namespace.path}/#{project.path}/status/#{sha}.json`
  - Have your service return `200 { status: ['failed'|'canceled'|'running'|'pending'|'success'|'success-with-warnings'|'skipped'|'not_found'] }`.
  - If the service returns a 404, the service is interpreted as `pending`.
- `build_page`: `#{project.namespace.path}/#{project.path}/status/#{sha}`
  - Where the build is linked to (whether or not it's implemented).

For an example Mock CI server, see [`gitlab-org/gitlab-mock-ci-service`](https://gitlab.com/gitlab-org/gitlab-mock-ci-service).
