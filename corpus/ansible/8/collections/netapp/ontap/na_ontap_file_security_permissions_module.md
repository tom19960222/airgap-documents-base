---
collection: ansible
version: "8"
title: "netapp.ontap.na_ontap_file_security_permissions module – NetApp ONTAP NTFS file security permissions"
source_url: https://docs.ansible.com/projects/ansible/8/collections/netapp/ontap/na_ontap_file_security_permissions_module.html
fetched_at: 2026-07-28T02:42:07+00:00
---
# netapp.ontap.na_ontap_file_security_permissions module – NetApp ONTAP NTFS file security permissions

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
> see [Requirements](na_ontap_file_security_permissions_module.md#ansible-collections-netapp-ontap-na-ontap-file-security-permissions-module-requirements) for details.
>
> To use it in a playbook, specify: `netapp.ontap.na_ontap_file_security_permissions`.

New in netapp.ontap 22.0.0

- [Synopsis](na_ontap_file_security_permissions_module.md#synopsis)
- [Requirements](na_ontap_file_security_permissions_module.md#requirements)
- [Parameters](na_ontap_file_security_permissions_module.md#parameters)
- [Notes](na_ontap_file_security_permissions_module.md#notes)
- [Examples](na_ontap_file_security_permissions_module.md#examples)

## [Synopsis](na_ontap_file_security_permissions_module.md#id1)

- Create, delete, or modify NTFS file security and audit policies of file or directory on NetApp ONTAP.
- Note that ACLs are mached based on (‘user’, ‘access’, ‘access_control’, ‘apply_to’). In order to modify any of these 4 properties, the module deletes the ACL and creates a new one.

## [Requirements](na_ontap_file_security_permissions_module.md#id2)

The below requirements are needed on the host that executes this module.

- Ansible 2.9 or later - 2.12 or later is recommended.
- Python3 - 3.9 or later is recommended.
- When using ZAPI, netapp-lib 2018.11.13 or later (install using ‘pip install netapp-lib’), netapp-lib 2020.3.12 is strongly recommended as it provides better error reporting for connection issues
- a physical or virtual clustered Data ONTAP system, the modules support Data ONTAP 9.1 and onward, REST support requires ONTAP 9.6 or later

## [Parameters](na_ontap_file_security_permissions_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **access_control**  string | An Access Control Level specifies the access control of the task to be applied.  Valid values are “file-directory” or “Storage-Level Access Guard (SLAG)”.  SLAG is used to apply the specified security descriptors with the task for the volume or qtree.  Otherwise, the security descriptors are applied on files and directories at the specified path.  The value slag is not supported on FlexGroups volumes. The default value is “file-directory”.  This field requires ONTAP 9.10.1 or later. This defaults to “file_directory”.  When state is present, all ACLs not listed in `acls` are deleted when this option is absent. If this option is present, only ACLs matching its value are deleted.  When state is absent, all ACLs are deleted when this option is absent. If this option is present, only ACLs matching its value are deleted.  **Choices:**   - `"file_directory"` - `"slag"` |
| **acls**  list / elements=dictionary | A discretionary access security list (DACL) identifies the trustees that are allowed or denied access to a securable object.  When a process tries to access a securable object, the system checks the access control entries (ACEs) in the object’s DACL to determine whether to grant access to it. |
| **access**  string / required | Specifies whether the ACL is for DACL or SACL.  Currently tested with access_allow, access_deny for DACL and audit_failure, audit_success for SACL.  **Choices:**   - `"access_allow"` - `"access_deny"` - `"access_allowed_callback"` - `"access_denied_callback"` - `"access_allowed_callback_object"` - `"access_denied_callback_object"` - `"system_audit_callback"` - `"system_audit_callback_object"` - `"system_resource_attribute"` - `"system_scoped_policy_id"` - `"audit_failure"` - `"audit_success"` - `"audit_success_and_failure"` |
| **access_control**  string | An Access Control Level specifies the access control of the task to be applied.  Valid values are “file-directory” or “Storage-Level Access Guard (SLAG)”.  SLAG is used to apply the specified security descriptors with the task for the volume or qtree.  Otherwise, the security descriptors are applied on files and directories at the specified path.  The value slag is not supported on FlexGroups volumes. The default value is “file-directory”.  This field requires ONTAP 9.10.1 or later. This defaults to “file_directory”.  **Choices:**   - `"file_directory"` - `"slag"` |
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
| **apply_to**  dictionary / required | Specifies where to apply the DACL or SACL entries.  At least one suboption must be set to true. Suboptions that are not set are assumed to be false.  With SLAGs, ONTAP accepts the three suboptions to be set to true, but creates 2 ACLs. This module requires the 2 ACLs to be present to preserve idempotency. See also `validate_changes`. |
| **files**  boolean | Apply to Files.  **Choices:**   - `false` ← (default) - `true` |
| **sub_folders**  boolean | Apply to all sub-folders.  **Choices:**   - `false` ← (default) - `true` |
| **this_folder**  boolean | Apply only to this folder  **Choices:**   - `false` ← (default) - `true` |
| **ignore_paths**  list / elements=string | For each file or directory in the list, specifies that permissions on this file or directory cannot be replaced. |
| **propagation_mode**  string | Specifies how to propagate security settings to child subfolders and files.  Defaults to propagate.  This option valid only in create ACL.  **Choices:**   - `"propagate"` - `"replace"` |
| **rights**  string | Specifies the access right controlled by the ACE for the account specified.  The “rights” parameter is mutually exclusive with the “advanced_rights” parameter.  ONTAP translates rights into advanced_rights and this module is not idempotent when rights are used.  Make sure to use `advanced_rights` to maintain idempotency. `rights` can be used to discover the mapping to `advanced_rights`.  **Choices:**   - `"no_access"` - `"full_control"` - `"modify"` - `"read_and_execute"` - `"read"` - `"write"` |
| **user**  aliases: acl_user  string / required | Specifies the account to which the ACE applies. Specify either name or SID.  As of 21.24.0, the module is not idempotent when using a SID.  To make it easier when also using `na_ontap_file_security_permissions_acl`, this is aliased to `acl_user`. |
| **cert_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client cert file (.pem).  not supported with python 2.6. |
| **control_flags**  string | Specifies the control flags in the SD. It is a Hexadecimal Value. |
| **feature_flags**  dictionary  *added in netapp.ontap 20.5.0* | Enable or disable a new feature.  This can be used to enable an experimental feature or disable a new feature that breaks backward compatibility.  Supported keys and values are subject to change without notice. Unknown keys are ignored. |
| **force_ontap_version**  string  *added in netapp.ontap 21.23.0* | Override the cluster ONTAP version when using REST.  The behavior is undefined if the version does not match the target cluster.  This is provided as a work-around when the cluster version cannot be read because of permission issues. See <https://github.com/ansible-collections/netapp.ontap/wiki/Known-issues>.  This should be in the form 9.10 or 9.10.1 with each element being an integer number.  When `use_rest` is set to auto, this may force a switch to ZAPI based on the version and platform capabilities.  Ignored with ZAPI. |
| **group**  string | Specifies the owner’s primary group.  Specify the owner group using either a group name or SID. |
| **hostname**  string / required | The hostname or IP address of the ONTAP instance. |
| **http_port**  integer | Override the default port (80 or 443) with this port |
| **https**  boolean | Enable and disable https.  Ignored when using REST as only https is supported.  Ignored when using SSL certificate authentication as it requires SSL.  **Choices:**   - `false` ← (default) - `true` |
| **ignore_paths**  list / elements=string | For each file or directory in the list, specifies that permissions on this file or directory cannot be replaced. |
| **key_filepath**  string  *added in netapp.ontap 20.6.0* | path to SSL client key file. |
| **ontapi**  integer | The ontap api version to use |
| **owner**  string | Specifies the owner of the NTFS security descriptor (SD).  You can specify the owner using either a user name or security identifier (SID).  The owner of the SD can modify the permissions on the file (or folder) or files (or folders) to which the SD is applied and can give other users the right to take ownership of the object or objects to which the SD is applied. |
| **password**  aliases: pass  string | Password for the specified user. |
| **path**  string / required | The path of the file or directory on which to apply security permissions. |
| **propagation_mode**  string | Specifies how to propagate security settings to child subfolders and files.  Defaults to propagate.  **Choices:**   - `"propagate"` - `"replace"` |
| **state**  string | Whether the specified file security permission should exist or not.  When absent, all ACLs are deleted, irrespective of the contents of `acls`.  See `access_control` to only delete all SLAG ACLS, or only delete file-directory ACLs.  Inherited ACLs are ignored, they can’t be deleted or modified.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **use_rest**  string | Whether to use REST or ZAPI.  always – will always use the REST API if the module supports REST. A warning is issued if the module does not support REST. An error is issued if a module option is not supported in REST.  never – will always use ZAPI if the module supports ZAPI. An error may be issued if a REST option is not supported in ZAPI.  auto – will try to use the REST API if the module supports REST and modules options are supported. Reverts to ZAPI otherwise.  **Default:** `"auto"` |
| **username**  aliases: user  string | This can be a Cluster-scoped or SVM-scoped account, depending on whether a Cluster-level or SVM-level API is required.  For more information, please read the documentation <https://mysupport.netapp.com/NOW/download/software/nmsdk/9.4/>.  Two authentication methods are supported   1. basic authentication, using username and password, 2. SSL certificate authentication, using a ssl client cert file, and optionally a private key file.   To use a certificate, the certificate must have been installed in the ONTAP cluster, and cert authentication must have been enabled. |
| **validate_certs**  boolean | If set to `no`, the SSL certificates will not be validated.  This should only set to `False` used on personally controlled sites using self-signed certificates.  **Choices:**   - `false` - `true` ← (default) |
| **validate_changes**  string | ACLs may not be applied as expected.  For instance, if Everyone is inherited will all permissions, additional users will be granted all permissions, regardless of the request.  For this specific example, you can either delete the top level Everyone, or create a new ACL for Everyone at a lower level.  When using `rights`, ONTAP translates them into `advanced_rights` so the validation will always fail.  Valid values are `ignore`, no checking; `warn` to issue a warning; `error` to fail the module.  With SLAGS, ONTAP may split one ACL into two ACLs depending on the `apply_to` settings. To maintain idempotency, please provide 2 ACLs as input.  **Choices:**   - `"ignore"` - `"warn"` - `"error"` ← (default) |
| **vserver**  string / required | Name of the vserver to use. |

## [Notes](na_ontap_file_security_permissions_module.md#id4)

> **Note:**
>
> - Supports check_mode.
> - Only supported with REST and requires ONTAP 9.9.1 or later..
> - SLAG requires ONTAP 9.10.1 or later.
> - When state is present, if an ACL is inherited, and a desired ACL matches, a new ACL is created as the inherited cannot be modified.
> - When state is absent, inherited ACLs are ignored.
> - The modules prefixed with na_ontap are built to support the ONTAP storage platform.
> - https is enabled by default and recommended. To enable http on the cluster you must run the following commands ‘set -privilege advanced;’ ‘system services web modify -http-enabled true;’

## [Examples](na_ontap_file_security_permissions_module.md#id5)

```yaml+jinja
- name: Create file directory security permissions.
  netapp.ontap.na_ontap_file_security_permissions:
    state: present
    vserver: svm1
    access_control: file_directory
    path: /vol200/newfile.txt
    owner: "{{ user }}"
    # Note, wihout quotes, use a single backslash in AD user names
    # with quotes, it needs to be escaped as a double backslash
    # user: "ANSIBLE_CIFS\user1"
    # we can't show an example with a single backslash as this is a python file, but it works in YAML.
    acls:
      - access: access_deny
        user: "{{ user }}"
        apply_to:
          files: true
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    https: "{{ https }}"
    validate_certs: "{{ validate_certs }}"

- name: Modify file directory security permissions.
  netapp.ontap.na_ontap_file_security_permissions:
    state: present
    vserver: svm1
    access_control: file_directory
    path: /vol200/newfile.txt
    acls:
      - access: access_deny
        user: "{{ user }}"
        apply_to:
          files: true
      - access: access_allow
        user: "{{ user }}"
        apply_to:
          files: true
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    https: "{{ https }}"
    validate_certs: "{{ validate_certs }}"

- name: Delete file directory security ACLs.
  netapp.ontap.na_ontap_file_security_permissions:
    state: absent
    vserver: svm1
    access_control: file_directory
    path: /vol200/newfile.txt
    acls:
      - access: access_deny
        user: "{{ user }}"
        apply_to:
          files: true
      - access: access_allow
        user: "{{ user }}"
        apply_to:
          files: true
    hostname: "{{ hostname }}"
    username: "{{ username }}"
    password: "{{ password }}"
    https: "{{ https }}"
    validate_certs: "{{ validate_certs }}"
```

### Authors

- NetApp Ansible Team (@carchi8py)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/netapp.ontap/issues)
- [Homepage](https://netapp.io/configuration-management-and-automation/)
- [Repository (Sources)](https://github.com/ansible-collections/netapp.ontap)
