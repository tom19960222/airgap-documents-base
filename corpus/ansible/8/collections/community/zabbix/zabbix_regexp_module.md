---
collection: ansible
version: "8"
title: "community.zabbix.zabbix_regexp module – Create/update/delete Zabbix regular expression"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/zabbix/zabbix_regexp_module.html
fetched_at: 2026-07-28T02:02:52+00:00
---
# community.zabbix.zabbix_regexp module – Create/update/delete Zabbix regular expression

> **Note:**
>
> This module is part of the [community.zabbix collection](https://galaxy.ansible.com/ui/repo/published/community/zabbix/) (version 2.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.zabbix`.
> You need further requirements to be able to use this module,
> see [Requirements](zabbix_regexp_module.md#ansible-collections-community-zabbix-zabbix-regexp-module-requirements) for details.
>
> To use it in a playbook, specify: `community.zabbix.zabbix_regexp`.

New in community.zabbix 2.1.0

- [Synopsis](zabbix_regexp_module.md#synopsis)
- [Requirements](zabbix_regexp_module.md#requirements)
- [Parameters](zabbix_regexp_module.md#parameters)
- [Notes](zabbix_regexp_module.md#notes)
- [Examples](zabbix_regexp_module.md#examples)
- [Return Values](zabbix_regexp_module.md#return-values)

## [Synopsis](zabbix_regexp_module.md#id1)

- This module allows you to create, update and delete Zabbix regular expression.

## [Requirements](zabbix_regexp_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.9

## [Parameters](zabbix_regexp_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **expressions**  list / elements=dictionary | List of expressions.  The regular expression returns true when all expressions return true.  Required when `state=present`. |
| **case_sensitive**  boolean | If true, the expression will be case sensitive.  **Choices:**   - `false` ← (default) - `true` |
| **exp_delimiter**  string | Delimiter for expression.  Used if expression_type is `any_character_string_included`.  Default values is `,`  **Choices:**   - `","` - `"."` - `"/"` |
| **expression**  string / required | A expression string |
| **expression_type**  string / required | A expression string  **Choices:**   - `"character_string_included"` - `"any_character_string_included"` - `"character_string_not_included"` - `"result_is_true"` - `"result_is_false"` |
| **http_login_password**  string | Basic Auth password |
| **http_login_user**  string | Basic Auth login |
| **name**  string / required | Name of this regular expression |
| **state**  string | State of the regular expression.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **test_string**  string | A test string for this regular expression |

## [Notes](zabbix_regexp_module.md#id4)

> **Note:**
>
> - Only Zabbix >= 6.0 is supported.

## [Examples](zabbix_regexp_module.md#id5)

```yaml+jinja
# If you want to use Username and Password to be authenticated by Zabbix Server
- name: Set credentials to access Zabbix Server API
  ansible.builtin.set_fact:
    ansible_user: Admin
    ansible_httpapi_pass: zabbix

# If you want to use API token to be authenticated by Zabbix Server
# https://www.zabbix.com/documentation/current/en/manual/web_interface/frontend_sections/administration/general#api-tokens
- name: Set API token
  ansible.builtin.set_fact:
    ansible_zabbix_auth_key: 8ec0d52432c15c91fcafe9888500cf9a607f44091ab554dbee860f6b44fac895

- name: Update regexp of 'File systems for discovery'
  # set task level variables as we change ansible_connection plugin here
  vars:
    ansible_network_os: community.zabbix.zabbix
    ansible_connection: httpapi
    ansible_httpapi_port: 443
    ansible_httpapi_use_ssl: true
    ansible_httpapi_validate_certs: false
    ansible_zabbix_url_path: 'zabbixeu'  # If Zabbix WebUI runs on non-default (zabbix) path ,e.g. http://<FQDN>/zabbixeu
    ansible_host: zabbix-example-fqdn.org
  community.zabbix.zabbix_regexp:
    name: File systems for discovery
    test_string: ext2
    expressions:
      - expression: "^(btrfs|ext2|ext3|ext4|reiser|xfs|ffs|ufs|jfs|jfs2|vxfs|hfs|apfs|refs|ntfs|fat32|zfs)$"
        expression_type: result_is_true
```

## [Return Values](zabbix_regexp_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | The result of the operation  **Returned:** success  **Sample:** `"Successfully updated regular expression setting"` |

### Authors

- ONODERA Masaru(@masa-orca)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.zabbix/issues)
- [Homepage](https://github.com/ansible-collections/community.zabbix)
- [Repository (Sources)](https://github.com/ansible-collections/community.zabbix.git)
