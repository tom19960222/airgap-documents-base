---
collection: ansible
version: "8"
title: "fortinet.fortimanager.fmgr_system_csf module – Add this device to a Security Fabric or set up a new Security Fabric on this device."
source_url: https://docs.ansible.com/projects/ansible/8/collections/fortinet/fortimanager/fmgr_system_csf_module.html
fetched_at: 2026-07-28T02:18:21+00:00
---
# fortinet.fortimanager.fmgr_system_csf module – Add this device to a Security Fabric or set up a new Security Fabric on this device.

> **Note:**
>
> This module is part of the [fortinet.fortimanager collection](https://galaxy.ansible.com/ui/repo/published/fortinet/fortimanager/) (version 2.3.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install fortinet.fortimanager`.
>
> To use it in a playbook, specify: `fortinet.fortimanager.fmgr_system_csf`.

New in fortinet.fortimanager 2.3.0

- [Synopsis](fmgr_system_csf_module.md#synopsis)
- [Parameters](fmgr_system_csf_module.md#parameters)
- [Notes](fmgr_system_csf_module.md#notes)
- [Examples](fmgr_system_csf_module.md#examples)
- [Return Values](fmgr_system_csf_module.md#return-values)

## [Synopsis](fmgr_system_csf_module.md#id1)

- This module is able to configure a FortiManager device.
- Examples include all parameters and values which need to be adjusted to data sources before usage.

## [Parameters](fmgr_system_csf_module.md#id2)

| Parameter | Comments |
| --- | --- |
| **access_token**  string | The token to access FortiManager without using username and password. |
| **bypass_validation**  boolean | Only set to True when module schema diffs with FortiManager API structure, module continues to execute without validating parameters.  **Choices:**   - `false` ← (default) - `true` |
| **enable_log**  boolean | Enable/Disable logging for task.  **Choices:**   - `false` ← (default) - `true` |
| **forticloud_access_token**  string | Authenticate Ansible client with forticloud API access token. |
| **proposed_method**  string | The overridden method for the underlying Json RPC request.  **Choices:**   - `"update"` - `"set"` - `"add"` |
| **rc_failed**  list / elements=integer | The rc codes list with which the conditions to fail will be overriden. |
| **rc_succeeded**  list / elements=integer | The rc codes list with which the conditions to succeed will be overriden. |
| **system_csf**  dictionary | the top level parameters set |
| **accept-auth-by-cert**  string | Accept connections with unknown certificates and ask admin for approval.  disable - Do not accept SSL connections with unknown certificates.  enable - Accept SSL connections without automatic certificate verification.  **Choices:**   - `"disable"` - `"enable"` |
| **authorization-request-type**  string | Authorization request type.  certificate - Request verification by certificate.  serial - Request verification by serial number.  **Choices:**   - `"certificate"` - `"serial"` |
| **certificate**  string | Certificate. |
| **configuration-sync**  string | Configuration sync mode.  default - Synchronize configuration for IPAM, FortiAnalyzer, FortiSandbox, and Central Management to root node.  local - Do not synchronize configuration with root node.  **Choices:**   - `"default"` - `"local"` |
| **downstream-access**  string | Enable/disable downstream device access to this device&apos;s configuration and data.  disable - Disable downstream device access to this device&apos;s configuration and data.  enable - Enable downstream device access to this device&apos;s configuration and data.  **Choices:**   - `"disable"` - `"enable"` |
| **downstream-accprofile**  string | Default access profile for requests from downstream devices. |
| **fabric-connector**  list / elements=dictionary | no description |
| **accprofile**  string | Override access profile. |
| **configuration-write-access**  string | Enable/disable downstream device write access to configuration.  disable - Disable downstream device write access to configuration.  enable - Enable downstream device write access to configuration.  **Choices:**   - `"disable"` - `"enable"` |
| **serial**  string | Serial. |
| **fabric-object-unification**  string | Fabric CMDB Object Unification.  local - Global CMDB objects will not be synchronized to and from this device.  default - Global CMDB objects will be synchronized in Security Fabric.  **Choices:**   - `"local"` - `"default"` |
| **fabric-workers**  integer | Number of worker processes for Security Fabric daemon. |
| **file-mgmt**  string | Enable/disable Security Fabric daemon file management.  disable - Disable daemon file management.  enable - Enable daemon file management.  **Choices:**   - `"disable"` - `"enable"` |
| **file-quota**  integer | Maximum amount of memory that can be used by the daemon files |
| **file-quota-warning**  integer | Warn when the set percentage of quota has been used. |
| **fixed-key**  list / elements=string | no description |
| **forticloud-account-enforcement**  string | Fabric FortiCloud account unification.  disable - Disable FortiCloud accound ID matching for Security Fabric.  enable - Enable FortiCloud account ID matching for Security Fabric.  **Choices:**   - `"disable"` - `"enable"` |
| **group-name**  string | Security Fabric group name. |
| **group-password**  list / elements=string | no description |
| **log-unification**  string | Enable/disable broadcast of discovery messages for log unification.  disable - Disable broadcast of discovery messages for log unification.  enable - Enable broadcast of discovery messages for log unification.  **Choices:**   - `"disable"` - `"enable"` |
| **saml-configuration-sync**  string | SAML setting configuration synchronization.  local - Do not apply SAML configuration generated by root.  default - SAML setting for fabric members is created by fabric root.  **Choices:**   - `"local"` - `"default"` |
| **status**  string | Enable/disable Security Fabric.  disable - Disable Security Fabric.  enable - Enable Security Fabric.  **Choices:**   - `"disable"` - `"enable"` |
| **trusted-list**  list / elements=dictionary | no description |
| **action**  string | Security fabric authorization action.  accept - Accept authorization request.  deny - Deny authorization request.  **Choices:**   - `"accept"` - `"deny"` |
| **authorization-type**  string | Authorization type.  serial - Verify downstream by serial number.  certificate - Verify downstream by certificate.  **Choices:**   - `"serial"` - `"certificate"` |
| **certificate**  string | Certificate. |
| **downstream-authorization**  string | Trust authorizations by this node&apos;s administrator.  disable - Disable downstream authorization.  enable - Enable downstream authorization.  **Choices:**   - `"disable"` - `"enable"` |
| **ha-members**  string | HA members. |
| **index**  integer | Index of the downstream in tree. |
| **name**  string | Name. |
| **serial**  string | Serial. |
| **upstream**  string | IP/FQDN of the FortiGate upstream from this FortiGate in the Security Fabric. |
| **upstream-port**  integer | The port number to use to communicate with the FortiGate upstream from this FortiGate in the Security Fabric |
| **workspace_locking_adom**  string | The adom to lock for FortiManager running in workspace mode, the value can be global and others including root. |
| **workspace_locking_timeout**  integer | The maximum time in seconds to wait for other user to release the workspace lock.  **Default:** `300` |

## [Notes](fmgr_system_csf_module.md#id3)

> **Note:**
>
> - Running in workspace locking mode is supported in this FortiManager module, the top level parameters workspace_locking_adom and workspace_locking_timeout help do the work.
> - To create or update an object, use state present directive.
> - To delete an object, use state absent directive.
> - Normally, running one module can fail when a non-zero rc is returned. you can also override the conditions to fail or succeed with parameters rc_failed and rc_succeeded

## [Examples](fmgr_system_csf_module.md#id4)

```yaml+jinja
- hosts: fortimanager-inventory
  collections:
    - fortinet.fortimanager
  connection: httpapi
  vars:
    ansible_httpapi_use_ssl: True
    ansible_httpapi_validate_certs: False
    ansible_httpapi_port: 443
  tasks:
    - name: Add this device to a Security Fabric or set up a new Security Fabric on this device.
      fmgr_system_csf:
        bypass_validation: False
        workspace_locking_adom: <value in [global, custom adom including root]>
        workspace_locking_timeout: 300
        rc_succeeded: [0, -2, -3, ...]
        rc_failed: [-2, -3, ...]
        system_csf:
          accept-auth-by-cert: <value in [disable, enable]>
          authorization-request-type: <value in [certificate, serial]>
          certificate: <string>
          configuration-sync: <value in [default, local]>
          downstream-access: <value in [disable, enable]>
          downstream-accprofile: <string>
          fabric-connector:
            -
              accprofile: <string>
              configuration-write-access: <value in [disable, enable]>
              serial: <string>
          fabric-object-unification: <value in [local, default]>
          fabric-workers: <integer>
          file-mgmt: <value in [disable, enable]>
          file-quota: <integer>
          file-quota-warning: <integer>
          fixed-key: <list or string>
          forticloud-account-enforcement: <value in [disable, enable]>
          group-name: <string>
          group-password: <list or string>
          log-unification: <value in [disable, enable]>
          saml-configuration-sync: <value in [local, default]>
          status: <value in [disable, enable]>
          trusted-list:
            -
              action: <value in [accept, deny]>
              authorization-type: <value in [serial, certificate]>
              certificate: <string>
              downstream-authorization: <value in [disable, enable]>
              ha-members: <string>
              index: <integer>
              name: <string>
              serial: <string>
          upstream: <string>
          upstream-port: <integer>
```

## [Return Values](fmgr_system_csf_module.md#id5)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **meta**  dictionary | The result of the request.  **Returned:** always |
| **request_url**  string | The full url requested.  **Returned:** always  **Sample:** `"/sys/login/user"` |
| **response_code**  integer | The status of api request.  **Returned:** always  **Sample:** `0` |
| **response_data**  list / elements=string | The api response.  **Returned:** always |
| **response_message**  string | The descriptive message of the api response.  **Returned:** always  **Sample:** `"OK."` |
| **system_information**  dictionary | The information of the target system.  **Returned:** always |
| **rc**  integer | The status the request.  **Returned:** always  **Sample:** `0` |
| **version_check_warning**  list / elements=string | Warning if the parameters used in the playbook are not supported by the current FortiManager version.  **Returned:** complex |

### Authors

- Xinwei Du (@dux-fortinet)
- Xing Li (@lix-fortinet)
- Jie Xue (@JieX19)
- Link Zheng (@chillancezen)
- Frank Shen (@fshen01)
- Hongbin Lu (@fgtdev-hblu)

### Collection links

- [Issue Tracker](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection/issues)
- [Homepage](https://fortinet.com)
- [Repository (Sources)](https://github.com/fortinet-ansible-dev/ansible-galaxy-fortimanager-collection)
