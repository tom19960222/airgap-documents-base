---
collection: ansible
version: "6"
title: "f5networks.f5_modules.bigip_remote_role module – Manage remote roles on a BIG-IP"
source_url: https://docs.ansible.com/projects/ansible/6/collections/f5networks/f5_modules/bigip_remote_role_module.html
fetched_at: 2026-07-27T17:27:39+00:00
---
# f5networks.f5_modules.bigip_remote_role module – Manage remote roles on a BIG-IP

> **Note:**
>
> This module is part of the [f5networks.f5_modules collection](https://galaxy.ansible.com/f5networks/f5_modules) (version 1.21.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install f5networks.f5_modules`.
>
> To use it in a playbook, specify: `f5networks.f5_modules.bigip_remote_role`.

New in f5networks.f5_modules 1.0.0

- [Synopsis](bigip_remote_role_module.md#synopsis)
- [Parameters](bigip_remote_role_module.md#parameters)
- [Notes](bigip_remote_role_module.md#notes)
- [Examples](bigip_remote_role_module.md#examples)
- [Return Values](bigip_remote_role_module.md#return-values)

## [Synopsis](bigip_remote_role_module.md#id1)

- Manages remote roles on a BIG-IP system. Remote roles are used in situations where user authentication is handled off-box. Local access control to the BIG-IP is controlled by the defined remote role, and authentication (and by extension, assignment to the role) is handled off-box.

## [Parameters](bigip_remote_role_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **assigned_role**  string | Specifies the authorization (level of access) for the account.  When creating a new remote role, if this parameter is not provided, the default is `none`.  The `partition_access` parameter controls which partitions the account can access.  The role you choose may affect the partitions that one is allowed to specify. Specifically, roles such as `administrator`, `auditor` and `resource-administrator` require a `partition_access` of `all`.  A set of pre-existing roles ship with the system. They are `none`, `guest`, `operator`, `application-editor`, `manager`, `certificate-manager`, `irule-manager`, `user-manager`, `resource-administrator`, `auditor`, `administrator`, and `firewall-manager`. |
| **attribute_string**  string | Specifies the user account attributes saved in the group, in the format `cn=, ou=, dc=`.  When creating a new remote role, this parameter is required. |
| **line_order**  integer | Specifies the order of the line in the file `/config/bigip/auth/remoterole`.  The LDAP and Active Directory servers read this file line by line.  The order of the information is important; therefore, F5 recommends you set the first line at 1000. This allows you to insert lines before the first line in the future.  When creating a new remote role, this parameter is required. |
| **name**  string / required | Specifies the name of the remote role. |
| **partition_access**  string | Specifies the accessible partitions for the account.  This parameter supports the reserved names `all` and `Common`, as well as specific partitions a user may access.  Users who have access to a partition can operate on objects in that partition, as determined by the permissions conferred by the user’s `assigned_role`.  When creating a new remote role, if this parameter is not specified, the default is `all`. |
| **provider**  dictionary  added in f5networks.f5_modules 1.0.0 | A dict object containing connection details. |
| **auth_provider**  string | Configures the auth provider for to obtain authentication tokens from the remote device.  This option is really used when working with BIG-IQ devices. |
| **no_f5_teem**  boolean | If `yes`, TEEM telemetry data is not sent to F5.  You may omit this option by setting the environment variable `F5_TELEMETRY_OFF`.  Previously used variable `F5_TEEM` is deprecated as its name was confusing.  Choices:   - `false` ← (default) - `true` |
| **password**  aliases: pass, pwd  string / required | The password for the user account used to connect to the BIG-IP.  You may omit this option by setting the environment variable `F5_PASSWORD`. |
| **server**  string / required | The BIG-IP host.  You may omit this option by setting the environment variable `F5_SERVER`. |
| **server_port**  integer | The BIG-IP server port.  You may omit this option by setting the environment variable `F5_SERVER_PORT`.  Default: `443` |
| **timeout**  integer | Specifies the timeout in seconds for communicating with the network device for either connecting or sending commands. If the timeout is exceeded before the operation is completed, the module will error. |
| **transport**  string | Configures the transport connection to use when connecting to the remote device.  Choices:   - `"rest"` ← (default) |
| **user**  string / required | The username to connect to the BIG-IP with. This user must have administrative privileges on the device.  You may omit this option by setting the environment variable `F5_USER`. |
| **validate_certs**  boolean | If `no`, SSL certificates are not validated. Use this only on personally controlled sites using self-signed certificates.  You may omit this option by setting the environment variable `F5_VALIDATE_CERTS`.  Choices:   - `false` - `true` ← (default) |
| **remote_access**  boolean | Enables or disables remote access for the specified group of remotely authenticated users.  When creating a new remote role, if this parameter is not specified, the default is `yes`.  Choices:   - `false` - `true` |
| **state**  string | When `present`, guarantees the remote role exists.  When `absent`, removes the remote role from the system.  Choices:   - `"absent"` - `"present"` ← (default) |
| **terminal_access**  string | Specifies terminal-based accessibility for remote accounts not already explicitly assigned a user role.  Common values for this include `tmsh` and `none`, but you can also specify custom values.  When creating a new remote role, if this parameter is not specified, the default is `none`. |

## [Notes](bigip_remote_role_module.md#id3)

> **Note:**
>
> - For more information on using Ansible to manage F5 Networks devices see <https://www.ansible.com/integrations/networks/f5>.
> - Requires BIG-IP software version >= 12.
> - The F5 modules only manipulate the running configuration of the F5 product. To ensure that BIG-IP specific configuration persists to disk, be sure to include at least one task that uses the [f5networks.f5_modules.bigip_config](bigip_config_module.md#ansible-collections-f5networks-f5-modules-bigip-config-module) module to save the running configuration. Refer to the module’s documentation for the correct usage of the module to save your running configuration.

## [Examples](bigip_remote_role_module.md#id4)

```yaml+jinja
- name: Create a remote role
  bigip_remote_role:
    name: ldap_group
    line_order: 1
    attribute_string: memberOf=cn=ldap_group,cn=ldap.group,ou=ldap
    remote_access: yes
    assigned_role: administrator
    partition_access: all
    terminal_access: none
    state: present
    provider:
      password: secret
      server: lb.mydomain.com
      user: admin
  delegate_to: localhost
```

## [Return Values](bigip_remote_role_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **assigned_role**  string | System role this remote role is associated with.  Returned: changed  Sample: `"administrator"` |
| **attribute_string**  string | The new attribute string of the resource.  Returned: changed  Sample: `"memberOf=cn=ldap_group,cn=ldap.group,ou=ldap"` |
| **line_order**  integer | Order of the remote role for LDAP and Active Directory servers.  Returned: changed  Sample: `1000` |
| **partition_access**  string | Partition the role has access to.  Returned: changed  Sample: `"all"` |
| **remote_access**  boolean | Whether remote access is allowed or not.  Returned: changed  Sample: `false` |
| **terminal_access**  string | The terminal setting of the remote role.  Returned: changed  Sample: `"tmsh"` |

### Authors

- Tim Rupp (@caphrim007)

### Collection links

[Issue Tracker](https://github.com/F5Networks/f5-ansible/issues)
[Homepage](https://clouddocs.f5.com/products/orchestration/ansible/devel/)
[Repository (Sources)](https://github.com/F5Networks/f5-ansible-f5modules)
