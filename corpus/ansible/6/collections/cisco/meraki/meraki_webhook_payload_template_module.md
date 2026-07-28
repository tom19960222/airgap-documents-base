---
collection: ansible
version: "6"
title: "cisco.meraki.meraki_webhook_payload_template module – Manage webhook payload templates for a network in the Meraki cloud"
source_url: https://docs.ansible.com/projects/ansible/6/collections/cisco/meraki/meraki_webhook_payload_template_module.html
fetched_at: 2026-07-27T17:00:44+00:00
---
# cisco.meraki.meraki_webhook_payload_template module – Manage webhook payload templates for a network in the Meraki cloud

> **Note:**
>
> This module is part of the [cisco.meraki collection](https://galaxy.ansible.com/cisco/meraki) (version 2.13.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.meraki`.
>
> To use it in a playbook, specify: `cisco.meraki.meraki_webhook_payload_template`.

- [Synopsis](meraki_webhook_payload_template_module.md#synopsis)
- [Parameters](meraki_webhook_payload_template_module.md#parameters)
- [Notes](meraki_webhook_payload_template_module.md#notes)
- [Examples](meraki_webhook_payload_template_module.md#examples)
- [Return Values](meraki_webhook_payload_template_module.md#return-values)

## [Synopsis](meraki_webhook_payload_template_module.md#id1)

- Allows for querying, deleting, creating, and updating of webhook payload templates.

## [Parameters](meraki_webhook_payload_template_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **auth_key**  string / required | Authentication key provided by the dashboard. Required if environmental variable `MERAKI_KEY` is not set. |
| **body**  string | The liquid template used for the body of the webhook message. |
| **headers**  list / elements=dictionary | List of the liquid templates used with the webhook headers.  Default: `[]` |
| **name**  string | The name of the header template. |
| **template**  string | The liquid template for the headers |
| **host**  string | Hostname for Meraki dashboard.  Can be used to access regional Meraki environments, such as China.  Default: `"api.meraki.com"` |
| **internal_error_retry_time**  integer | Number of seconds to retry if server returns an internal server error.  Default: `60` |
| **name**  string | Name of the template. |
| **net_id**  string | ID of network containing access points. |
| **net_name**  string | Name of network containing access points. |
| **org_id**  string | ID of organization. |
| **org_name**  aliases: organization  string | Name of organization. |
| **output_format**  string | Instructs module whether response keys should be snake case (ex. `net_id`) or camel case (ex. `netId`).  Choices:   - `"snakecase"` ← (default) - `"camelcase"` |
| **output_level**  string | Set amount of debug output during module execution.  Choices:   - `"debug"` - `"normal"` ← (default) |
| **rate_limit_retry_time**  integer | Number of seconds to retry if rate limiter is triggered.  Default: `165` |
| **state**  string | Specifies whether payload template should be queried, created, modified, or deleted.  Choices:   - `"absent"` - `"query"` ← (default) - `"present"` |
| **timeout**  integer | Time to timeout for HTTP requests.  Default: `30` |
| **use_https**  boolean | If `no`, it will use HTTP. Otherwise it will use HTTPS.  Only useful for internal Meraki developers.  Choices:   - `false` - `true` ← (default) |
| **use_proxy**  boolean | If `no`, it will not use a proxy, even if one is defined in an environment variable on the target hosts.  Choices:   - `false` ← (default) - `true` |
| **validate_certs**  boolean | Whether to validate HTTP certificates.  Choices:   - `false` - `true` ← (default) |

## [Notes](meraki_webhook_payload_template_module.md#id3)

> **Note:**
>
> - More information about the Meraki API can be found at <https://dashboard.meraki.com/api_docs>.
> - Some of the options are likely only used for developers within Meraki.
> - As of Ansible 2.9, Meraki modules output keys as snake case. To use camel case, set the `ANSIBLE_MERAKI_FORMAT` environment variable to `camelcase`.
> - Ansible’s Meraki modules will stop supporting camel case output in Ansible 2.13. Please update your playbooks.
> - Check Mode downloads the current configuration from the dashboard, then compares changes against this download. Check Mode will report changed if there are differences in the configurations, but does not submit changes to the API for validation of change.

## [Examples](meraki_webhook_payload_template_module.md#id4)

```yaml+jinja
- name: Query all configuration templates
  meraki_webhook_payload_template:
    auth_key: abc12345
    org_name: YourOrg
    state: query
  delegate_to: localhost

- name: Query specific configuration templates
  meraki_webhook_payload_template:
    auth_key: abc12345
    org_name: YourOrg
    state: query
    name: Twitter
  delegate_to: localhost

- name: Create payload template
  meraki_webhook_payload_template:
    auth_key: abc12345
    org_name: YourOrg
    state: query
    name: TestTemplate
    body: Testbody
    headers:
        - name: testheader
          template: testheadertemplate
  delegate_to: localhost

- name: Delete a configuration template
  meraki_config_template:
    auth_key: abc123
    state: absent
    org_name: YourOrg
    name: TestTemplate
  delegate_to: localhost
```

## [Return Values](meraki_webhook_payload_template_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **data**  complex | Information about queried object.  Returned: success |
| **body**  string | The liquid template used for the body of the webhook message.  Returned: success  Sample: `"{'client_payload': {'text': '{{alertData}}'}, 'event_type': '{{alertTypeId}}'}"` |
| **headers**  list / elements=string | List of the liquid templates used with the webhook headers.  Returned: success |
| **name**  string | The name of the template  Returned: success  Sample: `"testTemplate"` |
| **template**  string | The liquid template for the header  Returned: success  Sample: `"Bearer {{sharedSecret}}"` |
| **name**  string | The name of the template  Returned: success  Sample: `"testTemplate"` |

### Authors

- Joshua Coronado (@joshuajcoronado)

### Collection links

[Issue Tracker](https://github.com/CiscoDevNet/ansible-meraki/issues)
[Repository (Sources)](https://github.com/CiscoDevNet/ansible-meraki)
