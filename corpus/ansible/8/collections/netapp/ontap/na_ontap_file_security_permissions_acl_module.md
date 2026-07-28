---
collection: ansible
version: "8"
title: "netapp.ontap.na_ontap_file_security_permissions_acl module – NetApp ONTAP file security permissions ACL"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/ontap/na_ontap_file_security_permissions_acl_module.html
fetched_at: 2026-07-28T02:42:08+00:00
---
# netapp.ontap.na_ontap_file_security_permissions_acl module – NetApp ONTAP file security permissions ACL

> **Note:**
>
> This module is part of the [netapp.ontap collection](https://galaxy.ansible.com/ui/repo/published/netapp/ontap/) (version 22.8.3).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install netapp.ontap`.
> You need further requirements to be able to use this module,
> see [Requirements](na_ontap_file_security_permissions_acl_module.md#ansible-collections-netapp-ontap-na-ontap-file-security-permissions-acl-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_file_security_permissions_acl`.

New in netapp.ontap 22.0.0

- [Synopsis](na_ontap_file_security_permissions_acl_module.md#synopsis)
- [Requirements](na_ontap_file_security_permissions_acl_module.md#requirements)
- [Parameters](na_ontap_file_security_permissions_acl_module.md#parameters)
- [Notes](na_ontap_file_security_permissions_acl_module.md#notes)
- [Examples](na_ontap_file_security_permissions_acl_module.md#examples)

## [Synopsis](na_ontap_file_security_permissions_acl_module.md#id1)

- Add, delete, or modify a file_security_permissions ACL on NetApp ONTAP.
- Note that ACLs are mached based on (‘user’, ‘access’, ‘access_control’, ‘apply_to’). To modify any of these 4 properties, you would need to delete the ACL and create a new one. Or use `netapp.ontap.na_ontap_file_security_permissions`.

## [Requirements](na_ontap_file_security_permissions_acl_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_file_security_permissions_acl_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access**  string / required | An ACE is an element in an access control list (ACL). An ACL can have zero or more ACEs.  Each ACE controls or monitors access to an object by a specified trustee.  **Choices:**   - `"access_allow"` - `"access_deny"` - `"audit_failure"` - `"audit_success"` |
| **access_control**  string | An Access Control Level specifies the access control of the task to be applied.  Valid values are “file-directory” or “Storage-Level Access Guard (SLAG)”.  SLAG is used to apply the specified security descriptors with the task for the volume or qtree.  Otherwise, the security descriptors are applied on files and directories at the specified path.  The value slag is not supported on FlexGroups volumes. The default value is “file-directory”.  This field requires ONTAP 9.10.1 or later. This defaults to “file_directory”.  **Choices:**   - `"file_directory"` - `"slag"` |
| **acl_user**  string / required | Specifies the account to which the ACE applies. Specify either name or SID.  As of 22.0.0, the module is not idempotent when using a SID.  Note - we cannot use `user` as if conflicts with the option for the admin user. |
| **advanced_rights**  dictionary | Specifies the advanced access right controlled by the ACE for the account specified. |
| **append_data**  boolean | Append Data.  **Choices:**   - `false` - `true` |
| **delete**  boolean | Delete.  **Choices:**   - `false` - `true` |
| **delete_child**  boolean | Delete Child.  **Choices:**   - `false` - `true` |
| **execute_file**  boolean | Execute File.  **Choices:**   - `false` - `true` |
| **full_control**  boolean | Full Control.  **Choices:**   - `false` - `true` |
| **read_attr**  boolean | Read Attributes.  **Choices:**   - `false` - `true` |
| **read_data**  boolean | Read Data.  **Choices:**   - `false` - `true` |
| **read_ea**  boolean | Read Extended Attributes.  **Choices:**   - `false` - `true` |
| **read_perm**  boolean | Read Permissions.  **Choices:**   - `false` - `true` |
| **write_attr**  boolean | Write Attributes.  **Choices:**   - `false` - `true` |
| **write_data**  boolean | Write Data.  **Choices:**   - `false` - `true` |
| **write_ea**  boolean | Write Extended Attributes.  **Choices:**   - `false` - `true` |
| **write_owner**  boolean | Write Owner.  **Choices:**   - `false` - `true` |
| **write_perm**  boolean | Write Permission.  **Choices:**   - `false` - `true` |
| **apply_to**  dictionary / required | Specifies where to apply the DACL or SACL entries.  With SLAGs, ONTAP accepts the three suboptions to be set to true, but creates 2 ACLs. This module requires the 2 ACLs to be present to preserve idempotency. See also `validate_changes`. |
| **files**  boolean | Apply to Files.  **Choices:**   - `false` ← (default) - `true` |
| **sub_folders**  boolean | Apply to all sub-folders.  **Choices:**   - `false` ← (default) - `true` |
| **this_folder**  boolean | Apply only to this folder  **Choices:**   - `false` ← (default) - `true` |
| **cert_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **feature_flags**  dictionary  *added in netapp.ontap 20.5.0* | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **force_ontap_version**  string  *added in netapp.ontap 21.23.0* | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  **Choices:**   - `false` ← (default) - `true` |
| **ignore_paths**  list / elements=string | For each file or directory in the list, specifies that permissions on this file or directory cannot be replaced. |
| **key_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client key file. |
| **ontapi**  integer | The ontap api version to use |
| **password**  aliases: pass  string | Password for the specified user. |
| **path**  string / required | The path of the file or directory on which to apply security permissions. |
| **propagation_mode**  string | Specifies how to propagate security settings to child subfolders and files.  Defaults to propagate.  This option is valid in create, but cannot modify.  **Choices:**   - `"propagate"` - `"replace"` |
| **rights**  string | Specifies the access right controlled by the ACE for the account specified.  The “rights” parameter is mutually exclusive with the “advanced_rights” parameter.  ONTAP translates rights into advanced_rights and this module is not idempotent when rights are used.  Make sure to use `advanced_rights` to maintain idempotency. `rights` can be used to discover the mapping to `advanced_rights`.  **Choices:**   - `"no_access"` - `"full_control"` - `"modify"` - `"read_and_execute"` - `"read"` - `"write"` |
| **state**  string | Whether the specified file security permissions ACL should exist or not.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  **Default:** `"auto"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |
| **validate_changes**  string | ACLs may not be applied as expected.  For instance, if Everyone is inherited will all permissions, additional users will be granted all permissions, regardless of the request.  For this specific example, you can either delete the top level Everyone, or create a new ACL for Everyone at a lower level.  When using `rights`, ONTAP translates them into `advanced_rights` so the validation will always fail.  Valid values are `ignore`, no checking; `warn` to issue a warning; `error` to fail the module.  With SLAGS, ONTAP may split one ACL into two ACLs depending on the `apply_to` settings. To maintain idempotency, please provide 2 ACLs as input.  **Choices:**   - `"ignore"` - `"warn"` - `"error"` ← (default) |
| **vserver**  string / required | Name of the vserver to use. |

## [Notes](na_ontap_file_security_permissions_acl_module.md#id4)

> **Note:**
>
> - Supports check_mode.
> - Only supported with REST and requires ONTAP 9.9.1 or later.
> - SLAG requires ONTAP 9.10.1 or later.
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_file_security_permissions_acl_module.md#id5)

```yaml+jinja
- name: Add ACL for file or directory security permissions.
  netapp.ontap.na_ontap_file_security_permissions_acl:
    vserver: "{{ vserver_name }}"
    access_control: file_directory
    path: "{{ file_mount_path }}"
    validate_changes: warn
    access: access_allow
    # Note, wihout quotes, use a single backslash in AD user names
    # with quotes, it needs to be escaped as a double backslash
    # user: "ANSIBLE_CIFS\user1"
    # we can't show an example with a single backslash as this is a python file, but it works in YAML.
    acl_user: "user1"
    apply_to:
      this_folder: true
    advanced_rights:
      append_data: true
      delete: false

- name: Modify ACL for file or directory security permissions.
  netapp.ontap.na_ontap_file_security_permissions_acl:
    vserver: "{{ vserver_name }}"
    access_control: file_directory
    path: "{{ file_mount_path }}"
    validate_changes: warn
    access: access_allow
    acl_user: "user1"
    apply_to:
      this_folder: true
    advanced_rights:
      append_data: false
      delete: true

- name: Delete ACL for file or directory security permissions.
  netapp.ontap.na_ontap_file_security_permissions_acl:
    vserver: "{{ vserver_name }}"
    access_control: file_directory
    path: "{{ file_mount_path }}"
    validate_changes: warn
    access: access_allow
    acl_user: "user1"
    apply_to:
      this_folder: true
    state: absent
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/netapp.ontap/issues)
- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.ontap)
