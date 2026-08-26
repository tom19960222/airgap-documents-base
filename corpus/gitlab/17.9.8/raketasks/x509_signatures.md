---
collection: gitlab
version: "17.9.8"
title: "X.509 signatures Rake task"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/raketasks/x509_signatures.md
fetched_at: 2025-05-07T10:05:15Z
---
- Tier: Free, Premium, Ultimate
- Offering: GitLab Self-Managed

When [signing commits with X.509](../user/project/repository/signed_commits/x509.md),
the trust anchor might change and the signatures stored in the database must be updated.

## Update all X.509 signatures

This task:

- Iterates through all X.509-signed commits.
- Updates their verification status based on the current certificate store.
- Modifies only the database entries for the signatures.
- Leaves the commits unchanged.

To update all X.509 signatures, run:

**Tab: Linux package (Omnibus)**

```shell
sudo gitlab-rake gitlab:x509:update_signatures
```

**Tab: Self-compiled (source)**

```shell
sudo -u git -H bundle exec rake gitlab:x509:update_signatures RAILS_ENV=production
```
