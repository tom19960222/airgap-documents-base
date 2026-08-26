---
collection: gitlab
version: "17.9.8"
title: "Dependency Scanning compared to Container Scanning"
source_url: https://gitlab.com/gitlab-org/gitlab/-/blob/v17.9.8-ee/doc/user/application_security/comparison_dependency_and_container_scanning.md
fetched_at: 2025-05-07T10:05:15Z
---
GitLab offers both [Dependency Scanning](dependency_scanning/_index.md) and
[Container Scanning](container_scanning/_index.md) to ensure coverage for all of these
dependency types. To cover as much of your risk area as possible, we encourage you to use all of our
security scanning tools:

- Dependency Scanning analyzes your project and tells you which software dependencies,
  including upstream dependencies, have been included in your project, and what known
  risks the dependencies contain.
- Container Scanning analyzes your containers and tells you about known risks in the operating
  system's (OS) packages.

The following table summarizes which types of dependencies each scanning tool can detect:

| Feature                                                                                      | Dependency Scanning | Container Scanning              |
|----------------------------------------------------------------------------------------------|---------------------|---------------------------------|
| Identify the manifest, lock file, or static file that introduced the dependency              | [icon: check-circle]  | [icon: dotted-circle]             |
| Development dependencies                                                                     | [icon: check-circle]  | [icon: dotted-circle]             |
| Dependencies in a lock file committed to your repository                                     | [icon: check-circle]  | [icon: check-circle] <sup>1</sup> |
| Binaries built by Go                                                                         | [icon: dotted-circle] | [icon: check-circle] <sup>2</sup> |
| Dynamically-linked language-specific dependencies installed by the Operating System          | [icon: dotted-circle] | [icon: check-circle]              |
| Operating system dependencies                                                                | [icon: dotted-circle] | [icon: check-circle]              |
| Language-specific dependencies installed on the operating system (not built by your project) | [icon: dotted-circle] | [icon: check-circle]              |

1. Lock file must be present in the image to be detected.
1. [Report language-specific findings](container_scanning/_index.md#report-language-specific-findings) must be enabled, and binaries must be present in the image to be detected.
