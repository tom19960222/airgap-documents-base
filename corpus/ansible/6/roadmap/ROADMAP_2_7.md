---
collection: ansible
version: "6"
title: "Ansible 2.7"
source_url: https://docs.ansible.com/projects/ansible/6/roadmap/ROADMAP_2_7.html
fetched_at: 2026-07-27T16:43:01+00:00
---
# [Ansible 2.7](ROADMAP_2_7.md#id4)

Topics

- [Ansible 2.7](ROADMAP_2_7.md#ansible-2-7)

  - [Release Schedule](ROADMAP_2_7.md#release-schedule)

    - [Expected](ROADMAP_2_7.md#expected)
  - [Release Manager](ROADMAP_2_7.md#release-manager)
  - [Cleaning Duty](ROADMAP_2_7.md#cleaning-duty)
  - [Engine Improvements](ROADMAP_2_7.md#engine-improvements)
  - [Core Modules](ROADMAP_2_7.md#core-modules)
  - [Cloud Modules](ROADMAP_2_7.md#cloud-modules)

    - [General](ROADMAP_2_7.md#general)
    - [AWS](ROADMAP_2_7.md#aws)
    - [Azure](ROADMAP_2_7.md#azure)
  - [Network](ROADMAP_2_7.md#network)

    - [General](ROADMAP_2_7.md#id1)
    - [Modules](ROADMAP_2_7.md#modules)
  - [Windows](ROADMAP_2_7.md#windows)

    - [General](ROADMAP_2_7.md#id2)
    - [Modules](ROADMAP_2_7.md#id3)

## [Release Schedule](ROADMAP_2_7.md#id5)

### [Expected](ROADMAP_2_7.md#id6)

- 2018-08-23 Core Freeze (Engine and Core Modules/Plugins)
- 2018-08-23 Alpha Release 1
- 2018-08-30 Community Freeze (Non-Core Modules/Plugins)
- 2018-08-30 Beta Release 1
- 2018-09-06 Release Candidate 1 (If needed)
- 2018-09-13 Release Candidate 2 (If needed)
- 2018-09-20 Release Candidate 3 (If needed)
- 2018-09-27 Release Candidate 4 (If needed)
- 2018-10-04 General Availability

## [Release Manager](ROADMAP_2_7.md#id7)

Toshio Kuratomi (IRC: abadger1999; GitHub: @abadger)

## [Cleaning Duty](ROADMAP_2_7.md#id8)

- Drop Py2.6 for controllers [Docs PR #42971](https://github.com/ansible/ansible/pull/42971) and
  [issue #42972](https://github.com/ansible/ansible/issues/42972)
- Remove dependency on simplejson [issue #42761](https://github.com/ansible/ansible/issues/42761)

## [Engine Improvements](ROADMAP_2_7.md#id9)

- Performance improvement invoking Python modules [pr #41749](https://github.com/ansible/ansible/pull/41749)
- Jinja native types will allow for users to render a Python native type. [pr #32738](https://github.com/ansible/ansible/pull/32738)

## [Core Modules](ROADMAP_2_7.md#id10)

- Include feature changes and improvements

  - Create new argument `apply` that will allow for included tasks to inherit explicitly provided attributes. [pr #39236](https://github.com/ansible/ansible/pull/39236)
  - Create “private” functionality for allowing vars/default to be exposed outside of roles. [pr #41330](https://github.com/ansible/ansible/pull/41330)
- Provide a parameter for the `template` module to output to different encoding formats [pr
  #42171](https://github.com/ansible/ansible/pull/42171)
- `reboot` module for Linux hosts (@samdoran) [pr #35205](https://github.com/ansible/ansible/pull/35205)

## [Cloud Modules](ROADMAP_2_7.md#id11)

### [General](ROADMAP_2_7.md#id12)

- Cloud auth plugin [proposal #24](https://github.com/ansible/proposals/issues/24)

### [AWS](ROADMAP_2_7.md#id13)

- Inventory plugin for RDS [pr #41919](https://github.com/ansible/ansible/pull/41919)
- Count support for ec2_instance
- aws_eks module [pr #41183](https://github.com/ansible/ansible/pull/41183)
- Cloudformation stack sets support ([PR#41669](https://github.com/ansible/ansible/pull/41669))
- RDS instance and snapshot modules [pr #39994](https://github.com/ansible/ansible/pull/39994) [pr #43789](https://github.com/ansible/ansible/pull/43789)
- Diff mode improvements for cloud modules [pr #44533](https://github.com/ansible/ansible/pull/44533)

### [Azure](ROADMAP_2_7.md#id14)

- Azure inventory plugin [issue #42769](https://github.com/ansible/ansible/issues/42769)

## [Network](ROADMAP_2_7.md#id15)

### [General](ROADMAP_2_7.md#id16)

- Refactor the APIs in cliconf ([issue #39056](https://github.com/ansible/ansible/issues/39056)) and netconf ([issue #39160](https://github.com/ansible/ansible/issues/39160)) plugins so that they have a uniform signature across supported network platforms. **done**
  ([PR #41846](https://github.com/ansible/ansible/pull/41846)) ([PR #43643](https://github.com/ansible/ansible/pull/43643)) ([PR #43837](https://github.com/ansible/ansible/pull/43837))
  ([PR #43203](https://github.com/ansible/ansible/pull/43203)) ([PR #42300](https://github.com/ansible/ansible/pull/42300)) ([PR #44157](https://github.com/ansible/ansible/pull/44157))

### [Modules](ROADMAP_2_7.md#id17)

- New `cli_config` module [issue #39228](https://github.com/ansible/ansible/issues/39228) **done** [PR #42413](https://github.com/ansible/ansible/pull/42413).
- New `cli_command` module [issue #39284](https://github.com/ansible/ansible/issues/39284)
- Refactor `netconf_config` module to add additional functionality. **done** [proposal #104](https://github.com/ansible/proposals/issues/104) ([PR #44379](https://github.com/ansible/ansible/pull/44379))

## [Windows](ROADMAP_2_7.md#id18)

### [General](ROADMAP_2_7.md#id19)

- Added new connection plugin that uses PSRP as the connection protocol [pr #41729](https://github.com/ansible/ansible/pull/41729)

### [Modules](ROADMAP_2_7.md#id20)

- Revamp Chocolatey to fix bugs and support offline installation [pr #43013](https://github.com/ansible/ansible/pull/43013).
- Add Chocolatey modules that can manage the following Chocolatey features

  > - [Sources](https://chocolatey.org/docs/commands-sources) [pr #42790](https://github.com/ansible/ansible/pull/42790)
  > - [Features](https://chocolatey.org/docs/chocolatey-configuration#features) [pr #42848](https://github.com/ansible/ansible/pull/42848)
  > - [Config](https://chocolatey.org/docs/chocolatey-configuration#config-settings) [pr #42915](h*ttps:/github.com/ansible/ansible/pull/42915.md)
