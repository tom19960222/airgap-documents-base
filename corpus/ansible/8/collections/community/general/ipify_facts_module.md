---
collection: ansible
version: "8"
title: "community.general.ipify_facts module – Retrieve the public IP of your internet gateway"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/ipify_facts_module.html
fetched_at: 2026-07-28T01:46:49+00:00
---
# community.general.ipify_facts module – Retrieve the public IP of your internet gateway

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.ipify_facts`.

- [Synopsis](ipify_facts_module.md#synopsis)
- [Parameters](ipify_facts_module.md#parameters)
- [Attributes](ipify_facts_module.md#attributes)
- [Notes](ipify_facts_module.md#notes)
- [Examples](ipify_facts_module.md#examples)
- [Return Values](ipify_facts_module.md#return-values)

## [Synopsis](ipify_facts_module.md#id1)

- If behind NAT and need to know the public IP of your internet gateway.

Aliases: net_tools.ipify_facts

## [Parameters](ipify_facts_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_url**  string | URL of the ipify.org API service.  `?format=json` will be appended per default.  **Default:** `"https://api.ipify.org/"` |
| **timeout**  integer | HTTP connection timeout in seconds.  **Default:** `10` |
| **validate_certs**  boolean | When set to `false`, SSL certificates will not be validated.  **Choices:**   - `false` - `true` ← (default) |

## [Attributes](ipify_facts_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full**  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:**  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |
| **facts** | **Support:** **full** | Action returns an `ansible_facts` dictionary that will update existing host facts. |

## [Notes](ipify_facts_module.md#id4)

> **Note:**
>
> - Visit <https://www.ipify.org> to get more information.

## [Examples](ipify_facts_module.md#id5)

```yaml+jinja
# Gather IP facts from ipify.org
- name: Get my public IP
  community.general.ipify_facts:

# Gather IP facts from your own ipify service endpoint with a custom timeout
- name: Get my public IP
  community.general.ipify_facts:
    api_url: http://api.example.com/ipify
    timeout: 20
```

## [Return Values](ipify_facts_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **ipify_public_ip**  string | Public IP of the internet gateway.  **Returned:** success  **Sample:** `"1.2.3.4"` |

### Authors

- René Moser (@resmo)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
