---
collection: ansible
version: "6"
title: "dellemc.openmanage.ome_discovery module – Create, modify, or delete a discovery job on OpenManage Enterprise"
source_url: https://docs.ansible.com/projects/ansible/6/collections/dellemc/openmanage/ome_discovery_module.html
fetched_at: 2026-07-27T17:25:37+00:00
---
# dellemc.openmanage.ome_discovery module – Create, modify, or delete a discovery job on OpenManage Enterprise

> **Note:**
>
> This module is part of the [dellemc.openmanage collection](https://galaxy.ansible.com/dellemc/openmanage) (version 5.5.0).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install dellemc.openmanage`.
> You need further requirements to be able to use this module,
> see [Requirements](ome_discovery_module.md#ansible-collections-dellemc-openmanage-ome-discovery-module-requirements) for details.
>
> To use it in a playbook, specify: `dellemc.openmanage.ome_discovery`.

New in dellemc.openmanage 3.3.0

- [Synopsis](ome_discovery_module.md#synopsis)
- [Requirements](ome_discovery_module.md#requirements)
- [Parameters](ome_discovery_module.md#parameters)
- [Notes](ome_discovery_module.md#notes)
- [Examples](ome_discovery_module.md#examples)
- [Return Values](ome_discovery_module.md#return-values)

## [Synopsis](ome_discovery_module.md#id1)

- This module allows to create, modify, or delete a discovery job.

## [Requirements](ome_discovery_module.md#id2)

The below requirements are needed on the host that executes this module.

- python >= 3.8.6

## [Parameters](ome_discovery_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **ca_path**  path  added in dellemc.openmanage 5.0.0 | The Privacy Enhanced Mail (PEM) file that contains a CA certificate to be used for the validation. |
| **community_string**  boolean | Enable the use of SNMP community strings to receive SNMP traps using Application Settings in OpenManage Enterprise. This option is available only for the discovered iDRAC servers and MX7000 chassis.  Choices:   - `false` ← (default) - `true` |
| **cron**  string | Provide a cron expression based on Quartz cron format. |
| **discovery_config_targets**  list / elements=dictionary | Provide the list of discovery targets.  Each discovery target is a set of *network_address_detail*, *device_types*, and one or more protocol credentials.  This is mandatory when *state* is `present`.  `WARNING` Modification of this field is not supported, this field is overwritten every time. Ensure to provide all the required details for this field. |
| **device_types**  list / elements=string / required | Provide the type of devices to be discovered.  The accepted types are SERVER, CHASSIS, NETWORK SWITCH, and STORAGE.  A combination or all of the above can be provided.  Supported protocols for each device type are:  SERVER - *wsman*, *redfish*, *snmp*, *ipmi*, *ssh*, and *vmware*.  CHASSIS - *wsman*, and *redfish*.  NETWORK SWITCH - *snmp*.  STORAGE - *storage*, and *snmp*. |
| **ipmi**  dictionary | Intelligent Platform Management Interface (IPMI) |
| **kgkey**  string | KgKey for the IPMI protocol. |
| **password**  string / required | Provide a password for the protocol. |
| **retries**  integer | Enter the number of repeated attempts required to discover a device.  Default: `3` |
| **timeout**  integer | Enter the time in seconds after which a job must stop running.  Default: `60` |
| **username**  string / required | Provide a username for the protocol. |
| **network_address_detail**  list / elements=string / required | Provide the list of IP addresses, host names, or the range of IP addresses of the devices to be discovered or included.  Sample Valid IP Range Formats  192.35.0.0  192.36.0.0-10.36.0.255  192.37.0.0/24  2345:f2b1:f083:135::5500/118  2345:f2b1:f083:135::a500-2607:f2b1:f083:135::a600  hostname.domain.tld  hostname  2345:f2b1:f083:139::22a  Sample Invalid IP Range Formats  192.35.0.\*  192.36.0.0-255  192.35.0.0/255.255.255.0  `NOTE` The range size for the number of IP addresses is limited to 16,385 (0x4001).  `NOTE` Both IPv6 and IPv6 CIDR formats are supported. |
| **redfish**  dictionary | REDFISH protocol. |
| **ca_check**  boolean | Enable the Certificate Authority (CA) check.  Choices:   - `false` ← (default) - `true` |
| **certificate_data**  string | Provide certificate data for the CA check. |
| **cn_check**  boolean | Enable the Common Name (CN) check.  Choices:   - `false` ← (default) - `true` |
| **domain**  string | Provide a domain for the protocol. |
| **password**  string / required | Provide a password for the protocol. |
| **port**  integer | Enter the port number that the job must use to discover the devices.  Default: `443` |
| **retries**  integer | Enter the number of repeated attempts required to discover a device.  Default: `3` |
| **timeout**  integer | Enter the time in seconds after which a job must stop running.  Default: `60` |
| **username**  string / required | Provide a username for the protocol. |
| **snmp**  dictionary | Simple Network Management Protocol (SNMP). |
| **community**  string / required | Community string for the SNMP protocol. |
| **port**  integer | Enter the port number that the job must use to discover the devices.  Default: `161` |
| **retries**  integer | Enter the number of repeated attempts required to discover a device.  Default: `3` |
| **timeout**  integer | Enter the time in seconds after which a job must stop running.  Default: `3` |
| **ssh**  dictionary | Secure Shell (SSH). |
| **check_known_hosts**  boolean | Verify the known host key.  Choices:   - `false` ← (default) - `true` |
| **is_sudo_user**  boolean | Use the SUDO option.  Choices:   - `false` ← (default) - `true` |
| **password**  string / required | Provide a password for the protocol. |
| **port**  integer | Enter the port number that the job must use to discover the devices.  Default: `22` |
| **retries**  integer | Enter the number of repeated attempts required to discover a device.  Default: `3` |
| **timeout**  integer | Enter the time in seconds after which a job must stop running.  Default: `60` |
| **username**  string / required | Provide a username for the protocol. |
| **storage**  dictionary | HTTPS Storage protocol. |
| **ca_check**  boolean | Enable the Certificate Authority (CA) check.  Choices:   - `false` ← (default) - `true` |
| **certificate_data**  string | Provide certificate data for the CA check. |
| **cn_check**  boolean | Enable the Common Name (CN) check.  Choices:   - `false` ← (default) - `true` |
| **domain**  string | Provide a domain for the protocol. |
| **password**  string / required | Provide a password for the protocol. |
| **port**  integer | Enter the port number that the job must use to discover the devices.  Default: `443` |
| **retries**  integer | Enter the number of repeated attempts required to discover a device.  Default: `3` |
| **timeout**  integer | Enter the time in seconds after which a job must stop running.  Default: `60` |
| **username**  string / required | Provide a username for the protocol. |
| **vmware**  dictionary | VMWARE protocol. |
| **ca_check**  boolean | Enable the Certificate Authority (CA) check.  Choices:   - `false` ← (default) - `true` |
| **certificate_data**  string | Provide certificate data for the CA check. |
| **cn_check**  boolean | Enable the Common Name (CN) check.  Choices:   - `false` ← (default) - `true` |
| **domain**  string | Provide a domain for the protocol. |
| **password**  string / required | Provide a password for the protocol. |
| **port**  integer | Enter the port number that the job must use to discover the devices.  Default: `443` |
| **retries**  integer | Enter the number of repeated attempts required to discover a device.  Default: `3` |
| **timeout**  integer | Enter the time in seconds after which a job must stop running.  Default: `60` |
| **username**  string / required | Provide a username for the protocol. |
| **wsman**  dictionary | Web Services-Management (WS-Man). |
| **ca_check**  boolean | Enable the Certificate Authority (CA) check.  Choices:   - `false` ← (default) - `true` |
| **certificate_data**  string | Provide certificate data for the CA check. |
| **cn_check**  boolean | Enable the Common Name (CN) check.  Choices:   - `false` ← (default) - `true` |
| **domain**  string | Provide a domain for the protocol. |
| **password**  string / required | Provide a password for the protocol. |
| **port**  integer | Enter the port number that the job must use to discover the devices.  Default: `443` |
| **retries**  integer | Enter the number of repeated attempts required to discover a device.  Default: `3` |
| **timeout**  integer | Enter the time in seconds after which a job must stop running.  Default: `60` |
| **username**  string / required | Provide a username for the protocol. |
| **discovery_id**  integer | ID of the discovery configuration group.  This value is DiscoveryConfigGroupId in the return values under discovery_status.  It is mutually exclusive with *discovery_job_name*. |
| **discovery_job_name**  string | Name of the discovery configuration job.  It is mutually exclusive with *discovery_id*. |
| **email_recipient**  string | Enter the email address to which notifications are to be sent about the discovery job status. Configure the SMTP settings to allow sending notifications to an email address. |
| **hostname**  string / required | OpenManage Enterprise IP address or hostname. |
| **ignore_partial_failure**  boolean | Provides the option to ignore partial failures. Partial failures occur when there is a combination of both discovered and undiscovered IPs.  If `False`, then the partial failure is not ignored, and the module will error out.  If `True`, then the partial failure is ignored.  This option is only applicable if *job_wait* is `True`.  Choices:   - `false` ← (default) - `true` |
| **job_wait**  boolean | Provides the option to wait for job completion.  This option is applicable when *state* is `present`.  Choices:   - `false` - `true` ← (default) |
| **job_wait_timeout**  integer | The maximum wait time of *job_wait* in seconds. The job is tracked only for this duration.  This option is applicable when *job_wait* is `True`.  Default: `10800` |
| **new_name**  string | New name of the discovery configuration job. |
| **password**  string / required | OpenManage Enterprise password. |
| **port**  integer | OpenManage Enterprise HTTPS port.  Default: `443` |
| **schedule**  string | Provides the option to schedule the discovery job.  If `RunLater` is selected, then *cron* must be specified.  Choices:   - `"RunNow"` ← (default) - `"RunLater"` |
| **state**  string | `present` creates a discovery job or modifies an existing discovery job.  *discovery_job_name* is mandatory for the creation of a new discovery job.  If multiple discoveries of the same *discovery_job_name* exist, then the new discovery job will not be created.  `absent` deletes an existing discovery job(s) with the specified *discovery_job_name*.  Choices:   - `"present"` ← (default) - `"absent"` |
| **timeout**  integer  added in dellemc.openmanage 5.0.0 | The socket level timeout in seconds.  Default: `30` |
| **trap_destination**  boolean | Enable OpenManage Enterprise to receive the incoming SNMP traps from the discovered devices.  This is effective only for servers discovered by using their iDRAC interface.  Choices:   - `false` ← (default) - `true` |
| **username**  string / required | OpenManage Enterprise username. |
| **validate_certs**  boolean  added in dellemc.openmanage 5.0.0 | If `False`, the SSL certificates will not be validated.  Configure `False` only on personally controlled sites where self-signed certificates are used.  Prior to collection version `5.0.0`, the *validate_certs* is `False` by default.  Choices:   - `false` - `true` ← (default) |

## [Notes](ome_discovery_module.md#id4)

> **Note:**
>
> - Run this module from a system that has direct access to Dell EMC OpenManage Enterprise.
> - This module does not support `check_mode`.
> - If *state* is `present`, then Idempotency is not supported.

## [Examples](ome_discovery_module.md#id5)

```yaml+jinja
---
- name: Discover servers in a range
  dellemc.openmanage.ome_discovery:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    discovery_job_name: "Discovery_server_1"
    discovery_config_targets:
      - network_address_detail:
          - 192.96.24.1-192.96.24.255
        device_types:
          - SERVER
        wsman:
          username: user
          password: password

- name: Discover chassis in a range
  dellemc.openmanage.ome_discovery:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    discovery_job_name: "Discovery_chassis_1"
    discovery_config_targets:
      - network_address_detail:
          - 192.96.24.1-192.96.24.255
        device_types:
          - CHASSIS
        wsman:
          username: user
          password: password

- name: Discover switches in a range
  dellemc.openmanage.ome_discovery:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    discovery_job_name: "Discover_switch_1"
    discovery_config_targets:
      - network_address_detail:
          - 192.96.24.1-192.96.24.255
        device_types:
          - NETWORK SWITCH
        snmp:
          community: snmp_creds

- name: Discover storage in a range
  dellemc.openmanage.ome_discovery:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    discovery_job_name: "Discover_storage_1"
    discovery_config_targets:
      - network_address_detail:
          - 192.96.24.1-192.96.24.255
        device_types:
          - STORAGE
        storage:
          username: user
          password: password
        snmp:
          community: snmp_creds

- name: Delete a discovery job
  dellemc.openmanage.ome_discovery:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    state: "absent"
    discovery_job_name: "Discovery-123"

- name: Schedule the discovery of multiple devices ignoring partial failure and enable trap to receive alerts
  dellemc.openmanage.ome_discovery:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    state: "present"
    discovery_job_name: "Discovery-123"
    discovery_config_targets:
      - network_address_detail:
          - 192.96.24.1-192.96.24.255
          - 192.96.0.0/24
          - 192.96.26.108
        device_types:
          - SERVER
          - CHASSIS
          - STORAGE
          - NETWORK SWITCH
        wsman:
          username: wsman_user
          password: wsman_pwd
        redfish:
          username: redfish_user
          password: redfish_pwd
        snmp:
          community: snmp_community
      - network_address_detail:
          - 192.96.25.1-192.96.25.255
          - ipmihost
          - esxiserver
          - sshserver
        device_types:
          - SERVER
        ssh:
          username: ssh_user
          password: ssh_pwd
        vmware:
          username: vm_user
          password: vmware_pwd
        ipmi:
          username: ipmi_user
          password: ipmi_pwd
    schedule: RunLater
    cron: "0 0 9 ? * MON,WED,FRI *"
    ignore_partial_failure: True
    trap_destination: True
    community_string: True
    email_recipient: test_email@company.com

- name: Discover servers with ca check enabled
  dellemc.openmanage.ome_discovery:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    discovery_job_name: "Discovery_server_ca1"
    discovery_config_targets:
      - network_address_detail:
          - 192.96.24.108
        device_types:
          - SERVER
        wsman:
          username: user
          password: password
          ca_check: True
          certificate_data: "{{ lookup('ansible.builtin.file', '/path/to/certificate_data_file') }}"

- name: Discover chassis with ca check enabled data
  dellemc.openmanage.ome_discovery:
    hostname: "192.168.0.1"
    username: "username"
    password: "password"
    ca_path: "/path/to/ca_cert.pem"
    discovery_job_name: "Discovery_chassis_ca1"
    discovery_config_targets:
      - network_address_detail:
          - 192.96.24.108
        device_types:
          - CHASSIS
        redfish:
          username: user
          password: password
          ca_check: True
          certificate_data: "-----BEGIN CERTIFICATE-----\r\n
          ABCDEFGHIJKLMNOPQRSTUVWXYZaqwertyuiopasdfghjklzxcvbnmasdasagasvv\r\n
          ABCDEFGHIJKLMNOPQRSTUVWXYZaqwertyuiopasdfghjklzxcvbnmasdasagasvv\r\n
          ABCDEFGHIJKLMNOPQRSTUVWXYZaqwertyuiopasdfghjklzxcvbnmasdasagasvv\r\n
          aqwertyuiopasdfghjklzxcvbnmasdasagasvv=\r\n
          -----END CERTIFICATE-----"
```

## [Return Values](ome_discovery_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **discovery_ids**  list / elements=string | IDs of the discoveries with duplicate names.  Returned: when discoveries with duplicate name exist for *state* is `present`  Sample: `[1234, 5678]` |
| **discovery_status**  dictionary | Details of the discovery job created or modified.  If *job_wait* is true, Completed and Failed IPs are also listed.  Returned: when *state* is `present`  Sample: `{"Completed": ["192.168.24.17", "192.168.24.20", "192.168.24.22"], "DiscoveredDevicesByType": [{"Count": 3, "DeviceType": "SERVER"}], "DiscoveryConfigDiscoveredDeviceCount": 3, "DiscoveryConfigEmailRecipient": "myemail@dell.com", "DiscoveryConfigExpectedDeviceCount": 9, "DiscoveryConfigGroupId": 125, "Failed": ["192.168.24.15", "192.168.24.16", "192.168.24.18", "192.168.24.19", "192.168.24.21", "host123"], "JobDescription": "D1", "JobEnabled": true, "JobEndTime": "2021-01-01 06:27:29.99", "JobId": 12666, "JobName": "D1", "JobNextRun": null, "JobProgress": "100", "JobSchedule": "startnow", "JobStartTime": "2021-01-01 06:24:10.071", "JobStatusId": 2090, "LastUpdateTime": "2021-01-01 06:27:30.001", "UpdatedBy": "admin"}` |
| **error_info**  dictionary | Details of the HTTP Error.  Returned: on HTTP error  Sample: `{"error": {"@Message.ExtendedInfo": [{"Message": "Unable to process the request because an error occurred.", "MessageArgs": [], "MessageId": "GEN1234", "RelatedProperties": [], "Resolution": "Retry the operation. If the issue persists, contact your system administrator.", "Severity": "Critical"}], "code": "Base.1.0.GeneralError", "message": "A general error has occurred. See ExtendedInfo for more information."}}` |
| **msg**  string | Overall status of the discovery operation.  Returned: always  Sample: `"Successfully deleted 1 discovery job(s)."` |

### Authors

- Jagadeesh N V (@jagadeeshnv)
- Sajna Shetty (@Sajna-Shetty)

### Collection links

[Issue Tracker](https://github.com/dell/dellemc-openmanage-ansible-modules/issues)
[Homepage](https://github.com/dell/dellemc-openmanage-ansible-modules)
[Repository (Sources)](https://github.com/dell/dellemc-openmanage-ansible-modules/tree/collections)
