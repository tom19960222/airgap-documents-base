---
collection: gitlab
version: "17.9.8"
title: "Packages and Registries"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/user/packages/_index.md
fetched_at: 2025-05-07T10:05:15Z
---
- Tier: Free, Premium, Ultimate
- Offering: GitLab.com, GitLab Self-Managed, GitLab Dedicated

The GitLab [package registry](package_registry/_index.md) acts as a private or public registry
for a variety of common package managers. You can publish and share
packages, which can be easily consumed as a dependency in downstream projects.

## Container registry

The GitLab [Container Registry](container_registry/_index.md) is a secure and private registry for container images. It's built on open source software and completely integrated within GitLab. Use GitLab CI/CD to create and publish images. Use the GitLab [API](../../api/container_registry.md) to manage the registry across groups and projects.

## Terraform Module Registry

The GitLab [Terraform Module Registry](terraform_module_registry/_index.md) is a secure and private registry for Terraform modules. You can use GitLab CI/CD to create and publish modules.

## Dependency Proxy

The [Dependency Proxy](dependency_proxy/_index.md) is a local proxy for frequently-used upstream images and packages.
