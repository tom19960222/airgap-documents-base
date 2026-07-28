---
collection: ansible
version: "8"
title: "community.general.serverless module – Manages a Serverless Framework project"
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/general/serverless_module.html
fetched_at: 2026-07-28T01:50:34+00:00
---
# community.general.serverless module – Manages a Serverless Framework project

> **Note:**
>
> This module is part of the [community.general collection](https://galaxy.ansible.com/ui/repo/published/community/general/) (version 7.5.2).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.general`.
> You need further requirements to be able to use this module,
> see [Requirements](serverless_module.md#ansible-collections-community-general-serverless-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.serverless`.

- [Synopsis](serverless_module.md#synopsis)
- [Requirements](serverless_module.md#requirements)
- [Parameters](serverless_module.md#parameters)
- [Attributes](serverless_module.md#attributes)
- [Notes](serverless_module.md#notes)
- [Examples](serverless_module.md#examples)
- [Return Values](serverless_module.md#return-values)

## [Synopsis](serverless_module.md#id1)

- Provides support for managing Serverless Framework (<https://serverless.com/>) project deployments and stacks.

Aliases: cloud.misc.serverless

## [Requirements](serverless_module.md#id2)

The below requirements are needed on the host that executes this module.

- serverless
- yaml

## [Parameters](serverless_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **deploy**  boolean | Whether or not to deploy artifacts after building them.  When this option is `false` all the functions will be built, but no stack update will be run to send them out.  This is mostly useful for generating artifacts to be stored/deployed elsewhere.  **Choices:**   - `false` - `true` ← (default) |
| **force**  boolean | Whether or not to force full deployment, equivalent to serverless `--force` option.  **Choices:**   - `false` ← (default) - `true` |
| **region**  string | AWS region to deploy the service to.  This parameter defaults to `us-east-1`.  **Default:** `""` |
| **serverless_bin_path**  path | The path of a serverless framework binary relative to the ‘service_path’ eg. node_module/.bin/serverless |
| **service_path**  path / required | The path to the root of the Serverless Service to be operated on. |
| **stage**  string | The name of the serverless framework project stage to deploy to.  This uses the serverless framework default “dev”.  **Default:** `""` |
| **state**  string | Goal state of given stage/project.  **Choices:**   - `"absent"` - `"present"` ← (default) |
| **verbose**  boolean | Shows all stack events during deployment, and display any Stack Output.  **Choices:**   - `false` ← (default) - `true` |

## [Attributes](serverless_module.md#id4)

| Attribute | Support | Description |
| --- | --- | --- |
| **check_mode** | **Support:** **none** | Can run in `check_mode` and return changed status prediction without modifying target. |
| **diff_mode** | **Support:** **none** | Will return details on what has changed (or possibly needs changing in `check_mode`), when in diff mode. |

## [Notes](serverless_module.md#id5)

> **Note:**
>
> - Currently, the `serverless` command must be in the path of the node executing the task. In the future this may be a flag.

## [Examples](serverless_module.md#id6)

```yaml+jinja
- name: Basic deploy of a service
  community.general.serverless:
    service_path: '{{ project_dir }}'
    state: present

- name: Deploy a project, then pull its resource list back into Ansible
  community.general.serverless:
    stage: dev
    region: us-east-1
    service_path: '{{ project_dir }}'
  register: sls

# The cloudformation stack is always named the same as the full service, so the
# cloudformation_info module can get a full list of the stack resources, as
# well as stack events and outputs
- cloudformation_info:
    region: us-east-1
    stack_name: '{{ sls.service_name }}'
    stack_resources: true

- name: Deploy a project using a locally installed serverless binary
  community.general.serverless:
    stage: dev
    region: us-east-1
    service_path: '{{ project_dir }}'
    serverless_bin_path: node_modules/.bin/serverless
```

## [Return Values](serverless_module.md#id7)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **command**  string | Full `serverless` command run by this module, in case you want to re-run the command outside the module.  **Returned:** always  **Sample:** `"serverless deploy --stage production"` |
| **service_name**  string | The service name specified in the serverless.yml that was just deployed.  **Returned:** always  **Sample:** `"my-fancy-service-dev"` |
| **state**  string | Whether the stack for the serverless project is present/absent.  **Returned:** always |

### Authors

- Ryan Scott Brown (@ryansb)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.general/issues)
- [Repository (Sources)](https://github.com/ansible-collections/community.general)
- [Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
- [Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
- [Communication](index.md#communication-for-community-general)
