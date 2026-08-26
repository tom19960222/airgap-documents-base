---
collection: gitlab
version: "17.9.8"
title: "Package and container registry development guidelines"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/development/packages/_index.md
fetched_at: 2025-05-07T10:05:15Z
---
The documentation for package and container registry development is split into two groups.

## Package registry development

Development and architectural documentation for the package registry:

- [Debian repository structure](debian_repository.md)
- [Developing a new format](new_format_development.md)
- [Settings](settings.md)
- [Structure / Schema](structure.md)
- API documentation
  - [Composer](../../api/packages/composer.md)
  - [Conan](../../api/packages/conan.md)
  - [Debian](../../api/packages/debian.md)
  - [Generic](../../user/packages/generic_packages/_index.md)
  - [Go Proxy](../../api/packages/go_proxy.md)
  - [Helm](../../api/packages/helm.md)
  - [Maven](../../api/packages/maven.md)
  - [npm](../../api/packages/npm.md)
  - [NuGet](../../api/packages/nuget.md)
  - [PyPI](../../api/packages/pypi.md)
  - [Ruby Gems](../../api/packages/rubygems.md)

## Container registry development

Development and architectural documentation for the container registry

- [Dependency proxy structure](dependency_proxy.md)
- [Settings](settings.md)
- [Structure / Schema](structure.md)
- [Cleanup policies](cleanup_policies.md)

## Harbor registry development

Development and architectural documentation for the harbor registry

- [Development documentation](harbor_registry_development.md)
