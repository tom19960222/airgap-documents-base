---
collection: gitlab
version: "17.9.8"
title: "Smoke Tests"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/development/testing_guide/smoke.md
fetched_at: 2025-05-07T10:05:15Z
---
It is imperative in any testing suite that we have Smoke Tests. In short, smoke
tests run quick end-to-end functional tests from GitLab QA and are
designed to run against the specified environment to ensure that basic
functionality is working.

Our suite consists of this basic functionality coverage:

- User standard authentication
- SSH Key creation and addition to a user
- Project simple creation
- Project creation with Auto-DevOps enabled
- Issue creation
- Issue user mentions
- Merge Request creation
- Snippet creation

Smoke tests have the `:smoke` RSpec metadata.

## Health check suite

This is a very small subset smoke tests with the `:health_check` RSpec metadata.
Its function is to monitor the status and health of the application.

See [End-to-end Testing](end_to_end/_index.md) for more details about
end-to-end tests.

---

[Return to Testing documentation](_index.md)
