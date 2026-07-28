---
collection: ansible
version: "8"
title: "community.general.ipinfoio_facts module – Retrieve IP geolocation facts of a host’s IP address"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/ipinfoio_facts_module.html
fetched_at: 2026-07-28T01:46:50+00:00
---
# community.general.ipinfoio_facts module – Retrieve IP geolocation facts of a host’s IP address

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
> To use it in a playbook, specify: `community.general.ipinfoio_facts`.

- [Synopsis](ipinfoio_facts_module.md#synopsis)
- [Parameters](ipinfoio_facts_module.md#parameters)
- [Attributes](ipinfoio_facts_module.md#attributes)
- [Notes](ipinfoio_facts_module.md#notes)
- [Examples](ipinfoio_facts_module.md#examples)
- [Returned Facts](ipinfoio_facts_module.md#returned-facts)

## [Synopsis](ipinfoio_facts_module.md#id1)

- Gather IP geolocation facts of a host’s IP address using ipinfo.io API

Aliases: net_tools.ipinfoio_facts

## [Parameters](ipinfoio_facts_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **http_agent**  string | Set http user agent  **Default:** `"ansible-ipinfoio-module/0.0.1"` |
| **timeout**  integer | HTTP connection timeout in seconds  **Default:** `10` |

## [Attributes](ipinfoio_facts_module.md#id3)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **full**  This action does not modify state. | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:**  N/A  This action does not modify state. | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |
| **facts** | **Support:** **full** | Action returns an `ansible_facts` dictionary that will update existing host facts. |

## [Notes](ipinfoio_facts_module.md#id4)

> **Note:**
>
> - Check <http://ipinfo.io/> for more information

## [Examples](ipinfoio_facts_module.md#id5)

```yaml+jinja
# Retrieve geolocation data of a host's IP address
- name: Get IP geolocation data
  community.general.ipinfoio_facts:
```

## [Returned Facts](ipinfoio_facts_module.md#id6)

Facts returned by this module are added/updated in the `hostvars` host facts and can be referenced by name just like any other host fact. They do not need to be registered in order to use them.

| Key | Description |
| --- | --- |
| **city**  string | City name  **Returned:** success  **Sample:** `"Mountain View"` |
| **country**  string | ISO 3166-1 alpha-2 country code  **Returned:** success  **Sample:** `"US"` |
| **hostname**  string | Domain name  **Returned:** success  **Sample:** `"google-public-dns-a.google.com"` |
| **ip**  string | Public IP address of a host  **Returned:** success  **Sample:** `"8.8.8.8"` |
| **loc**  string | Latitude and Longitude of the location  **Returned:** success  **Sample:** `"37.3860,-122.0838"` |
| **org**  string | organization’s name  **Returned:** success  **Sample:** `"AS3356 Level 3 Communications, Inc."` |
| **postal**  string | Postal code  **Returned:** success  **Sample:** `"94035"` |
| **region**  string | State or province name  **Returned:** success  **Sample:** `"California"` |

### Authors

- Aleksei Kostiuk (@akostyuk)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
