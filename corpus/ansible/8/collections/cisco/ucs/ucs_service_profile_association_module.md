---
collection: ansible
version: "8"
title: "cisco.ucs.ucs_service_profile_association module – Configures Service Profile Association on Cisco UCS Manager"
source_url: https://docs.ansible.com/projects/ansible/8/collections/cisco/ucs/ucs_service_profile_association_module.html
fetched_at: 2026-07-28T01:39:40+00:00
---
# cisco.ucs.ucs_service_profile_association module – Configures Service Profile Association on Cisco UCS Manager

> **Note:**
>
> This module is part of the [cisco.ucs collection](https://galaxy.ansible.com/ui/repo/published/cisco/ucs/) (version 1.10.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install cisco.ucs`.
> You need further requirements to be able to use this module,
> see [Requirements](ucs_service_profile_association_module.md#ansible-collections-cisco-ucs-ucs-service-profile-association-module-requirements) for details.
>
> To use it in a playbook, specify: `cisco.ucs.ucs_service_profile_association`.

New in cisco.ucs 2.1

- [Synopsis](ucs_service_profile_association_module.md#synopsis)
- [Requirements](ucs_service_profile_association_module.md#requirements)
- [Parameters](ucs_service_profile_association_module.md#parameters)
- [Examples](ucs_service_profile_association_module.md#examples)
- [Return Values](ucs_service_profile_association_module.md#return-values)

## [Synopsis](ucs_service_profile_association_module.md#id1)

- Configures Service Profile Association (change association or disassociate) on Cisco UCS Manager.

## [Requirements](ucs_service_profile_association_module.md#id2)

The below requirements are needed on the host that executes this module.

- ucsmsdk

## [Parameters](ucs_service_profile_association_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **hostname**  string / required | IP address or hostname of Cisco UCS Manager.  Modules can be used with the UCS Platform Emulator <https://cs.co/ucspe> |
| **org_dn**  string | The distinguished name (dn) of the organization where the resource is assigned.  **Default:** `"org-root"` |
| **password**  string / required | Password for Cisco UCS Manager authentication. |
| **port**  integer | Port number to be used during connection (by default uses 443 for https and 80 for http connection). |
| **proxy**  string | If use_proxy is no, specfies proxy to be used for connection. e.g. ‘<http://proxy.xy.z:8080>’ |
| **restrict_migration**  string | Restricts the migration of the service profile after it has been associated with a server.  If set to no, Cisco UCS Manager does not perform any compatibility checks on the new server before migrating the existing service profile.  If set to no and the hardware of both servers used in migration are not similar, the association might fail.  **Choices:**   - `"yes"` - `"no"` ← (default) |
| **server_assignment**  string / required | Specifies how to associate servers with this service profile using the following choices:  server - Use to pre-provision a slot or select an existing server. Slot or server is specified by the server_dn option.  pool - Use to select from a server pool. The server_pool option specifies the name of the server pool to use.  Option is not valid if the service profile is bound to a template.  Optional if the state is absent.  **Choices:**   - `"server"` - `"pool"` |
| **server_dn**  string | The Distinguished Name (dn) of the server object used for pre-provisioning or selecting an existing server.  Required if the server_assignment option is server.  Optional if the state is absent. |
| **server_pool_name**  string | Name of the server pool used for server pool based assignment.  Required if the server_assignment option is pool.  Optional if the state is absent. |
| **service_profile_name**  string / required | The name of the Service Profile being associated or disassociated. |
| **state**  string | If `present`, will verify service profile association and associate with specified server or server pool if needed.  If `absent`, will verify service profile is not associated and will disassociate if needed. This is the same as specifying Assign Later in the webUI.  **Choices:**   - `"present"` ← (default) - `"absent"` |
| **use_proxy**  boolean | If `no`, will not use the proxy as defined by system environment variable.  **Choices:**   - `false` - `true` ← (default) |
| **use_ssl**  boolean | If `no`, an HTTP connection will be used instead of the default HTTPS connection.  **Choices:**   - `false` - `true` ← (default) |
| **username**  string | Username for Cisco UCS Manager authentication.  **Default:** `"admin"` |

## [Examples](ucs_service_profile_association_module.md#id4)

```yaml+jinja
- name: Change Service Profile Association to server pool Container-Pool and restrict migration
  cisco.ucs.ucs_service_profile_association:
    hostname: 172.16.143.150
    username: admin
    password: password
    service_profile_name: test-sp
    server_assignment: pool
    server_pool_name: Container-Pool
    restrict_migration: 'yes'

- name: Attempt to change association once a minute for up to 10 minutes
  cisco.ucs.ucs_service_profile_association:
    hostname: 172.16.143.150
    username: admin
    password: password
    service_profile_name: test-sp
    server_assignment: server
    server_dn: sys/chassis-2/blade-1
  register: result
  until: result.assign_state == 'assigned' and result.assoc_state == 'associated'
  retries: 10
  delay: 60

- name: Disassociate Service Profile
  cisco.ucs.ucs_service_profile_association:
    hostname: 172.16.143.150
    username: admin
    password: password
    service_profile_name: test-sp
    state: absent
```

## [Return Values](ucs_service_profile_association_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **assign_state**  string | The logical server Assigned State (assigned, unassigned, or failed).  **Returned:** success  **Sample:** `"assigned"` |
| **assoc_state**  string | The logical server Association State (associated or unassociated).  **Returned:** success  **Sample:** `"associated"` |

### Authors

- David Soper (@dsoper2)
- CiscoUcs (@CiscoUcs)

### Collection links

- [Issue Tracker](https://github.com/CiscoDevNet/ansible-ucs)
- [Repository (Sources)](https://github.com/CiscoDevNet/ansible-ucs)
