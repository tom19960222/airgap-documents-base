---
collection: ansible
version: "6"
title: "How to install the vmware_rest collection"
source_url: https://docs.ansible.com/projects/ansible/6/scenario_guides/vmware_rest_scenarios/installation.html
fetched_at: 2026-07-27T16:43:17+00:00
---
# How to install the vmware_rest collection

- [Requirements](installation.md#requirements)
- [aiohttp](installation.md#aiohttp)
- [Installation](installation.md#installation)

## [Requirements](installation.md#id2)

The collection depends on:

- Ansible >=2.9.10 or greater
- Python 3.6 or greater

## [aiohttp](installation.md#id3)

[aiohttp](https://docs.aiohttp.org/en/stable/) is the only dependency of the collection. You can install it with `pip` if you use a virtualenv to run Ansible.

```shell
$ pip install aiohttp
```

Or using an RPM.

```shell
$ sudo dnf install python3-aiohttp
```

## [Installation](installation.md#id4)

The best option to install the collection is to use the `ansible-galaxy` command:

```shell
$ ansible-galaxy collection install vmware.vmware_rest
```
