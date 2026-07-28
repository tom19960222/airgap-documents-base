---
collection: ansible
version: "6"
title: "community.network.ig_config module – Manage the configuration database on an Ingate SBC."
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/network/ig_config_module.html
fetched_at: 2026-07-27T17:18:51+00:00
---
# community.network.ig_config module – Manage the configuration database on an Ingate SBC.

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/community/network) (version 4.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
> You need further requirements to be able to use this module,
> see [Requirements](ig_config_module.md#ansible-collections-community-network-ig-config-module-requirements) for details.
>
> To use it in a playbook, specify: `community.network.ig_config`.

- [Synopsis](ig_config_module.md#synopsis)
- [Requirements](ig_config_module.md#requirements)
- [Parameters](ig_config_module.md#parameters)
- [Notes](ig_config_module.md#notes)
- [Examples](ig_config_module.md#examples)
- [Return Values](ig_config_module.md#return-values)

## [Synopsis](ig_config_module.md#id1)

- Manage the configuration database on an Ingate SBC.

## [Requirements](ig_config_module.md#id2)

The below requirements are needed on the host that executes this module.

- ingatesdk >= 1.0.6

## [Parameters](ig_config_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **add**  boolean | Add a row to a table.  Choices:   - `false` - `true` |
| **client**  string | A dict object containing connection details. |
| **address**  string / required | The hostname or IP address to the unit. |
| **password**  string / required | The password for the REST API user. |
| **port**  integer | Which HTTP(S) port to connect to. |
| **scheme**  string / required | Which HTTP protocol to use.  Choices:   - `"http"` - `"https"` |
| **timeout**  integer | The timeout (in seconds) for REST API requests. |
| **username**  string / required | The username of the REST API user. |
| **validate_certs**  aliases: verify_ssl  boolean | Verify the unit’s HTTPS certificate.  Choices:   - `false` - `true` ← (default) |
| **version**  string | REST API version.  Choices:   - `"v1"` ← (default) |
| **columns**  string | A dict containing column names/values. |
| **delete**  boolean | Delete all rows in a table or a specific row.  Choices:   - `false` - `true` |
| **download**  boolean | Download the configuration database from the unit.  Choices:   - `false` - `true` |
| **factory**  boolean | Reset the preliminary configuration to its factory defaults.  Choices:   - `false` - `true` |
| **filename**  string | The name of the file to store the downloaded configuration in. Refer to the `download` option. |
| **get**  boolean | Return all rows in a table or a specific row.  Choices:   - `false` - `true` |
| **modify**  boolean | Modify a row in a table.  Choices:   - `false` - `true` |
| **no_response**  boolean | Expect no response when storing the preliminary configuration. Refer to the `store` option.  Choices:   - `false` ← (default) - `true` |
| **path**  string | Where in the filesystem to store the downloaded configuration. Refer to the `download` option. |
| **return_rowid**  boolean | Get rowid(s) from a table where the columns match.  Choices:   - `false` - `true` |
| **revert**  boolean | Reset the preliminary configuration.  Choices:   - `false` - `true` |
| **rowid**  integer | A row id. |
| **store**  boolean | Store the preliminary configuration.  Choices:   - `false` - `true` |
| **store_download**  boolean | If the downloaded configuration should be stored on disk. Refer to the `download` option.  Choices:   - `false` ← (default) - `true` |
| **table**  string | The name of the table. |

## [Notes](ig_config_module.md#id4)

> **Note:**
>
> - If `store_download` is set to True, and `path` and `filename` is omitted, the file will be stored in the current directory with an automatic filename.
> - This module requires that the Ingate Python SDK is installed on the host. To install the SDK use the pip command from your shell `pip install ingatesdk`.

## [Examples](ig_config_module.md#id5)

```yaml+jinja
- name: Add/remove DNS servers
  hosts: 192.168.1.1
  connection: local
  vars:
    client_rw:
      version: v1
      address: "{{ inventory_hostname }}"
      scheme: http
      username: alice
      password: foobar
  tasks:

  - name: Load factory defaults
    community.network.ig_config:
      client: "{{ client_rw }}"
      factory: true
    register: result
  - ansible.builtin.debug:
      var: result

  - name: Revert to last known applied configuration
    community.network.ig_config:
      client: "{{ client_rw }}"
      revert: true
    register: result
  - ansible.builtin.debug:
      var: result

  - name: Change the unit name
    community.network.ig_config:
      client: "{{ client_rw }}"
      modify: true
      table: misc.unitname
      columns:
        unitname: "Test Ansible"
    register: result
  - ansible.builtin.debug:
      var: result

  - name: Add a DNS server
    community.network.ig_config:
      client: "{{ client_rw }}"
      add: true
      table: misc.dns_servers
      columns:
        server: 192.168.1.21
    register: result
  - ansible.builtin.debug:
      var: result

  - name: Add a DNS server
    community.network.ig_config:
      client: "{{ client_rw }}"
      add: true
      table: misc.dns_servers
      columns:
        server: 192.168.1.22
    register: result
  - ansible.builtin.debug:
      var: result

  - name: Add a DNS server
    community.network.ig_config:
      client: "{{ client_rw }}"
      add: true
      table: misc.dns_servers
      columns:
        server: 192.168.1.23
    register: last_dns
  - ansible.builtin.debug:
      var: last_dns

  - name: Modify the last added DNS server
    community.network.ig_config:
      client: "{{ client_rw }}"
      modify: true
      table: misc.dns_servers
      rowid: "{{ last_dns['add'][0]['id'] }}"
      columns:
        server: 192.168.1.24
    register: result
  - ansible.builtin.debug:
      var: result

  - name: Return the last added DNS server
    community.network.ig_config:
      client: "{{ client_rw }}"
      get: true
      table: misc.dns_servers
      rowid: "{{ last_dns['add'][0]['id'] }}"
    register: result
  - ansible.builtin.debug:
      var: result

  - name: Remove last added DNS server
    community.network.ig_config:
      client: "{{ client_rw }}"
      delete: true
      table: misc.dns_servers
      rowid: "{{ last_dns['add'][0]['id'] }}"
    register: result
  - ansible.builtin.debug:
      var: result

  - name: Return the all rows from table misc.dns_servers
    community.network.ig_config:
      client: "{{ client_rw }}"
      get: true
      table: misc.dns_servers
    register: result
  - ansible.builtin.debug:
      var: result

  - name: Remove remaining DNS servers
    community.network.ig_config:
      client: "{{ client_rw }}"
      delete: true
      table: misc.dns_servers
    register: result
  - ansible.builtin.debug:
      var: result

  - name: Get rowid for interface eth0
    community.network.ig_config:
      client: "{{ client_rw }}"
      return_rowid: true
      table: network.local_nets
      columns:
        interface: eth0
    register: result
  - ansible.builtin.debug:
      var: result

  - name: Store the preliminary configuration
    community.network.ig_config:
      client: "{{ client_rw }}"
      store: true
    register: result
  - ansible.builtin.debug:
      var: result

  - name: Do backup of the configuration database
    community.network.ig_config:
      client: "{{ client_rw }}"
      download: true
      store_download: true
    register: result
  - ansible.builtin.debug:
      var: result
```

## [Return Values](ig_config_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **add**  complex | A list containing information about the added row  Returned: when `add` is yes and success |
| **data**  complex | Column names/values  Returned: success  Sample: `{"number": "2", "server": "10.48.254.33"}` |
| **href**  string | The REST API URL to the added row  Returned: success  Sample: `"http://192.168.1.1/api/v1/misc/dns_servers/2"` |
| **id**  integer | The row id  Returned: success  Sample: `22` |
| **delete**  complex | A list containing information about the deleted row(s)  Returned: when `delete` is yes and success |
| **data**  complex | Column names/values  Returned: success  Sample: `{"number": "2", "server": "10.48.254.33"}` |
| **id**  integer | The row id  Returned: success  Sample: `22` |
| **table**  string | The name of the table  Returned: success  Sample: `"misc.dns_servers"` |
| **download**  complex | Configuration database and meta data  Returned: when `download` is yes and success |
| **config**  string | The configuration database  Returned: success |
| **filename**  string | A suggested name for the configuration  Returned: success  Sample: `"testname_2018-10-01T214040.cfg"` |
| **mimetype**  string | The mimetype  Returned: success  Sample: `"application/x-config-database"` |
| **factory**  complex | A command status message  Returned: when `factory` is yes and success |
| **msg**  string | The command status message  Returned: success  Sample: `"reverted the configuration to the factory configuration."` |
| **get**  complex | A list containing information about the row(s)  Returned: when `get` is yes and success |
| **data**  complex | Column names/values  Returned: success  Sample: `{"number": "2", "server": "10.48.254.33"}` |
| **href**  string | The REST API URL to the row  Returned: success  Sample: `"http://192.168.1.1/api/v1/misc/dns_servers/1"` |
| **id**  integer | The row id  Returned: success  Sample: `1` |
| **table**  string | The name of the table  Returned: success  Sample: `"Testname"` |
| **modify**  complex | A list containing information about the modified row  Returned: when `modify` is yes and success |
| **data**  complex | Column names/values  Returned: success  Sample: `{"number": "2", "server": "10.48.254.33"}` |
| **href**  string | The REST API URL to the modified row  Returned: success  Sample: `"http://192.168.1.1/api/v1/misc/dns_servers/1"` |
| **id**  integer | The row id  Returned: success  Sample: `10` |
| **table**  string | The name of the table  Returned: success  Sample: `"Testname"` |
| **return_rowid**  list / elements=string | The matched row id(s).  Returned: when `return_rowid` is yes and success  Sample: `[1, 3]` |
| **revert**  complex | A command status message  Returned: when `revert` is yes and success |
| **msg**  string | The command status message  Returned: success  Sample: `"reverted the configuration to the last applied configuration."` |
| **store**  complex | A command status message  Returned: when `store` is yes and success |
| **msg**  string | The command status message  Returned: success  Sample: `"Successfully applied and saved the configuration."` |

### Authors

- Ingate Systems AB (@ingatesystems)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.network/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.network)
