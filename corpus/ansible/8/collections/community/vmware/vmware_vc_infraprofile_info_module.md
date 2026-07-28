---
collection: ansible
version: "8"
title: "community.vmware.vmware_vc_infraprofile_info module – List and Export VMware vCenter infra profile configs."
source_url: https://docs.ansible.com/projects/ansible/8/collections/community/vmware/vmware_vc_infraprofile_info_module.html
fetched_at: 2026-07-28T02:01:15+00:00
---
# community.vmware.vmware_vc_infraprofile_info module – List and Export VMware vCenter infra profile configs.

> **Note:**
>
> This module is part of the [community.vmware collection](https://galaxy.ansible.com/ui/repo/published/community/vmware/) (version 3.11.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install community.vmware`.
> You need further requirements to be able to use this module,
> see [Requirements](vmware_vc_infraprofile_info_module.md#ansible-collections-community-vmware-vmware-vc-infraprofile-info-module-requirements) for details.
>
> To use it in a playbook, specify: `community.vmware.vmware_vc_infraprofile_info`.

- [Synopsis](vmware_vc_infraprofile_info_module.md#synopsis)
- [Requirements](vmware_vc_infraprofile_info_module.md#requirements)
- [Parameters](vmware_vc_infraprofile_info_module.md#parameters)
- [Examples](vmware_vc_infraprofile_info_module.md#examples)
- [Return Values](vmware_vc_infraprofile_info_module.md#return-values)

## [Synopsis](vmware_vc_infraprofile_info_module.md#id1)

- Module to manage VMware vCenter infra profile configs.
- vCenter infra profile Library feature is introduced in vSphere 7.0 version, so this module is not supported in the earlier versions of vSphere.
- All variables and VMware object names are case sensitive.

## [Requirements](vmware_vc_infraprofile_info_module.md#id2)

The below requirements are needed on the host that executes this module.

- vSphere Automation SDK

## [Parameters](vmware_vc_infraprofile_info_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **api**  string | API which needs to be executed  **Choices:**   - `"export"` - `"import"` - `"list"` - `"validate"` |
| **config_path**  string | Config file path which contains infra profile config JSON data, supports both relative and absolute path.  This parameter is required only when `import`,`validate` APIs are being used. |
| **decryption_key**  string | decryption_key argument for while doing import profile task as of now its not taken into account form API team. |
| **description**  string | Description of about encryption or decryption key. |
| **encryption_key**  string | encryption_key argument for while doing import profile task as of now its not taken into account form API team. |
| **hostname**  string | The hostname or IP address of the vSphere vCenter server.  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead. |
| **password**  aliases: pass, pwd  string | The password of the vSphere vCenter server.  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead. |
| **port**  integer | The port number of the vSphere vCenter.  If the value is not specified in the task, the value of environment variable `VMWARE_PORT` will be used instead.  **Default:** `443` |
| **profiles**  string | A list of profile names to be exported, imported, and validated.  This parameter is not required while running for List API, not for `export`,`import` and `validate`. |
| **protocol**  string | The connection to protocol.  **Choices:**   - `"http"` - `"https"` ← (default) |
| **proxy_host**  string | Address of a proxy that will receive all HTTPS requests and relay them.  The format is a hostname or a IP.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_HOST` will be used instead. |
| **proxy_port**  integer | Port of the HTTP proxy that will receive all HTTPS requests and relay them.  If the value is not specified in the task, the value of environment variable `VMWARE_PROXY_PORT` will be used instead. |
| **username**  aliases: admin, user  string | The username of the vSphere vCenter server.  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead. |
| **validate_certs**  boolean | Allows connection when SSL certificates are not valid.  Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |

## [Examples](vmware_vc_infraprofile_info_module.md#id4)

```yaml+jinja
- name: Get information about VC infraprofile
  vmware_vc_infraprofile_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
  delegate_to: localhost

- name: export vCenter appliance infra profile config
  vmware_vc_infraprofile_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    api: "export"
    profiles: "ApplianceManagement"
  delegate_to: localhost

- name: validate vCenter appliance infra profile config
  vmware_vc_infraprofile_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    api: "validate"
    profiles: "ApplianceManagement"
    config_path: "export.json"

- name: import vCenter appliance infra profile config
  vmware_vc_infraprofile_info:
    hostname: '{{ vcenter_hostname }}'
    username: '{{ vcenter_username }}'
    password: '{{ vcenter_password }}'
    api: "import"
    profiles: "ApplianceManagement"
    config_path: "import.json"
  delegate_to: localhost
```

## [Return Values](vmware_vc_infraprofile_info_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **export_infra**  dictionary | A message about the exported file  **Returned:** On success with API set as “export”  **Sample:** `{"export_config_json": "json exported to file"}` |
| **import_profile**  dictionary | A message about import on import_profile spec  **Returned:** On success with API set as “import”  **Sample:** `{"changed": true, "failed": false, "status": "0.0"}` |
| **list_infra**  list / elements=string | A list of infra configs,  **Returned:** on success with API as “list”  **Sample:** `[{"info": "ApplianceManagement", "name": "ApplianceManagement"}, {"info": "ApplianceNetwork", "name": "ApplianceNetwork"}, {"info": "Authentication & Authorization Management", "name": "AuthManagement"}]` |
| **validate_infra**  dictionary | A message about validate on exported file  **Returned:** On success with API set as “validate”  **Sample:** `{"changed": false, "failed": false, "status": "VALID"}` |

### Authors

- Naveenkumar G P (@ngp)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/community.vmware/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/community.vmware)
- [Repository (Sources)](https://github.com/ansible-collections/community.vmware.git)
