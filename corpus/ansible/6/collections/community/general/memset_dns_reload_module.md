---
collection: ansible
version: "6"
title: "community.general.memset_dns_reload module – Request reload of Memset’s DNS infrastructure,"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/memset_dns_reload_module.html
fetched_at: 2026-07-27T17:10:54+00:00
---
# community.general.memset_dns_reload module – Request reload of Memset’s DNS infrastructure,

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
>
> To use it in a playbook, specify: `community.general.memset_dns_reload`.

- [Synopsis](memset_dns_reload_module.md#synopsis)
- [Parameters](memset_dns_reload_module.md#parameters)
- [Notes](memset_dns_reload_module.md#notes)
- [Examples](memset_dns_reload_module.md#examples)
- [Return Values](memset_dns_reload_module.md#return-values)

## [Synopsis](memset_dns_reload_module.md#id1)

- Request a reload of Memset’s DNS infrastructure, and optionally poll until it finishes.

## [Parameters](memset_dns_reload_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **api_key**  string / required | The API key obtained from the Memset control panel. |
| **poll**  boolean | Boolean value, if set will poll the reload job’s status and return when the job has completed (unless the 30 second timeout is reached first). If the timeout is reached then the task will not be marked as failed, but stderr will indicate that the polling failed.  Choices:   - `false` ← (default) - `true` |

## [Notes](memset_dns_reload_module.md#id3)

> **Note:**
>
> - DNS reload requests are a best-effort service provided by Memset; these generally happen every 15 minutes by default, however you can request an immediate reload if later tasks rely on the records being created. An API key generated via the Memset customer control panel is required with the following minimum scope - *dns.reload*. If you wish to poll the job status to wait until the reload has completed, then *job.status* is also required.

## [Examples](memset_dns_reload_module.md#id4)

```yaml+jinja
- name: Submit DNS reload and poll
  community.general.memset_dns_reload:
    api_key: 5eb86c9196ab03919abcf03857163741
    poll: true
  delegate_to: localhost
```

## [Return Values](memset_dns_reload_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **memset_api**  complex | Raw response from the Memset API.  Returned: always |
| **error**  boolean | Whether the job ended in error state.  Returned: always  Sample: `true` |
| **finished**  boolean | Whether the job completed before the result was returned.  Returned: always  Sample: `true` |
| **id**  string | Job ID.  Returned: always  Sample: `"c9cc8ad2a3e3fb8c63ed83c424928ef8"` |
| **status**  string | Job status.  Returned: always  Sample: `"DONE"` |
| **type**  string | Job type.  Returned: always  Sample: `"dns"` |

### Authors

- Simon Weald (@glitchcrab)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
