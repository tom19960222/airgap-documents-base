---
collection: ansible
version: "8"
title: "dellemc.enterprise_sonic.sonic_api module – Manages REST operations on devices running Enterprise SONiC"
source_url: https://docs.ansible.com/projects/ansible/8/collections/dellemc/enterprise_sonic/sonic_api_module.html
fetched_at: 2026-07-28T02:03:26+00:00
---
# dellemc.enterprise_sonic.sonic_api module – Manages REST operations on devices running Enterprise SONiC

> **Note:**
>
> This module is part of the [dellemc.enterprise_sonic collection](https://galaxy.ansible.com/ui/repo/published/dellemc/enterprise_sonic/) (version 2.2.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.enterprise_sonic`.
>
> To use it in a playbook, specify: `dellemc.enterprise_sonic.sonic_api`.

New in dellemc.enterprise_sonic 1.0.0

- [Synopsis](sonic_api_module.md#synopsis)
- [Parameters](sonic_api_module.md#parameters)
- [Notes](sonic_api_module.md#notes)
- [Examples](sonic_api_module.md#examples)
- [Return Values](sonic_api_module.md#return-values)

## [Synopsis](sonic_api_module.md#id1)

- Manages REST operations on devices running Enterprise SONiC Distribution by Dell Technologies. This module provides an implementation for working with SONiC REST operations in a deterministic way.

> **Note:**
>
> This module has a corresponding [action plugin](../../../plugins/action.md#action-plugins).

## [Parameters](sonic_api_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **body**  any | The body of the HTTP request/response to the web service which contains the payload. |
| **method**  string / required | The HTTP method of the request or response. Must be a valid method accepted by the service that handles the request.  **Choices:**   - `"GET"` - `"PUT"` - `"POST"` - `"PATCH"` - `"DELETE"` |
| **status_code**  list / elements=integer / required | A list of valid, numeric, HTTP status codes that signifies the success of a request. |
| **url**  path / required | The HTTP path of the request after ‘restconf/’. |

## [Notes](sonic_api_module.md#id3)

> **Note:**
>
> - Tested against Enterprise SONiC Distribution by Dell Technologies.
> - Supports `check_mode`.

## [Examples](sonic_api_module.md#id4)

```yaml+jinja
- name: Checks that you can connect (GET) to a page and it returns a status 200
  dellemc.enterprise_sonic.sonic_api:
    url: data/openconfig-interfaces:interfaces/interface=Ethernet60
    method: "GET"
    status_code: 200

- name: Appends data to an existing interface using PATCH and verifies if it returns status 204
  dellemc.enterprise_sonic.sonic_api:
    url: data/openconfig-interfaces:interfaces/interface=Ethernet60/config/description
    method: "PATCH"
    body: {"openconfig-interfaces:description": "Eth-60"}
    status_code: 204

- name: Deletes an associated IP address using DELETE and verifies if it returns status 204
  dellemc.enterprise_sonic.sonic_api:
    url: >
      data/openconfig-interfaces:interfaces/interface=Ethernet64/subinterfaces/subinterface=0/
      openconfig-if-ip:ipv4/addresses/address=1.1.1.1/config/prefix-length
    method: "DELETE"
    status_code: 204

- name: Adds a VLAN network instance using PUT and verifies if it returns status 204
  dellemc.enterprise_sonic.sonic_api:
    url: data/openconfig-network-instance:network-instances/network-instance=Vlan100/
    method: "PUT"
    body: {"openconfig-network-instance:network-instance": [{"name": "Vlan100","config": {"name": "Vlan100"}}]}
    status_code: 204

- name: Adds a prefix-set to a routing policy using POST and verifies if it returns 201
  dellemc.enterprise_sonic.sonic_api:
        url: data/openconfig-routing-policy:routing-policy/defined-sets/prefix-sets/prefix-set=p1
        method: "POST"
        body: {"openconfig-routing-policy:config": {"name": "p1","mode": "IPV4" }}
        status_code: 201
```

## [Return Values](sonic_api_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **msg**  string | The HTTP error message from the request.  **Returned:** HTTP Error |
| **response**  list / elements=string | The response at the network device end for the REST call which contains the status code.  **Returned:** always  **Sample:** `{"response": [204, {"": null}]}` |

### Authors

- Abirami N (@abirami-n)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/dellemc.enterprise_sonic/issues)
- [Repository (Sources)](https://github.com/ansible-collections/dellemc.enterprise_sonic)
