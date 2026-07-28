---
collection: ansible
version: "6"
title: "community.zabbix.zabbix httpapi – HttpApi Plugin for Zabbix"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/zabbix/zabbix_httpapi.html
fetched_at: 2026-07-27T17:24:26+00:00
---
# community.zabbix.zabbix httpapi – HttpApi Plugin for Zabbix

> **Note:**
>
> This httpapi plugin is part of the [community.zabbix collection](https://galaxy.ansible.com/community/zabbix) (version 1.9.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.zabbix`.
>
> To use it in a playbook, specify: `community.zabbix.zabbix`.

New in community.zabbix 1.8.0

- [Synopsis](zabbix_httpapi.md#synopsis)
- [Parameters](zabbix_httpapi.md#parameters)

## [Synopsis](zabbix_httpapi.md#id1)

- This HttpApi plugin provides methods to connect to Zabbix over their HTTP(S)-based api.

## [Parameters](zabbix_httpapi.md#id2)

| Parameter | Comments |
| --- | --- |
| **zabbix_auth_key**  string | Specifies API authentication key  Configuration:   - Environment variable: [`ANSIBLE_ZABBIX_AUTH_KEY`](../../environment_variables.md#envvar-ANSIBLE_ZABBIX_AUTH_KEY) - Variable: ansible_zabbix_auth_key |
| **zabbix_url_path**  string | Specifies path portion in Zabbix WebUI URL, e.g. for <https://myzabbixfarm.com/zabbixeu> zabbix_url_path=zabbixeu  Default: `"zabbix"`  Configuration:   - Environment variable: [`ANSIBLE_ZABBIX_URL_PATH`](../../environment_variables.md#envvar-ANSIBLE_ZABBIX_URL_PATH) - Variable: ansible_zabbix_url_path |

### Authors

- Markus Fischbacher (@rockaut)
- Evgeny Yurchenko (@BGmot)

> **Hint:**
>
> Configuration entries for each entry type have a low to high priority order. For example, a variable that is lower in the list will override a variable that is higher up.

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.zabbix/issues)
[Homepage](https://github.com/ansible-collections/community.zabbix)
[Repository (Sources)](https://github.com/ansible-collections/community.zabbix.git)
