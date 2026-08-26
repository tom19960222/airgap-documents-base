---
collection: gitlab
version: "17.9.8"
title: "SPDX license list import Rake task"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/raketasks/spdx.md
fetched_at: 2025-05-07T10:05:15Z
---
- Tier: Ultimate
- Offering: GitLab Self-Managed

GitLab provides a Rake task for uploading a fresh copy of the [SPDX license list](https://spdx.org/licenses/)
to a GitLab instance. This list is needed for matching the names of [License approval policies](../user/compliance/license_approval_policies.md).

To import a fresh copy of the PDX license list, run:

```shell
# omnibus-gitlab
sudo gitlab-rake gitlab:spdx:import

# source installations
bundle exec rake gitlab:spdx:import RAILS_ENV=production
```

To perform this task in the [offline environment](../user/application_security/offline_deployments/_index.md#defining-offline-environments),
an outbound connection to [`licenses.json`](https://spdx.org/licenses/licenses.json) should be
allowed.
