---
collection: ansible
version: "6"
title: "Community.Sops"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/sops/
fetched_at: 2026-07-28T00:25:10+00:00
---
# Community.Sops

Collection version 1.5.0

- [Description](index.md#description)
- [Communication](index.md#communication)
- [Scenario Guide](index.md#scenario-guide)
- [Plugin Index](index.md#plugin-index)
- [Role Index](index.md#role-index)

## [Description](index.md#id1)

Support usage of mozilla/sops from your Ansible playbooks

**Author:**

- Edoardo Tenani

**Supported ansible-core versions:**

- 2.9.10 or newer

[Issue Tracker](https://github.com/ansible-collections/community.sops/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.sops)
[Submit a bug report](https://github.com/ansible-collections/community.sops/issues/new?assignees=&labels=&template=bug_report.md)
[Request a feature](https://github.com/ansible-collections/community.sops/issues/new?assignees=&labels=&template=feature_request.md)

## [Communication](index.md#id2)

- Matrix room `#users:ansible.im`: [General usage and support questions](https://matrix.to/#/#users:ansible.im).
- IRC channel `#ansible` (Libera network):
  [General usage and support questions](https://web.libera.chat/?channel=#ansible).
- Mailing list: [Ansible Project List](https://groups.google.com/g/ansible-project).
  ([Subscribe](mailto:ansible-project+subscribe%40googlegroups.com?subject=subscribe))

## [Scenario Guide](index.md#id3)

- [Protecting Ansible secrets with Mozilla SOPS](docsite/guide.md)

## [Plugin Index](index.md#id4)

These are the plugins in the community.sops collection:

### Modules

- [load_vars module](load_vars_module.md#ansible-collections-community-sops-load-vars-module) – Load sops-encrypted variables from files, dynamically within a task
- [sops_encrypt module](sops_encrypt_module.md#ansible-collections-community-sops-sops-encrypt-module) – Encrypt data with sops

### Lookup Plugins

- [sops lookup](sops_lookup.md#ansible-collections-community-sops-sops-lookup) – Read sops encrypted file contents

### Vars Plugins

- [sops vars](sops_vars.md#ansible-collections-community-sops-sops-vars) – Loading sops-encrypted vars files

## [Role Index](index.md#id5)

These are the roles in the community.sops collection:

- [install role](install_role.md#ansible-collections-community-sops-install-role) – Install Mozilla sops

> **See also:**
>
> List of [collections](../../index.md#list-of-collections) with docs hosted here.
