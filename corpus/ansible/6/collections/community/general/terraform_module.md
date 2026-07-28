---
collection: ansible
version: "6"
title: "community.general.terraform module – Manages a Terraform deployment (and plans)"
source_url: https://docs.ansible.com/projects/ansible/6/collections/community/general/terraform_module.html
fetched_at: 2026-07-27T17:13:35+00:00
---
# community.general.terraform module – Manages a Terraform deployment (and plans)

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
> see [Requirements](terraform_module.md#ansible-collections-community-general-terraform-module-requirements) for details.
>
> To use it in a playbook, specify: `community.general.terraform`.

- [Synopsis](terraform_module.md#synopsis)
- [Requirements](terraform_module.md#requirements)
- [Parameters](terraform_module.md#parameters)
- [Notes](terraform_module.md#notes)
- [Examples](terraform_module.md#examples)
- [Return Values](terraform_module.md#return-values)

## [Synopsis](terraform_module.md#id1)

- Provides support for deploying resources with Terraform and pulling resource information back into Ansible.

## [Requirements](terraform_module.md#id2)

The below requirements are needed on the host that executes this module.

- terraform

## [Parameters](terraform_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **backend_config**  dictionary | A group of key-values to provide at init stage to the -backend-config parameter. |
| **backend_config_files**  list / elements=path  added in community.general 0.2.0 | The path to a configuration file to provide at init state to the -backend-config parameter. This can accept a list of paths to multiple configuration files. |
| **binary_path**  path | The path of a terraform binary to use, relative to the ‘service_path’ unless you supply an absolute path. |
| **check_destroy**  boolean  added in community.general 3.3.0 | Apply only when no resources are destroyed. Note that this only prevents “destroy” actions, but not “destroy and re-create” actions. This option is ignored when *state=absent*.  Choices:   - `false` ← (default) - `true` |
| **complex_vars**  boolean  added in community.general 5.7.0 | Enable/disable capability to handle complex variable structures for `terraform`.  If `true` the *variables* also accepts dictionaries, lists, and booleans to be passed to `terraform`. Strings that are passed are correctly quoted.  When disabled, supports only simple variables (strings, integers, and floats), and passes them on unquoted.  Choices:   - `false` ← (default) - `true` |
| **force_init**  boolean | To avoid duplicating infra, if a state file can’t be found this will force a `terraform init`. Generally, this should be turned off unless you intend to provision an entirely new Terraform deployment.  Choices:   - `false` ← (default) - `true` |
| **init_reconfigure**  boolean  added in community.general 1.3.0 | Forces backend reconfiguration during init.  Choices:   - `false` ← (default) - `true` |
| **lock**  boolean | Enable statefile locking, if you use a service that accepts locks (such as S3+DynamoDB) to store your statefile.  Choices:   - `false` - `true` ← (default) |
| **lock_timeout**  integer | How long to maintain the lock on the statefile, if you use a service that accepts locks (such as S3+DynamoDB). |
| **overwrite_init**  boolean  added in community.general 3.2.0 | Run init even if `.terraform/terraform.tfstate` already exists in *project_path*.  Choices:   - `false` - `true` ← (default) |
| **parallelism**  integer  added in community.general 3.8.0 | Restrict concurrent operations when Terraform applies the plan. |
| **plan_file**  path | The path to an existing Terraform plan file to apply. If this is not specified, Ansible will build a new TF plan and execute it. Note that this option is required if ‘state’ has the ‘planned’ value. |
| **plugin_paths**  list / elements=path  added in community.general 3.0.0 | List of paths containing Terraform plugin executable files.  Plugin executables can be downloaded from <https://releases.hashicorp.com/>.  When set, the plugin discovery and auto-download behavior of Terraform is disabled.  The directory structure in the plugin path can be tricky. The Terraform docs <https://learn.hashicorp.com/tutorials/terraform/automate-terraform#pre-installed-plugins> show a simple directory of files, but actually, the directory structure has to follow the same structure you would see if Terraform auto-downloaded the plugins. See the examples below for a tree output of an example plugin directory. |
| **project_path**  path / required | The path to the root of the Terraform directory with the vars.tf/main.tf/etc to use. |
| **provider_upgrade**  boolean  added in community.general 4.8.0 | Allows Terraform init to upgrade providers to versions specified in the project’s version constraints.  Choices:   - `false` ← (default) - `true` |
| **purge_workspace**  boolean | Only works with state = absent  If true, the workspace will be deleted after the “terraform destroy” action.  The ‘default’ workspace will not be deleted.  Choices:   - `false` ← (default) - `true` |
| **state**  string | Goal state of given stage/project  Choices:   - `"planned"` - `"present"` ← (default) - `"absent"` |
| **state_file**  path | The path to an existing Terraform state file to use when building plan. If this is not specified, the default `terraform.tfstate` will be used.  This option is ignored when plan is specified. |
| **targets**  list / elements=string | A list of specific resources to target in this plan/application. The resources selected here will also auto-include any dependencies.  Default: `[]` |
| **variables**  dictionary | A group of key-values pairs to override template variables or those in variables files. By default, only string and number values are allowed, which are passed on unquoted.  Support complex variable structures (lists, dictionaries, numbers, and booleans) to reflect terraform variable syntax when *complex_vars=true*.  Ansible integers or floats are mapped to terraform numbers.  Ansible strings are mapped to terraform strings.  Ansible dictionaries are mapped to terraform objects.  Ansible lists are mapped to terraform lists.  Ansible booleans are mapped to terraform booleans.  **Note** passwords passed as variables will be visible in the log output. Make sure to use *no_log=true* in production! |
| **variables_files**  aliases: variables_file  list / elements=path | The path to a variables file for Terraform to fill into the TF configurations. This can accept a list of paths to multiple variables files.  Up until Ansible 2.9, this option was usable as *variables_file*. |
| **workspace**  string | The terraform workspace to work with.  Default: `"default"` |

## [Notes](terraform_module.md#id4)

> **Note:**
>
> - To just run a `terraform plan`, use check mode.

## [Examples](terraform_module.md#id5)

```yaml+jinja
- name: Basic deploy of a service
  community.general.terraform:
    project_path: '{{ project_dir }}'
    state: present

- name: Define the backend configuration at init
  community.general.terraform:
    project_path: 'project/'
    state: "{{ state }}"
    force_init: true
    backend_config:
      region: "eu-west-1"
      bucket: "some-bucket"
      key: "random.tfstate"

- name: Define the backend configuration with one or more files at init
  community.general.terraform:
    project_path: 'project/'
    state: "{{ state }}"
    force_init: true
    backend_config_files:
      - /path/to/backend_config_file_1
      - /path/to/backend_config_file_2

- name: Disable plugin discovery and auto-download by setting plugin_paths
  community.general.terraform:
    project_path: 'project/'
    state: "{{ state }}"
    force_init: true
    plugin_paths:
      - /path/to/plugins_dir_1
      - /path/to/plugins_dir_2

- name: Complex variables example
  community.general.terraform:
    project_path: '{{ project_dir }}'
    state: present
    camplex_vars: true
    variables:
      vm_name: "{{ inventory_hostname }}"
      vm_vcpus: 2
      vm_mem: 2048
      vm_additional_disks:
        - label: "Third Disk"
          size: 40
          thin_provisioned: true
          unit_number: 2
        - label: "Fourth Disk"
          size: 22
          thin_provisioned: true
          unit_number: 3
    force_init: true

### Example directory structure for plugin_paths example
# $ tree /path/to/plugins_dir_1
# /path/to/plugins_dir_1/
# └── registry.terraform.io
#     └── hashicorp
#         └── vsphere
#             ├── 1.24.0
#             │   └── linux_amd64
#             │       └── terraform-provider-vsphere_v1.24.0_x4
#             └── 1.26.0
#                 └── linux_amd64
#                     └── terraform-provider-vsphere_v1.26.0_x4
```

## [Return Values](terraform_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **command**  string | Full `terraform` command built by this module, in case you want to re-run the command outside the module or debug a problem.  Returned: always  Sample: `"terraform apply ..."` |
| **outputs**  complex | A dictionary of all the TF outputs by their assigned name. Use `.outputs.MyOutputName.value` to access the value.  Returned: on success  Sample: `"{\"bukkit_arn\": {\"sensitive\": false, \"type\": \"string\", \"value\": \"arn:aws:s3:::tf-test-bukkit\"}"` |
| **sensitive**  boolean | Whether Terraform has marked this value as sensitive  Returned: always |
| **type**  string | The type of the value (string, int, etc)  Returned: always |
| **value**  string | The value of the output as interpolated by Terraform  Returned: always |
| **stdout**  string | Full `terraform` command stdout, in case you want to display it or examine the event log  Returned: always  Sample: `""` |

### Authors

- Ryan Scott Brown (@ryansb)

### Collection links

[Issue Tracker](https://github.com/ansible-collections/community.general/issues)
[Repository (Sources)](https://github.com/ansible-collections/community.general)
[Submit a bug report](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=bug_report.yml)
[Request a feature](https://github.com/ansible-collections/community.general/issues/new?assignees=&labels=&template=feature_request.yml)
[Communication](index.md#communication-for-community-general)
