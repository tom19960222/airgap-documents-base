---
collection: ansible
version: "6"
title: "vultr.cloud.ssh_key module – Manages ssh keys on Vultr."
source_url: https://docs.ansible.com/projects/ansible/6/collections/vultr/cloud/ssh_key_module.html
fetched_at: 2026-07-28T00:23:06+00:00
---
# vultr.cloud.ssh_key module – Manages ssh keys on Vultr.

> **Note:**
>
> This module is part of the [vultr.cloud collection](https://galaxy.ansible.com/vultr/cloud) (version 1.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install vultr.cloud`.
>
> To use it in a playbook, specify: `vultr.cloud.ssh_key`.

New in vultr.cloud 1.0.0

- [Synopsis](ssh_key_module.md#synopsis)
- [Parameters](ssh_key_module.md#parameters)
- [Notes](ssh_key_module.md#notes)
- [Examples](ssh_key_module.md#examples)
- [Return Values](ssh_key_module.md#return-values)

## [Synopsis](ssh_key_module.md#id1)

- Create, update and remove ssh keys.

## [Parameters](ssh_key_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_endpoint**  string | URL to API endpint (without trailing slash).  Fallback environment variable `VULTR_API_ENDPOINT`.  Default: `"https://api.vultr.com/v2"` |
| **api_key**  string / required | API key of the Vultr API.  Fallback environment variable `VULTR_API_KEY`. |
| **api_retries**  integer | Amount of retries in case of the Vultr API retuns an HTTP 503 code.  Fallback environment variable `VULTR_API_RETRIES`.  Default: `5` |
| **api_retry_max_delay**  integer | Retry backoff delay in seconds is exponential up to this max. value, in seconds.  Fallback environment variable `VULTR_API_RETRY_MAX_DELAY`.  Default: `12` |
| **api_timeout**  integer | HTTP timeout to Vultr API.  Fallback environment variable `VULTR_API_TIMEOUT`.  Default: `60` |
| **name**  string / required | Name of the ssh key. |
| **ssh_key**  string | SSH public key.  Required if `state=present`. |
| **state**  string | State of the ssh key.  Choices:   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | Validate SSL certs of the Vultr API.  Choices:   - `false` - `true` ← (default) |

## [Notes](ssh_key_module.md#id3)

> **Note:**
>
> - Also see the API documentation on <https://www.vultr.com/api/>.

## [Examples](ssh_key_module.md#id4)

```yaml+jinja
- name: ensure an SSH key is present
  vultr.cloud.ssh_key:
    name: my ssh key
    ssh_key: "{{ lookup('file', '~/.ssh/id_rsa.pub') }}"

- name: ensure an SSH key is absent
  vultr.cloud.ssh_key:
    name: my ssh key
    state: absent
```

## [Return Values](ssh_key_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **vultr_api**  dictionary | Response from Vultr API with a few additions/modification.  Returned: success |
| **api_endpoint**  string | Endpoint used for the API requests.  Returned: success  Sample: `"https://api.vultr.com/v2"` |
| **api_retries**  integer | Amount of max retries for the API requests.  Returned: success  Sample: `5` |
| **api_retry_max_delay**  integer | Exponential backoff delay in seconds between retries up to this max delay value.  Returned: success  Sample: `12` |
| **api_timeout**  integer | Timeout used for the API requests.  Returned: success  Sample: `60` |
| **vultr_ssh_key**  dictionary | Response from Vultr API.  Returned: success |
| **date_created**  string | Date the ssh key was created.  Returned: success  Sample: `"2020-10-10T01:56:20+00:00"` |
| **id**  string | ID of the ssh key.  Returned: success  Sample: `"cb676a46-66fd-4dfb-b839-443f2e6c0b60"` |
| **name**  string | Name of the ssh key.  Returned: success  Sample: `"my ssh key"` |
| **ssh_key**  string | SSH public key.  Returned: success  Sample: `"ssh-rsa AA... someother@example.com"` |

### Authors

- René Moser (@resmo)

### Collection links

[Issue Tracker](https://github.com/vultr/ansible-collection-vultr/issues)
[Repository (Sources)](https://github.com/vultr/ansible-collection-vultr)
