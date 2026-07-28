---
collection: ansible
version: "8"
title: "How to install the vmware_rest collection"
source_url: https://docs.ansible.com/projects/ansible/8/collections/vmware/vmware_rest/docsite/vmware_rest_scenarios/vcenter/1_installation.html
fetched_at: 2026-07-28T03:01:09+00:00
---
# How to install the vmware_rest collection

## Requirements

The collection depends on:

- Ansible >=2.9.10 or greater
- Python 3.6 or greater

## aiohttp

[aiohttp](https://docs.aiohttp.org/en/stable/) is the only
dependency of the collection. You can install it with `pip` if you
use a virtualenv to run Ansible.

```shell
$ pip install aiohttp
```

Or using an RPM.

```shell
$ sudo dnf install python3-aiohttp
```

## Installation

The best option to install the collection is to use the
`ansible-galaxy` command:

```shell
$ ansible-galaxy collection install vmware.vmware_rest
```
