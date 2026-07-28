---
collection: ansible
version: "8"
title: "Ansible project 3.0"
source_url: https://docs.ansible.com/projects/ansible/8/roadmap/COLLECTIONS_3_0.html
fetched_at: 2026-07-28T00:59:38+00:00
---
# Ansible project 3.0

This release schedule includes dates for the [ansible](https://pypi.org/project/ansible/) package, with a few dates for the [ansible-base](https://pypi.org/project/ansible-base/) package as well. All dates are subject to change. Ansible 3.x.x includes `ansible-base` 2.10. See [Ansible-base 2.10](ROADMAP_2_10.md#base-roadmap-2-10) for the most recent updates on `ansible-base`.

- [Release schedule](COLLECTIONS_3_0.md#release-schedule)
- [Ansible minor releases](COLLECTIONS_3_0.md#ansible-minor-releases)
- [ansible-base release](COLLECTIONS_3_0.md#ansible-base-release)

## [Release schedule](COLLECTIONS_3_0.md#id7)

> **Note:**
>
> Ansible is switching from its traditional versioning scheme to [semantic versioning](https://semver.org/) starting with this release. So this version is 3.0.0 instead of 2.11.0.

2020-12-16:
:   Finalize rules for net-new collections submitted for the ansible release.

2021-01-27:
:   Final day for new collections to be **reviewed and approved**. They MUST be
    submitted prior to this to give reviewers a chance to look them over and for collection owners
    to fix any problems.

2021-02-02:
:   Ansible-3.0.0-beta1 – feature freeze [[1]](COLLECTIONS_3_0.md#id4)

2021-02-09:
:   Ansible-3.0.0-rc1 – final freeze [[2]](COLLECTIONS_3_0.md#id5) [[3]](COLLECTIONS_3_0.md#id6)

2021-02-16:
:   Release of Ansible-3.0.0

2021-03-09:
:   Release of Ansible-3.1.0 (bugfix + compatible features: every three weeks)

[[1](COLLECTIONS_3_0.md#id1)]

No new modules or major features accepted after this date. In practice this means we will freeze the semver collection versions to compatible release versions. For example, if the version of community.crypto on this date was community-crypto-2.1.0; ansible-3.0.0 could ship with community-crypto-2.1.1. It would not ship with community-crypto-2.2.0.

[[2](COLLECTIONS_3_0.md#id2)]

After this date only changes blocking a release are accepted. Accepted changes require creating a new rc and may slip the final release date.

[[3](COLLECTIONS_3_0.md#id3)]

Collections will only be updated to a new version if a blocker is approved. Collection owners should discuss any blockers at a community meeting (before this freeze) to decide whether to bump the version of the collection for a fix. See the [Community meeting agenda](https://github.com/ansible/community/issues/539).

> **Note:**
>
> Breaking changes may be introduced in Ansible 3.0.0, although we encourage collection owners to use deprecation periods that will show up in at least one Ansible release before the breaking change happens.

## [Ansible minor releases](COLLECTIONS_3_0.md#id8)

Ansible 3.x.x minor releases will occur approximately every three weeks if changes to collections have been made or if it is deemed necessary to force an upgrade to a later ansible-base-2.10.x. Ansible 3.x.x minor releases may contain new features but not backwards incompatibilities. In practice, this means we will include new collection versions where either the patch or the minor version number has changed but not when the major number has changed. For example, if Ansible-3.0.0 ships with community-crypto-2.1.0; Ansible-3.1.0 may ship with community-crypto-2.2.0 but would not ship with community-crypto-3.0.0).

> **Note:**
>
> Minor releases will stop when [Ansible-4](COLLECTIONS_4.md#ansible-4-roadmap) is released. See the [Release and Maintenance Page](../reference_appendices/release_and_maintenance.md#release-and-maintenance) for more information.

For more information, reach out on a mailing list or a chat channel - see [Communicating with the Ansible community](../community/communication.md#communication) for more details.

## [ansible-base release](COLLECTIONS_3_0.md#id9)

Ansible 3.x.x works with `ansible-base` 2.10. See [Ansible-base 2.10](ROADMAP_2_10.md#base-roadmap-2-10) for details.
