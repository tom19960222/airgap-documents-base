---
collection: ansible
version: "8"
title: "community.network.netscaler_nitro_request module – Issue Nitro API requests to a Netscaler instance."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/network/netscaler_nitro_request_module.html
fetched_at: 2026-07-28T01:57:10+00:00
---
# community.network.netscaler_nitro_request module – Issue Nitro API requests to a Netscaler instance.

> **Note:**
>
> This module is part of the [community.network collection](https://galaxy.ansible.com/ui/repo/published/community/network/) (version 5.0.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.network`.
>
> To use it in a playbook, specify: `community.network.netscaler_nitro_request`.

- [Synopsis](netscaler_nitro_request_module.md#synopsis)
- [Parameters](netscaler_nitro_request_module.md#parameters)
- [Examples](netscaler_nitro_request_module.md#examples)
- [Return Values](netscaler_nitro_request_module.md#return-values)

## [Synopsis](netscaler_nitro_request_module.md#id1)

- Issue Nitro API requests to a Netscaler instance.
- This is intended to be a short hand for using the uri Ansible module to issue the raw HTTP requests directly.
- It provides consistent return values and has no other dependencies apart from the base Ansible runtime environment.
- This module is intended to run either on the Ansible control node or a bastion (jumpserver) with access to the actual Netscaler instance

Aliases: network.netscaler.netscaler_nitro_request

## [Parameters](netscaler_nitro_request_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **action**  string | The action to perform when the *operation* value is set to `action`.  Some common values for this parameter are `enable`, `disable`, `rename`. |
| **args**  string | A dictionary which defines the key arguments by which we will select the Nitro object to operate on.  It is required for the following *operation* values: `get_by_args`, `'delete_by_args'`. |
| **attributes**  string | The attributes of the Nitro object we are operating on.  It is required for the following *operation* values: `add`, `update`, `action`. |
| **expected_nitro_errorcode**  string | A list of numeric values that signify that the operation was successful.  **Default:** `[0]` |
| **filter**  string | A dictionary which defines the filter with which to refine the Nitro objects returned by the `get_filtered` *operation*. |
| **instance_id**  string | The id of the target Netscaler instance when issuing a Nitro request through a MAS proxy. |
| **instance_ip**  string | The IP address of the target Netscaler instance when issuing a Nitro request through a MAS proxy. |
| **instance_name**  string | The name of the target Netscaler instance when issuing a Nitro request through a MAS proxy. |
| **name**  string | The name of the resource we are operating on.  It is required for the following *operation* values: `update`, `get`, `delete`. |
| **nitro_auth_token**  string | The authentication token provided by the `mas_login` operation. It is required when issuing Nitro API calls through a MAS proxy. |
| **nitro_pass**  string / required | The password with which to authenticate to the Netscaler node. |
| **nitro_protocol**  string | Which protocol to use when accessing the Nitro API objects.  **Choices:**   - `"http"` ← (default) - `"https"` |
| **nitro_user**  string / required | The username with which to authenticate to the Netscaler node. |
| **nsip**  string | The IP address of the Netscaler or MAS instance where the Nitro API calls will be made.  The port can be specified with the colon `:`. E.g. `192.168.1.1:555`. |
| **operation**  string | Define the Nitro operation that we want to perform.  **Choices:**   - `"add"` - `"update"` - `"get"` - `"get_by_args"` - `"get_filtered"` - `"get_all"` - `"delete"` - `"delete_by_args"` - `"count"` - `"mas_login"` - `"save_config"` - `"action"` |
| **resource**  string | The type of resource we are operating on.  It is required for all *operation* values except `mas_login` and `save_config`. |
| **validate_certs**  boolean | If `no`, SSL certificates will not be validated. This should only be used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |

## [Examples](netscaler_nitro_request_module.md#id3)

```yaml+jinja
- name: Add a server
  delegate_to: localhost
  community.network.netscaler_nitro_request:
    nsip: "{{ nsip }}"
    nitro_user: "{{ nitro_user }}"
    nitro_pass: "{{ nitro_pass }}"
    operation: add
    resource: server
    name: test-server-1
    attributes:
      name: test-server-1
      ipaddress: 192.168.1.1

- name: Update server
  delegate_to: localhost
  community.network.netscaler_nitro_request:
    nsip: "{{ nsip }}"
    nitro_user: "{{ nitro_user }}"
    nitro_pass: "{{ nitro_pass }}"
    operation: update
    resource: server
    name: test-server-1
    attributes:
      name: test-server-1
      ipaddress: 192.168.1.2

- name: Get server
  delegate_to: localhost
  register: result
  community.network.netscaler_nitro_request:
    nsip: "{{ nsip }}"
    nitro_user: "{{ nitro_user }}"
    nitro_pass: "{{ nitro_pass }}"
    operation: get
    resource: server
    name: test-server-1

- name: Delete server
  delegate_to: localhost
  register: result
  community.network.netscaler_nitro_request:
    nsip: "{{ nsip }}"
    nitro_user: "{{ nitro_user }}"
    nitro_pass: "{{ nitro_pass }}"
    operation: delete
    resource: server
    name: test-server-1

- name: Rename server
  delegate_to: localhost
  community.network.netscaler_nitro_request:
    nsip: "{{ nsip }}"
    nitro_user: "{{ nitro_user }}"
    nitro_pass: "{{ nitro_pass }}"
    operation: action
    action: rename
    resource: server
    attributes:
      name: test-server-1
      newname: test-server-2

- name: Get server by args
  delegate_to: localhost
  register: result
  community.network.netscaler_nitro_request:
    nsip: "{{ nsip }}"
    nitro_user: "{{ nitro_user }}"
    nitro_pass: "{{ nitro_pass }}"
    operation: get_by_args
    resource: server
    args:
      name: test-server-1

- name: Get server by filter
  delegate_to: localhost
  register: result
  community.network.netscaler_nitro_request:
    nsip: "{{ nsip }}"
    nitro_user: "{{ nitro_user }}"
    nitro_pass: "{{ nitro_pass }}"
    operation: get_filtered
    resource: server
    filter:
      ipaddress: 192.168.1.2

# Doing a NITRO request through MAS.
# Requires to have an authentication token from the mas_login and used as the nitro_auth_token parameter
# Also nsip is the MAS address and the target Netscaler IP must be defined with instance_ip
# The rest of the task arguments remain the same as when issuing the NITRO request directly to a Netscaler instance.

- name: Do mas login
  delegate_to: localhost
  register: login_result
  community.network.netscaler_nitro_request:
    nsip: "{{ mas_ip }}"
    nitro_user: "{{ nitro_user }}"
    nitro_pass: "{{ nitro_pass }}"
    operation: mas_login

- name: Add resource through MAS proxy
  delegate_to: localhost
  community.network.netscaler_nitro_request:
    nsip: "{{ mas_ip }}"
    nitro_auth_token: "{{ login_result.nitro_auth_token }}"
    instance_ip: "{{ nsip }}"
    operation: add
    resource: server
    name: test-server-1
    attributes:
      name: test-server-1
      ipaddress: 192.168.1.7
```

## [Return Values](netscaler_nitro_request_module.md#id4)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **http_response_body**  string | A string with the actual HTTP response body content if existent. If there is no HTTP response body it is an empty string.  **Returned:** always  **Sample:** `"{ errorcode: 0, message: Done, severity: NONE }"` |
| **http_response_data**  dictionary | A dictionary that contains all the HTTP response’s data.  **Returned:** always  **Sample:** `"status: 200"` |
| **nitro_auth_token**  string | The token returned by the `mas_login` operation when successful.  **Returned:** when applicable  **Sample:** `"##E8D7D74DDBD907EE579E8BB8FF4529655F22227C1C82A34BFC93C9539D66"` |
| **nitro_errorcode**  integer | A numeric value containing the return code of the NITRO operation. When 0 the operation is successful. Any non zero value indicates an error.  **Returned:** always  **Sample:** `0` |
| **nitro_message**  string | A string containing a human readable explanation for the NITRO operation result.  **Returned:** always  **Sample:** `"Success"` |
| **nitro_object**  list / elements=string | The object returned from the NITRO operation. This is applicable to the various get operations which return an object.  **Returned:** when applicable  **Sample:** `[{"ipaddress": "192.168.1.8", "ipv6address": "NO", "maxbandwidth": "0", "name": "test-server-1", "port": 0, "sp": "OFF", "state": "ENABLED"}]` |
| **nitro_severity**  string | A string describing the severity of the NITRO operation error or NONE.  **Returned:** always  **Sample:** `"NONE"` |

### Authors

- George Nikolopoulos (@giorgos-nikolopoulos)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.network/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.network)
