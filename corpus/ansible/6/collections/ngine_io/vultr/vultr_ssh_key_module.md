---
collection: ansible
version: "6"
title: "ngine_io.vultr.vultr_ssh_key module – Manages ssh keys on Vultr."
source_url: https://docs.ansible.com/projects/ansible/6/collections/ngine_io/vultr/vultr_ssh_key_module.html
fetched_at: 2026-07-28T00:16:13+00:00
---
# ngine_io.vultr.vultr_ssh_key module – Manages ssh keys on Vultr.

> **Note:**
>
> This module is part of the [ngine_io.vultr collection](https://galaxy.ansible.com/ngine_io/vultr) (version 1.1.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install ngine_io.vultr`.
> You need further requirements to be able to use this module,
> see [Requirements](vultr_ssh_key_module.md#ansible-collections-ngine-io-vultr-vultr-ssh-key-module-requirements) for details.
>
> To use it in a playbook, specify: `ngine_io.vultr.vultr_ssh_key`.

New in ngine_io.vultr 0.1.0

- [Synopsis](vultr_ssh_key_module.md#synopsis)
- [Requirements](vultr_ssh_key_module.md#requirements)
- [Parameters](vultr_ssh_key_module.md#parameters)
- [Notes](vultr_ssh_key_module.md#notes)
- [Examples](vultr_ssh_key_module.md#examples)
- [Return Values](vultr_ssh_key_module.md#return-values)

## [Synopsis](vultr_ssh_key_module.md#id1)

- Create, update and remove ssh keys.

## [Requirements](vultr_ssh_key_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 2.6

## [Parameters](vultr_ssh_key_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api_account**  string | Name of the ini section in the `vultr.ini` file.  The ENV variable `VULTR_API_ACCOUNT` is used as default, when defined.  Default: `"default"` |
| **api_endpoint**  string | URL to API endpint (without trailing slash).  The ENV variable `VULTR_API_ENDPOINT` is used as default, when defined.  Fallback value is <https://api.vultr.com> if not specified. |
| **api_key**  string | API key of the Vultr API.  The ENV variable `VULTR_API_KEY` is used as default, when defined. |
| **api_retries**  integer | Amount of retries in case of the Vultr API retuns an HTTP 503 code.  The ENV variable `VULTR_API_RETRIES` is used as default, when defined.  Fallback value is 5 retries if not specified. |
| **api_retry_max_delay**  integer | Retry backoff delay in seconds is exponential up to this max. value, in seconds.  The ENV variable `VULTR_API_RETRY_MAX_DELAY` is used as default, when defined.  Fallback value is 12 seconds. |
| **api_timeout**  integer | HTTP timeout to Vultr API.  The ENV variable `VULTR_API_TIMEOUT` is used as default, when defined.  Fallback value is 60 seconds if not specified. |
| **name**  string / required | Name of the ssh key. |
| **ssh_key**  string | SSH public key.  Required if `state=present`. |
| **state**  string | State of the ssh key.  Choices:   - `"present"` ← (default) - `"absent"` |
| **validate_certs**  boolean | Validate SSL certs of the Vultr API.  Choices:   - `false` - `true` ← (default) |

## [Notes](vultr_ssh_key_module.md#id4)

> **Note:**
>
> - Also see the API documentation on <https://www.vultr.com/api/>.

## [Examples](vultr_ssh_key_module.md#id5)

```yaml+jinja
- name: ensure an SSH key is present
  ngine_io.vultr.vultr_ssh_key:
    name: my ssh key
    ssh_key: "{{ lookup('file', '~/.ssh/id_rsa.pub') }}"

- name: ensure an SSH key is absent
  ngine_io.vultr.vultr_ssh_key:
    name: my ssh key
    state: absent
```

## [Return Values](vultr_ssh_key_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **vultr_api**  complex | Response from Vultr API with a few additions/modification  Returned: success |
| **api_account**  string | Account used in the ini file to select the key  Returned: success  Sample: `"default"` |
| **api_endpoint**  string | Endpoint used for the API requests  Returned: success  Sample: `"https://api.vultr.com"` |
| **api_retries**  integer | Amount of max retries for the API requests  Returned: success  Sample: `5` |
| **api_retry_max_delay**  integer | Exponential backoff delay in seconds between retries up to this max delay value.  Returned: success  Sample: `12` |
| **api_timeout**  integer | Timeout used for the API requests  Returned: success  Sample: `60` |
| **vultr_ssh_key**  complex | Response from Vultr API  Returned: success |
| **date_created**  string | Date the ssh key was created  Returned: success  Sample: `"2017-08-26 12:47:48"` |
| **id**  string | ID of the ssh key  Returned: success  Sample: `"5904bc6ed9234"` |
| **name**  string | Name of the ssh key  Returned: success  Sample: `"my ssh key"` |
| **ssh_key**  string | SSH public key  Returned: success  Sample: `"ssh-rsa AA... someother@example.com"` |

### Authors

- René Moser (@resmo)

### Collection links

[Issue Tracker](https://github.com/ngine-io/ansible-collection-vultr/issues)
[Repository (Sources)](https://github.com/ngine-io/ansible-collection-vultr)
