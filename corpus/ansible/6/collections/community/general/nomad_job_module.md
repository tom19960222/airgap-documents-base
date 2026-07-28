---
collection: ansible
version: "6"
title: "community.general.nomad_job module – Launch a Nomad Job"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/nomad_job_module.html
fetched_at: 2026-07-27T17:11:07+00:00
---
# community.general.nomad_job module – Launch a Nomad Job

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/community/general) (version 5.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](nomad_job_module.md#ansible-collections-community-general-nomad-job-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.nomad_job`.

New in community.general 1.3.0

- [Synopsis](nomad_job_module.md#synopsis)
- [Requirements](nomad_job_module.md#requirements)
- [Parameters](nomad_job_module.md#parameters)
- [Notes](nomad_job_module.md#notes)
- [See Also](nomad_job_module.md#see-also)
- [Examples](nomad_job_module.md#examples)

## [Synopsis](nomad_job_module.md#id1)

- Launch a Nomad job.
- Stop a Nomad job.
- Force start a Nomad job

## [Requirements](nomad_job_module.md#id2)

The below requirements are needed on the host that executes this module.

- python-nomad

## [Parameters](nomad_job_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **client_cert**  path | Path of certificate for TLS/SSL. |
| **client_key**  path | Path of certificate’s private key for TLS/SSL. |
| **content**  string | Content of Nomad job.  Either this or *name* must be specified. |
| **content_format**  string | Type of content of Nomad job.  Choices:   - `"hcl"` ← (default) - `"json"` |
| **force_start**  boolean | Force job to started.  Choices:   - `false` ← (default) - `true` |
| **host**  string / required | FQDN of Nomad server. |
| **name**  string | Name of job for delete, stop and start job without source.  Name of job for delete, stop and start job without source.  Either this or *content* must be specified. |
| **namespace**  string | Namespace for Nomad. |
| **state**  string / required | Deploy or remove job.  Choices:   - `"present"` - `"absent"` |
| **timeout**  integer | Timeout (in seconds) for the request to Nomad.  Default: `5` |
| **token**  string | ACL token for authentification. |
| **use_ssl**  boolean | Use TLS/SSL connection.  Choices:   - `false` - `true` ← (default) |
| **validate_certs**  boolean | Enable TLS/SSL certificate validation.  Choices:   - `false` - `true` ← (default) |

## [Notes](nomad_job_module.md#id4)

> **Note:**
>
> - `check_mode` is supported.

## [See Also](nomad_job_module.md#id5)

> **See also:**
>
> [Nomad jobs documentation](https://www.nomadproject.io/api-docs/jobs/)
> :   Complete documentation for Nomad API jobs.

## [Examples](nomad_job_module.md#id6)

```yaml+jinja
- name: Create job
  community.general.nomad_job:
    host: localhost
    state: present
    content: "{{ lookup('ansible.builtin.file', 'job.hcl') }}"
    timeout: 120

- name: Stop job
  community.general.nomad_job:
    host: localhost
    state: absent
    name: api

- name: Force job to start
  community.general.nomad_job:
    host: localhost
    state: present
    name: api
    timeout: 120
    force_start: true
```

### Authors

- FERREIRA Christophe (@chris93111)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
