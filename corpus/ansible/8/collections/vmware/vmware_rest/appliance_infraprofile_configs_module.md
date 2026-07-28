---
collection: ansible
version: "8"
title: "vmware.vmware_rest.appliance_infraprofile_configs module – Exports the desired profile specification."
source_url: https://docs.ansible.com/projects/ansible/8/collections/vmware/vmware_rest/appliance_infraprofile_configs_module.html
fetched_at: 2026-07-28T02:57:06+00:00
---
# vmware.vmware_rest.appliance_infraprofile_configs module – Exports the desired profile specification.

> **Note:**
>
> This module is part of the [vmware.vmware_rest collection](https://galaxy.ansible.com/ui/repo/published/vmware/vmware_rest/) (version 2.3.1).
>
> You might already have this collection installed if you are using the `ansible` package.
> It is not included in `ansible-core`.
> To check whether it is installed, run `ansible-galaxy collection list`.
>
> To install it, use: `ansible-galaxy collection install vmware.vmware_rest`.
> You need further requirements to be able to use this module,
> see [Requirements](appliance_infraprofile_configs_module.md#ansible-collections-vmware-vmware-rest-appliance-infraprofile-configs-module-requirements) for details.
>
> To use it in a playbook, specify: `vmware.vmware_rest.appliance_infraprofile_configs`.

New in vmware.vmware_rest 2.0.0

- [Synopsis](appliance_infraprofile_configs_module.md#synopsis)
- [Requirements](appliance_infraprofile_configs_module.md#requirements)
- [Parameters](appliance_infraprofile_configs_module.md#parameters)
- [Notes](appliance_infraprofile_configs_module.md#notes)
- [Examples](appliance_infraprofile_configs_module.md#examples)
- [Return Values](appliance_infraprofile_configs_module.md#return-values)

## [Synopsis](appliance_infraprofile_configs_module.md#id1)

- Exports the desired profile specification.

## [Requirements](appliance_infraprofile_configs_module.md#id2)

The below requirements are needed on the host that executes this module.

- vSphere 7.0.2 or greater
- python >= 3.6
- aiohttp

## [Parameters](appliance_infraprofile_configs_module.md#id3)

| Parameter | Comments |
| --- | --- |
| **description**  string | Custom description provided by the user.  If unset description will be empty. |
| **encryption_key**  string | Encryption Key to encrypt/decrypt profiles.  If unset encryption will not be used for the profile. |
| **profiles**  list / elements=string | Profiles to be exported/imported.  If unset or empty, all profiles will be returned.  When clients pass a value of this structure as a parameter, the field must contain the id of resources returned by [vmware.vmware_rest.appliance_infraprofile_configs](appliance_infraprofile_configs_module.md#ansible-collections-vmware-vmware-rest-appliance-infraprofile-configs-module). |
| **session_timeout**  float  *added in vmware.vmware_rest 2.1.0* | Timeout settings for client session.  The maximal number of seconds for the whole operation including connection establishment, request sending and response.  The default value is 300s. |
| **state**  string / required | **Choices:**   - `"export"` |
| **vcenter_hostname**  string / required | The hostname or IP address of the vSphere vCenter  If the value is not specified in the task, the value of environment variable `VMWARE_HOST` will be used instead. |
| **vcenter_password**  string / required | The vSphere vCenter password  If the value is not specified in the task, the value of environment variable `VMWARE_PASSWORD` will be used instead. |
| **vcenter_rest_log_file**  string | You can use this optional parameter to set the location of a log file.  This file will be used to record the HTTP REST interaction.  The file will be stored on the host that run the module.  If the value is not specified in the task, the value of  environment variable `VMWARE_REST_LOG_FILE` will be used instead. |
| **vcenter_username**  string / required | The vSphere vCenter username  If the value is not specified in the task, the value of environment variable `VMWARE_USER` will be used instead. |
| **vcenter_validate_certs**  boolean | Allows connection when SSL certificates are not valid. Set to `false` when certificates are not trusted.  If the value is not specified in the task, the value of environment variable `VMWARE_VALIDATE_CERTS` will be used instead.  **Choices:**   - `false` - `true` ← (default) |

## [Notes](appliance_infraprofile_configs_module.md#id4)

> **Note:**
>
> - Tested on vSphere 7.0.2

## [Examples](appliance_infraprofile_configs_module.md#id5)

```yaml+jinja
- name: Export the ApplianceManagement profile
  vmware.vmware_rest.appliance_infraprofile_configs:
    state: export
    profiles:
    - ApplianceManagement
  register: result
```

## [Return Values](appliance_infraprofile_configs_module.md#id6)

Common return values are documented [here](../../../reference_appendices/common_return_values.md#common-return-values), the following are the fields unique to this module:

| Key | Description |
| --- | --- |
| **value**  string | Export the ApplianceManagement profile  **Returned:** On success  **Sample:** `"{\"action\":\"RESTART_SERVICE\",\"productName\":\"VMware vCenter Server\",\"creationTime\":\"2022-11-23T20:11:00+0000\",\"version\":\"7.0.3.00800\",\"profiles\":{\"ApplianceManagement\":{\"action\":\"RESTART_SERVICE\",\"actionOn\":{\"VC_SERVICES\":[\"applmgmt\"],\"SYSTEMD\":[\"sendmail\",\"rsyslog\"]},\"description\":\"Appliance Mangment Service\",\"version\":\"7.0\",\"config\":{\"/etc/applmgmt/appliance/appliance.conf\":{\"Is shell Enabled\":true,\"Shell Expiration Time\":9,\"TimeSync Mode (Host/NTP)\":\"NTP\"},\"/etc/ntp.conf\":{\"Time servers\":\"time.nist.gov\"},\"/etc/shadow\":{\"root\":{\"maximumDays\":\"90\",\"warningDays\":\"7\"},\"bin\":{\"maximumDays\":\"90\",\"warningDays\":\"7\"},\"daemon\":{\"maximumDays\":\"90\",\"warningDays\":\"7\"},\"messagebus\":{\"maximumDays\":\"90\",\"warningDays\":\"7\"},\"systemd-bus-proxy\":{\"maximumDays\":\"90\",\"warningDays\":\"7\"},\"systemd-journal-gateway\":{\"maximumDays\":\"90\",\"warningDays\":\"7\"},\"systemd-journal-remote\":{\"maximumDays\":\"90\",\"warningDays\":\"7\"},\"systemd-journal-upload\":{\"maximumDays\":\"90\",\"warningDays\":\"7\"},\"systemd-network\":{\"maximumDays\":\"90\",\"warningDays\":\"7\"},\"systemd-resolve\":{\"maximumDays\":\"90\",\"warningDays\":\"7\"},\"systemd-timesync\":{\"maximumDays\":\"90\",\"warningDays\":\"7\"},\"nobody\":{\"maximumDays\":\"90\",\"warningDays\":\"7\"},\"rpc\":{\"maximumDays\":\"90\",\"warningDays\":\"7\"},\"sshd\":{\"maximumDays\":\"90\",\"warningDays\":\"7\"},\"ntp\":{\"maximumDays\":\"90\",\"warningDays\":\"7\"},\"smmsp\":{\"maximumDays\":\"90\",\"warningDays\":\"7\"},\"apache\":{\"maximumDays\":\"90\",\"warningDays\":\"7\"},\"tftp\":{\"maximumDays\":\"\",\"warningDays\":\"\"},\"named\":{\"maximumDays\":\"\",\"warningDays\":\"\"},\"vmdird\":{\"maximumDays\":\"90\",\"warningDays\":\"7\"},\"sso-user\":{\"maximumDays\":\"90\",\"warningDays\":\"7\"},\"dnsmasq\":{\"maximumDays\":\"\",\"warningDays\":\"\"},\"observability\":{\"maximumDays\":\"\",\"warningDays\":\"\"},\"vdtc\":{\"maximumDays\":\"\",\"warningDays\":\"\"},\"vmafdd-user\":{\"maximumDays\":\"90\",\"warningDays\":\"7\"},\"vmcad-user\":{\"maximumDays\":\"90\",\"warningDays\":\"7\"},\"pod\":{\"maximumDays\":\"\",\"warningDays\":\"\"},\"vmonapi\":{\"maximumDays\":\"\",\"warningDays\":\"\"},\"envoy\":{\"maximumDays\":\"\",\"warningDays\":\"\"},\"vpostgres\":{\"maximumDays\":\"\",\"warningDays\":\"7\"},\"lookupsvc\":{\"maximumDays\":\"\",\"warningDays\":\"\"},\"cis-license\":{\"maximumDays\":\"\",\"warningDays\":\"\"},\"pschealth\":{\"maximumDays\":\"\",\"warningDays\":\"\"},\"netdumper\":{\"maximumDays\":\"\",\"warningDays\":\"\"},\"vapiEndpoint\":{\"maximumDays\":\"90\",\"warningDays\":\"7\"},\"vpxd-svcs\":{\"maximumDays\":\"\",\"warningDays\":\"\"},\"certauth\":{\"maximumDays\":\"90\",\"warningDays\":\"7\"},\"certmgr\":{\"maximumDays\":\"90\",\"warningDays\":\"7\"},\"infraprofile\":{\"maximumDays\":\"\",\"warningDays\":\"\"},\"topologysvc\":{\"maximumDays\":\"90\",\"warningDays\":\"7\"},\"trustmanagement\":{\"maximumDays\":\"\",\"warningDays\":\"\"},\"vpxd\":{\"maximumDays\":\"\",\"warningDays\":\"\"},\"analytics\":{\"maximumDays\":\"\",\"warningDays\":\"\"},\"eam\":{\"maximumDays\":\"90\",\"warningDays\":\"7\"},\"sps\":{\"maximumDays\":\"\",\"warningDays\":\"\"},\"deploy\":{\"maximumDays\":\"\",\"warningDays\":\"\"},\"updatemgr\":{\"maximumDays\":\"\",\"warningDays\":\"\"},\"vlcm\":{\"maximumDays\":\"90\",\"warningDays\":\"7\"},\"vmcam\":{\"maximumDays\":\"90\",\"warningDays\":\"7\"},\"vsan-health\":{\"maximumDays\":\"90\",\"warningDays\":\"7\"},\"vsm\":{\"maximumDays\":\"90\",\"warningDays\":\"7\"},\"vsphere-ui\":{\"maximumDays\":\"90\",\"warningDays\":\"7\"},\"vtsdbuser\":{\"maximumDays\":\"\",\"warningDays\":\"\"},\"vstatsuser\":{\"maximumDays\":\"\",\"warningDays\":\"\"},\"wcp\":{\"maximumDays\":\"\",\"warningDays\":\"7\"},\"content-library\":{\"maximumDays\":\"90\",\"warningDays\":\"7\"},\"imagebuilder\":{\"maximumDays\":\"90\",\"warningDays\":\"7\"},\"perfcharts\":{\"maximumDays\":\"90\",\"warningDays\":\"7\"},\"vpgmonusr\":{\"maximumDays\":\"\",\"warningDays\":\"7\"},\"vtsdbmonusr\":{\"maximumDays\":\"\",\"warningDays\":\"7\"},\"zuul\":{\"maximumDays\":\"90\",\"warningDays\":\"7\"},\"Send Waring before this No of Days.\":null,\"Password validity (days)\":null},\"/etc/sysconfig/clock\":{\"Time zone\":\"\\\"Etc/UTC\\\"\",\"UTC\":\"1\"},\"/usr/bin/systemctl/sshd.service\":{\"Enable SSH\":\"true\"},\"/etc/mail/sendmail.cf\":{\"SMTP Port\":null,\"Mail server\":null},\"/etc/vmware-syslog/syslog.conf\":{\"Port [2]\":null,\"Port [1]\":null,\"Port [0]\":null,\"Protocol [2]\":null,\"Remote Syslog Host [1]\":null,\"Protocol [1]\":null,\"Remote Syslog Host [0]\":null,\"Protocol [0]\":null,\"Remote Syslog Host [2]\":null},\"/etc/pam.d/system-auth\":{\"Deny Login after these many Unsuccessful Attempts.\":null,\"Unlock root after (seconds)\":null,\"On Error Login will be.\":null,\"Include Root user for SSH lockout.\":null,\"Unlock user after (seconds)\":null}},\"name\":\"ApplianceManagement\"}}}"` |

### Authors

- Ansible Cloud Team (@ansible-collections)

### Collection links

- [Issue Tracker](https://github.com/ansible-collections/vmware.vmware_rest/issues?q=is%3Aissue+is%3Aopen+sort%3Aupdated-desc)
- [Homepage](https://github.com/ansible-collections/vmware.vmware_rest)
- [Repository (Sources)](https://github.com/ansible-collections/vmware.vmware_rest.git)
