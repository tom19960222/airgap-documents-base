---
collection: ansible
version: "8"
title: "Ansible-core 2.12"
source_url: https://docs.ansible.com/projects/ansible/8/roadmap/ROADMAP_2_12.html
fetched_at: 2026-07-28T00:59:42+00:00
---
# Ansible-core 2.12

- [Release Schedule](ROADMAP_2_12.md#release-schedule)

  - [Expected](ROADMAP_2_12.md#expected)
- [Release Manager](ROADMAP_2_12.md#release-manager)

  - [Planned work](ROADMAP_2_12.md#planned-work)
  - [Delayed work](ROADMAP_2_12.md#delayed-work)

## [Release Schedule](ROADMAP_2_12.md#id1)

### [Expected](ROADMAP_2_12.md#id2)

PRs must be raised well in advance of the dates below to have a chance of being included in this ansible-core release.

> **Note:**
>
> There is no Alpha phase in 2.12.

> **Note:**
>
> Dates subject to change.

- 2021-09-24 Feature Freeze (and `stable-2.12` branching from `devel`)
  No new functionality (including modules/plugins) to any code
- 2021-09-27 Beta 1
- 2021-10-04 Beta 2 (if necessary)
- 2021-10-18 Release Candidate 1
- 2021-10-25 Release Candidate 2 (if necessary)
- 2021-11-08 Release

## [Release Manager](ROADMAP_2_12.md#id3)

> Ansible Core Team

### [Planned work](ROADMAP_2_12.md#id4)

- Bump the minimum Python version requirement for the controller to Python 3.8. This will be a hard requirement.
- Deprecate Python 2.6 support for managed/target hosts. The release of `ansible-core==2.13` will remove Python 2.6 support.
- Introduce split-controller testing in `ansible-test` to separate dependencies for the controller from dependencies on the target.
- Extend the functionality of `module_defaults` `action_groups` to be created and presented by collections.

### [Delayed work](ROADMAP_2_12.md#id5)

The following work has been delayed and retargeted for a future release

- Implement object proxies, to expose restricted interfaces between parts of the code, and enable deprecations of attributes and variables.
