---
collection: gitlab
version: "17.9.8"
title: "Supported package managers"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/user/packages/package_registry/supported_package_managers.md
fetched_at: 2025-05-07T10:05:15Z
---
- Tier: Free, Premium, Ultimate
- Offering: GitLab.com, GitLab Self-Managed, GitLab Dedicated

> **Warning:**
>
> Not all package manager formats are ready for production use.

The package registry supports the following package manager types:

| Package type                                      | Status |
|---------------------------------------------------|--------|
| [Composer](../composer_repository/_index.md)      | [Beta](https://gitlab.com/groups/gitlab-org/-/epics/6817) |
| [Conan](../conan_repository/_index.md)            | [Experiment](https://gitlab.com/groups/gitlab-org/-/epics/6816) |
| [Debian](../debian_repository/_index.md)          | [Experiment](https://gitlab.com/groups/gitlab-org/-/epics/6057) |
| [Generic packages](../generic_packages/_index.md) | Generally available     |
| [Go](../go_proxy/_index.md)                       | [Experiment](https://gitlab.com/groups/gitlab-org/-/epics/3043) |
| [Helm](../helm_repository/_index.md)              | [Beta](https://gitlab.com/groups/gitlab-org/-/epics/6366) |
| [Maven](../maven_repository/_index.md)            | Generally available      |
| [npm](../npm_registry/_index.md)                  | Generally available      |
| [NuGet](../nuget_repository/_index.md)            | Generally available      |
| [PyPI](../pypi_repository/_index.md)              | Generally available      |
| [Ruby gems](../rubygems_registry/_index.md)       | [Experiment](https://gitlab.com/groups/gitlab-org/-/epics/3200) |

[View what each status means](../../../policy/development_stages_support.md).

You can also use the [API](../../../api/packages.md) to administer the package registry.
